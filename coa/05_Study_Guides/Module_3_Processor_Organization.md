# COA Module 3

*Processor Organization and Control Unit Design*

B.E. CSE (AI & ML) · Sem III · Course 2023114 · 8 teaching hours · CO3

Built from *chapter 3 coa.docx*, *Assignment 3.docx*, the supplied question banks, the MUSA practice material and the official University of Mumbai syllabus.

## Syllabus and scope

**Official module name:** Processor Organization and Control Unit Design · **Teaching hours:** 8 · **Course outcome:** CO3.

*Official University of Mumbai syllabus, course 2023114 (Module 3 row)*

“8086 Processor: Architecture of 8086 processor, Register Organization, Instruction formats, instruction cycle, addressing modes. Control Unit: Instruction interpretation and sequencing, Micro-programmed and hardwired control unit design methods. Microinstruction sequencing and execution, Micro programs. RISC and CISC: Introduction to RISC and CISC architectures and design issues.”

The official row lists no self-study topic for this module.

This is the largest module in the course: 8 teaching hours, twice Module 5. It has three clear halves, and the exam treats them separately even when one question mixes them.

| Syllabus unit | What it asks you to do | Taught in |
| --- | --- | --- |
| **3.1 · 8086 processor** | Draw and explain the architecture; classify the registers; decode the instruction format; describe the instruction cycle; compute effective and physical addresses for every addressing mode. | Sections 2–7 |
| **3.2 · Control unit** | Explain instruction interpretation and sequencing; design and compare hardwired and microprogrammed control; explain microinstruction sequencing and execution; write a small microprogram. | Sections 8–10 |
| **3.3 · RISC and CISC** | Define both architectures; compare them on instruction set, length, addressing, registers, pipelining and control-unit style; state the design issues. | Section 11 |

**Prescribed versus supplementary.** The table below separates what the syllabus names from what this guide adds so that the questions can be answered fully. Anything marked supplementary is written for this guide and is never presented as teacher or University material.

| Status | Content | Why it is here |
| --- | --- | --- |
| **Prescribed** | 8086 architecture; register organization; instruction formats; instruction cycle; addressing modes; instruction interpretation and sequencing; hardwired and microprogrammed control; microinstruction sequencing and execution; microprograms; RISC and CISC. | Named in the official Module 3 row. |
| **Supplementary** | Segment-to-physical address arithmetic; word alignment on the 16-bit bus; bus-cycle timing; decoding a real 8086 instruction byte-by-byte; control-memory sizing; horizontal-versus-vertical encoding arithmetic; a CPI-based RISC/CISC comparison. | These turn the descriptive syllabus into answerable numericals and give the “explain with an example” parts something concrete to say. |

**Exam pattern.** The end-semester paper is 60 marks in 2 hours, with six 20-mark questions. Question 1 is compulsory and mixes modules; you attempt any three of the remaining questions. Module 3 is 8 hours and supplies a large share of the descriptive marks. Typical patterns are: a 7-mark “architecture of 8086 with diagram”, a 7-mark “addressing modes with examples”, a 3-mark “differentiate hardwired and microprogrammed”, a 5-mark “instruction cycle state diagram”, and a 3–5-mark “microinstruction sequencing”. Numerical marks usually come from physical-address and effective-address calculations, not from long arithmetic.

*How to use this guide*

The teaching sections follow the teacher’s *chapter 3 coa.docx* and *Assignment 3.docx*. Where this guide adds a derivation, a numerical or an explanation that the teacher’s notes do not contain, the block is labelled **Supplementary clarification** or **Supplementary worked example**. Question wording in Sections 12 and 13 is copied from the supplied documents. No question is labelled a University paper unless a real paper was checked, and none was supplied for this course.

## 1 · The processor and the control unit

### 1.1 Two halves of a processor

A processor is easier to understand if you split it into a **datapath** and a **control unit**. The datapath contains the parts that hold and transform data: registers, the ALU, internal buses and the interface to memory. The control unit contains the logic that decides *what the datapath should do next*. It reads the instruction, works out which operation is required, and then asserts the control signals that open the right register gates, select the ALU function and start a memory transfer.

The distinction matters because the syllabus asks you to design the control unit, not the ALU. A datapath can perform only a fixed set of micro-operations: “copy register A to the internal bus”, “add”, “increment the program counter”, “read memory into the data register”. The control unit is the sequencer that orders those micro-operations into the execution of each machine instruction.

> **control unit = next-state logic + control-signal generator**

The next-state logic answers “which step am I in, and what comes next?”. The signal generator answers “which control lines must be active during this step?”. The two design styles in the syllabus differ only in how the answers are stored:

| Style | Where the answer lives | Consequence |
| --- | --- | --- |
| **Hardwired** | Fixed combinational logic and a state counter. | Fast, but the instruction set is frozen into the wiring. |
| **Microprogrammed** | Microinstructions in a control memory. | Slower by one memory access, but easy to change and extend. |

### 1.2 What the control unit must do for every instruction

1. **Fetch.** Put the program counter on the address bus, read the instruction, place it in the instruction register, and increment the program counter.
2. **Interpret.** Decode the opcode and the operand fields to discover the operation, the source, the destination and the addressing mode.
3. **Sequence.** Break the operation into micro-operations and issue them in the correct order, waiting where necessary for memory or the ALU.
4. **Handle the exceptional path.** If the instruction is a branch, change the program counter; if an interrupt is pending and enabled, enter the interrupt cycle.

Every question in this module is a variation on those four steps. When you are unsure how to start an answer, name the step you are describing.

### 1.3 Why the 8086 is the case study

The 8086 is small enough to draw completely in an exam and rich enough to show every idea the syllabus needs. It has a split fetch and execute unit (pipelining), segmented memory (address arithmetic), a variable-length instruction format (decoding), eight addressing modes (effective addresses), and a documented set of flags (conditional control). Its control unit is microprogrammed, which makes the hardwired-versus-microprogrammed comparison concrete rather than abstract.

Two numbers anchor the whole module: the 8086 has a **16-bit data bus** and **20 address lines**. From those two facts you can derive the 1 MB address space, the 64 KB segment size, the 2-byte word, and the two-bus-cycle penalty for a misaligned word. Keep them in front of you.

## 2 · 8086 architecture: BIU and EU

### 2.1 The headline specification

| Feature | 8086 | What it implies |
| --- | --- | --- |
| Data bus | 16 bits, multiplexed with the low address lines (AD15–AD0) | One word (2 bytes) per transfer; a word at an odd address needs two bus cycles. |
| Address bus | 20 bits | 2^(20) = 1,048,576 bytes = 1 MB of physical memory. |
| Registers | 16 bits | An offset can span 64 KB; two registers are needed to form a 20-bit address. |
| Instruction queue | 6 bytes | The BIU fetches ahead while the EU executes. |
| Clock | 5, 8 or 10 MHz depending on the version | One clock period is 200, 125 or 100 ns. |

The phrase “16-bit microprocessor” refers to the data bus and the internal word size, not to the address bus. That is why a 16-bit machine can address 1 MB: the address is built from two 16-bit registers, not from one.

### 2.2 The Bus Interface Unit

The **Bus Interface Unit (BIU)** is the processor’s connection to the outside world. It sends out every address, performs every memory and I/O read or write, and prefetches instructions. It contains five functional parts:

| Part | Function |
| --- | --- |
| **Instruction queue** | A 6-byte FIFO that holds prefetched instruction bytes. It lets the BIU fetch the next instructions while the EU is still executing the current one. |
| **Segment registers** | CS, DS, SS and ES hold the 16-bit base of the current code, data, stack and extra segments. |
| **Instruction pointer** | IP holds the 16-bit offset of the next instruction inside the code segment. The BIU updates it as bytes are fetched. |
| **Address adder** | Computes the 20-bit physical address as (segment × 10H) + offset. |
| **Bus control logic** | Generates ALE, BHE, read/write, ready and bus-request/grant signals, and drives the multiplexed address/data lines. |

Because the address lines are multiplexed with data, the BIU must latch the address early in the bus cycle with the **ALE** (Address Latch Enable) signal. This is a favourite short-answer point: ALE tells external latches “the value on AD15–AD0 is an address now, not data”.

### 2.3 The Execution Unit

The **Execution Unit (EU)** executes instructions. It takes bytes out of the queue, decodes them, computes effective addresses and performs arithmetic and logic. It contains:

| Part | Function |
| --- | --- |
| **Control system** | Sequences the internal operations of the EU. |
| **Instruction decoder** | Translates the opcode and operand fields into the required operation. |
| **ALU** | Performs addition, subtraction, AND, OR, XOR, NOT, shifts and rotates. |
| **Flag register** | Records the status of the last result and holds control flags. |
| **General-purpose registers** | AX, BX, CX and DX, each split into two 8-bit halves. |
| **Pointer and index registers** | SP, BP, SI and DI, used for stack and string addressing. |

The EU never drives the external bus. When it needs memory, it asks the BIU for the required bytes and continues with whatever it can do internally. This separation is the architectural reason for the 8086’s performance advantage over earlier 8-bit designs.

**The three internal buses.** The teacher’s notes name three internal buses. The **A-Bus** is the interface between the BIU and the EU; the **B-Bus** carries instruction fetches, data fetches, address transfers and effective-address computation; the **C-Bus** carries the instructions, addresses and data that the BIU passes to the EU. Figure 1 draws them as one internal-bus connection. Naming them separately is a cheap way to add detail to an architecture answer, because it shows that the two units are physically connected and not merely logically separate.

> *Figure 1. The 8086 in two halves. The BIU owns every external transfer; the EU decodes and executes from the queue.*

### 2.4 Why split the processor into BIU and EU

Earlier 8-bit processors used a strict fetch–execute alternation: fetch an instruction, execute it, fetch the next, execute it. During the fetch the execution logic sat idle, and during execution the bus sat idle. The 8086 breaks that alternation by giving fetching and executing to two units that run asynchronously.

When the EU begins executing an instruction, the BIU can already be fetching the next one into the queue. When the EU finishes, the next instruction is often waiting, so the fetch time disappears from the critical path. This is the 8086’s form of **pipelining**: the fetch stage of instruction *n+1* overlaps the execute stage of instruction *n*.

| Time slot | BIU | EU |
| --- | --- | --- |
| 1 | Fetch I1 | Idle |
| 2 | Fetch I2 | Execute I1 |
| 3 | Fetch I3 | Execute I2 |
| 4 | Fetch I4 (queue full → wait) | Execute I3 |

Supplementary clarification. The table is a timing sketch, not a cycle-accurate simulation. The real 8086 stalls the BIU when the 6-byte queue is full and flushes the queue on a branch.

The queue has a second, examinable consequence. A taken jump or call makes the prefetched bytes useless, so the BIU **flushes the queue** and refetches from the target. That is why branches cost more than straight-line instructions even when the instruction itself is short.

### 2.5 Memory segmentation

Twenty address lines can name 1 MB, but every register is 16 bits wide and can hold only 64 KB worth of offset. The 8086 bridges the gap with **segmentation**: a 16-bit segment register supplies a base, and a 16-bit offset is added to it.

> **physical address = (segment register × 10H) + offset**

> **physical address = (segment register << 4) + offset**

Multiplying by 10H is the same as appending four zero bits. A 16-bit segment value therefore becomes a 20-bit base, and the 16-bit offset is added to it. The offset is also called the **effective address** when it has been computed from the addressing mode.

| Quantity | Reason | Value |
| --- | --- | --- |
| Address space | 2^(20) | 1,048,576 bytes = 1 MB |
| Maximum segment size | 16-bit offset | 2^(16) = 65,536 bytes = 64 KB |
| Non-overlapping segments | 1 MB ÷ 64 KB | 16 |
| Distinct segment bases | 16-bit segment register | 65,536 |
| Address step per segment increment | one unit × 10H | 16 bytes |

Because there are 65,536 possible bases but only 16 non-overlapping 64 KB slots, segments **overlap**. Two different segment:offset pairs can name the same physical byte. For example, 1000:0020 and 1002:0000 both give 10020H. This is not an error; it is how the 8086 lets a program place a segment anywhere on a 16-byte boundary.

**Worked example — physical address from CS:IP**

The code segment register contains 2000H and the instruction pointer contains 0050H. Find the physical address of the next instruction.

**Question.** CS = 2000H, IP = 0050H. Find the physical address.

**Solution.**

> **base = CS × 10H = 2000H × 10H = 20000H**

> **physical = base + IP = 20000H + 0050H = 20050H**

**Check:** the base ends in 0H, as every segment base must, and the offset 0050H lies inside the 64 KB segment.

**Final Answer:** Physical address = 20050H.

**Worked example — stack address and the reset vector**

(a) SS = 3000H, SP = FFFEH. (b) At reset the 8086 loads CS = F000H and IP = FFF0H. Find both physical addresses.

**Question.** Compute the physical address for (a) SS:SP = 3000H:FFFEH and (b) CS:IP = F000H:FFF0H.

**Solution.**

> **(a) 3000H × 10H = 30000H; 30000H + FFFEH = 3FFFEH**

> **(b) F000H × 10H = F0000H; F0000H + FFF0H = FFFF0H**

Part (b) is the reset vector: execution begins 16 bytes below the top of memory. Part (a) is the top of a 64 KB stack segment, which is why the stack grows downwards from FFFEH.

**Final Answer:** (a) 3FFFEH   (b) FFFF0H.

### 2.6 Word alignment on the 16-bit bus

The 8086 data bus is 16 bits wide, so memory is organised as two banks of 512 KB: an even bank selected by A0 = 0 and an odd bank selected by BHE = 0. A word stored at an even address occupies one location in each bank and is transferred in one bus cycle. A word stored at an odd address straddles the banks and needs two bus cycles.

> **aligned word (even address): 1 bus cycle  ·  misaligned word (odd address): 2 bus cycles**

This is why compilers and assemblers align 16-bit data on even addresses. A 100-word array that starts at an odd address therefore costs 200 bus cycles instead of 100, which is a 100% penalty for a one-byte misalignment.

### 2.7 Exam answer plan — architecture of the 8086

1. State the headline: 16-bit data bus, 20 address lines, 1 MB, 6-byte queue.
2. Draw the two-box diagram: BIU on the left, EU on the right, internal buses between them.
3. List the BIU parts and one function for each: queue, segment registers, IP, address adder, bus control.
4. List the EU parts: control, decoder, ALU, flags, general registers, pointers.
5. Explain the overlap: the BIU prefetches while the EU executes, which removes fetch time from the critical path.
6. Add segmentation: physical = segment × 10H + offset, 64 KB segments, 1 MB total.
7. Close with the queue-flush penalty on branches.

## 3 · Register organization

The 8086 programmer’s model is a set of 16-bit registers in five groups. Learn the groups, not fourteen unrelated names, because exam questions ask you to “classify and explain”.

| Group | Registers | Width | Main job |
| --- | --- | --- | --- |
| General purpose | AX, BX, CX, DX | 16 (two 8-bit halves) | Data, arithmetic, counters, I/O |
| Segment | CS, DS, SS, ES | 16 | Hold segment bases |
| Pointer | SP, BP | 16 | Stack top and stack frame base |
| Index | SI, DI | 16 | String source and destination offsets |
| Control | IP, FLAGS | 16 | Next instruction offset; processor status |

### 3.1 General-purpose registers

Each of AX, BX, CX and DX can be used as one 16-bit register or as two independent 8-bit registers. The names are not arbitrary; each has a conventional role that the instruction set rewards.

| 16-bit | High byte | Low byte | Conventional role |
| --- | --- | --- | --- |
| **AX** — accumulator | AH | AL | Preferred register for arithmetic, logic, multiply/divide and I/O. Many instructions have a shorter form when they use AX/AL. |
| **BX** — base | BH | BL | Holds a base address for memory operands; one of the registers allowed inside `[ ]`. |
| **CX** — counter | CH | CL | Loop counter for `LOOP`; count for shifts and rotates (only CL can be the count). |
| **DX** — data | DH | DL | Holds the high-order word in a 32-bit multiply/divide result; port number for indirect `IN`/`OUT`. |

Because the halves are separate, writing AL does not disturb AH. That is useful for byte processing but dangerous when you expect a 16-bit value to survive: `MOV AL, 05H` changes only the low byte of AX.

### 3.2 Segment registers and their default pairings

Four segment registers let a program keep code, data, stack and an extra area in separate 64 KB windows. The processor does not use them at random: each kind of access has a default segment, and the default can be overridden with a segment prefix.

| Segment register | Default use | Default offset register | Override prefix |
| --- | --- | --- | --- |
| **CS** — code | Instruction fetch | IP | None (CS cannot be overridden for fetch) |
| **DS** — data | Ordinary data operands | BX, SI, DI, or a displacement | `CS:`, `SS:`, `ES:` |
| **SS** — stack | Stack push/pop and frame access | SP or BP | `DS:`, `ES:`, `CS:` |
| **ES** — extra | String destination and extra data | DI | `DS:`, `SS:`, `CS:` |

The pairing rule is worth memorising: **BP defaults to SS**, everything else that can be an offset defaults to DS. That single exception is why a stack frame addressed through BP survives a change to DS.

### 3.3 Pointer and index registers

| Register | Meaning | Typical use |
| --- | --- | --- |
| **SP** — stack pointer | Offset of the current top of stack from the start of SS | `PUSH` decrements SP by 2; `POP` increments it by 2. |
| **BP** — base pointer | Offset of a frame inside the stack segment | Accesses parameters and locals at fixed displacements while SP moves. |
| **SI** — source index | Offset of a source string element | Used by string instructions and as a general index. |
| **DI** — destination index | Offset of a destination string element | Used with ES for string destination and as a general index. |

SP and BP are pointers because they normally address the stack; SI and DI are index registers because they normally address arrays and strings. All four are 16 bits and all four can appear inside a memory operand, but only BX, BP, SI and DI are allowed there. AX, CX and DX cannot be used as an address register in the 8086.

### 3.4 Instruction pointer

IP holds the offset of the next instruction byte inside the code segment. The programmer cannot write IP directly with a `MOV`; it changes through control-transfer instructions (`JMP`, `CALL`, `RET`, interrupts) and through the BIU’s automatic increment as it fetches. The pair CS:IP is the complete address of the next instruction.

### 3.5 The flag register

The flag register is 16 bits wide but only nine bits are defined: six **status flags** that describe the last result and three **control flags** that change processor behaviour. The rest are undefined and should not be relied on.

| Bit | Flag | Name | Meaning |
| --- | --- | --- | --- |
| 0 | CF | Carry | Set by a carry out of, or borrow into, the most significant bit. |
| 2 | PF | Parity | Set when the low byte of the result has an even number of 1s. |
| 4 | AF | Auxiliary carry | Carry out of bit 3; used by BCD adjustment instructions. |
| 6 | ZF | Zero | Set when the result is zero. |
| 7 | SF | Sign | Copy of the most significant bit of the result (1 = negative in signed interpretation). |
| 8 | TF | Trap | Single-step mode for debugging. |
| 9 | IF | Interrupt enable | Allows maskable interrupts when set. |
| 10 | DF | Direction | String operations auto-increment when clear, auto-decrement when set. |
| 11 | OF | Overflow | Set when a signed result does not fit in the destination. |

> *Figure 2. The nine defined flags. The shaded bits are the control flags.*

### 3.6 Worked example — reading the register state

**Worked example — what changes and what does not**

Initially AX = 1234H, BX = 5678H, CX = 0005H and SP = 0100H. The following instructions execute in order: `MOV AL, 99H`, `PUSH AX`, `DEC CX`. State the final values of AX, CX and SP, and the two bytes written to the stack.

**Question.** AX = 1234H, BX = 5678H, CX = 0005H, SP = 0100H. Execute MOV AL,99H; PUSH AX; DEC CX. Find AX, CX, SP and the stored bytes.

**Solution.**

> **MOV AL,99H → AX = 1299H (AH unchanged, AL replaced)**

> **PUSH AX → SP = 0100H − 2 = 00FEH; bytes 99H at 00FEH, 12H at 00FFH**

> **DEC CX → CX = 0005H − 1 = 0004H**

**Why the byte order looks reversed:** the 8086 stores a word low byte first (little-endian), so the low byte 99H goes to the lower address 00FEH and the high byte 12H to 00FFH. A `POP AX` reverses the operation and restores AX = 1299H.

**Final Answer:** AX = 1299H, CX = 0004H, SP = 00FEH; memory 00FEH = 99H, 00FFH = 12H.

### 3.7 Exam answer plan — register organization

1. Draw the programmer’s model as five labelled groups, not a flat list.
2. For general-purpose registers, give the 16-bit name, both 8-bit halves and one conventional use each.
3. For segment registers, give the four names and the default offset pairing; mention that BP defaults to SS.
4. For pointers and index registers, distinguish SP/BP (stack) from SI/DI (strings and arrays).
5. Explain IP as the next-instruction offset, not a general register.
6. For flags, state 16 bits, 9 defined, 6 status and 3 control, and give the meaning of each.
7. Add one sentence on why segmentation is needed: 16-bit registers cannot hold a 20-bit address.

## 4 · Instruction format

### 4.1 Variable length, 1 to 6 bytes

Unlike a RISC machine with fixed 4-byte instructions, the 8086 uses a variable-length format. A single-byte instruction such as `NOP` (90H) is one byte; a move with a 16-bit displacement and a 16-bit immediate can reach six bytes. The processor does not know the length in advance, so it must decode the first byte before it knows how many more bytes belong to the instruction.

> **maximum length = 1 (opcode) + 1 (ModR/M) + 2 (displacement) + 2 (immediate) = 6 bytes**

That maximum is why the BIU’s queue is exactly six bytes: the queue must be able to hold the longest possible instruction. It is a neat example of one architectural number explaining another.

### 4.2 The fields

| Field | Size | Purpose |
| --- | --- | --- |
| **Opcode** | 6 bits | Names the operation. The remaining two bits of the first byte are D and W. |
| **D** (direction) | 1 bit | Selects which operand is the destination: D = 1 means the `reg` field is the destination; D = 0 means the `r/m` field is. |
| **W** (word) | 1 bit | W = 0 selects an 8-bit operation; W = 1 selects a 16-bit operation. |
| **mod** | 2 bits | Distinguishes register-direct (mod = 11) from memory addressing with 0, 8 or 16 bits of displacement. |
| **reg** | 3 bits | Names one register: a general register, a segment register or an opcode extension. |
| **r/m** | 3 bits | Names a register or a memory-addressing form, depending on `mod`. |
| **Displacement** | 0, 8 or 16 bits | A signed constant added to the effective address. |
| **Immediate** | 0, 8 or 16 bits | A constant operand carried inside the instruction. |

> *Figure 3. The general format. Not every instruction uses every field; the opcode determines which optional fields follow.*

### 4.3 Worked example — decoding a real instruction

**Worked example — decode 89 D8**

The two bytes 89H and D8H are fetched as one instruction. Decode every field and state the assembly instruction.

**Question.** Decode the 8086 instruction bytes 89H D8H.

**Solution.**

**Byte 1 = 89H = 1000 1001.**

> **opcode = 100010 (MOV) · D = 0 · W = 1**

**Byte 2 = D8H = 1101 1000.**

> **mod = 11 · reg = 011 · r/m = 000**

- `W = 1`: the operation is 16-bit, so the operands are 16-bit registers.
- `mod = 11`: both operands are registers; there is no memory access and no displacement.
- `reg = 011`: BX. `r/m = 000`: AX.
- `D = 0`: the `r/m` field is the destination, so AX receives and BX is the source.

**Check:** the same move can also be encoded as 8BH C3H, where D = 1 and the `reg` field is the destination. Both encodings are legal; assemblers choose one.

**Final Answer:** 89H D8H = MOV AX, BX (AX ← BX).

### 4.4 Worked example — maximum instruction length

**Worked example — counting bytes and bits**

An instruction uses a one-byte opcode, a ModR/M byte, a 16-bit displacement and a 16-bit immediate. Find its total length in bytes and bits. How many such instructions fit in the 6-byte queue?

**Question.** Find the length of an instruction with opcode + ModR/M + 16-bit displacement + 16-bit immediate, in bytes and bits. How many fit in the queue?

**Solution.**

> **bytes = 1 + 1 + 2 + 2 = 6 bytes**

> **bits = 6 × 8 = 48 bits**

> **queue capacity = 6 bytes ÷ 6 bytes per instruction = 1 instruction**

The queue holds one maximum-length instruction, or up to six one-byte instructions. That is exactly why the 8086 queue is six bytes deep: it is sized to the worst case, not the average.

**Final Answer:** 6 bytes = 48 bits; one maximum-length instruction fits in the queue.

### 4.5 Exam answer plan — instruction format

1. State that the 8086 format is variable-length, 1 to 6 bytes.
2. Draw the field diagram: opcode 6, D 1, W 1, mod 2, reg 3, r/m 3, displacement, immediate.
3. Explain D and W in one line each; they are the two bits students most often omit.
4. Explain mod = 11 as register-direct and the other values as memory forms with 0, 8 or 16 bits of displacement.
5. Decode one real instruction (89 D8 is ideal) to prove you can use the format.
6. State the 6-byte maximum and connect it to the 6-byte queue.

### 4.6 The instruction set at a glance

The syllabus names instruction formats, not the complete instruction set, but the teacher’s notes classify the 8086 instruction set into seven groups. A “classify the 8086 instructions” question is easy marks if you know the groups and one example each.

| Group | What it does | Examples |
| --- | --- | --- |
| **Data transfer** | Moves data between registers, memory and I/O ports without changing it. | `MOV`, `PUSH`/`POP`, `XCHG`, `IN`/`OUT`, `LEA`, `LDS`/`LES` |
| **Arithmetic** | Adds, subtracts, multiplies, divides and adjusts BCD or ASCII values. | `ADD`/`ADC`, `SUB`/`SBB`, `INC`/`DEC`, `MUL`/`IMUL`, `DIV`/`IDIV`, `DAA`/`DAS`, `CMP` |
| **Logical and bit manipulation** | Performs Boolean operations and moves bits. | `AND`, `OR`, `XOR`, `NOT`, `TEST`, `SHL`/`SAL`, `SHR`, `SAR`, `ROL`, `ROR`, `RCL`, `RCR` |
| **String** | Operates on a sequence of bytes or words, using SI, DI and the direction flag. | `MOVS`, `CMPS`, `SCAS`, `LODS`, `STOS`; `REP`, `REPE`/`REPZ`, `REPNE`/`REPNZ` |
| **Control transfer** | Changes the program counter, conditionally or unconditionally. | `JMP`, `CALL`, `RET`; `JE`/`JZ`, `JNE`/`JNZ`, `JC`/`JNC`, `JG`/`JL`; `LOOP`, `LOOPE`/`LOOPNE`, `JCXZ` |
| **Processor control and flags** | Changes processor state or the flag register directly. | `STC`/`CLC`/`CMC`, `STD`/`CLD`, `STI`/`CLI`, `HLT`, `NOP`, `WAIT`, `ESC`, `LOCK` |
| **Interrupt** | Transfers control to an interrupt service routine and returns. | `INT n`, `INTO`, `IRET` |

Adapted from the teacher’s chapter 3 notes. This is a classification, not a complete opcode list; each group contains many more instructions and forms than the examples shown.

## 5 · Instruction cycle

### 5.1 The three phases and the fourth check

The **instruction cycle** is the sequence a processor repeats for every instruction: fetch it, decode it, execute it. A complete description adds a fourth step — check for interrupts before starting the next fetch — because that check is what makes interrupts possible without a separate controller seizing the CPU.

| Phase | Question answered | Typical micro-operations |
| --- | --- | --- |
| **Fetch** | Where is the next instruction? | MAR ← PC; MDR ← M[MAR]; IR ← MDR; PC ← PC + 1 |
| **Decode** | What does it mean? | Decode opcode and operand fields; compute effective address if required |
| **Execute** | What must change? | ALU operation, memory read/write, register transfer, branch |
| **Interrupt check** | Should the CPU serve a device first? | If IF = 1 and a request is pending, enter the interrupt cycle |

Some descriptions add a fifth phase, **write-back** (or store), in which the result is written to its destination. On the 8086 this is part of execute rather than a separate pipeline stage, but naming it is harmless and matches the teacher’s notes. The four phases above are the ones to draw.

The fetch phase is almost identical for every instruction, which is why it can be hardwired or microcoded once and reused. The execute phase is different for every opcode, which is why the control unit needs a separate sequence for each instruction.

### 5.2 Fetch in detail

> **MAR ← IP  ·  MDR ← M[MAR]  ·  IR ← MDR  ·  IP ← IP + length**

On the 8086 the BIU has already prefetched the bytes, so the EU’s “fetch” is really “read the next byte from the queue”. The external memory read happened earlier. For exam answers, describe the general fetch sequence first, then add the 8086 refinement: the queue hides the memory access when it is not empty, and a branch flushes it.

The program counter increment is not always +1. Because instructions are variable-length, the CPU adds the number of bytes actually consumed. A one-byte `NOP` advances IP by 1; a six-byte move advances it by 6. In a simplified teaching model you may write PC ← PC + 1 per byte fetched, which gives the same result.

### 5.3 Decode and execute

**Decode** separates the opcode from the operands. In the 8086 this means reading the 6-bit opcode, the D and W bits, and — if present — the ModR/M byte that says whether an operand is a register or a memory location. The output of decode is a set of control signals plus, for memory operands, an effective address.

**Execute** performs the operation. It may be as short as a register transfer or as long as a string move that repeats CX times. The control unit sequences it as a series of micro-operations, each of which can complete in one or more clock cycles.

### 5.4 The state diagram

> *Figure 4. The instruction cycle. The interrupt check sits between execute and the next fetch.*

### 5.5 Clock, machine cycle and instruction cycle

Three time units are easy to confuse. The **clock cycle** (T-state) is one period of the processor clock. The **machine cycle** or bus cycle is the time to complete one memory or I/O transfer; the 8086 minimum is four T-states. The **instruction cycle** is the time to fetch, decode and execute one whole instruction, and it contains one or more machine cycles.

> **T = 1 / f  ·  bus cycle = 4T (minimum)  ·  instruction time = number of T-states × T**

**Worked example — timing an instruction**

An 8086 runs at 5 MHz. Its minimum bus cycle is four clock periods, and an instruction needs four bus cycles. Find the clock period, the bus-cycle time and the instruction time. How long does a loop of 100 such instructions take?

**Question.** f = 5 MHz, 4 T per bus cycle, 4 bus cycles per instruction, 100 instructions. Find T, the bus-cycle time, the instruction time and the loop time.

**Solution.**

> **T = 1 / (5 × 10^(6)) = 0.2 × 10^(−6) s = 200 ns**

> **bus cycle = 4T = 4 × 200 ns = 800 ns = 0.8 µs**

> **instruction = 4 bus cycles = 4 × 0.8 µs = 3.2 µs**

> **loop = 100 × 3.2 µs = 320 µs**

**Check:** 100 instructions × 16 T each = 1600 T; 1600 × 200 ns = 320,000 ns = 320 µs.

**Final Answer:** T = 200 ns; bus cycle 0.8 µs; instruction 3.2 µs; loop 320 µs.

Supplementary worked example. Real 8086 instructions take between about 2 and 200 clock cycles; the four-bus-cycle figure is a teaching assumption, not a datasheet value for a named instruction.

### 5.6 The interrupt cycle

When the check succeeds, the processor finishes the current instruction, saves the return state, and jumps to the service routine. On the 8086 the saved state is the flag register, CS and IP; the return address is pushed so that `IRET` can restore it. The interrupt cycle is therefore not a separate instruction — it is a hardware-initiated extension of the cycle.

1. Complete the current instruction.
2. Push the flag register, then CS, then IP.
3. Clear IF and TF (unless the interrupt is non-maskable).
4. Load CS:IP from the interrupt vector table.
5. Execute the service routine; finish with `IRET`, which restores IP, CS and the flags.

### 5.7 Exam answer plan — instruction cycle

1. Define the cycle as fetch → decode → execute, with an interrupt check at the end.
2. Draw the state diagram with the interrupt branch.
3. Give the fetch micro-operations explicitly; they earn marks.
4. Explain that decode produces control signals and, for memory operands, an effective address.
5. Distinguish clock cycle, machine cycle and instruction cycle.
6. Add the interrupt sequence: save flags, CS and IP; load the vector; return with `IRET`.

## 6 · Addressing modes

### 6.1 What an addressing mode specifies

An **addressing mode** is the rule that tells the processor where an operand is. The operand may be inside the instruction (immediate), inside a register (register), or in memory at an address computed in a particular way. For memory operands the rule produces an **effective address (EA)**: the 16-bit offset that is added to a segment base.

> **EA = base register + index register + displacement**

The 8086 allows only certain combinations. BX or BP may be the base; SI or DI may be the index; the displacement is 0, 8 or 16 bits. You cannot use AX, CX or DX as an address register, and you cannot combine BX with BP or SI with DI in one operand.

### 6.2 The modes you must know

| Mode | Where the operand is | EA rule | Example | Default segment |
| --- | --- | --- | --- | --- |
| **Immediate** | Inside the instruction | No EA; the constant is part of the instruction | `MOV AX, 2000H` | — |
| **Register** | In a register | No EA; the register is named in the instruction | `MOV AX, BX` | — |
| **Direct** | In memory at a fixed offset | EA = displacement | `MOV AX, [0500H]` | DS |
| **Register indirect** | In memory at the address in a register | EA = BX, BP, SI or DI | `MOV AX, [SI]` | DS (SS if BP) |
| **Based** | In memory at base + displacement | EA = BX or BP + disp | `MOV AL, [BP+0100H]` | SS for BP, DS for BX |
| **Indexed** | In memory at index + displacement | EA = SI or DI + disp | `MOV AX, [SI+2000H]` | DS |
| **Based indexed** | In memory at base + index | EA = BX or BP + SI or DI | `MOV AX, [BX+SI]` | DS (SS if BP) |
| **Based indexed with displacement** | In memory at base + index + displacement | EA = BX or BP + SI or DI + disp | `MOV AL, [BX+SI+0100H]` | DS (SS if BP) |

Three further modes appear in the syllabus and in the teacher’s notes but are usually described separately: **string** mode (SI and DI auto-update, with DF setting the direction), **I/O** mode (`IN`/`OUT` with a port number), and **relative** mode (the target is IP + a signed displacement, used by jumps). Learn them as a short list; the eight memory modes above carry most of the marks.

### 6.3 How the ModR/M byte selects the mode

The processor does not guess the addressing mode; the `mod` and `r/m` fields encode it. This table is the bridge between Section 4 and this section, and it answers the common exam question “how does the CPU know which addressing mode is used?”.

| r/m | mod ≠ 00 | mod = 00 |
| --- | --- | --- |
| 000 | BX + SI | BX + SI |
| 001 | BX + DI | BX + DI |
| 010 | BP + SI | BP + SI |
| 011 | BP + DI | BP + DI |
| 100 | SI | SI |
| 101 | DI | DI |
| 110 | BP | direct address (disp16) |
| 111 | BX | BX |

The special case is `r/m = 110` with `mod = 00`: instead of “BP with no displacement”, the encoding means a direct 16-bit address. That is why direct mode exists without a separate opcode.

### 6.4 From effective address to physical address

> *Figure 5. Two additions produce the physical address. The segment is shifted, not merely added, because it is a 16-bit base for a 20-bit space.*

**Worked example — based indexed with displacement**

DS = 2000H, BX = 0100H, SI = 0020H and the instruction is `MOV AX, [BX+SI+0010H]`. Find the effective address and the physical address.

**Question.** DS = 2000H, BX = 0100H, SI = 0020H, displacement = 0010H. Find EA and the physical address.

**Solution.**

> **EA = BX + SI + disp = 0100H + 0020H + 0010H = 0130H**

> **physical = DS × 10H + EA = 20000H + 0130H = 20130H**

**Check:** the operand lies 0130H bytes into the data segment, and the segment base is 20000H, so the byte is at 20130H.

**Final Answer:** EA = 0130H; physical address = 20130H.

**Worked example — the BP default segment**

SS = 3000H, BP = 0200H, displacement = 0010H and the instruction is `MOV AL, [BP+0010H]`. Find EA and the physical address. What changes if the programmer writes `MOV AL, DS:[BP+0010H]`?

**Question.** SS = 3000H, BP = 0200H, disp = 0010H. Find EA and the physical address for [BP+0010H], and state the effect of a DS: override.

**Solution.**

> **EA = BP + disp = 0200H + 0010H = 0210H**

> **physical = SS × 10H + EA = 30000H + 0210H = 30210H**

With the default, the operand is in the stack segment. Writing `DS:[BP+0010H]` keeps the same EA (0210H) but changes the base, so the physical address becomes 20000H + 0210H = 20210H if DS = 2000H.

**Final Answer:** EA = 0210H; default physical = 30210H; a DS: override changes only the segment base.

### 6.5 Comparing the modes

| Criterion | Immediate | Register | Direct | Indirect / based / indexed |
| --- | --- | --- | --- | --- |
| Extra memory access for the operand | No | No | Yes | Yes |
| Instruction length | Grows by the constant size | Shortest | Grows by 2 bytes | Grows by 0–2 bytes of displacement |
| Can the address change at run time? | No | No | No | Yes — change the register |
| Typical use | Constants | Temporary values | Fixed global variables | Arrays, records, stack frames, strings |
| Relative speed | Fast | Fastest | Slower (memory) | Slower, plus address arithmetic |

The exam point is not that one mode is “best”. Immediate and register modes are fast but inflexible; the indexed forms cost an address calculation but let one instruction serve an entire array by changing a register. That trade-off is the reason the 8086 provides eight memory forms instead of one.

### 6.6 Exam answer plan — addressing modes

1. Define an addressing mode and an effective address.
2. For each of the eight modes, give the EA rule, one assembly example, and the default segment.
3. State the legal register combinations: BX/BP for base, SI/DI for index, displacement 0/8/16.
4. Work one numerical example end to end: EA, then physical address.
5. Mention the special case `mod = 00, r/m = 110` = direct addressing.
6. Finish with the trade-off table: speed versus flexibility.

## 7 · Instruction interpretation and sequencing

### 7.1 Interpretation is decoding plus operand identification

**Instruction interpretation** is the control unit’s job of deciding what an instruction means. It has two outputs: the *operation* to perform and the *operands* it applies to. The opcode names the operation; the remaining fields name the operands and their addressing modes.

The teacher’s notes express this in **Register Transfer Notation (RTN)**. Square brackets mean “the contents of the location”, and the arrow means “is assigned to”.

> **R3 ← [R1] + [R2]**

Read it as: fetch the contents of R1 and R2, add them, and store the result in R3. RTN is useful in exams because it states a micro-operation without committing to a particular circuit.

### 7.2 Instruction formats by number of addresses

The same operation can be encoded with different numbers of explicit operands. The choice affects instruction length, the number of memory accesses and the pressure on registers.

| Format | Example | Meaning | Trade-off |
| --- | --- | --- | --- |
| **Three-address** | `ADD A, B, C` | A ← B + C | One instruction, no extra moves; longest encoding. |
| **Two-address** | `ADD A, B` | A ← A + B | Compact; destroys the original A. |
| **One-address** | `ADD B` | Accumulator ← Accumulator + B | Very short opcode; accumulator becomes a bottleneck. |
| **Zero-address** | `ADD` | Pop two, push the sum | Short instructions; stack traffic replaces register names. |

The 8086 is primarily a two-address machine: `ADD AX, BX` means AX ← AX + BX. The 8086 also has one-address forms for multiply, divide and some string operations, and it uses the stack implicitly for `PUSH`, `POP`, `CALL` and `RET`.

### 7.3 Sequencing

**Instruction sequencing** is the control unit’s job of deciding the order of operations. It has two levels. At the instruction level, it fetches instructions in program order unless a branch changes the program counter. At the micro-operation level, it issues the steps of the current instruction in the correct order.

| Level | Question | Mechanism |
| --- | --- | --- |
| Instruction sequencing | Which instruction runs next? | PC/IP increment; branch and call; interrupt vector |
| Micro-operation sequencing | Which step of this instruction runs next? | State counter (hardwired) or microinstruction address (microprogrammed) |

Straight-line sequencing simply increments the program counter. A conditional branch changes it only when the tested flag matches. A call saves the return address and jumps; a return restores it. An interrupt saves the state and jumps to a vector. All four are the same mechanism — write a new value into the program counter — with different sources for that value.

### 7.4 Micro-operations for a fetch and an add

The table below is the level of detail a “describe the steps involved in fetching, decoding and executing an instruction” question expects. It is a generic register-transfer machine, not a cycle-accurate 8086 trace.

| Step | Micro-operation | Control signals (typical) |
| --- | --- | --- |
| 1 | MAR ← PC | PC out, MAR in |
| 2 | MDR ← M[MAR]; PC ← PC + 1 | Memory read, MDR in, PC increment |
| 3 | IR ← MDR | MDR out, IR in |
| 4 | Decode opcode | Decoder enable |
| 5 | MAR ← IR(address field) | IR out, MAR in |
| 6 | MDR ← M[MAR] | Memory read, MDR in |
| 7 | R1 ← [R1] + [MDR] | ALU add, register write |
| 8 | Update flags | Flag register write |

Steps 1–4 are the fetch and decode phases; steps 5–8 are the execute phase for a memory-source add. A different opcode replaces steps 5–8 but keeps steps 1–4. That reuse is the economic argument for a microprogrammed control unit: the fetch routine is written once and shared by every instruction.

### 7.5 Exam answer plan — interpretation and sequencing

1. Define interpretation as decoding the opcode and identifying the operands.
2. Use RTN to show one operation; explain the brackets and the arrow.
3. List the four address-count formats and one trade-off each.
4. Separate instruction sequencing from micro-operation sequencing.
5. Give the fetch micro-operations in order with their control signals.
6. Explain branches and interrupts as writes to the program counter from different sources.

## 8 · Hardwired control unit

### 8.1 The idea

A **hardwired control unit** generates control signals from fixed combinational logic. The inputs are the instruction register, the condition flags, the clock and the state of a sequence counter. The outputs are the control lines that drive the datapath. There is no control memory and no microinstruction: the instruction set is encoded into gates.

> **control signal = f(opcode, flags, timing state)**

Because the function is combinational, the signal appears as soon as its inputs are stable. That is the source of the hardwired unit’s speed advantage, and also of its rigidity: adding an instruction means redesigning the logic and the chip.

> *Figure 6. A hardwired control unit. The timing state and the decoded opcode are combined in fixed logic.*

### 8.2 The parts

| Part | Function |
| --- | --- |
| **Instruction register (IR)** | Holds the current instruction so that its opcode and operand fields are stable for the whole execute phase. |
| **Opcode decoder** | Converts the *n*-bit opcode into one active line out of 2^(n). |
| **Sequence counter** | Counts clock pulses and produces the timing states T0, T1, T2 … that divide an instruction into steps. |
| **State decoder** | Turns the counter value into one active timing line. |
| **Flag inputs** | Allow conditional operations: a branch signal is gated by ZF, CF, SF and so on. |
| **Combinational logic** | ANDs the opcode line with the timing line and the relevant flag, then ORs the terms for each control signal. |

### 8.3 The design methods

“Discuss the major design methods used for implementing hardwired control” is a standard 5–7 mark question. The methods differ in how the timing states are produced.

| Method | How timing is produced | Notes |
| --- | --- | --- |
| **Sequence counter** | An *n*-bit counter drives a decoder that produces 2^(n) timing states. | Most common. Simple, regular, easy to extend to more states by widening the counter. |
| **Ring counter** | A shift register with a single 1 circulating through it; each flip-flop is one timing state. | One-hot states need no decoder, but *n* states need *n* flip-flops. |
| **Johnson counter** | A twisted-ring shift register with *n* flip-flops producing 2*n* states. | More states per flip-flop than a ring counter; the state decode is slightly more complex. |
| **Delay element** | A chain of delay elements or monostables, each tap giving a delayed pulse. | Cheap for very short sequences; sensitive to temperature and manufacturing variation. |
| **PLA / ROM logic** | A programmable logic array or small ROM implements the signal equations directly. | Regular layout and easy to modify before fabrication; still fixed after the chip is made. |

### 8.4 Worked example — writing the control equations

**Worked example — a four-state fetch sequence**

A hardwired control unit uses a 2-bit sequence counter with states T0–T3. Design the control signals for the fetch sequence: T0: MAR ← PC; T1: MDR ← M[MAR], PC ← PC + 1; T2: IR ← MDR; T3: decode. Write the Boolean equation for each control signal.

**Question.** Given states T0–T3 and the four micro-operations above, write equations for MAR_in, MEM_read, PC_inc, IR_in and DECODE.

**Solution.**

> **MAR_in = T0**

> **MEM_read = T1  ·  PC_inc = T1**

> **IR_in = T2**

> **DECODE = T3**

Each signal is simply the timing state in which its micro-operation runs, because this fetch sequence does not depend on the opcode. For an execute step that depends on the instruction, the term is gated by the decoded opcode:

> **ALU_add = T3 · ADD_op  +  T4 · INC_op**

**Interpretation:** the AND terms select “which instruction, which step”; the OR collects every situation in which the same control line must be active.

**Final Answer:** MAR_in = T0; MEM_read = PC_inc = T1; IR_in = T2; DECODE = T3.

### 8.5 Advantages and disadvantages

| Advantages | Disadvantages |
| --- | --- |
| Fast: signals are produced by combinational logic, with no control-memory read. | Rigid: the instruction set is fixed in hardware. |
| No control memory, so no ROM cost and no microinstruction fetch. | Complex and error-prone to design for a large instruction set. |
| Deterministic timing, which simplifies worst-case analysis. | Difficult to modify, extend or patch after fabrication. |
| Well suited to a small, simple, fixed instruction set (classic RISC). | Poor fit for variable-length instructions and many addressing modes (classic CISC). |

### 8.6 Exam answer plan — hardwired control

1. Define it: fixed combinational logic driven by the IR, flags and a timing state.
2. Draw the block diagram: IR → opcode decoder; clock → sequence counter → decoder; both into the logic array; logic → control signals.
3. List the design methods: sequence counter, ring counter, Johnson counter, delay element, PLA/ROM.
4. Give one Boolean equation to show how opcode and timing are combined.
5. State two advantages and two disadvantages, and name RISC as the natural application.

## 9 · Microprogrammed control unit

### 9.1 The idea

A **microprogrammed control unit** replaces the fixed logic with a small program. Each machine instruction is broken into micro-operations, and each micro-operation is encoded as a **microinstruction** stored in a **control memory**. Executing an instruction means running its microprogram.

The idea was proposed by Maurice Wilkes in 1951. It turns a hardware design problem into a firmware problem: the control memory is a ROM (or a writable control store), and changing the microprogram changes the instruction set without changing the datapath.

> **machine instruction → microprogram → sequence of microinstructions → control signals**

> *Figure 7. A microprogrammed control unit. The control memory holds the microprogram; the sequencer chooses the next microinstruction.*

### 9.2 The parts

| Part | Function |
| --- | --- |
| **Control memory** | Stores the microprogram. Usually ROM; a writable control store allows patching or user microprogramming. |
| **Control address register (CAR)** | Holds the address of the microinstruction being executed. |
| **Microinstruction register (MIR)** | Holds the current microinstruction while its fields are used. |
| **Sequencer** | Computes the next address: increment, branch, subroutine call or return. |
| **Mapping logic** | Converts the machine opcode into the start address of that instruction’s microprogram. |
| **Subroutine register** | Stores a return address when a microprogram calls a shared micro-routine. |

### 9.3 Horizontal and vertical microinstructions

The width and encoding of a microinstruction is a design choice with a direct cost in control-memory size.

| Property | Horizontal | Vertical |
| --- | --- | --- |
| Control field | One bit per control signal | Signals encoded in a compact field and decoded before use |
| Width | Wide | Narrow |
| Parallelism | Many signals can be asserted in one microinstruction | Few signals per microinstruction; more microinstructions needed |
| Control-memory size | Large | Small |
| Decoding | Little or none | Needs a decoder and therefore delay |
| Typical use | Fast machines, wide control words | Cost-sensitive machines, compact firmware |

**Worked example — control-memory size**

A microprogrammed control unit has a control memory of 512 microinstructions, each 40 bits wide. Find the number of address bits, the total size in bits and the total size in kilobytes.

**Question.** 512 words × 40 bits. Find the address width, total bits and total KB.

**Solution.**

> **address bits = log_(2) 512 = 9 bits**

> **total = 512 × 40 = 20,480 bits**

> **total = 20,480 ÷ 8 = 2,560 bytes = 2.5 KB**

**Check:** 2^(9) = 512, so a 9-bit CAR can address every microinstruction exactly once.

**Final Answer:** 9 address bits; 20,480 bits; 2.5 KB.

**Worked example — horizontal versus vertical width**

A processor has 64 control signals and needs a 9-bit next-address field. Compare the microinstruction width for (a) fully horizontal encoding, (b) fully vertical encoding with one signal at a time, and (c) grouped vertical encoding with 8 groups of 8 signals, one signal per group.

**Question.** 64 signals, 9-bit next address. Find the control-word width for horizontal, vertical and 8 × 8 grouped vertical encoding.

**Solution.**

**(a) Horizontal.** One bit per signal:

> **control field = 64 bits; total = 64 + 9 = 73 bits**

**(b) Vertical, one at a time.** The field must name one of 64 signals or “none”, so it needs log_(2)(64 + 1) rounded up:

> **control field = ⌈log_(2) 65⌉ = 7 bits; total = 7 + 9 = 16 bits**

**(c) Grouped vertical, 8 groups of 8.** Each group must name one of 8 signals or “none”:

> **bits per group = ⌈log_(2) 9⌉ = 4; control field = 8 × 4 = 32 bits**

> **total = 32 + 9 = 41 bits**

**Interpretation:** horizontal is 73 bits, grouped vertical is 41 bits and fully vertical is 16 bits. The saving in control-memory width is paid for in decoding logic and in the number of microinstructions, because a narrow word can assert fewer signals at once.

**Final Answer:** Horizontal 73 bits; fully vertical 16 bits; 8 × 8 grouped vertical 41 bits.

### 9.4 Microinstruction formats

| Format | Next-address information | Effect |
| --- | --- | --- |
| **Two-address field** | One field for the sequential successor, one for a branch target. | Flexible branching, but a wide word. |
| **Single-address field** | One field used either for the successor or for a branch. | Narrower word; the sequencer must decide how to use the field. |
| **Variable format** | A format bit selects between a control-signal word and a branch word. | Compact, but decoding costs time and the microprogram is harder to read. |

**Two-level control.** The teacher’s notes also distinguish single-level and two-level microprogramming. In single-level control, each microinstruction directly supplies the control signals. In two-level control, a microinstruction points to a **nano-instruction** that supplies the signals; the extra level compacts the control memory but adds a second access. The exam only needs the single-level model, but one sentence on the distinction shows that you know why a designer might accept the extra delay.

### 9.5 A microprogram for fetch and add

This is the “micro programs” part of the syllabus in its smallest useful form. Addresses are arbitrary; the point is the structure.

| Address | Micro-operation | Control signals | Next |
| --- | --- | --- | --- |
| 0 | MAR ← PC | PC_out, MAR_in | 1 |
| 1 | MDR ← M[MAR]; PC ← PC + 1 | MEM_read, MDR_in, PC_inc | 2 |
| 2 | IR ← MDR | MDR_out, IR_in | 3 |
| 3 | Map opcode to routine | Decoder enable | mapping |
| 10 | MAR ← IR(address) | IR_out, MAR_in | 11 |
| 11 | MDR ← M[MAR] | MEM_read, MDR_in | 12 |
| 12 | R1 ← R1 + MDR | ALU_add, R1_in | 0 |

Addresses 0–3 are the shared fetch routine. Addresses 10–12 are the add routine. The last microinstruction of every routine returns to address 0, which starts the next fetch. That single convention is what makes the control unit a loop rather than a one-shot sequence.

### 9.6 Advantages and disadvantages

| Advantages | Disadvantages |
| --- | --- |
| Flexible: change the microprogram to change the instruction set. | Slower: every microinstruction costs a control-memory access. |
| Regular design: the same structure serves a large, complex instruction set. | Extra memory and a wider control path. |
| Easy to patch bugs and add instructions after fabrication. | Decoding overhead for vertical formats. |
| Supports complex instructions and addressing modes (classic CISC). | Harder for a beginner to read and debug than fixed logic. |

### 9.7 Exam answer plan — microprogrammed control

1. Define it: control signals come from microinstructions in a control memory.
2. Draw the block diagram: control memory → MIR → signals; CAR → control memory; sequencer → CAR; mapping logic from the opcode.
3. Define microinstruction, micro-operation and microprogram in one line each.
4. Distinguish horizontal and vertical encoding, with the width trade-off.
5. Give the control-memory size calculation (512 × 40 = 2.5 KB).
6. Write a four-line fetch microprogram to show that you can use the structure.

## 10 · Microinstruction sequencing and execution

### 10.1 The next-address problem

Every microinstruction must answer two questions: which control signals to assert now, and which microinstruction to execute next. The first is a field in the microinstruction. The second is the job of the **microsequencer**.

> **next CAR ← one of { CAR + 1, branch target, mapping address, subroutine return }**

There are four standard sources for the next address:

| Source | When used | Example |
| --- | --- | --- |
| **Increment** | The next microinstruction is physically next. | Steps 0 → 1 → 2 → 3 of a fetch. |
| **Branch** | A condition or an unconditional jump selects a different address. | “If ZF = 1 go to the zero-result routine.” |
| **Mapping** | A new machine instruction starts, so the opcode selects its routine. | Opcode 25H → address 94H. |
| **Subroutine** | A shared micro-routine is called and must return. | Call a common “effective address” routine. |

> *Figure 8. The sequencer chooses among four next-address sources. Only one passes through the multiplexer at a time.*

### 10.2 Addressing fields and branching

The microinstruction’s next-address field is only an address; it does not say what to do with it. A separate branch-control field selects the source and states the condition. A typical branch field has three parts:

| Part | Meaning |
| --- | --- |
| **Branch condition** | Unconditional, zero, carry, sign, overflow, or an external flag. |
| **Branch type** | Jump to the address field, call a micro-subroutine, or return. |
| **Address selection** | Use the address field, use CAR + 1, or use the mapping address. |

If the condition is false, the sequencer ignores the branch address and increments CAR. If it is true, the branch address is loaded. This is exactly the behaviour of a conditional jump in a normal program, one level lower.

### 10.3 Execution of a microinstruction

Execution has three steps that are easy to state in an exam:

1. **Read.** The CAR addresses the control memory; the selected word is loaded into the MIR.
2. **Decode and drive.** The control fields are decoded as necessary and asserted on the datapath for one clock period (or more, if the operation needs it).
3. **Sequence.** The sequencer computes the next CAR from the next-address field, the branch condition and the flags.

A microinstruction that asserts several control signals performs several micro-operations in parallel. That is why horizontal microcode is fast: one wide word can open several register gates at once. A vertical microinstruction asserts fewer signals, so the same work needs more words.

**Worked example — mapping an opcode to a microprogram**

A machine has a 6-bit opcode. Each instruction’s microprogram starts at a 4-word boundary in control memory. Find the start address for opcode 25H. How many control-memory words are needed for 100 instructions that average 5 microinstructions each, plus a shared 4-word fetch routine?

**Question.** 6-bit opcode, routines at multiples of 4. Find the start address for 25H. Find the control-memory size for 100 instructions × 5 microinstructions + 4 fetch words.

**Solution.**

> **25H = 2 × 16 + 5 = 37 decimal**

> **start address = opcode × 4 = 37 × 4 = 148 decimal = 94H**

> **words = (100 × 5) + 4 = 504**

The next power of two is 512, so a 512-word control memory with a 9-bit CAR is enough. The mapping is a simple shift: multiplying the opcode by 4 appends two zero bits, which is why hardware mapping logic is often just a shift and a concatenation.

**Final Answer:** Start address 94H; 504 words needed, so a 512-word (9-bit) control memory.

### 10.4 Exam answer plan — microinstruction sequencing

1. State the problem: each microinstruction must name its successor.
2. List the four sources: increment, branch, mapping, subroutine return.
3. Draw the multiplexer and CAR diagram.
4. Explain the branch-control field: condition, type, address selection.
5. Give the three execution steps: read, drive, sequence.
6. Work the opcode-to-address mapping numerical.

## 11 · RISC and CISC

### 11.1 Two philosophies

**RISC** stands for *Reduced Instruction Set Computer*. It keeps the instruction set small, simple and fixed-length, and expects the compiler to build complex operations from simple ones. **CISC** stands for *Complex Instruction Set Computer*. It provides many instructions, some of which do a lot of work in one instruction, and expects the hardware to absorb that complexity.

The names describe a design tendency, not a binary law. A modern x86 is a CISC instruction set implemented on a RISC-like core: the decoder translates complex instructions into simple internal micro-operations. When you answer a comparison question, say “classic RISC” and “classic CISC” so that you are not trapped by the exceptions.

### 11.2 RISC

| Characteristic | Reason |
| --- | --- |
| Small, fixed-length instruction set | Fixed length makes fetch and decode regular; the next instruction boundary is known immediately. |
| Load/store architecture | Only `LOAD` and `STORE` touch memory; arithmetic works on registers. |
| Many general-purpose registers | Keeps operands in the register file and reduces memory traffic. |
| Simple addressing modes | Address computation stays out of the critical path. |
| One instruction per clock (ideally) | Enables deep, regular pipelining. |
| Hardwired control | Simple instructions do not need microcode. |
| Compiler does the optimisation | Hardware stays simple; software takes on scheduling and register allocation. |

**Advantages:** fast and predictable execution, efficient pipelining, simpler hardware, lower power, easier verification. **Disadvantages:** larger programs (more instructions to do the same work), higher instruction-fetch bandwidth, more pressure on the compiler.

### 11.3 CISC

| Characteristic | Reason |
| --- | --- |
| Large, complex instruction set | One instruction can implement a high-level operation. |
| Variable-length instructions | Short encodings for common operations, longer ones for complex operands. |
| Many addressing modes | Memory operands can be named directly, reducing the number of instructions. |
| Fewer registers | Historical cost of registers; memory operands are acceptable. |
| Multi-cycle instructions | Complex operations are sequenced internally. |
| Microprogrammed control | Microcode makes a large instruction set manageable and patchable. |
| Smaller programs | Each instruction does more, so fewer are needed. |

**Advantages:** compact code, less instruction-fetch traffic, easier assembly for complex operations, better fit for memory-constrained systems. **Disadvantages:** slower clock, complex decode, difficult pipelining, higher power, harder verification.

### 11.4 The comparison table

| Criterion | RISC | CISC |
| --- | --- | --- |
| Instruction set size | Small | Large |
| Instruction length | Fixed | Variable |
| Addressing modes | Few, simple | Many, complex |
| Registers | Many general-purpose | Fewer, with special-purpose roles |
| Memory access | Only load/store | Any instruction may use memory |
| CPI | Close to 1 | Often greater than 1 |
| Pipelining | Easy and regular | Difficult because of variable length |
| Control unit | Usually hardwired | Usually microprogrammed |
| Program size | Larger | Smaller |
| Power | Lower | Higher |
| Typical examples | ARM, MIPS, RISC-V, SPARC | x86, VAX, PDP-11, 8086 family |

### 11.5 Design issues

The syllabus asks for “design issues”, which means the trade-offs a designer must settle before choosing a style.

| Issue | Question the designer must answer |
| --- | --- |
| **Instruction encoding** | Fixed or variable length? Fixed simplifies fetch and decode; variable saves code size. |
| **Addressing modes** | How many, and how complex? Each mode adds decode logic and may add a cycle. |
| **Register file** | How many registers? More registers reduce memory traffic but cost chip area and increase access time. |
| **Pipelining** | Can instructions be fetched before the previous one finishes? Variable length and complex modes make this harder. |
| **Control implementation** | Hardwired for speed and simplicity, or microprogrammed for flexibility and complex instructions. |
| **Compiler support** | Who absorbs the complexity: the hardware or the compiler? |
| **Code size versus speed** | RISC usually trades code size for a simpler, faster pipeline; CISC does the reverse. |

**Worked example — comparing RISC and CISC execution time**

A CISC program executes 1,000,000 instructions at an average CPI of 4.0. The equivalent RISC program needs 1.4 times as many instructions but has an average CPI of 1.2. Both run at the same clock. Find the cycle counts, the execution times at 1 GHz, and the speed-up.

**Question.** CISC: 1,000,000 instructions, CPI 4.0. RISC: 1.4× instructions, CPI 1.2. Same clock, 1 GHz. Compare cycles, time and speed-up.

**Solution.**

> **CISC cycles = 1,000,000 × 4.0 = 4,000,000 cycles**

> **RISC instructions = 1.4 × 1,000,000 = 1,400,000**

> **RISC cycles = 1,400,000 × 1.2 = 1,680,000 cycles**

> **CISC time = 4,000,000 ÷ 10^(9) = 4.0 ms**

> **RISC time = 1,680,000 ÷ 10^(9) = 1.68 ms**

> **speed-up = 4,000,000 ÷ 1,680,000 = 2.38**

**Interpretation:** the RISC machine wins here because its CPI advantage (4.0 ÷ 1.2 = 3.33) is larger than its instruction-count penalty (1.4). If the RISC code needed 3.5 times as many instructions, the advantage would disappear: 3.5 × 1.2 = 4.2 cycles per CISC-equivalent instruction.

**Final Answer:** CISC 4.0 ms; RISC 1.68 ms; speed-up ≈ 2.38×.

Supplementary worked example. The CPI values are teaching figures, not measurements of a named processor. The method is the examinable part: cycles = instructions × CPI, time = cycles ÷ clock, speed-up = old time ÷ new time.

### 11.6 Exam answer plan — RISC and CISC

1. Define both acronyms and state the core philosophy in one sentence each.
2. Give four or five characteristics of each, not a long list.
3. Draw the comparison table: set size, length, addressing, registers, CPI, pipelining, control unit, program size, power.
4. Name two design issues: instruction encoding and who absorbs complexity (hardware or compiler).
5. Add the CPI numerical to show the trade-off quantitatively.
6. Close with the modern convergence: x86 translates to RISC-like micro-operations internally.

## 12 · Question bank and assignment coverage

This section covers the teacher’s 40-question document (Q18–Q28) and *Assignment 3.docx*. The teacher’s Module IV–VI question bank contains no Module 3 questions, so nothing is claimed from it here. Question wording is preserved exactly, including the original punctuation.

### 12.1 Coverage map

| Source | Question | Topic | Taught in |
| --- | --- | --- | --- |
| 40Q | Q18 | 8086 architecture; BIU and EU | Section 2 |
| 40Q | Q19 | Register organization | Section 3 |
| 40Q | Q20 | Instruction format | Section 4 |
| 40Q | Q21 | Instruction cycle | Section 5 |
| 40Q | Q22 | Addressing modes | Section 6 |
| 40Q | Q23 | Assembly program: count 0s and 1s | Section 12.2 |
| 40Q | Q24 | Instruction interpretation and sequencing | Section 7 |
| 40Q | Q25 | Hardwired control design | Section 8 |
| 40Q | Q26 | Microprogrammed control; microinstructions | Sections 9–10 |
| 40Q | Q27 | Hardwired versus microprogrammed | Sections 8–9 |
| 40Q | Q28 | RISC versus CISC | Section 11 |
| Assignment 3 | Groups 1–5 | Architecture, registers, format, cycle, addressing | Sections 2–6 |

### 12.2 Forty-question document, Q18–Q28 — model answers

**40Q Q18**

*Teacher 40-question document — not a University paper*

> Draw and explain the architecture of the 8086 microprocessor. Explain the functions of the Execution Unit and Bus Interface Unit.

**Model answer.** Draw Figure 1. State the headline numbers: 16-bit data bus, 20 address lines, 1 MB, 6-byte queue. The **BIU** interfaces the processor to the outside world: it holds the instruction queue, the four segment registers, IP, the address adder and the bus control logic; it performs every memory and I/O transfer and prefetches instructions. The **EU** executes: it contains the control system, instruction decoder, ALU, flag register, general-purpose registers and pointer/index registers; it computes effective addresses and asks the BIU for operands. The two units run asynchronously, so fetching overlaps execution. Add segmentation: physical = segment × 10H + offset, with 64 KB segments inside a 1 MB space. **Final:** two independent units, one external and one execution-oriented, coupled by the queue and internal buses.

**40Q Q19**

*Teacher 40-question document — not a University paper*

> Explain the register organization of 8086. Classify and explain:

> General-purpose registers
Segment registers
Pointer/index registers
Flag register
Instruction pointer.

**Model answer.** Draw the programmer’s model in five groups. **General purpose:** AX (accumulator, AH/AL), BX (base, BH/BL), CX (counter, CH/CL), DX (data, DH/DL); each is 16 bits and can be split into two 8-bit halves. **Segment:** CS, DS, SS, ES hold 16-bit bases; CS:IP fetches, SS:SP/BP addresses the stack, DS:BX/SI/DI addresses data, ES:DI addresses string destinations. **Pointer/index:** SP is the stack top, BP is a stack frame base (defaults to SS), SI and DI are source and destination indexes. **Flag register:** 16 bits, 9 defined — six status flags (CF, PF, AF, ZF, SF, OF) and three control flags (TF, IF, DF). **IP:** the offset of the next instruction in CS; it is changed by the BIU and by control-transfer instructions, not by an ordinary `MOV`. **Final:** five groups, with segmentation needed because 16-bit registers cannot hold a 20-bit address.

**40Q Q20**

*Teacher 40-question document — not a University paper*

> Explain the instruction format of 8086. Describe the different fields present in an 8086 instruction.

**Model answer.** The format is variable-length, 1 to 6 bytes. Draw Figure 3 and define each field: a 6-bit opcode; D (direction) choosing whether `reg` or `r/m` is the destination; W (word) choosing 8- or 16-bit operation; a 2-bit `mod`; a 3-bit `reg`; a 3-bit `r/m`; an optional 8- or 16-bit displacement; an optional 8- or 16-bit immediate. Explain `mod = 11` as register-direct and the other values as memory forms. Decode 89H D8H: opcode 100010 (MOV), D = 0, W = 1; mod = 11, reg = 011 (BX), r/m = 000 (AX); therefore `MOV AX, BX`. State the 6-byte maximum: 1 + 1 + 2 + 2. **Final:** 1–6 bytes, with opcode, D/W, ModR/M, displacement and immediate fields.

**40Q Q21**

*Teacher 40-question document — not a University paper*

> Explain the instruction cycle with a neat state diagram. Describe the different stages involved in instruction execution.

**Model answer.** Draw Figure 4: fetch → decode → execute → interrupt check → back to fetch, with an interrupt branch to the interrupt cycle. **Fetch:** MAR ← PC, MDR ← M[MAR], IR ← MDR, PC ← PC + length. **Decode:** split the opcode from the operands; compute the effective address if the operand is in memory. **Execute:** perform the ALU operation, memory transfer or branch. **Interrupt check:** if IF = 1 and a request is pending, save flags, CS and IP and load the vector. Distinguish clock cycle, machine cycle and instruction cycle; the 8086 minimum bus cycle is four T-states. **Final:** three phases plus an interrupt check, repeated for every instruction.

**40Q Q22**

*Teacher 40-question document — not a University paper*

> Explain the following 8086 addressing modes with suitable examples:

> Immediate
Register
Direct
Register indirect
Based
Indexed
Based indexed.

**Model answer.** Define an addressing mode and the effective address. For each mode give the EA rule, one example and the default segment: immediate `MOV AX, 2000H` (no EA); register `MOV AX, BX` (no EA); direct `MOV AX, [0500H]` (EA = 0500H, DS); register indirect `MOV AX, [SI]` (EA = SI, DS); based `MOV AL, [BP+0100H]` (EA = BP + disp, SS); indexed `MOV AX, [SI+2000H]` (EA = SI + disp, DS); based indexed `MOV AX, [BX+SI]` (EA = BX + SI, DS). Add the legal combinations and the `mod = 00, r/m = 110` direct special case. Work one numerical: DS = 2000H, BX = 0100H, SI = 0020H, disp = 0010H → EA = 0130H, physical = 20130H. **Final:** eight memory forms, all reducing to EA = base + index + displacement.

**40Q Q23**

*Teacher 40-question document — not a University paper*

> Write an 8086 assembly language program to count the number of 0s and 1s in an 8-bit binary number.

**Model answer.** The method is to rotate the byte eight times, test the bit that comes out in the carry flag, and increment a counter. The number of 0s is 8 minus the number of 1s. The program below assumes the byte is at offset 2000H in the data segment.

```asm
        MOV     AL, [2000H]     ; AL = the 8-bit number
        MOV     BL, 0           ; BL = count of 1s
        MOV     CL, 8           ; loop eight times
NEXT:   ROR     AL, 1           ; LSB moves to CF
        JNC     SKIP            ; CF = 0 means the bit was 0
        INC     BL              ; count a 1
SKIP:   DEC     CL
        JNZ     NEXT
        MOV     BH, 8
        SUB     BH, BL          ; BH = count of 0s
        MOV     [2001H], BL     ; store the 1s count
        MOV     [2002H], BH     ; store the 0s count
        HLT
```

**How it works.** `ROR AL,1` rotates the byte right; the bit that leaves bit 0 appears in CF and also re-enters at bit 7. After eight rotations the original byte is restored. `JNC SKIP` skips the increment when the tested bit was 0, so BL ends with the number of 1s. `SUB BH, BL` gives the number of 0s because every bit is either 0 or 1. For the byte 10110101B there are five 1s, so BL = 05H and BH = 03H. **Final:** 5 ones and 3 zeros for 10110101B; the two counts are stored at 2001H and 2002H.

**40Q Q24**

*Teacher 40-question document — not a University paper*

> Explain instruction interpretation and sequencing in a processor. Describe the steps involved in fetching, decoding and executing an instruction.

**Model answer.** Interpretation is decoding: the opcode selects the operation and the operand fields identify the source and destination. Express one operation in RTN, for example R3 ← [R1] + [R2], and explain the brackets and the arrow. Sequencing is ordering: at the instruction level the PC selects the next instruction (increment, branch, call, interrupt); at the micro-operation level a state counter or microinstruction address selects the next step. Give the fetch micro-operations with control signals: MAR ← PC; MDR ← M[MAR], PC ← PC + 1; IR ← MDR; decode. Then give the execute steps for a memory-source add: MAR ← IR(address); MDR ← M[MAR]; R1 ← R1 + MDR; update flags. Mention the four address-count formats (three-, two-, one-, zero-address) and one trade-off each. **Final:** decode names the operation and operands; sequencing orders the micro-operations that carry it out.

**40Q Q25**

*Teacher 40-question document — not a University paper*

> Explain the design of a hardwired control unit. Discuss the major design methods used for implementing hardwired control.

**Model answer.** Define the hardwired unit as fixed combinational logic driven by the IR, the flags and a timing state. Draw Figure 6: IR → opcode decoder; clock → sequence counter → state decoder; both into the logic array; the array drives the control lines. Give one equation, such as `MAR_in = T0` and `ALU_add = T3 · ADD_op + T4 · INC_op`, to show how opcode and timing are combined. Discuss the design methods: sequence counter (most common), ring counter (one-hot, no decoder), Johnson counter (2n states from n flip-flops), delay-element chain (cheap but drift-prone), and PLA/ROM logic (regular layout, still fixed after fabrication). State advantages (fast, no control memory, deterministic) and disadvantages (rigid, hard to modify, complex for large instruction sets). **Final:** fast and fixed; best for small instruction sets such as classic RISC.

**40Q Q26**

*Teacher 40-question document — not a University paper*

> Explain the design of a microprogrammed control unit. What is a microinstruction? Explain microinstruction sequencing and execution.

**Model answer.** Define a microinstruction as one control word that specifies a set of micro-operations and a next-address choice; a microprogram is the sequence of microinstructions for one machine instruction. Draw Figure 7: control memory → MIR → control signals; CAR → control memory; sequencer → CAR; mapping logic from the opcode. Explain horizontal versus vertical encoding and give the width trade-off (64 signals: 64 bits horizontal, 7 bits fully vertical, 32 bits for eight groups of eight). For sequencing, list the four next-address sources: increment, branch, mapping and subroutine return. For execution, give the three steps: read the control word into MIR, drive the datapath, compute the next CAR. Add the control-memory calculation: 512 × 40 bits = 2.5 KB, 9 address bits. **Final:** a microprogrammed unit trades one control-memory access for flexibility and a regular design.

**40Q Q27**

*Teacher 40-question document — not a University paper*

> Differentiate between hardwired and microprogrammed control units with respect to:

> Speed
Flexibility
Hardware complexity
Modification
Applications.

**Model answer.** Use a five-row table. **Speed:** hardwired is faster because signals come from gates; microprogrammed pays a control-memory access per microinstruction. **Flexibility:** hardwired is fixed; microprogrammed is changeable by rewriting the control store. **Hardware complexity:** hardwired logic grows irregularly with the instruction set; microprogrammed has a regular memory-plus-sequencer structure. **Modification:** hardwired needs redesign and refabrication; microprogrammed needs a new microprogram or a patch. **Applications:** hardwired suits RISC, small fixed instruction sets and embedded controllers; microprogrammed suits CISC, large instruction sets and processors that need field patches. **Final:** speed and simplicity favour hardwired; flexibility and complexity favour microprogrammed.

**40Q Q28**

*Teacher 40-question document — not a University paper*

> Explain RISC and CISC architectures. Compare them with respect to instruction set, instruction length, addressing modes, registers, pipelining and control-unit implementation.

**Model answer.** Define RISC as a small, fixed-length, load/store instruction set with many registers and hardwired control; define CISC as a large, variable-length set with complex addressing, fewer registers and microprogrammed control. Compare on the six named criteria: instruction set (small versus large), length (fixed versus variable), addressing modes (few versus many), registers (many versus fewer), pipelining (regular versus difficult), control unit (hardwired versus microprogrammed). Add program size (RISC larger) and power (RISC lower). State the design issues: encoding, addressing complexity, register-file size, pipeline regularity and who absorbs complexity — hardware or compiler. Add the CPI numerical: CISC 1,000,000 × 4.0 = 4,000,000 cycles; RISC 1,400,000 × 1.2 = 1,680,000 cycles; speed-up 2.38×. **Final:** RISC optimises the pipeline and the compiler; CISC optimises code density and the instruction set.

### 12.3 Assignment 3 coverage

The assignment asks for five topic groups. The wording below is copied from *Assignment 3.docx*.

*Teacher assignment — Assignment 3.docx*

| Assignment group | Where the full answer is | What to add for full marks |
| --- | --- | --- |
| 1 · Architecture of the 8086 | Section 2 and Figure 1 | BIU/EU split, 6-byte queue, 1 MB from 20 lines, one sentence on overlap. |
| 2 · Register organization | Section 3 and Figure 2 | Five groups, 8-bit halves, default segment pairings, 9 flags. |
| 3 · Instruction format with example | Section 4 and Figure 3 | Decode 89 D8 field by field; state the 6-byte maximum. |
| 4 · Instruction cycle with diagram | Section 5 and Figure 4 | Fetch micro-operations, interrupt check, clock versus machine cycle. |
| 5 · Addressing modes | Section 6 and Figure 5 | EA rule and default segment for each mode, plus one physical-address numerical. |

## 13 · MUSA question bank

*Student-association material — not a University paper*

**MUSA (Mumbai University Students Association) Question Bank of Computer Organization and Architecture**, S.E. Sem-III, NEP 2020, Winter Session 2026, for COMP/SAIML/AIDS/IOT/CS/DS. The same association’s **Practice Paper Set-1** (Winter 2025, 60 marks, 2 hours) supplies four Module 3 questions. Both are student-association documents, not verified University of Mumbai papers, and are labelled accordingly.

### 13.1 Question bank items

**MUSA QB Q2**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Draw and explain the architecture of 8086 with neat diagram.

**Model answer.** Use Figure 1 and the Section 2 answer plan: BIU (queue, segment registers, IP, address adder, bus control) and EU (control, decoder, ALU, flags, general registers, pointers), plus the 20-bit physical address and the fetch/execute overlap. **Final:** a two-unit diagram with one function per block.

**MUSA QB Q8**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Explain different addressing modes of 8086 with examples.

**Model answer.** Use the eight-mode table in Section 6.2, the EA formula, the default segments and the worked example DS = 2000H, BX = 0100H, SI = 0020H, disp = 0010H → EA = 0130H, physical = 20130H. **Final:** every mode reduces to EA = base + index + displacement, with direct mode as the `mod = 00, r/m = 110` special case.

**MUSA QB Q12**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Explain Register organization of 8086 processor.

**Model answer.** Use the five-group table in Section 3: general purpose (AX/BX/CX/DX with halves), segment (CS/DS/SS/ES), pointer/index (SP/BP/SI/DI), IP and flags (9 defined). Add the default pairings and the 1 MB / 64 KB reason for segmentation. **Final:** five groups, 14 named registers plus the flag register.

**MUSA QB Q13**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Explain Hardwired control unit. List and explain various methods to design hardwired control unit.

**Model answer.** Define the hardwired unit, draw Figure 6 and list the five design methods from Section 8.3: sequence counter, ring counter, Johnson counter, delay element, PLA/ROM logic. Add the Boolean equation example and two advantages and two disadvantages. **Final:** fast and fixed; best for small instruction sets.

**MUSA QB Q14**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Explain microprogrammed control unit design with suitable diagram.

**Model answer.** Use Figure 7 and Section 9.2: control memory, CAR, MIR, sequencer, mapping logic and subroutine register. Explain horizontal versus vertical encoding, give the 512 × 40 = 2.5 KB calculation, and add the four-line fetch microprogram. **Final:** a regular memory-plus-sequencer design that trades speed for flexibility.

**MUSA QB Q17**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Draw and explain microinstruction sequencing and execution organization.

**Model answer.** Draw Figure 8: the four next-address sources (increment, branch, mapping, subroutine return) into a multiplexer that loads the CAR. Explain the branch-control field (condition, type, address selection) and the three execution steps (read into MIR, drive the datapath, sequence the next CAR). Add the opcode-mapping numerical: 25H → 37 × 4 = 148 = 94H. **Final:** sequencing chooses the next microinstruction; execution asserts its control signals.

**MUSA QB Q20**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Draw and explain the instruction formats of 8086 with suitable examples.

**Model answer.** Draw Figure 3, define opcode, D, W, mod, reg, r/m, displacement and immediate, and decode 89H D8H as `MOV AX, BX`. State the 1–6 byte range and the 6-byte maximum with a 16-bit displacement and a 16-bit immediate. **Final:** variable length, with the ModR/M byte selecting register or memory operands.

**MUSA QB Q23**

*MUSA question bank (Winter 2026) — student association, not a University paper*

> Differentiate between the following:

> i) Hardwired control unit and Microprogrammed control unit
ii) RISC and CISC architecture

**Model answer.** For (i) use the five-row table in the Q27 answer: speed, flexibility, hardware complexity, modification and applications. For (ii) use the comparison table in Section 11.4: set size, instruction length, addressing modes, registers, memory access, CPI, pipelining, control unit, program size and power. **Final:** two compact tables, each with the basis of comparison in the first column.

### 13.2 Practice paper Set-1 (Winter 2025)

**MUSA Paper Q1(c) · 3 marks**

*MUSA Practice Paper Set-1 (Winter 2025) — student association, not a University paper*

> Differentiate between Hardwired control unit and Micro programmed control unit.

> *OR* Compare RISC and CISC architecture.

**Model answer.** For 3 marks, give four or five rows only: speed, flexibility, hardware, modification and typical use. Hardwired: faster, fixed, irregular logic, needs redesign, used in RISC. Microprogrammed: slower, flexible, regular memory-plus-sequencer, change the microcode, used in CISC. If you choose the RISC/CISC alternative, give five rows: instruction size, length, addressing, registers and control unit. **Final:** a five-row table is enough for 3 marks; do not write two long paragraphs.

**MUSA Paper Q1(f) · 3 marks**

*MUSA Practice Paper Set-1 (Winter 2025) — student association, not a University paper*

> Draw and explain Microinstruction sequencing organization.

**Model answer.** Draw the CAR, control memory, MIR and sequencer, with the four next-address sources feeding a multiplexer. Explain in two lines: increment for the next sequential microinstruction, branch for a conditional jump, mapping for a new opcode, subroutine for a shared routine. **Final:** the sequencer selects one source and loads the CAR.

**MUSA Paper Q2(b) · 7 marks**

*MUSA Practice Paper Set-1 (Winter 2025) — student association, not a University paper*

> Explain different addressing modes of 8086 with example.

> *OR* Explain the architecture of 8086 with neat diagram.

**Model answer.** For the addressing-mode option, give all eight modes with the EA rule, an example and the default segment, then one numerical. For the architecture option, draw Figure 1 and explain BIU and EU block by block. Either way, 7 marks needs a diagram plus about eight labelled points, not a long essay. **Final:** diagram first, then one short paragraph per block or per mode.

**MUSA Paper Q6(c) · 5 marks**

*MUSA Practice Paper Set-1 (Winter 2025) — Q6 is 15 marks for any three short notes, so each note is about 5 marks*

> Draw instruction cycle state diagram with interrupt.

**Model answer.** Draw Figure 4 and label fetch, decode, execute, interrupt check, interrupt cycle and the two return paths. Add the save sequence: flags, CS, IP; load the vector; return with `IRET`. State that the check happens after the current instruction completes. **Final:** a state diagram with one interrupt branch and one no-interrupt branch.

## 14 · Independent practice

These questions are **written for this guide**. They are not teacher questions and not University questions. Attempt them with the book closed, then mark yourself from the separate answer key in Section 15. Show the formula, the substitution and the unit in every numerical answer.

### Practice Questions

#### A · Basic (one definition or one formula)

1. How many address lines are needed to address 4 MB?
2. An 8086 has CS = 1200H and IP = 00A0H. Find the physical address of the next instruction.
3. Convert the segment:offset pair 1000H:0020H to a physical address, and give one other pair that names the same byte.
4. A segment register holds 4000H. What is the highest offset that stays inside that 64 KB segment, and what physical address does it give?
5. How many bytes are there in 64 KB? How many 16-bit words?
6. What is the maximum length of an 8086 instruction? Show the addition that gives it.

#### B · Intermediate (two or three steps)

7. DS = 3000H, BX = 0200H, SI = 0040H, displacement = 0010H. For `MOV AX, [BX+SI+0010H]`, find the effective address and the physical address.
8. SS = 5000H, BP = 0100H, displacement = 0020H. For `MOV AL, [BP+0020H]`, find the effective address and the physical address.
9. Decode the instruction bytes 8BH C3H. State the operation, the direction, the word size and both registers.
10. An 8086 runs at 8 MHz with a 4-T minimum bus cycle. Find the clock period, the bus-cycle time, and the time for 250 bus cycles.
11. A control memory has 256 microinstructions, each 32 bits wide. Find the number of address bits, the total size in bits and the total size in bytes.
12. A program executes 200,000 instructions at an average CPI of 3.5 on a 2 GHz processor. Find the cycle count and the execution time.

#### C · Advanced (comparison, multi-step, or a written justification)

13. A CISC program executes 500,000 instructions at CPI 5.0. The equivalent RISC program needs 1.6 times as many instructions at CPI 1.25. Both run at 1.5 GHz. Find both execution times and the speed-up.
14. A 64 KB block is transferred as 16-bit words. How many bus cycles are needed if the first word is aligned? How many if the first word is at an odd address? Explain the difference.
15. A processor has 64 control signals and a 10-bit next-address field. Compare the microinstruction width for (a) fully horizontal, (b) fully vertical one-at-a-time, and (c) four groups of sixteen signals with one signal per group.
16. A control memory must hold 80 instructions that average 6 microinstructions each, plus a shared 5-word fetch routine. Find the number of words and the minimum CAR width.
17. Write the control-signal equations for a four-state sequence: T0: MAR ← PC; T1: MDR ← M[MAR]; T2: IR ← MDR; T3: PC ← PC + 1 and decode.
18. The byte 11001010B is processed by the Q23 counting program. How many 1s and how many 0s are stored?

## 15 · Answer key

Mark the working, not only the final number. A correct answer with a missing unit loses marks in this module.

### Answers

#### A · Basic

1. **22 address lines.**
   4 MB = 4 × 2^(20) = 2^(22) bytes, so 22 lines. Check: 2^(22) = 4,194,304 bytes.
2. **120A0H.**
   base = 1200H × 10H = 12000H; physical = 12000H + 00A0H = 120A0H.
3. **10020H; another pair is 1002H:0000H.**
   1000H × 10H = 10000H; 10000H + 0020H = 10020H. For 1002H:0000H, 1002H × 10H = 10020H; adding 0000H leaves 10020H. The two pairs differ because segments overlap every 16 bytes.
4. **Offset FFFFH; physical 4FFFFH.**
   A 16-bit offset runs from 0000H to FFFFH. base = 4000H × 10H = 40000H; 40000H + FFFFH = 4FFFFH.
5. **65,536 bytes; 32,768 words.**
   64 KB = 64 × 1024 = 65,536 bytes. Each 16-bit word is 2 bytes, so 65,536 ÷ 2 = 32,768 words.
6. **6 bytes.**
   1 opcode byte + 1 ModR/M byte + 2 displacement bytes + 2 immediate bytes = 6 bytes. The 6-byte instruction queue is sized to hold exactly this worst case.

#### B · Intermediate

7. **EA = 0250H; physical = 30250H.**
   EA = 0200H + 0040H + 0010H = 0250H. base = 3000H × 10H = 30000H. Physical = 30000H + 0250H = 30250H.
8. **EA = 0120H; physical = 50120H.**
   EA = 0100H + 0020H = 0120H. BP defaults to SS, so base = 5000H × 10H = 50000H. Physical = 50000H + 0120H = 50120H. If a `DS:` override were used, only the base would change.
9. **8BH C3H = MOV AX, BX.**
   8BH = 1000 1011 → opcode 100010 (MOV), D = 1, W = 1. C3H = 1100 0011 → mod = 11, reg = 000 (AX), r/m = 011 (BX). D = 1 means `reg` is the destination, so AX ← BX. This is the second legal encoding of the move decoded in Section 4.3.
10. **T = 125 ns; bus cycle = 500 ns; 250 cycles = 125 µs.**
   T = 1 ÷ (8 × 10^(6)) = 125 ns. 4T = 500 ns. 250 × 500 ns = 125,000 ns = 125 µs.
11. **8 address bits; 8,192 bits; 1,024 bytes.**
   log_(2) 256 = 8. 256 × 32 = 8,192 bits. 8,192 ÷ 8 = 1,024 bytes = 1 KB.
12. **700,000 cycles; 350 µs.**
   cycles = 200,000 × 3.5 = 700,000. time = 700,000 ÷ (2 × 10^(9)) = 350 × 10^(−6) s = 350 µs.

#### C · Advanced

13. **CISC ≈ 1.67 ms; RISC ≈ 0.67 ms; speed-up 2.5×.**
   CISC cycles = 500,000 × 5 = 2,500,000. CISC time = 2,500,000 ÷ (1.5 × 10^(9)) = 1.6667 × 10^(−3) s ≈ 1.67 ms. RISC instructions = 1.6 × 500,000 = 800,000; RISC cycles = 800,000 × 1.25 = 1,000,000; RISC time = 1,000,000 ÷ (1.5 × 10^(9)) = 0.6667 ms ≈ 0.67 ms. Speed-up = 2,500,000 ÷ 1,000,000 = 2.5. The RISC machine executes more instructions but far fewer cycles per instruction.
14. **Aligned: 32,768 bus cycles. Odd start: 65,536 bus cycles.**
   64 KB ÷ 2 B per word = 32,768 words. An aligned word occupies one location in each of the two 8-bit banks and moves in one bus cycle. A word starting at an odd address straddles the banks, so it needs two bus cycles. Misalignment therefore doubles the bus traffic: 32,768 → 65,536 cycles.
15. **(a) 74 bits; (b) 17 bits; (c) 30 bits.**
   (a) 64 control bits + 10 next-address bits = 74. (b) ⌈log_(2) 65⌉ = 7 control bits + 10 = 17. (c) Each of four groups must name one of 16 signals or none: ⌈log_(2) 17⌉ = 5 bits; 4 × 5 = 20 control bits + 10 = 30. Grouped vertical keeps some parallelism while cutting the word from 74 to 30 bits.
16. **485 words needed; 512-word memory; 9-bit CAR.**
   80 × 6 = 480, plus 5 fetch words = 485. The next power of two is 512, and log_(2) 512 = 9. Rounding up is necessary because the CAR must address every word with a whole number of bits.
17. **MAR_in = T0; MEM_read = MDR_in = T1; IR_in = T2; PC_inc = DECODE = T3.**
   Each signal is active in exactly one timing state because this sequence does not depend on the opcode. If a state depended on the instruction, the term would be ANDed with the decoded opcode, for example `ALU_add = T3 · ADD_op`.
18. **Four 1s and four 0s.**
   11001010B has 1s in bit positions 7, 6, 3 and 1, so the 1s count is 4. The 0s count is 8 − 4 = 4. The program stores 04H at 2001H and 04H at 2002H.

## 16 · Common mistakes

### Errors that cost marks, and the fix

| Mistake | Why it is wrong | Correct approach |
| --- | --- | --- |
| Saying the 8086 has a 20-bit data bus | It has a 16-bit data bus and a 20-bit address bus. | 16 data lines → 2 bytes per transfer; 20 address lines → 1 MB. |
| Computing segment + offset without shifting | The segment register is a 16-bit base for a 20-bit space. | physical = (segment × 10H) + offset, or segment << 4 plus offset. |
| Mixing decimal 16 with hexadecimal digits | Multiplying by 16 and then adding hex is fine, but writing “2000 × 16 = 32000” and adding 0050H is not. | Stay in hex: 2000H × 10H = 20000H; then add 0050H. |
| Using AX, CX or DX as an address register | Only BX, BP, SI and DI may appear inside `[ ]`. | Move the value to BX/SI/DI first, or use a different mode. |
| Pairing BX with BP, or SI with DI | The base must be BX or BP; the index must be SI or DI; one of each at most. | Legal: BX+SI, BX+DI, BP+SI, BP+DI. Illegal: BX+BP, SI+DI. |
| Assuming BP defaults to DS | BP is the one offset register that defaults to SS. | BP → SS; BX, SI, DI and direct addresses → DS. |
| Saying the queue holds six instructions | It holds six *bytes*. | Six one-byte instructions, or one six-byte instruction. |
| Loading IP with `MOV IP, 1000H` | IP is not a general destination register. | Change it with `JMP`, `CALL`, `RET` or an interrupt. |
| Confusing the D and W bits | D selects the destination direction; W selects byte or word. | D = 1 → `reg` is destination; W = 1 → 16-bit operation. |
| Saying `mod = 11` means memory | `mod = 11` means register-direct; the other values mean memory. | mod = 00/01/10 → memory with 0/8/16-bit displacement. |
| Forgetting the direct-address special case | `mod = 00, r/m = 110` is not “BP with no displacement”. | It encodes a 16-bit direct address. |
| Putting the immediate before the displacement | The order on the wire is opcode, ModR/M, displacement, immediate. | The immediate is the last field. |
| Treating the instruction cycle as one clock | An instruction takes many clock cycles and several bus cycles. | Distinguish T-state, machine cycle and instruction cycle. |
| Saying hardwired control is slower | It is faster: no control-memory access. | Hardwired is faster but rigid; microprogrammed is slower but flexible. |
| Saying microprogrammed control has no memory | It is built around a control memory. | Control memory (ROM or writable store) holds the microinstructions. |
| Swapping horizontal and vertical encoding | Horizontal is wide (one bit per signal); vertical is narrow (encoded). | Horizontal = more bits, more parallelism; vertical = fewer bits, more decoding. |
| Using ⌈log_(2) n⌉ for vertical encoding | The field must also encode “no signal”. | Use ⌈log_(2)(n + 1)⌉. |
| Claiming RISC is always faster | A RISC program usually needs more instructions. | Compare cycles = instructions × CPI, not CPI alone. |
| Using 1 KB = 1000 bytes | Memory sizes use powers of two. | 1 KB = 1024 bytes unless the question says otherwise. |
| Giving a physical address with no H suffix | “20050” could be decimal. | Write 20050H and state that it is hexadecimal. |

## 17 · Last-minute revision sheet

### Ten minutes before the paper

**8086 numbers.** 16-bit data bus, 20 address lines, 1 MB, 64 KB segments, 16 non-overlapping segments, 65,536 possible bases, 6-byte queue, 1–6 byte instructions, 5/8/10 MHz versions.

**Physical address.** physical = (segment × 10H) + offset = (segment << 4) + offset. Always keep the H suffix. 2000H:0050H → 20050H.

**BIU.** Queue, CS/DS/SS/ES, IP, address adder, bus control. It performs every external transfer and prefetches. A branch flushes the queue.

**EU.** Control, decoder, ALU, flags, AX/BX/CX/DX, SP/BP/SI/DI. It computes effective addresses and executes from the queue.

**Registers.** AX accumulator, BX base, CX counter, DX data; each split AH/AL etc. CS:IP code, DS data, SS:SP/BP stack, ES:DI extra. BP is the only offset register that defaults to SS. IP cannot be loaded by `MOV`.

**Flags.** 16 bits, 9 defined: CF, PF, AF, ZF, SF, OF (status); TF, IF, DF (control).

**Instruction format.** Opcode 6, D 1, W 1; mod 2, reg 3, r/m 3; displacement 0/8/16; immediate 0/8/16. Maximum 1+1+2+2 = 6 bytes = 48 bits. D = 1 → reg is destination. W = 1 → word. mod = 11 → register.

**Instruction cycle.** Fetch → decode → execute → interrupt check. Fetch: MAR←PC, MDR←M[MAR], IR←MDR, PC←PC+length. Interrupt: save flags, CS, IP; load vector; `IRET`.

**Addressing.** EA = base + index + displacement. Base = BX or BP; index = SI or DI. Modes: immediate, register, direct, register indirect, based, indexed, based indexed, based indexed with displacement. Direct special case: mod = 00, r/m = 110.

**Interpretation.** Opcode → operation; operand fields → operands. RTN: R3 ← [R1] + [R2]. Formats: three-, two-, one- and zero-address.

**Hardwired CU.** Fixed combinational logic from IR + flags + timing state. Methods: sequence counter, ring counter, Johnson counter, delay element, PLA/ROM. Fast, rigid, no control memory. Suits RISC.

**Microprogrammed CU.** Control memory + CAR + MIR + sequencer + mapping logic. Horizontal = one bit per signal (wide); vertical = encoded (narrow, ⌈log_(2)(n+1)⌉). Slower by one memory access; flexible. Suits CISC.

**Micro-sequencing.** Next CAR from increment, branch, mapping or subroutine return. Execution: read into MIR, drive signals, compute next CAR.

**RISC vs CISC.** Small/fixed/many registers/load-store/hardwired/CPI ≈ 1 versus large/variable/fewer registers/memory operands/microprogrammed/CPI > 1. Compare cycles = instructions × CPI, never CPI alone.

**Answer discipline.** Draw the diagram first if the question says “with a neat diagram”. Define every abbreviation at first use. For a numerical, write the formula, substitute with units, show the arithmetic, box the answer, and add one line of interpretation. For a comparison, use a table with the basis in the first column.

## 18 · References and verification notes

### Sources used

- **Official syllabus.** University of Mumbai, Faculty of Science and Technology, B.E. Computer Science and Engineering (Artificial Intelligence and Machine Learning), Semester III and IV, Course 2023114 *Computer Organization and Architecture*, 2025–26. Module 3 row: “Processor Organization and Control Unit Design”, 8 hours, CO3. The row, hours and CO mapping were checked against the published syllabus tables; the wording is quoted verbatim. [mu.ac.in syllabus PDF](https://mu.ac.in/old/wp-content/uploads/2025/06/6.21-N-B.E.-AI-ML-sem-III-IV.pdf).
- **Teacher notes.** *chapter 3 coa.docx*, supplied in `COA.zip`. Used for the 8086 architecture, register organization, instruction set overview, addressing modes, control-unit description, microinstruction sequencing and the RISC/CISC comparison. The guide follows the teacher’s order and terminology.
- **Teacher assignment.** *Assignment 3.docx*, supplied in `COA.zip`. Used to confirm the five required topic groups: architecture, register organization, instruction format, instruction cycle and addressing modes. Wording reproduced in Section 12.3.
- **Teacher question bank.** *Computer Organization 40 questions.docx*, Module 3, Q18–Q28. Wording preserved. This is a question-bank document, not a University paper. The separate *question bank.docx* contains no Module 3 questions.
- **Student association material.** MUSA *Question Bank of Computer Organization and Architecture* (Winter 2026) and MUSA *Practice Paper Set-1* (Winter 2025, 60 marks, 2 hours). Used for additional practice and clearly labelled; **not** verified University of Mumbai papers.
- **Background references for the supplementary explanations.** Stallings, *Computer Organization and Architecture*; Patterson and Hennessy, *Computer Organization and Design*; Hamacher, Vranesic and Zaky, *Computer Organization*; Tanenbaum, *Structured Computer Organization*; Mano, *Computer System Architecture*. These were not supplied with the course and are listed only as standard sources for the general explanations; no page numbers are claimed.

### What was verified

- Every numerical in Sections 2–15 was recomputed independently in Python: 20050H, 3FFFEH and FFFF0H physical addresses; 1 MB / 64 KB / 16 segments; 20130H and 30210H effective-address examples; 120A0H, 10020H, 4FFFFH, 30250H and 50120H practice answers.
- Instruction-length and queue arithmetic: 6 bytes = 48 bits; one maximum-length instruction per 6-byte queue.
- Control-memory arithmetic: 512 × 40 = 20,480 bits = 2.5 KB with a 9-bit CAR; 256 × 32 = 8,192 bits = 1 KB; 504 and 485 words both round to a 512-word, 9-bit memory.
- Encoding widths: 73 / 16 / 41 bits for 64 signals with a 9-bit next address; 74 / 17 / 30 bits with a 10-bit next address.
- Timing: 5 MHz → 200 ns, 0.8 µs bus cycle, 3.2 µs instruction, 320 µs loop; 8 MHz → 125 ns, 0.5 µs bus cycle, 125 µs for 250 cycles.
- CPI comparisons: 4,000,000 versus 1,680,000 cycles (2.38×); 2,500,000 versus 1,000,000 cycles (2.5×).
- Word alignment: 64 KB = 32,768 aligned word transfers, 65,536 misaligned.
- The bit counts in the Q23 program example: 10110101B → 5 ones, 3 zeros; 11001010B → 4 ones, 4 zeros.
- Question wording in Sections 12 and 13 was copied from the supplied documents, including the original punctuation and the “Micro programmed” spelling in the MUSA paper.

### Notes and limitations

- No verified University of Mumbai end-semester paper for course 2023114 was present in the supplied material. Nothing in this guide is labelled as a verified University question.
- The Module 3 syllabus row lists **no self-study topic**. Nothing here is marked self-study.
- The 8086 timing examples are teaching assumptions, labelled as such. Real instruction timings vary by opcode and by the number of wait states; no datasheet cycle count is claimed.
- “Classic RISC” and “classic CISC” are used deliberately. Modern processors mix the two, and the guide says so rather than pretending the boundary is absolute.
- MUSA material is student-association material, not University of Mumbai material, and is attributed to MUSA wherever it appears.
- Practice questions in Section 14 and the supplementary worked examples are written for this guide. They are labelled and are not attributed to the teacher or the University.
- Diagrams are hand-authored SVG in this page. No generated images are used.

### Attribution

Teaching content adapted from the teacher-supplied chapter, assignment and question bank listed above. Syllabus text quoted from the official University of Mumbai document. Explanatory prose, additional examples, numerical practice and the SVG diagrams are **supplementary clarification** written for this guide. Student-association material is attributed to MUSA and is not presented as University material.
