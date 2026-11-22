# COA Module 5

*I/O Organization*

B.E. CSE (AI & ML) · Sem III · Course 2023114 · 4 teaching hours · CO5

Built from *Assignment 5.docx*, the supplied question banks, the MUSA practice material and the official University of Mumbai syllabus.

## Syllabus and scope

**Official module name:** I/O Organization · **Teaching hours:** 4 · **Course outcome:** CO5.

*Official University of Mumbai syllabus, course 2023114 (Module 5 row)*

“Introduction to Bus, Types of Buses and Bus Standards: Comparative study of bus standards. Bus Arbitration. I/O interface, I/O channels, I/O modules and I/O processors. Programmed I/O, Interrupt driven I/O, DMA.”

The official row lists no self-study topic for this module.

The syllabus is short but the question bank is specific. This guide follows the syllabus boundary and then teaches every term that the supplied questions name.

| Status | Content | Why it is here |
| --- | --- | --- |
| **Prescribed** | Bus introduction; types of buses; comparative study of bus standards; bus arbitration; I/O interface; I/O channels, modules and processors; programmed I/O; interrupt-driven I/O; DMA. | Named in the official Module 5 row. |
| **Supplementary** | Memory-mapped vs isolated I/O; synchronous vs asynchronous buses; bus bandwidth calculations; interrupt latency and overhead; DMA cycle stealing and cache coherence; PCIe as the successor to PCI. | Needed to answer the numericals and the “compare / explain” parts of the question bank. These are clearly marked as supplementary where they go beyond the syllabus line. |

**Exam pattern.** The end-semester paper is 60 marks in 2 hours, with six 20-mark questions. Question 1 is compulsory and mixes modules; you attempt any three of the remaining questions. Module 5 is only 4 teaching hours, so it usually appears as one part of a larger question (often 5–10 marks) rather than as a full 20-mark question. The DMA numerical is the most likely numerical from this module.

*What this guide does not claim*

No verified University of Mumbai question paper for course 2023114 was supplied. The questions reproduced in Section 11 are from the teacher’s question bank and the 40-question document. MUSA questions are student-association material. Nothing here is labelled as a verified University question.

## 1 · The I/O problem

### 1.1 Why I/O needs its own organization

A processor can execute an instruction in a fraction of a nanosecond, while a keyboard produces a character when a human presses a key and a disk may take milliseconds to reach a block. Peripherals also differ wildly: a mouse sends a few bytes per second, a camera sends hundreds of megabytes per second, and each device uses its own voltage levels, connectors and protocol. The processor cannot connect to every device directly. **I/O organization** is the set of buses, interfaces, controllers and transfer methods that let the CPU communicate with many different devices without knowing their electrical details.

Three problems must be solved:

| Problem | Why it is hard | Typical solution |
| --- | --- | --- |
| **Speed mismatch** | The CPU is orders of magnitude faster than most peripherals. Waiting for a device wastes processor time. | Buffering, interrupts and DMA let the CPU start a transfer and do other work. |
| **Device variety** | Different connectors, voltages, data formats (serial/parallel, analog/digital) and protocols. | An I/O interface or module hides the device details behind a standard bus interface. |
| **Addressing and control** | The CPU must select one device, state the operation, move data and learn when the operation finished. | Address decoding, control registers, status registers and interrupt or DMA handshaking. |

### 1.2 The I/O subsystem at a glance

At the top, the CPU and memory sit on the system bus. Below it, one or more **I/O modules** (also called controllers or interfaces) connect devices. A module may serve one device or several. In larger systems, a **channel** or **I/O processor** sits between the CPU and the modules and runs its own I/O program.

> **CPU ↔ system bus ↔ I/O module ↔ device**

The CPU never sees the device’s internal signals. It sees a small set of registers inside the module: a **data register** to move a word, a **status register** to ask “ready / busy / error?”, and a **control register** to start an operation or set a mode.

### 1.3 Memory-mapped and isolated I/O

There are two ways to give the CPU access to those registers.

| Feature | Memory-mapped I/O | Isolated (port-mapped) I/O |
| --- | --- | --- |
| Address space | Device registers occupy addresses in the normal memory space. | A separate I/O address space is used. |
| Instructions | Ordinary load and store instructions work on device registers. | Special instructions such as `IN` and `OUT`. |
| Control lines | Normal memory read/write lines. | Separate I/O read/write lines, plus a line that distinguishes memory from I/O. |
| Address space cost | Consumes part of the memory address range. | Does not reduce the memory address range. |
| Programming | Flexible: any instruction that can address memory can address a register. | Restricted to the I/O instructions, but keeps I/O separate from memory. |
| Typical use | Microcontrollers, memory-mapped peripherals, modern SoCs. | Intel-style processors with an I/O address space (for example the 8086 family). |

In an exam, a single sentence is enough: memory-mapped I/O uses normal memory instructions and addresses, while isolated I/O uses a separate port space and special instructions. The 8086 supports both.

### 1.4 The three transfer techniques, previewed

| Technique | Who moves each word? | CPU involvement |
| --- | --- | --- |
| **Programmed I/O** | The CPU, one word at a time, after polling the status register. | Continuous; the CPU busy-waits. |
| **Interrupt-driven I/O** | The CPU, one word at a time, inside an interrupt service routine. | Per word, but only when the device is ready. |
| **DMA** | The DMA controller, directly between device and memory. | Only at setup and completion. |

The rest of this module explains the buses that carry these transfers, the arbitration that decides who may use a bus, the interface that connects a device, and then each transfer technique in detail.

## 2 · Buses: structure and types

### 2.1 What a bus is

A **bus** is a set of shared electrical lines with a defined protocol that lets several units communicate. A unit that can start a transfer is a **bus master**; a unit that responds is a **bus slave**. The CPU is normally the master, but a DMA controller or another processor can also become master. Because the lines are shared, only one master may drive them at a time; this is why bus arbitration (Section 3) is needed.

> *Figure 1. A system bus has three functional groups. The address bus selects, the data bus carries, and the control bus coordinates.*

### 2.2 Data bus, address bus and control bus

| Bus | Direction | What it carries | Width determines |
| --- | --- | --- | --- |
| **Data bus** | Bidirectional | The actual data word between CPU, memory and I/O. | How many bits move in one transfer (8, 16, 32, 64 …). |
| **Address bus** | Unidirectional (master → slaves) | The address of the memory location or I/O register being selected. | The size of the address space: n lines → 2^(n) locations. |
| **Control bus** | Individual lines, both directions | Read/write, memory or I/O select, interrupt request and acknowledge, bus request and grant, clock, reset. | Which operation is performed and how the transfer is synchronised. |

The address bus is unidirectional because the master always names the target. The data bus is bidirectional because a read moves data towards the CPU and a write moves it away. The control bus is not one wire but a collection of single-purpose lines, each with its own direction and timing.

### 2.3 Bus width, bandwidth and transfer time

> **address space = 2^(address lines) locations**

> **bytes per transfer = data lines ÷ 8**

> **bandwidth = bytes per transfer × transfers per second**

> **transfer time = amount of data ÷ bandwidth**

For a bus that completes one transfer per clock cycle, the nominal bandwidth is:

> **bandwidth = (data lines ÷ 8) × clock frequency**

This is the *nominal* or peak value. Real bandwidth is lower because of wait states, arbitration, address phases, refresh and protocol overhead. Say “nominal” when you use the formula.

**Supplementary worked example — bus bandwidth**

A system bus has 32 data lines and runs at 66 MHz. One transfer is completed per clock cycle. Find the address space if the address bus has 24 lines, and the nominal data bandwidth.

**Question.** 32 data lines, 24 address lines, 66 MHz, one transfer per cycle. Find the address space and the nominal bandwidth.

**Solution.**

> **address space = 2^(24) bytes = 16,777,216 bytes = 16 MB**

> **bytes per transfer = 32 ÷ 8 = 4 bytes**

> **bandwidth = 4 × 66 × 10^(6) = 264 × 10^(6) B/s = 264 MB/s**

**Interpretation:** 264 MB/s is the peak. If the bus needs two clock cycles per transfer (an address phase and a data phase), the sustained value falls to 132 MB/s.

**Final Answer:** 16 MB address space; nominal bandwidth 264 MB/s.

Supplementary example written for this guide, not a teacher problem.

### 2.4 Synchronous and asynchronous buses

| Feature | Synchronous bus | Asynchronous bus |
| --- | --- | --- |
| Timing | All transfers are tied to a common clock. | Transfers use handshake signals (request / acknowledge). |
| Speed | Fast for devices that can meet the clock. | Adapts to each device; a slow device simply takes longer. |
| Design | Simpler protocol, but the bus must be short enough that signals arrive within one clock. | More control lines and logic, but tolerant of distance and mixed device speeds. |
| Typical use | Processor-local buses, memory buses, PCI. | Legacy peripheral buses, handshaked device interfaces, some on-chip buses. |

### 2.5 Single-bus and multiple-bus organisation

A **single-bus** system connects CPU, memory and all I/O to one shared bus. It is cheap and simple, but every transfer competes for the same lines, so the bus becomes a bottleneck. A **multiple-bus** or hierarchical system uses several buses: a fast processor-local bus, a memory bus, and one or more I/O buses connected by bridges. This lets the CPU and memory exchange data while I/O traffic proceeds on a separate bus, and it lets each bus run at a speed suited to its devices. Modern systems are hierarchical: CPU ↔ cache ↔ memory bus ↔ PCIe root complex ↔ USB/SATA controllers.

### 2.6 The bus transaction

1. **Request and arbitration:** a master asks for the bus; the arbiter grants it.
2. **Address phase:** the master puts the target address on the address bus and asserts the memory or I/O select line.
3. **Data phase:** for a write, the master drives data; for a read, the slave drives data. The read/write line states the direction.
4. **Acknowledgment:** the slave asserts ready or acknowledge when the transfer is complete; wait states may extend the cycle.
5. **Release:** the master releases the bus, and the arbiter may grant it to another master.

### 2.7 Exam answer plan

1. Define a bus and distinguish master from slave.
2. Draw the CPU–memory–I/O block diagram with the three buses.
3. Explain data, address and control buses: direction, function, and what the width determines.
4. Give the bandwidth formula and one numerical.
5. Contrast synchronous and asynchronous buses, and single-bus with multiple-bus organisation.
6. List the phases of a bus transaction.

## 3 · Bus arbitration

### 3.1 Why arbitration is needed

A bus is a shared resource, and only one master can drive it at a time. The CPU is the usual master, but a DMA controller, a network card or a second processor may also want the bus. If two masters drive the address or data lines together, the signals collide and the transfer is garbage. **Bus arbitration** is the process that decides which requesting master gets the bus next, and it must do so without corrupting a transfer that is already in progress.

A good arbitration scheme has to answer three questions: who asks, who decides, and how the decision reaches the winner. The first two separate centralized from distributed schemes.

### 3.2 Centralized arbitration

In **centralized arbitration**, one **bus arbiter** — often part of the CPU or the chipset — receives all requests and issues one grant. The arbiter can apply a fixed priority, a rotating priority (round-robin) or a programmable priority. There are three standard wiring methods.

**(a) Daisy chaining.** Every master shares one bus-request line. The grant line does not go to all masters at once; it passes from the arbiter through device 1 to device 2 and so on. A device that wants the bus asserts the request line. When the arbiter grants, the grant propagates along the chain and stops at the first requesting device. That device takes the bus and does not pass the grant further. The device nearest the arbiter therefore has the highest priority, and priority is fixed by physical position. Daisy chaining needs very few wires and is cheap, but a device far down the chain waits while the grant passes through every earlier device, and a faulty device can break the chain for everyone after it.

**(b) Polling.** The arbiter does not wait for a request line from every device. Instead it sends a poll signal — usually a device number on a set of poll lines — and asks, in effect, “Do you want the bus?” Each device answers only when its number appears. The first device that says yes gets the grant. Priority is set by the polling order, which can be changed in software. Polling uses fewer request lines than independent requests, but it spends time asking devices that do not want the bus, so the worst-case delay grows with the number of devices.

**(c) Independent requests.** Each master has its own request line and its own grant line to the arbiter. All requests arrive at once, and the arbiter chooses immediately using its priority logic. This is the fastest of the three because there is no chain propagation and no polling sequence. It is also the most expensive in pins and wiring, and it does not scale well to a large number of masters.

| Method | Lines | Priority | Speed | Weak point |
| --- | --- | --- | --- | --- |
| Daisy chaining | One request, one grant that passes through devices | Fixed by position; nearest is highest | Moderate; grant propagation delay | One faulty device can block later devices. |
| Polling | Poll lines plus a response | Set by polling order; can be changed | Slower as device count grows | Time wasted polling idle devices. |
| Independent request | One request and one grant per master | Fully programmable | Fastest | Many pins and wires; poor scaling. |

### 3.3 Distributed arbitration

In **distributed arbitration**, there is no central arbiter. Every master contains the logic needed to compete for the bus, and the decision emerges from the group. Two common ideas appear in textbooks.

**Self-selection.** Each master has a unique priority code and drives it onto a set of shared arbitration lines when it wants the bus. The lines use wired-OR or wired-AND logic, so the highest-priority code dominates. Each master compares the code on the lines with its own; if it sees a higher code, it withdraws, and the winner proceeds. There is no central point of failure, and the decision is fast, but the priority codes and the arbitration logic must be designed carefully.

**Collision detection.** A master listens to the bus while it transmits. If two masters start together, the resulting signal differs from what either sent, and both detect a collision. They stop, wait for a random or priority-based back-off, and try again. This is the method used by Ethernet (CSMA/CD). It is simple and needs no arbiter, but collisions waste time and the worst-case delay is not bounded unless the protocol adds priorities.

| Feature | Centralized | Distributed |
| --- | --- | --- |
| Decision maker | One arbiter | The masters themselves |
| Wiring | More centralized control lines; fewer per-device lines in daisy chain | Shared arbitration lines; no central unit |
| Speed | Fast with independent requests; slower with daisy chain or polling | Fast self-selection; collision detection loses time on conflicts |
| Fault tolerance | The arbiter is a single point of failure | No single arbiter, but a faulty master can still disturb the bus |
| Scalability | Independent requests need many pins; polling slows with size | Better for larger systems, at the cost of more complex logic |
| Typical use | Processor buses, PCI, DMA arbitration | Multiprocessor backplanes, some network and industrial buses |

### 3.4 What the examiner wants

A full answer defines arbitration, names the two families, draws or describes at least two centralized methods, explains distributed arbitration, and compares them on wiring, priority, speed and fault tolerance. A numerical is unlikely here; the marks are for the mechanism and the comparison. If the question says “with a diagram”, a simple chain of boxes with REQ and GRANT arrows is enough — do not spend ten minutes on artwork.

## 4 · Bus standards: PCI, USB and SATA

### 4.1 What a bus standard fixes

A **bus standard** is an agreed specification for connectors, signal levels, timing, protocol and mechanical dimensions, so that devices from different manufacturers can work together. Without standards, every card would need its own slot and its own driver. The syllabus asks for a comparative study, and the question bank names PCI, USB and SATA. They are not competitors in one market: PCI (and its successor PCIe) connects expansion cards inside the box, USB connects external peripherals, and SATA connects storage devices.

### 4.2 PCI — Peripheral Component Interconnect

PCI is a parallel, synchronous, shared bus introduced in the early 1990s to replace several proprietary expansion buses. A 32-bit PCI slot has 32 multiplexed address/data lines, so the address and data phases share the same wires. It runs at 33 MHz or 66 MHz and supports 32-bit or 64-bit widths. Because the bus is shared, only one card can transfer at a time, and the chipset arbitrates between the cards and the CPU. PCI supports burst transfers, parity checking and plug-and-play configuration: the operating system can read a card’s configuration space and assign its address and interrupt automatically.

> **32-bit PCI at 33 MHz: 4 B × 33.33 × 10^(6) ≈ 133 MB/s**

> **64-bit PCI at 66 MHz: 8 B × 66.66 × 10^(6) ≈ 533 MB/s**

Those are peak values. Real PCI transfers lose cycles to arbitration, address phases and wait states. PCI’s shared parallel wires also become hard to route at higher speeds, which is why it was replaced by PCI Express. **PCIe** is not a wider PCI; it is a completely different serial, point-to-point, packet-based interconnect. Each lane carries data in both directions, and a slot may use 1, 4, 8 or 16 lanes. A PCIe 3.0 lane carries about 985 MB/s per direction, a 4.0 lane about 1.97 GB/s, and a 5.0 lane about 3.94 GB/s. The important comparison for an exam is that PCI is a shared parallel bus while PCIe is a switched serial fabric.

### 4.3 USB — Universal Serial Bus

USB was designed for external peripherals: keyboards, mice, printers, cameras, storage and charging. It is a serial bus with a strict **host-controlled** model. The host controller polls devices; a device never starts a transfer on its own. The physical topology is a tiered star: the host controller connects to hubs, and hubs connect to devices or more hubs, allowing up to 127 devices per host controller. USB supports hot-plugging and provides power over the cable, which is why it replaced separate power adapters for many small devices.

| Version | Signalling rate | Approximate theoretical payload | Note |
| --- | --- | --- | --- |
| USB 1.1 | 12 Mb/s (full speed) | 1.5 MB/s | Keyboards, mice, old printers. |
| USB 2.0 | 480 Mb/s (high speed) | 60 MB/s | Still common for low-cost devices. |
| USB 3.2 Gen 1 | 5 Gb/s | 625 MB/s | Formerly USB 3.0; 8b/10b encoding. |
| USB 3.2 Gen 2 | 10 Gb/s | 1.21 GB/s | 128b/132b encoding. |
| USB4 | up to 40 Gb/s | up to about 5 GB/s | Tunneled PCIe and DisplayPort; USB-C connector. |

USB defines four transfer types: **control** for configuration, **bulk** for large data with no timing guarantee, **interrupt** for small periodic data such as a mouse, and **isochronous** for audio and video that need a steady rate but can tolerate an occasional lost sample. A USB answer that mentions host control, hot-plug, power and the four transfer types is usually enough.

### 4.4 SATA — Serial ATA

SATA connects storage devices. It replaced the wide parallel ATA ribbon cable with a thin serial cable and, more importantly, changed the topology from a shared bus to a **point-to-point link**: each SATA port serves one device. That removes the master/slave jumper problem of PATA and allows hot-swapping on controllers that support it. SATA uses 8b/10b encoding, so ten bits are transmitted for every eight bits of payload; the useful rate is therefore 80% of the signalling rate.

> **SATA 1.5 Gb/s → 150 MB/s  ·  SATA 3 Gb/s → 300 MB/s  ·  SATA 6 Gb/s → 600 MB/s**

SATA also supports Native Command Queuing (NCQ), which lets a drive reorder outstanding requests to reduce seek and rotational delay. It is a storage interconnect, not a general-purpose expansion bus: it carries disk commands and data, not arbitrary device registers.

### 4.5 Comparing the standards

| Feature | PCI | USB | SATA |
| --- | --- | --- | --- |
| Type | Parallel, shared, synchronous | Serial, host-controlled, tiered star | Serial, point-to-point |
| Typical use | Expansion cards inside a computer | External peripherals and charging | Hard disks and SSDs |
| Data width | 32 or 64 bits | 1 bit per direction (serial) | 1 bit per direction (serial) |
| Nominal rate | 133–533 MB/s | 1.5 MB/s to several GB/s depending on version | 150 / 300 / 600 MB/s |
| Hot-plug | Generally no | Yes | Yes on supported controllers |
| Topology | Shared bus with arbitration | Host + hubs + devices | One host port to one drive |
| Successor | PCI Express (serial, switched) | USB 3.x / USB4 | SATA Express / NVMe over PCIe |

**Supplementary worked example — comparing nominal rates**

A 32-bit PCI bus runs at 33 MHz and completes one transfer per cycle. A SATA III link runs at 6 Gb/s with 8b/10b encoding. A USB 2.0 link runs at 480 Mb/s. Compare their nominal payload rates in MB/s.

**Solution.**

> **PCI: 32 ÷ 8 = 4 B per transfer; 4 × 33.33 × 10^(6) ≈ 133 MB/s**

> **SATA III: 6 Gb/s × (8/10) = 4.8 Gb/s; 4.8 ÷ 8 = 0.6 GB/s = 600 MB/s**

> **USB 2.0: 480 Mb/s ÷ 8 = 60 MB/s**

**Interpretation:** these are peak signalling rates. PCI loses cycles to arbitration and address phases; SATA loses 20% to encoding; USB 2.0 loses protocol overhead and rarely exceeds about 40 MB/s in practice. Never quote a peak as a guaranteed throughput.

**Final Answer:** PCI ≈ 133 MB/s, SATA III = 600 MB/s, USB 2.0 = 60 MB/s (all nominal).

Supplementary example written for this guide. It is not a teacher problem.

### 4.6 Exam answer plan

1. Say what a bus standard is and why standards matter.
2. For each of PCI, USB and SATA: state whether it is parallel or serial, shared or point-to-point, and its typical use.
3. Give the nominal rates and one sentence on encoding or overhead.
4. Compare them in a table: topology, width, speed, hot-plug, use.
5. Add one sentence on the successor technology (PCIe, USB4, NVMe).

## 5 · The I/O interface

### 5.1 Why a device cannot sit directly on the bus

A disk, a keyboard and a temperature sensor do not speak the processor’s bus protocol. Their signals may be serial while the bus is parallel, their voltages may differ, and their timing is often much slower or completely unpredictable. An **I/O interface** (also called an I/O controller or adapter) sits between the system bus and the device. On the bus side it behaves like a well-behaved slave with addressable registers. On the device side it does whatever the device needs. The CPU therefore programs a standard set of registers and never has to know how the device actually works.

### 5.2 The functions of an interface

| Function | What it does | Why it matters |
| --- | --- | --- |
| **Address decoding** | Recognises when the CPU has selected one of its registers. | Lets several interfaces share the bus without responding to each other’s addresses. |
| **Data buffering** | Holds a word or a small FIFO between bus and device. | Absorbs the speed difference and lets the device take data when ready. |
| **Format conversion** | Serial ↔ parallel, bit-width conversion, sometimes analog ↔ digital at the device. | Matches the device’s signalling to the bus. |
| **Control and status** | Provides control and status registers to the CPU. | Gives the CPU a standard way to start an operation and ask whether it finished. |
| **Timing and handshaking** | Generates the strobes and waits for ready/acknowledge signals. | Makes a slow device work with a fast bus without corrupting data. |
| **Error detection** | Parity, checksum or protocol checks. | Reports a bad transfer instead of silently delivering wrong data. |
| **Interrupt generation** | Raises an interrupt when the device becomes ready or finishes. | Enables interrupt-driven I/O instead of polling. |
| **DMA handshaking** | Requests the bus and transfers data directly to memory when configured for DMA. | Removes the CPU from the per-word data path. |
| **Electrical isolation** | Drives the correct voltages and protects the bus from the device. | Prevents a faulty peripheral from damaging the system. |

### 5.3 The three registers the CPU sees

Almost every interface can be understood through three registers. The **data register** is the doorway: the CPU writes a byte or word here for output, or reads one here for input. The **status register** answers questions: is the device ready, is a transfer in progress, has an error occurred? The **control register** receives commands: start, stop, reset, set the transfer mode, enable interrupts. The interface’s control logic connects these registers to the device’s own signals.

| Register | Direction from CPU | Typical bits |
| --- | --- | --- |
| Data | Write (output) or read (input) | 8/16/32-bit data word |
| Status | Read | READY, BUSY, ERROR, INTERRUPT-PENDING |
| Control | Write | START, MODE, INTERRUPT-ENABLE, RESET |

### 5.4 A read and a write, step by step

**Output (CPU → device).** The CPU writes a word to the data register. It then sets the START bit in the control register. The interface asserts the device’s write strobe and waits for the device to accept the word. When the device acknowledges, the interface clears BUSY and sets READY (or raises an interrupt). If the CPU is polling, it sees READY and sends the next word.

**Input (device → CPU).** The interface waits for the device to present a word and assert its data-valid signal. It latches the word into the data register and sets READY. The CPU reads the status register, sees READY, reads the data register, and the interface clears READY so the next word can arrive. If interrupts are enabled, the interface raises an interrupt instead of making the CPU poll.

This handshake is the reason an interface is more than a connector. It converts an unpredictable device event into a bus transaction that the CPU can handle in a fixed way.

### 5.5 Where the registers live

The registers can be **memory-mapped**, in which case they occupy addresses in the normal memory space and the CPU uses ordinary load/store instructions, or **isolated**, in which case they live in a separate I/O space and the CPU uses special instructions such as `IN` and `OUT`. Section 1.3 compares the two. The choice affects the instruction set and the address decoder, not the internal structure of the interface.

### 5.6 Exam answer plan

1. Define an I/O interface and state the problem it solves (speed, format, voltage, protocol).
2. Draw the CPU — system bus — interface — device block diagram, labelling data, status and control paths.
3. List the functions: decoding, buffering, conversion, control/status, timing, error detection, interrupt and DMA support.
4. Explain the data, status and control registers.
5. Walk through one input and one output handshake.
6. Mention memory-mapped versus isolated I/O in one sentence.

## 6 · I/O module, channel and processor

### 6.1 The I/O module

An **I/O module** is the hardware that connects one or more devices to the system bus. It contains the interface logic described in Section 5, plus whatever device-specific control is needed. A simple module might serve a single serial port; a more complex one might control a disk, a keyboard and a timer. The CPU sees the module as a set of registers. The module sees the device as a set of electrical signals. Its job is to translate between the two, buffer data, report status and, when asked, raise an interrupt or request the bus for DMA.

The module is the unit that makes a device *look like* memory or like a set of ports. That is why the CPU can use the same load/store or IN/OUT instructions for devices from different manufacturers.

### 6.2 The I/O channel

An **I/O channel** is a step up in intelligence. It is a specialised processor that sits between the CPU and a group of I/O modules, with its own channel bus and its own small instruction set. The CPU does not issue one command per word. Instead it builds a **channel program** in memory — a sequence of **channel command words (CCWs)** — and tells the channel to execute it. Each CCW says something like “read 512 bytes from device 3 into memory address X” or “write this block to device 7”. The channel fetches the CCWs, drives the I/O modules, and interrupts the CPU only when the whole program finishes or an error occurs.

Channels come in a few flavours. A **selector channel** controls one high-speed device at a time and runs it at full speed. A **multiplexor channel** interleaves byte-by-byte transfers from several slow devices, so they appear to run together. A **block multiplexor channel** interleaves blocks from several high-speed devices. The terminology comes from mainframe I/O, but the idea — offload the per-word work to a small dedicated engine — is general.

### 6.3 The I/O processor

An **I/O processor** is a full processor dedicated to I/O. It has its own instruction set, its own local memory and the ability to run programs that manage many devices, perform protocol handling, buffer data and recover from errors. A front-end processor in a mainframe, a network processor on a router line card, or the controller inside a modern NVMe SSD are all examples of the same idea: put a processor where the I/O work is, so the main CPU does not have to do it.

The boundary between a channel and an I/O processor is not sharp. A channel is usually a limited, special-purpose engine that executes channel programs; an I/O processor is more general and can run arbitrary code. For an exam, the safe distinction is: *module* connects a device, *channel* executes a channel program for several modules, *processor* is a general-purpose computer dedicated to I/O.

| Feature | I/O module | I/O channel | I/O processor |
| --- | --- | --- | --- |
| What it is | Interface and controller for one or a few devices | Special-purpose processor for a group of modules | General-purpose processor dedicated to I/O |
| Programmability | Fixed logic or simple registers | Executes a channel program of CCWs | Runs arbitrary programs |
| CPU involvement | Per transfer or per interrupt | Per channel program | Per job or per high-level command |
| Devices managed | One or a few | Several modules | Many devices or a whole I/O subsystem |
| Cost and complexity | Low | Moderate | High |
| Typical example | UART, disk controller, USB host controller | Mainframe selector or multiplexor channel | Front-end processor, network processor, SSD controller |

### 6.4 Why the hierarchy improves performance

Each step moves more of the I/O work away from the CPU. With a module, the CPU still moves every word but is freed from device-level signalling. With a channel, the CPU issues one channel program and the channel moves the words. With an I/O processor, the CPU can hand over an entire job and go back to computation. The result is less CPU overhead, more overlap between computation and I/O, and better use of the memory bus because the channel or processor can schedule transfers efficiently. The cost is extra hardware and more complex software.

### 6.5 Exam answer plan

1. Define an I/O module and list its functions.
2. Define a channel and explain the channel program and CCW.
3. Define an I/O processor and give one example.
4. Compare the three in a table: programmability, devices, CPU involvement, cost.
5. Explain the performance benefit: offloading, overlap and fewer interrupts.

## 7 · Programmed I/O

### 7.1 The idea

**Programmed I/O** is the simplest transfer method. The CPU does all the work: it issues the command, waits for the device, moves each word and checks for errors. Waiting is done by **polling** — reading the status register in a loop until the ready bit is set. This is also called **busy-waiting**, because the CPU is busy doing nothing useful while it waits.

The method is easy to understand and needs almost no extra hardware: a data register, a status register and a control register are enough. That is why it survives in small microcontrollers and in situations where the CPU has nothing else to do.

### 7.2 The sequence

1. The CPU writes a command to the interface’s control register: direction, device address, maybe a count.
2. The CPU reads the status register.
3. If the ready bit is 0, the CPU jumps back to step 2. This is the polling loop.
4. When ready is 1, the CPU reads the data register (input) or writes it (output).
5. The interface clears ready and starts the next device operation.
6. The CPU updates its count and address, then repeats from step 2 until the block is finished.

The loop is the weakness. Every iteration costs several instructions, and the CPU cannot do anything else while it is inside the loop. If the device takes 1 ms to produce a byte and the polling loop takes 1 µs, the CPU wastes roughly 999 µs per byte.

### 7.3 A numerical view of the waste

**Supplementary worked example — programmed I/O time**

A device supplies one byte every 2 µs. The CPU polls the status register and moves one byte in 2 µs of its own time per byte. How long does it take to transfer 1 KB, and how much CPU time is consumed?

**Solution.**

> **1 KB = 1024 bytes**

> **time = 1024 × 2 µs = 2048 µs = 2.048 ms**

Because the CPU is in the polling loop for the whole transfer, it also consumes 2.048 ms of CPU time. No other program can run on that CPU during the transfer unless the loop is interrupted.

**Final Answer:** 2.048 ms, essentially all of it CPU time.

Supplementary example written for this guide.

### 7.4 Advantages, disadvantages and use

| Advantages | Disadvantages |
| --- | --- |
| Very simple hardware and software. | The CPU busy-waits and cannot do useful work. |
| No interrupt controller or DMA controller needed. | Throughput is limited by the polling loop and the CPU’s instruction rate. |
| Easy to debug: the CPU is in full control at every step. | Wasteful for slow devices and unacceptable for high-speed block transfers. |
| Fine for a single dedicated device or a microcontroller with nothing else to do. | Response time depends on how often the loop checks the status. |

**Typical uses:** reading a keypad or a set of switches, bit-banging a simple sensor, a boot loader polling a UART, or a small embedded system where simplicity matters more than throughput.

### 7.5 Exam answer plan

1. Define programmed I/O and polling/busy-waiting.
2. Give the sequence: command → status → wait → transfer → repeat.
3. Explain why the CPU is wasted and give the time calculation.
4. List advantages, disadvantages and typical uses.
5. Contrast it in one sentence with interrupt-driven I/O and DMA.

## 8 · Interrupt-driven I/O

### 8.1 The idea

Interrupt-driven I/O removes the polling loop. The CPU starts the device and then goes away to execute other instructions. When the device is ready, the interface asserts an **interrupt request**. The CPU finishes the current instruction, saves enough state to resume later, and jumps to an **interrupt service routine (ISR)** that moves the data. When the ISR returns, the CPU continues the interrupted program as if nothing had happened.

The gain is obvious: the CPU spends time on the ISR only when there is data to move, not while the device is idle. The cost is the overhead of entering and leaving the ISR — saving registers, identifying the source, restoring state — which is significant if interrupts arrive very often.

### 8.2 The interrupt sequence

1. The device becomes ready and the interface sets its interrupt-request line.
2. The CPU finishes the current instruction (interrupts are checked at instruction boundaries, not in the middle of one).
3. If interrupts are enabled and the new request has higher priority than the current mask level, the CPU acknowledges the request.
4. The CPU saves the program counter and status flags (and often some registers) on the stack.
5. The CPU obtains the ISR address. In a **vectored** system the interface supplies a vector number and the CPU looks up the address in a vector table; in a **non-vectored** system a fixed address is used.
6. The ISR identifies the device if necessary, reads or writes the data register, clears the interrupt flag and updates the count.
7. The ISR returns with a special instruction that restores the saved state.
8. The CPU resumes the interrupted program.

### 8.3 The vocabulary of interrupts

| Term | Meaning |
| --- | --- |
| **Maskable interrupt** | Can be disabled by the CPU when it is in a critical section. |
| **Non-maskable interrupt (NMI)** | Cannot be disabled; reserved for catastrophic events such as power failure or a hardware fault. |
| **Vectored interrupt** | The device supplies an identifier that points to its ISR. |
| **Non-vectored interrupt** | All devices share one fixed ISR address; the ISR must poll to find the source. |
| **Priority** | Determines which request is served first when several arrive together. |
| **Nested interrupt** | A higher-priority interrupt is allowed to interrupt a lower-priority ISR. |
| **Interrupt latency** | Time from the request to the first instruction of the ISR. |

### 8.4 Overhead and latency

Interrupt overhead has two parts: the fixed cost of entering and leaving the ISR (save, vector, restore) and the work done inside the ISR. If a device needs service every `T` seconds and the ISR takes `S` seconds, the fraction of CPU time consumed is `S ÷ T`.

> **CPU overhead fraction = ISR time ÷ interrupt period**

**Supplementary worked example — interrupt overhead**

A device requests an interrupt every 20 µs. The ISR, including entry and exit, takes 4 µs. What fraction of the CPU is consumed by this device?

**Solution.**

> **overhead = 4 µs ÷ 20 µs = 0.20 = 20%**

The device alone consumes one fifth of the CPU. Two such devices would consume 40%, and the system would soon run out of time. This is why very high-rate devices use DMA rather than one interrupt per word.

**Final Answer:** 20% of CPU time.

Supplementary example written for this guide.

### 8.5 Advantages, disadvantages and use

| Advantages | Disadvantages |
| --- | --- |
| The CPU does useful work while the device is idle. | Each interrupt has entry/exit overhead. |
| Responds quickly to an event, without waiting for a poll cycle. | Frequent interrupts can consume most of the CPU. |
| Handles unpredictable devices well: a key press or a packet can arrive at any time. | Needs an interrupt controller, priority logic and careful ISR design. |
| Supports priority and nesting for urgent events. | Shared data between ISR and main program needs protection (critical sections). |

**Typical uses:** keyboards and mice, serial ports, network packets at moderate rates, timers, and any device that needs a timely response without a dedicated DMA engine.

### 8.6 Exam answer plan

1. Define interrupt-driven I/O and contrast it with polling.
2. Give the sequence from device request to ISR return.
3. Explain vectored versus non-vectored, maskable versus NMI, and priority.
4. Give the overhead formula and one numerical.
5. List advantages, disadvantages and typical uses.

## 9 · Direct Memory Access

### 9.1 The idea

Interrupt-driven I/O still moves every word through the CPU. For a disk or a network card that produces megabytes per second, the interrupt rate would be enormous and the CPU would spend all its time copying. **Direct Memory Access (DMA)** removes the CPU from the data path. A **DMA controller** becomes a bus master, reads or writes memory directly, and moves a whole block between the device and memory. The CPU only programs the controller at the start and is interrupted once at the end.

This is the key sentence for an exam: *in DMA, the CPU initiates the transfer but does not execute the per-word transfer instructions.*

### 9.2 The DMA controller

> *Figure 2. A DMA controller sits between the device and memory. It holds the address, count and control information, and uses bus request/grant to become the bus master.*

The controller has four things to remember. The **address register** holds the next memory address. The **count register** holds how many words or bytes remain. The **control/status register** holds the direction, the transfer mode, interrupt enable and error flags. The **control logic** sequences the bus cycles and updates the address and count after each transfer.

### 9.3 The sequence of a DMA transfer

1. The CPU programs the DMA controller: start address, word count, direction (device → memory or memory → device), mode and interrupt enable.
2. The CPU starts the device and continues with other work.
3. The device asserts a DMA request when it has data (or needs data).
4. The controller asserts the bus-request (BRQ) line to the CPU.
5. The CPU finishes its current bus cycle and asserts bus-grant (BG). The CPU’s address, data and control outputs go to high impedance so the controller can drive the bus.
6. The controller places the memory address on the address bus, transfers one word or a burst, and asserts the appropriate read/write and device strobes.
7. The controller increments the address and decrements the count. If the count is not zero, it repeats from step 3 or continues the burst.
8. When the count reaches zero, the controller releases the bus and raises an interrupt (or sets a done bit) to tell the CPU that the block is complete.

### 9.4 Transfer modes

| Mode | How it uses the bus | Effect |
| --- | --- | --- |
| **Burst (block) transfer** | The controller keeps the bus for the whole block. | Fastest DMA, but the CPU cannot use the bus until the block ends. |
| **Cycle stealing** | The controller takes one bus cycle at a time, between CPU cycles. | The CPU slows down slightly, but it keeps running. Most common for moderate-speed devices. |
| **Transparent DMA** | The controller uses only cycles when the CPU does not need the bus (for example during refresh). | No CPU slowdown, but the transfer takes longer and is harder to schedule. |

### 9.5 The DMA numerical

**Teacher problem — DMA transfer time (question bank Q19)**

A DMA controller transfers data at a rate of 4 MB/s. Calculate the time required to transfer 32 MB of data. Also explain how DMA reduces CPU overhead.

**Question.** Rate = 4 MB/s, size = 32 MB. Find the time and explain the CPU benefit.

**Solution.**

**Step 1 — Write the relation with units.**

> **time = amount of data ÷ transfer rate**

**Step 2 — Substitute.** The data and the rate are both in MB, so the unit cancels and the answer is in seconds.

> **T = 32 MB ÷ 4 MB/s = 8 s**

**Step 3 — Check.** In one second the controller moves 4 MB; in eight seconds it moves 8 × 4 = 32 MB. Correct.

**Why this reduces CPU overhead.** Without DMA, the CPU would execute a load/store sequence for every word, and at 4 MB/s that is millions of instructions per second spent copying. With DMA, the CPU writes a few registers once, starts the device, and is interrupted once at the end. During the 8 seconds it can execute other programs. The CPU still shares the memory bus with the controller, so its memory accesses may be delayed by cycle stealing, but it is not spending instructions on the copy.

**Final Answer:** T = 32 MB ÷ 4 MB/s = 8 seconds.

### 9.6 DMA and cache coherence

DMA introduces a subtle problem. If the CPU has cached a memory block and the DMA controller writes new data directly to memory, the cached copy becomes stale. The CPU may then read the old value. Real systems handle this in one of three ways: mark DMA buffers as uncached (non-cacheable memory), invalidate the relevant cache lines after the DMA write, or use hardware that snoops DMA transfers and keeps the cache coherent. A short paragraph on this is often worth a mark in a DMA answer.

### 9.7 Advantages, disadvantages and use

| Advantages | Disadvantages |
| --- | --- |
| High throughput: the controller moves a block without per-word CPU instructions. | Extra hardware: a DMA controller and arbitration logic. |
| The CPU is free to do other work during the transfer. | The controller competes with the CPU for memory bus cycles. |
| Fewer interrupts: one per block instead of one per word. | Cache coherence must be managed. |
| Well suited to disks, SSDs, network cards, audio and video. | More complex to program and debug than polling. |

### 9.8 Exam answer plan

1. Define DMA and state the key idea: the CPU initiates, the controller moves.
2. Draw the CPU, DMA controller, device and memory block diagram with BRQ/BG.
3. List the registers: address, count, control/status.
4. Give the sequence from programming to final interrupt.
5. Explain burst, cycle stealing and transparent modes.
6. Solve T = size ÷ rate with units and explain the CPU benefit.
7. Add one sentence on cache coherence.

## 10 · Comparing the three techniques

### 10.1 The one-table answer

Most Module 5 questions end with a comparison. The three techniques differ in exactly one fundamental way: *who moves each word*. Everything else — hardware cost, speed, CPU load, typical use — follows from that.

| Point of comparison | Programmed I/O | Interrupt-driven I/O | DMA |
| --- | --- | --- | --- |
| **Who moves the data** | The CPU, one word at a time | The CPU, one word at a time, inside the ISR | The DMA controller, directly between device and memory |
| **CPU involvement** | Continuous — the CPU busy-waits in a polling loop | Per word — the CPU stops, services, and resumes | Only at setup and at block completion |
| **How the CPU learns the device is ready** | It repeatedly reads the status register | The device raises an interrupt | The controller requests the bus; the CPU is interrupted once per block |
| **Extra hardware** | None beyond the interface registers | Interrupt controller, priority logic, vector table | DMA controller plus bus-arbitration logic |
| **Data-transfer speed** | Lowest — limited by the polling loop and instruction rate | Moderate — limited by interrupt overhead per word | Highest — the controller moves blocks at bus speed |
| **CPU time wasted** | Very high; the CPU can do nothing else during the wait | Moderate; overhead is paid per word, not while idle | Low; only setup and one final interrupt |
| **Best suited to** | Slow, simple devices: keypad, switches, a boot-time UART | Unpredictable, moderate-rate devices: keyboard, mouse, serial port, network packets | High-speed block devices: disk, SSD, network card, audio, video |
| **Main weakness** | Busy-waiting wastes the processor | Frequent interrupts can consume the whole CPU | Controller competes for the memory bus; cache coherence must be managed |

### 10.2 How to choose, in plain words

Ask three questions in order. **How much data is there?** A few bytes from a keypad does not justify a DMA controller; a 4 MB video frame does. **How often does the device need attention?** If it is idle most of the time, polling wastes the CPU and an interrupt is better. If it needs attention every few microseconds, even interrupts become too expensive, and DMA is the only sensible choice. **What can the system afford?** Polling needs almost no hardware, interrupts need a controller, DMA needs a controller and arbitration. In a tiny microcontroller, simplicity often wins; in a general-purpose computer, the memory bus is the scarce resource, so DMA wins for every high-rate device.

The three techniques are not mutually exclusive. A real system uses all of them: the keyboard is interrupt-driven, the disk uses DMA, and a temperature sensor on an I²C bus may be polled once a second. The exam answer should say this, because it shows that you understand the trade-off rather than memorising a ranking.

### 10.3 A quantitative comparison on the same block

Take a 4 MB block and a system where the CPU needs 1 µs to move one 4-byte word by programmed I/O, and where the DMA controller sustains 8 MB/s.

> **words = 4 MB ÷ 4 B = 1,048,576 words**

> **programmed I/O time = 1,048,576 × 1 µs ≈ 1.05 s of pure CPU time**

> **DMA time = 4 MB ÷ 8 MB/s = 0.5 s, with the CPU free during almost all of it**

DMA is about twice as fast here, but the more important difference is that the 0.5 s is not CPU time. The CPU programs three registers and is interrupted once. With programmed I/O, the CPU is unavailable for the whole 1.05 s. That is the argument to write in an exam, not just the speed ratio.

Supplementary comparison written for this guide. The numbers are chosen to make the arithmetic clean, not taken from a datasheet.

### 10.4 Exam answer plan

1. State the fundamental difference: who moves each word.
2. Draw the comparison table with CPU involvement, hardware, speed and applications.
3. Explain each row in one sentence — do not just leave the table.
4. Give one numerical or one realistic example to show the scale of the difference.
5. Finish with the trade-off: simplicity versus CPU time versus throughput.

## 11 · Question bank coverage: Q11–Q20 and Q37–Q39

*Source and status*

The questions below are reproduced from the teacher-supplied *question bank.docx* (Module V, Q11–Q20) and *Computer Organization 40 questions.docx* (Module 5, Q37–Q39). The wording is preserved. These are **question-bank documents**, not verified University of Mumbai papers. Each model answer is a condensed exam version; the full treatment is in the section named after it.

### 11.1 Teacher question bank — Q11 to Q20

**Q11**

*Teacher question bank, Module V — not a University paper*

> Explain the different types of buses used in a computer system. Discuss data bus, address bus and control bus.

**Model answer.** A bus is a shared set of lines with a protocol that lets several units communicate; a unit that starts a transfer is a master and the responder is a slave. The system bus has three functional groups. The **data bus** is bidirectional and carries the actual word; its width (8, 16, 32, 64 bits) sets how much moves per transfer. The **address bus** is unidirectional from master to slave and selects the location; n lines give 2^(n) addresses. The **control bus** is a collection of single-purpose lines — read/write, memory or I/O select, interrupt request/acknowledge, bus request/grant, clock and reset — that state the operation and synchronise it. Buses may also be classified as synchronous (clocked) or asynchronous (handshaked), and as a single shared bus or a hierarchy of processor, memory and I/O buses. Section 2 gives the diagram, the bandwidth formula and a numerical.

**Q12**

*Teacher question bank, Module V — not a University paper*

> What is bus arbitration? Explain centralized and distributed bus arbitration techniques.

**Model answer.** Bus arbitration decides which of several requesting masters gets the shared bus, so that two masters never drive it at once. In **centralized arbitration** one arbiter receives the requests and issues the grant. It can use *daisy chaining* (one request line, and a grant that passes through devices in order, so the nearest device has the highest priority), *polling* (the arbiter asks devices in turn and the first requester wins), or *independent requests* (a separate request and grant per master, giving the fastest decision at the highest pin cost). In **distributed arbitration** there is no central arbiter: masters either drive priority codes onto shared lines and the highest code wins by wired-OR/AND self-selection, or they transmit and detect collisions, then back off. Centralized schemes are simple and predictable but the arbiter is a single point of failure; distributed schemes scale better but need more complex logic. Section 3 has the comparison table.

**Q13**

*Teacher question bank, Module V — not a University paper*

> Explain the following bus standards and compare their important characteristics: PCI, USB, SATA.

**Model answer.** A bus standard fixes connectors, signals, timing and protocol so devices from different makers interoperate. **PCI** is a parallel, synchronous, shared expansion bus: 32 or 64 bits, 33 or 66 MHz, with multiplexed address/data and plug-and-play configuration; peak rates are about 133 MB/s (32-bit, 33 MHz) and 533 MB/s (64-bit, 66 MHz), and it has been replaced by the serial, switched PCI Express. **USB** is a serial, host-controlled, tiered-star bus for external peripherals: hot-pluggable, supplies power, supports up to 127 devices per controller, and defines control, bulk, interrupt and isochronous transfers; rates run from 1.5 MB/s (USB 1.1) to several GB/s (USB4). **SATA** is a serial, point-to-point storage link: one device per port, 8b/10b encoding, 150/300/600 MB/s for the three generations, with native command queuing. The comparison is parallel-shared (PCI) versus serial-external (USB) versus serial-storage (SATA); Section 4 gives the full table.

**Q14**

*Teacher question bank, Module V — not a University paper*

> What is an I/O interface? Explain its functions and need in a computer system with a suitable block diagram.

**Model answer.** An I/O interface (controller or adapter) sits between the system bus and a device and translates between them. It is needed because devices differ in speed, signal format (serial or parallel), voltage and protocol, and the CPU must not have to know those details. On the bus side it behaves as a slave with addressable registers; on the device side it drives whatever the device needs. Its functions are address decoding, data buffering, format conversion, control and status reporting, timing and handshaking, error detection, interrupt generation, DMA handshaking and electrical isolation. The CPU sees three registers: **data** (move a word), **status** (ready, busy, error) and **control** (start, mode, interrupt enable, reset). A transfer is a handshake: the CPU writes a command, the interface asserts the device strobe, the device acknowledges, and the interface sets ready or raises an interrupt. Section 5 has the block diagram and the step-by-step read and write.

**Q15**

*Teacher question bank, Module V — not a University paper*

> Differentiate between an I/O module, I/O channel and I/O processor. Explain their roles in I/O organization.

**Model answer.** An **I/O module** is the hardware that connects one or a few devices to the bus; it contains the interface registers and the device-specific control, and the CPU still moves each word or services each interrupt. An **I/O channel** is a special-purpose processor between the CPU and several modules. The CPU builds a channel program of channel command words (CCWs) in memory and the channel executes it, so the CPU is involved once per program rather than once per word. A **selector** channel runs one high-speed device at a time; a **multiplexor** channel interleaves bytes from several slow devices; a **block multiplexor** interleaves blocks. An **I/O processor** is a general-purpose processor dedicated to I/O, with its own instruction set and memory, able to run arbitrary programs and manage many devices — a front-end processor or an SSD controller. The progression is: module connects, channel executes a channel program, processor runs a whole I/O job. Section 6 has the comparison table.

**Q16**

*Teacher question bank, Module V — not a University paper*

> Explain the following data transfer techniques: a) Programmed I/O b) Interrupt-driven I/O c) Direct Memory Access (DMA).

**Model answer.** **Programmed I/O**: the CPU issues the command and then polls the status register in a loop until the device is ready, moves one word, and repeats. It needs minimal hardware but busy-waits, so the CPU is unavailable for the whole transfer. **Interrupt-driven I/O**: the CPU starts the device and continues other work; when the device is ready it raises an interrupt, the CPU saves its state, jumps to the interrupt service routine, moves the word, and returns. It removes the polling waste but pays entry/exit overhead per word. **DMA**: the CPU programs a DMA controller with the start address, word count and direction, then the controller becomes bus master and moves the whole block directly between device and memory, interrupting the CPU once at the end. It gives the highest throughput and the lowest CPU load, at the cost of extra hardware and bus contention. Sections 7, 8 and 9 treat each in full.

**Q17**

*Teacher question bank, Module V — not a University paper*

> Compare Programmed I/O, Interrupt-driven I/O and DMA with respect to CPU involvement, hardware requirement, data-transfer speed and applications.

**Model answer.** **CPU involvement:** continuous busy-waiting (programmed), per word inside an ISR (interrupt), setup and one completion interrupt (DMA). **Hardware:** only interface registers (programmed), plus an interrupt controller and priority logic (interrupt), plus a DMA controller and arbitration logic (DMA). **Speed:** lowest, limited by the polling loop; moderate, limited by interrupt overhead; highest, limited by bus bandwidth. **Applications:** keypad, switches and simple sensors; keyboard, mouse, serial ports and moderate-rate network traffic; disks, SSDs, network cards, audio and video. The underlying reason is who moves each word — the CPU in the first two, the controller in DMA. Section 10 has the full table and a worked comparison on a 4 MB block.

**Q18**

*Teacher question bank, Module V — not a University paper*

> Draw and explain the DMA controller architecture. Describe the sequence of operations involved in a DMA transfer.

**Model answer.** The controller contains an **address register** (next memory address), a **count register** (words remaining), a **control/status register** (direction, mode, interrupt enable, error flags) and **control logic** that sequences the bus cycles. It connects to the CPU through the bus for programming and through bus-request/bus-grant lines for ownership, to memory through address, data and control lines, and to the device through data, status and control lines. **Sequence:** the CPU programs address, count, direction and mode; starts the device; the device asserts a DMA request; the controller asserts bus-request; the CPU finishes its current cycle, asserts bus-grant and floats its bus outputs; the controller drives the address and moves a word or burst; it increments the address and decrements the count; it repeats until the count is zero; then it releases the bus and interrupts the CPU. Section 9.2 has the diagram and Section 9.3 the numbered sequence.

**Q19**

*Teacher question bank, Module V — not a University paper*

> A DMA controller transfers data at a rate of 4 MB/s. Calculate the time required to transfer 32 MB of data. Also explain how DMA reduces CPU overhead.

**Model answer.** Time = amount of data ÷ transfer rate. Both quantities are in MB, so the unit cancels:

> **T = 32 MB ÷ 4 MB/s = 8 s**

**Check:** at 4 MB per second, eight seconds move 8 × 4 = 32 MB. **CPU benefit:** without DMA the CPU would execute a load/store sequence for every word, so at 4 MB/s it would spend millions of instructions per second copying. With DMA it writes a few registers once, starts the device, and is interrupted once at the end; during the 8 s it executes other programs. The controller still competes for memory cycles (cycle stealing), but the CPU does not spend instructions on the copy. Section 9.5 repeats the working with the full explanation.

**Q20**

*Teacher question bank, Module V — not a University paper*

> Explain I/O channels and I/O processors. How do they improve the performance of a computer system?

**Model answer.** An **I/O channel** is a special-purpose processor that executes a channel program of CCWs stored in memory, driving several I/O modules without per-word CPU help. A selector channel serves one high-speed device at a time; a multiplexor channel interleaves bytes from several slow devices; a block multiplexor interleaves blocks from high-speed devices. An **I/O processor** is a general-purpose processor dedicated to I/O, with its own instruction set and local memory, able to run arbitrary programs and manage many devices — for example a front-end processor or an SSD controller. Both improve performance by moving I/O work off the main CPU: fewer interrupts, fewer per-word instructions, and overlap between computation and I/O. The channel or processor can also schedule transfers to use the memory bus efficiently. The cost is extra hardware and more complex software. Section 6.4 explains the performance argument.

### 11.2 Forty-question document — Q37 to Q39

**Q37**

*Computer Organization 40 questions, Module 5 — not a University paper*

> Explain different types of buses used in computer systems. Describe bus arbitration and explain different bus arbitration techniques.

**Model answer.** This combines Q11 and Q12, so write it in two halves. *Buses:* define a bus and master/slave; describe the data bus (bidirectional, width sets bits per transfer), the address bus (unidirectional, n lines → 2^(n) locations) and the control bus (read/write, memory or I/O select, interrupt, bus request/grant, clock, reset); mention synchronous versus asynchronous and single versus multiple buses. *Arbitration:* explain that only one master may drive the bus, then describe centralized arbitration (daisy chaining, polling, independent requests) and distributed arbitration (self-selection by priority code, collision detection with back-off). Compare them on wiring, priority, speed, fault tolerance and scalability. Sections 2 and 3 together answer this question; a labelled CPU–memory–I/O diagram plus a simple REQ/GRANT chain earns the diagram marks.

**Q38**

*Computer Organization 40 questions, Module 5 — not a University paper*

> Explain the need and functions of an I/O module. Differentiate between: I/O module, I/O channel, I/O processor.

**Model answer.** *Need:* peripherals differ in speed, data format, voltage and protocol, and the CPU cannot connect to each directly or spend its time on device-level signalling. *Functions of a module:* address decoding, buffering, format conversion, control and status registers, timing and handshaking, error detection, interrupt generation, DMA support and electrical isolation. *Difference:* a module connects one or a few devices and leaves per-word work with the CPU; a channel is a special-purpose processor that executes a channel program of CCWs for several modules, so the CPU is involved once per program; an I/O processor is a general-purpose processor dedicated to I/O that runs arbitrary programs and can manage a whole I/O subsystem. In one line: module connects, channel executes a channel program, processor runs the I/O job. Sections 5 and 6 cover both halves.

**Q39**

*Computer Organization 40 questions, Module 5 — not a University paper*

> Explain and compare the following I/O data-transfer techniques: Programmed I/O, Interrupt-driven I/O, Direct Memory Access (DMA). Draw suitable diagrams.

**Model answer.** Use the same three-part structure as Q16 and finish with the comparison table from Q17. *Programmed I/O:* CPU polls status, moves each word, busy-waits. *Interrupt-driven:* device interrupts, CPU saves state, runs the ISR, moves the word, returns. *DMA:* CPU programs the controller, the controller becomes bus master and moves the block, one interrupt at the end. For diagrams, draw three simple flows: CPU → status loop → data register; device → interrupt line → CPU → ISR → data register; and CPU → DMA controller → memory/device with BRQ/BG. Then compare on who moves the data, CPU involvement, hardware, speed and applications. The examiner is looking for the phrase “the CPU initiates but does not execute the per-word transfer” in the DMA part. Sections 7–10 supply everything.

### 11.3 Assignment 5 coverage

The teacher’s *Assignment 5.docx* lists six topic groups. All six are covered, and none of them contains a numerical, so the assignment is a writing exercise.

| Assignment 5 topic | Where it is covered |
| --- | --- |
| Types of computer buses: data, address, control | Section 2.2, with the bus diagram and the width/bandwidth formulas |
| Bus arbitration; compare centralized and distributed | Section 3, with daisy chain, polling, independent requests, self-selection and collision detection |
| Bus standards, characteristics and applications | Section 4, with the PCI/USB/SATA comparison table and nominal-rate calculations |
| I/O interface: functions and need | Section 5, with the register model and the input/output handshakes |
| I/O module vs I/O channel vs I/O processor | Section 6, with the three-way comparison table |
| Programmed I/O, interrupt-driven I/O, DMA | Sections 7, 8 and 9, plus the comparison in Section 10 |

### 11.4 MUSA question bank (student association)

*Source and status*

These questions are reproduced from the **MUSA (Mumbai University Students Association) Question Bank of Computer Organization and Architecture, Winter 2026** and the **MUSA Practice Paper Set-1, Winter 2025**. MUSA is a student association. Its material is **not** a University of Mumbai paper, and its wording is not evidence that a question will appear in your exam. The wording is preserved exactly, including the original “interrupt-driver” typo, because you may meet the same phrasing in a practice paper.

**MUSA QB Q5**

*MUSA question bank (student association) — not a University paper*

> Explain and compare programmed I/O, interrupt-driver I/O and DMA.

**Answer.** Programmed I/O is the CPU polling the status register and moving each word itself; it needs almost no hardware but the CPU busy-waits for the whole transfer. Interrupt-driven I/O lets the CPU work until the device raises an interrupt, then the ISR moves the word; it removes the polling waste but pays entry and exit overhead per word. DMA hands the block to a controller that becomes bus master and moves data directly between device and memory; the CPU programs it once and is interrupted at the end. Compare them on who moves the data, CPU involvement, extra hardware, speed and applications, and finish with the trade-off: simplicity versus CPU time versus throughput. The full table is in Section 10 and the individual treatments in Sections 7–9.

**MUSA QB Q7**

*MUSA question bank (student association) — not a University paper*

> What is bus arbitration? Describe various Bus arbitration methods.

**Answer.** Arbitration decides which master gets a shared bus. Centralized methods use one arbiter: daisy chaining passes a grant through devices so priority follows physical position; polling asks devices in turn; independent requests give each master its own request and grant lines and are the fastest but need the most pins. Distributed methods have no arbiter: masters drive priority codes onto shared lines and the highest wins by self-selection, or they transmit and detect collisions and back off, as Ethernet does. Compare on wiring, priority, speed, fault tolerance and scalability. Section 3 has the mechanisms and the comparison table.

**MUSA QB Q19**

*MUSA question bank (student association) — not a University paper*

> Explain buses in I/O organization and explain different types of Buses.

**Answer.** In I/O organization the bus is the shared path between the CPU, memory and I/O modules. The data bus carries the word and is bidirectional; its width sets bits per transfer. The address bus selects the target and is unidirectional; n lines give 2^(n) locations. The control bus carries read/write, memory or I/O select, interrupt request and acknowledge, bus request and grant, clock and reset. Buses can also be classified as synchronous or asynchronous, and as a single shared bus or a hierarchy of processor, memory and I/O buses joined by bridges. Section 2 has the diagram, the bandwidth formulas and a worked numerical.

**MUSA QB Q22**

*MUSA question bank (student association) — not a University paper*

> Explain the concept of an I/O Interface, I/O modules and I/O channels.

**Answer.** An I/O interface is the circuit between the bus and a device; it decodes addresses, buffers data, converts formats, provides control and status registers, handles timing and handshaking, detects errors and can raise interrupts or request DMA. An I/O module is the package that contains one or more such interfaces plus device-specific control, connecting one or a few devices to the bus. An I/O channel is a more intelligent unit: a special-purpose processor that executes a channel program of CCWs for several modules, so the CPU is involved once per program instead of once per word. The progression is interface → module → channel, with the I/O processor as the most general form. Sections 5 and 6 cover all three.

**MUSA Practice Paper Set-1, Q3(b)**

*MUSA practice paper (student association) — not a University paper*

> What is bus arbitration? Describe various Bus arbitration methods.

**Answer.** This is the same question as MUSA QB Q7. Write the definition, the two families, at least two centralized methods with their priority behaviour, one distributed method, and a short comparison. Section 3 is the reference answer.

**MUSA Practice Paper Set-1, Q5(b)**

*MUSA practice paper (student association) — not a University paper*

> Explain the concept of DMA in detail with diagram. *OR* Explain in detail Programmed I/O and Interrupt driven I/O of data transfer techniques.

**Answer.** For the DMA option: define DMA, draw CPU–controller–device–memory with BRQ/BG, list the address, count and control/status registers, give the eight-step sequence, explain burst, cycle stealing and transparent modes, and add one sentence on cache coherence. For the other option: explain the polling loop and its waste for programmed I/O, then the interrupt sequence, vectored versus non-vectored interrupts and the overhead formula for interrupt-driven I/O, and compare the two. Sections 7, 8 and 9 have the full answers and diagrams.

### 11.5 Which question is most likely?

The DMA numerical (Q19) is the only numerical in the Module V question bank, and it is short enough to appear as a 3–5 mark part. The comparison of the three techniques (Q16, Q17, Q39) is the most repeated written question across all three documents, so it is the safest large answer to prepare. Bus arbitration appears in the teacher bank, the 40-question document, the MUSA bank and the MUSA practice paper — four independent sources — which makes it the most likely single written topic after the comparison. Prepare the table in Section 10 and the arbitration comparison in Section 3 until you can reproduce them from memory.

## 12 · Independent practice

These questions are **written for this guide**. They are not teacher questions and not University questions. They are ordered by difficulty and cover every calculation that Module 5 can reasonably ask. Attempt them with the book closed, then mark yourself from the separate answer key in Section 13. Give units in every final answer, and state any assumption you make about cycles per transfer or encoding overhead.

### Practice Questions

#### A · Basic (one definition or one formula)

1. A bus has 20 address lines and 16 data lines. Find the address space and the number of bytes moved per transfer.
2. A 64-bit data bus runs at 400 MHz and completes one transfer per clock cycle. Find the nominal bandwidth in GB/s.
3. A DMA controller transfers data at 8 MB/s. How long does it take to transfer 64 MB?
4. A device requests an interrupt every 50 µs. The interrupt service routine, including entry and exit, takes 5 µs. What fraction of the CPU does this device consume?
5. How many 8-bit words are there in 4 KB?
6. A bus has 32 data lines and runs at 100 MHz, but each transfer needs two clock cycles (an address phase and a data phase). Find the sustained bandwidth.

#### B · Intermediate (two or three steps, with unit conversion)

7. A 32-bit PCI bus runs at 33 MHz and needs two cycles per transfer. Find its sustained bandwidth in MB/s.
8. A SATA III link signals at 6 Gb/s and uses 8b/10b encoding. Find the payload rate in MB/s.
9. A USB 2.0 link signals at 480 Mb/s. Protocol overhead consumes 10% of the payload. Find the effective rate in MB/s.
10. A DMA controller moves 1 MB in 0.25 s. Find its transfer rate in MB/s.
11. A device becomes ready every 4 µs. Under programmed I/O the CPU needs 1 µs per byte to poll the status register and move the byte. Find the wall-clock time, the CPU time and the CPU fraction for a 1 KB transfer.
12. Under interrupt-driven I/O, a device interrupts every 10 µs and the ISR takes 2 µs. Find the CPU overhead fraction. Would this device be better served by DMA? Explain in one sentence.

#### C · Advanced (comparison, multi-step, or a written justification)

13. A 4 MB block must be transferred. Programmed I/O needs 1 µs of CPU time per 4-byte word. A DMA controller sustains 8 MB/s. Find both transfer times, the ratio, and state the more important difference between them.
14. A disk generates one interrupt for every 512-byte block. With DMA, the controller interrupts once per 64 KB block. By what factor does the number of interrupts fall?
15. Explain why daisy-chain arbitration gives the highest priority to the device nearest the arbiter. Your answer should mention what happens to the grant signal at each device. (Written answer, about 4 marks.)

## 13 · Answer key

Mark your work against the working, not only the final number. A correct final answer with a wrong method will not earn full marks in the exam.

### Answers

#### A · Basic

1. **Address space 1 MB; 2 bytes per transfer.**
   2^(20) = 1,048,576 locations = 1 MB. Data lines ÷ 8 = 16 ÷ 8 = 2 bytes. Check: 20 address lines can name 1,048,576 locations, and each transfer carries 16 bits.
2. **3.2 GB/s.**
   64 bits ÷ 8 = 8 bytes per transfer. 8 B × 400 × 10^(6) transfers/s = 3.2 × 10^(9) B/s = 3.2 GB/s. This is the peak; real transfers lose cycles to arbitration and wait states.
3. **8 s.**
   T = 64 MB ÷ 8 MB/s = 8 s. Check: 8 s × 8 MB/s = 64 MB.
4. **10%.**
   overhead = 5 µs ÷ 50 µs = 0.10 = 10%. The other 90% is available to the main program, minus the time the CPU takes to enter and leave the ISR (already included in the 5 µs).
5. **4096 words.**
   4 KB = 4 × 1024 = 4096 bytes. Each word is 8 bits = 1 byte, so 4096 words.
6. **200 MB/s.**
   32 bits ÷ 8 = 4 B per transfer. Two cycles per transfer ⇒ 100 MHz ÷ 2 = 50 × 10^(6) transfers/s. Bandwidth = 4 × 50 × 10^(6) = 200 × 10^(6) B/s = 200 MB/s. If you used one cycle per transfer you would get 400 MB/s; the two-cycle assumption halves it.

#### B · Intermediate

7. **66.66 MB/s.**
   32 bits ÷ 8 = 4 B. Two cycles per transfer ⇒ 33.33 MHz ÷ 2 = 16.665 × 10^(6) transfers/s. Bandwidth = 4 × 16.665 × 10^(6) ≈ 66.66 × 10^(6) B/s. The often-quoted 133 MB/s is the one-cycle peak; the sustained value is half that.
8. **600 MB/s.**
   8b/10b sends 8 payload bits for every 10 line bits, so payload = 6 Gb/s × (8/10) = 4.8 Gb/s. Divide by 8: 4.8 ÷ 8 = 0.6 GB/s = 600 MB/s. Forgetting the 20% encoding loss gives 750 MB/s, which is wrong.
9. **54 MB/s.**
   480 Mb/s ÷ 8 = 60 MB/s raw. With 10% overhead, 60 × 0.9 = 54 MB/s. USB also loses bandwidth to packet headers and polling, so real throughput is lower still.
10. **4 MB/s.**
   rate = amount ÷ time = 1 MB ÷ 0.25 s = 4 MB/s. Check: 0.25 s × 4 MB/s = 1 MB.
11. **Wall time 4.096 ms; CPU time 1.024 ms; CPU fraction 25%.**
   1 KB = 1024 bytes. The device supplies one byte every 4 µs, so the transfer cannot finish faster than 1024 × 4 µs = 4096 µs = 4.096 ms. The CPU spends 1 µs per byte, so its own time is 1024 × 1 µs = 1024 µs = 1.024 ms. Fraction = 1.024 ÷ 4.096 = 0.25 = 25%. The other 75% is spent waiting for the device inside the polling loop — it is not available to other programs.
12. **20%; yes, DMA would be better if the device moves blocks.**
   overhead = 2 µs ÷ 10 µs = 0.20 = 20%. One device already takes a fifth of the CPU, and several such devices would saturate it. DMA moves the block with one interrupt instead of one per word, so the CPU load falls sharply. DMA is worth its hardware cost whenever the device transfers more than a few bytes per interrupt.

#### C · Advanced

13. **Programmed ≈ 1.05 s; DMA = 0.5 s; ratio ≈ 2.1; the important difference is that the programmed time is CPU time.**
   Words = 4 MB ÷ 4 B = 1,048,576. Programmed time = 1,048,576 × 1 µs = 1.048576 s ≈ 1.05 s. DMA time = 4 MB ÷ 8 MB/s = 0.5 s. Ratio = 1.048576 ÷ 0.5 ≈ 2.1. DMA is about twice as fast, but the decisive point is that during the 0.5 s the CPU is free, whereas during the 1.05 s it is executing the copy loop and cannot run anything else.
14. **The interrupt count falls by a factor of 128.**
   64 KB ÷ 512 B = 65,536 ÷ 512 = 128. One interrupt now covers 128 blocks, so the rate is 1/128 of the old rate. This is the main reason DMA exists: it reduces interrupt overhead, not just data-copy instructions.
15. **Model written answer.** In a daisy chain every master shares one bus-request line, but the grant line is wired in series: the arbiter’s grant output goes to device 1, device 1’s grant output goes to device 2, and so on. When the arbiter grants the bus, the signal arrives at device 1 first. If device 1 is requesting, it takes the bus and does *not* pass the grant on, so devices 2, 3 … never see it. If device 1 is not requesting, it forwards the grant to device 2, and the same test repeats. The first requesting device in the physical order therefore wins, which makes priority a function of position rather than of software. The cost is propagation delay: a device far down the chain waits while the grant passes through every earlier device, and a faulty device that fails to forward the grant blocks everyone after it.

## 14 · Common mistakes

### Errors that cost marks, and the fix

| Mistake | Why it is wrong | Correct approach |
| --- | --- | --- |
| Saying the address bus is bidirectional | The master always names the target; slaves only decode. | Address bus: unidirectional, master → slaves. Data bus: bidirectional. |
| Confusing bus width with bus bandwidth | Width is bits per transfer; bandwidth is bytes per second. | Bandwidth = (data lines ÷ 8) × transfers per second. |
| Ignoring cycles per transfer | A real bus may need an address phase and a data phase. | Divide the clock by the number of cycles per transfer, and say that you are doing so. |
| Treating Mb/s and MB/s as the same | One is bits, the other is bytes; the factor is 8. | Divide Mb/s by 8 to get MB/s, then apply encoding or protocol overhead. |
| Forgetting 8b/10b encoding for SATA | Only 8 of every 10 line bits are payload. | Multiply the signalling rate by 0.8 before dividing by 8. |
| Saying DMA means the CPU is not involved at all | The CPU programs the controller and receives the completion interrupt. | “The CPU initiates the transfer but does not execute the per-word transfer instructions.” |
| Saying DMA removes all interrupts | DMA reduces interrupts from one per word to one per block. | One completion interrupt per block, plus error interrupts. |
| Confusing cycle stealing with burst mode | Cycle stealing takes one cycle at a time; burst keeps the bus for the block. | Cycle stealing slows the CPU slightly; burst locks the CPU out for the block duration. |
| Saying daisy-chain priority is programmable | It is fixed by physical position. | Polling order or independent-request priority logic can be programmable; daisy chain cannot. |
| Calling polling “interrupt-driven” | Polling is the CPU asking; interrupts are the device telling. | Programmed I/O polls; interrupt-driven I/O waits for a request. |
| Saying USB is peer-to-peer | USB is strictly host-controlled; devices never start transfers. | The host controller polls devices; the topology is a tiered star. |
| Saying PCIe is just a faster PCI | PCI is a shared parallel bus; PCIe is a switched serial fabric. | Describe PCIe as point-to-point, packet-based and lane-scalable. |
| Mixing up module, channel and processor | They differ in programmability and how much work they take from the CPU. | Module connects; channel executes a channel program; processor runs an I/O job. |
| Confusing vectored and non-vectored interrupts | In a vectored system the device supplies the ISR identifier. | Vectored: device supplies a vector. Non-vectored: one fixed address, and the ISR polls for the source. |
| Writing a DMA time with no unit | “8” could be seconds, milliseconds or megabytes. | Box the answer with its unit: 8 s. |
| Using 1 KB = 1000 bytes in these calculations | Memory and block sizes use powers of two. | 1 KB = 1024 bytes unless the question explicitly uses decimal units. |

## 15 · Last-minute revision sheet

### Ten minutes before the paper

**Bus.** Shared lines plus a protocol. Master starts, slave responds. Data bus bidirectional, width = bits per transfer. Address bus unidirectional, n lines → 2^(n) locations. Control bus: read/write, memory or I/O select, interrupt request/acknowledge, bus request/grant, clock, reset.

**Bandwidth.** bytes per transfer = data lines ÷ 8. Nominal bandwidth = bytes per transfer × transfers per second. If a transfer takes k cycles, divide the clock by k. State “nominal” or “peak” every time.

**Arbitration.** Centralized: daisy chain (priority by position, few wires, propagation delay), polling (priority by polling order, wastes time on idle devices), independent requests (separate REQ/GRANT per master, fastest, most pins). Distributed: self-selection by priority code, or collision detection with back-off.

**Standards.** PCI: parallel, shared, 32/64-bit, 33/66 MHz, ≈133/533 MB/s peak, succeeded by PCIe (serial, switched). USB: serial, host-controlled, tiered star, hot-plug, four transfer types. SATA: serial, point-to-point, 8b/10b, 150/300/600 MB/s.

**Interface.** Decode, buffer, convert format, control/status registers, timing and handshake, error detection, interrupt and DMA support, electrical isolation. Three registers: data, status, control.

**Module vs channel vs processor.** Module connects a device; channel executes a channel program of CCWs for several modules; processor is a general-purpose computer dedicated to I/O.

**Programmed I/O.** CPU polls status, moves each word, busy-waits. Simple, slow, wastes CPU. Time = words × time per word.

**Interrupt-driven I/O.** Device raises IRQ; CPU saves state, runs ISR, returns. Vectored vs non-vectored; maskable vs NMI; priority and nesting. Overhead fraction = ISR time ÷ interrupt period.

**DMA.** CPU programs address, count, direction, mode. Controller asserts BRQ, receives BG, becomes master, moves the block, increments address, decrements count, interrupts at zero. Modes: burst, cycle stealing, transparent. Time = size ÷ rate. Cache coherence must be handled.

**The comparison in one line.** Programmed: CPU moves every word and waits. Interrupt: CPU moves every word but only when asked. DMA: the controller moves the block and the CPU is free.

**Answer discipline.** State the formula, substitute with units, show the arithmetic, box the final answer with its unit, and add one line of interpretation. Draw the diagram first if the question says “with a neat diagram”.

## 16 · References and verification notes

### Sources used

- **Official syllabus.** University of Mumbai, Faculty of Science and Technology, B.E. Computer Science and Engineering (Artificial Intelligence and Machine Learning), Semester III and IV, Course 2023114 *Computer Organization and Architecture*, 2025–26. Module 5 row: “I/O Organization”, 4 hours, CO5. [mu.ac.in syllabus PDF](https://mu.ac.in/old/wp-content/uploads/2025/06/6.21-N-B.E.-AI-ML-sem-III-IV.pdf).
- **Teacher assignment.** *Assignment 5.docx*, supplied in `COA.zip`. Used to confirm the six required topic groups: bus types, arbitration, bus standards, I/O interface, module/channel/processor, and the three transfer techniques.
- **Teacher question bank.** *COA/question bank.docx*, Module V, Q11–Q20. Wording preserved. This is a question-bank document, not a University paper.
- **Forty-question document.** *Computer Organization 40 questions.docx*, Module 5, Q37–Q39. Wording preserved. Also a question-bank document, not a University paper.
- **Student association material.** MUSA *Question Bank of Computer Organization and Architecture* (Winter 2026) and MUSA *Practice Paper Set-1* (Winter 2025, 60 marks, 2 hours). Used for additional practice and clearly labelled; **not** verified University of Mumbai papers.
- **Background references for the supplementary explanations.** Patterson and Hennessy, *Computer Organization and Design*; Stallings, *Computer Organization and Architecture*; Hamacher, Vranesic and Zaky, *Computer Organization*; Tanenbaum, *Structured Computer Organization*. These were not supplied with the course and are listed only as standard sources for the general explanations; no page numbers are claimed.

### What was verified

- Every numerical in Sections 2–13 was recomputed independently in Python: the 16 MB address space and 264 MB/s bus, 133/600/60 MB/s standards comparison, 2.048 ms programmed-I/O example, 20% interrupt overhead, and the DMA answer of **8 s**.
- The practice answers were checked the same way: 1 MB/2 B, 3.2 GB/s, 8 s, 10%, 4096 words, 200 MB/s, 66.66 MB/s, 600 MB/s, 54 MB/s, 4 MB/s, 4.096 ms/1.024 ms/25%, 20%, 1.048576 s/0.5 s/≈2.1, and a factor of 128.
- The syllabus wording, the 4 teaching hours and the CO5 mapping were read from the official PDF, not inferred.
- The question wording in Sections 11 and the MUSA block was copied from the supplied documents, including the original “interrupt-driver” typo in MUSA QB Q5.

### Notes and limitations

- No verified University of Mumbai end-semester paper for course 2023114 was present in the supplied material. Nothing in this guide is labelled as a verified University question.
- The Module 5 syllabus row lists **no self-study topic**, unlike Module 4. Nothing here is marked self-study.
- Bus speeds and standards figures are nominal or peak values for the named generations. They are not measurements of a specific machine, and real throughput is lower because of arbitration, encoding, protocol overhead and wait states.
- “Typical” device speeds and interrupt rates are orders of magnitude, not specifications for a named device.
- Practice questions in Section 12 and the supplementary worked examples are written for this guide. They are labelled as such and are not attributed to the teacher or the University.
- Diagrams are hand-authored SVG in this page. No generated images are used.

### Attribution

Teaching content adapted from the teacher-supplied assignment and question banks listed above. Syllabus text quoted from the official University of Mumbai document. Explanatory prose, additional examples and practice questions are **supplementary clarification** written for this guide. Student-association material is attributed to MUSA and is not presented as University material.
