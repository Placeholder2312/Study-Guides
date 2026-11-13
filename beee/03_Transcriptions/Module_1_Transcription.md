# BEEE Module I — DC Circuits Transcription

This file transcribes the key content from `beee/modules/module-1.html` into markdown for reference and accessibility.

## Syllabus — what is examinable
The official NEP 2020 syllabus wording for ESC102 Module I, quoted verbatim.

## Exam pattern — read this before you plan revision
Official NEP pattern: six questions of 15 marks each; Q1 compulsory; answer any four (Q1 + 3 of remaining 5); 2 hours; 60 marks.  
June 2025 NEP paper (N10415): confirms the pattern — 60 marks, 2 hours, Q1 compulsory, attempt any three of remaining five.  
C-scheme 58654: different course; labelled as such.

## Prerequisites — from charge to power
DC circuit analysis built on six ideas: charge, current, voltage, resistance, power and the two ways of connecting resistors. If one is shaky, every later method feels like a trick.

## Circuit language, polarity and sign conventions
- **Node:** point where two or more elements meet; ideal wire is one node.
- **Branch:** single element (or series combination with no junction) between two nodes.
- **Loop:** any closed path through the circuit.
- **Mesh:** loop containing no other loop inside it; a "window" of a planar circuit.
- **Reference node:** chosen 0 V; every other node voltage measured w.r.t. it.
- **Assumed directions:** draw an arrow, solve, interpret the sign. Positive → current flows in arrow direction. Negative → current flows opposite; magnitude is absolute value.

## Source symbols
| Symbol | Meaning | How to read |
|--------|---------|-------------|
| Long line and short line | DC voltage source (battery) | Long line = positive terminal |
| Circle with arrow | Ideal current source | Arrow gives current direction; current leaves at arrow head |
| Circle with + and − | General voltage source | + terminal at higher potential when delivering power |

## KVL sign rules — the table to memorise
| While moving around the loop | Sign in KVL sum |
|-----------------------------|-----------------|
| Across a resistor *in the direction* of the current | −IR (potential drop) |
| Across a resistor *opposite* to the current | +IR (potential rise) |
| Through a voltage source from − to + | +V (rise) |
| Through a voltage source from + to − | −V (drop) |

Set algebraic sum to zero. Statement of energy conservation: rises equal drops.

## Two assumptions always in force
1. **Ideal wires:** zero resistance unless a value is printed; all points on a wire at one potential.
2. **Lumped elements:** each resistor, source and meter treated as a single element at a point; no stray capacitances or inductances in this module.

## Ideal and practical sources
- **Ideal voltage source:** holds terminal voltage V_s whatever current the circuit draws. V–I graph: vertical line at V = V_s.
- **Ideal current source:** holds current I_s whatever voltage appears across it. V–I graph: horizontal line at I = I_s.
- **Practical voltage source:** OpenStax model: ideal emf ε in series with internal resistance r. Terminal voltage: V_terminal = ε − Ir.
- **Practical current source:** approaches ideal when internal resistance is very large.

## Source transformation
- V_s in series with R ↔ I_s in parallel with R. Arrow points to the + terminal.
- Why it works: external behaviour (V–I relation) is identical.
- Rules and limits: only independent sources; cannot cross the boundary (e.g., cannot transform a dependent source this way).

## Kirchhoff's laws
### KCL — the junction rule
Algebraic sum of currents into a node is zero. Currents entering = currents leaving. A current source fixes the current in its branch, not the voltage across it.

### KVL — the loop rule
Algebraic sum of voltages around a closed loop is zero. Energy conservation: the rises equal the drops. A voltage source fixes the voltage between its terminals, not the current through it.

## Mesh analysis
- Assign mesh currents all clockwise (or all anticlockwise).
- Shared branch carries the *difference* of the two mesh currents.
- Write KVL for each mesh. No supermesh (syllabus exclusion).
- Exam procedure: identify meshes, assign currents, write KVL, solve, interpret signs.

## Nodal analysis
- Pick reference node (usually bottom rail or negative terminal of main source = 0 V).
- Write KCL at each non-reference node. Express every current as (node voltage − neighbour voltage)/resistance for currents leaving the node.
- No supernode (syllabus exclusion).
- Exam procedure: choose reference, write KCL, solve for node voltages.

## Star–delta and delta–star conversion
### Formulas
**Δ → Y:**  
R_A = R_AB · R_CA / S, R_B = R_AB · R_BC / S, R_C = R_BC · R_CA / S, where S = R_AB + R_BC + R_CA.

**Y → Δ:**  
R_AB = P / R_C, R_BC = P / R_A, R_CA = P / R_B, where P = R_A · R_B + R_B · R_C + R_C · R_A.

### Balanced shortcut
- All three Y legs equal R_Y → equivalent Δ: R_Δ = 3 R_Y.
- All three Δ resistors equal R_Δ → equivalent Y: R_Y = R_Δ / 3.

### Why the formulas work
Measure resistance between each pair of terminals with third terminal open. Three equations → solve for unknowns. Derivation comes from terminal equivalence.

### Exam procedure — star–delta
1. Identify a three-terminal star or delta not already in series/parallel.
2. Label terminals consistently in both original and converted drawing. Most errors are label errors, not arithmetic.
3. Choose direction that simplifies remaining circuit (e.g., converting bottom delta of a bridge).
4. Write formula with labels visible; substitute only after formula is complete.
5. Reduce circuit with series/parallel rules.
6. Check equivalent resistance: must be smaller than sum of all resistors and larger than smallest parallel path.

### Common mistakes
- Using delta formula when network is a star (or vice versa).
- Dividing by wrong sum (Δ→Y denominator is sum of all three delta resistors; Y→Δ denominator is the *opposite* star leg).
- Mixing terminal labels after redrawing.
- Forgetting balanced factor of 3 in Y→Δ direction.
- Applying conversion to network already having simple series/parallel reduction.

### Worked example (from guide)
Star: 2 Ω, 4 Ω, 6 Ω legs → Delta: R_AB = 22/3 Ω, R_BC = 22 Ω, R_CA = 11 Ω.  
Check: star resistance between A and B = 2 + 4 = 6 Ω; delta: 22/3 ∥ (22 + 11) = 6 Ω. Agrees.

## Superposition theorem
- Find voltage or current by adding contributions of independent sources one at a time.
- **Kill the others:** voltage sources → short circuits; current sources → open circuits.
- **Power warning:** Superposition applies to voltages and currents in linear circuits, **not** to power. Never add powers from superposition.
- Exam procedure: one source at a time, others killed, contributions added, polarity check.

## Thevenin's theorem
- Reduce any linear two-terminal network to V_th in series with R_th.
- V_th = open-circuit voltage across the terminals.
- R_th = resistance looking into terminals with all independent sources dead: voltage sources → short, current sources → open.
- Norton equivalence: I_N = V_th / R_th, R_N = R_th, V_th = I_N · R_N.
- Exam procedure: remove load, find V_oc, kill sources, find R_th, reattach load, calculate current/voltage.

## Norton's theorem
- Reduce the same network to I_N in parallel with R_N.
- I_N = short-circuit current through the terminals.
- R_N = R_th (same resistance, parallel configuration).
- Exam procedure: short the terminals, find I_sc, find R_th (same as Thevenin), place I_N in parallel with R_N.

## Maximum power transfer theorem
- **Condition:** R_L = R_th. Maximum power delivered to the load.
- **Formula:** P_max = V_th² / (4 · R_th).
- **Important:** Maximum power transfer does **not** coincide with maximum efficiency.
- Exam procedure: find V_th and R_th, set R_L = R_th, calculate P_max.

### Worked example (from guide)
12 V source, 3 Ω series resistor, 6 Ω load → V_th = 20 V, R_th = 2 Ω, I_L = 5 A, P_max = 50 W.

## Choosing a method under exam pressure
| If the question says… | Use… | Because… |
|----------------------|------|----------|
| "Find current in one branch" & network complicated | Nodal analysis | One unknown node voltage gives branch current directly |
| "Find several branch currents" in planar network | Mesh analysis | One unknown per window; shared-branch currents from differences |
| "Find current through load" & load can be removed | Thevenin or Norton | Network collapses to one source + one resistance |
| "Find R_L for maximum power" | Thevenin + MPT | Set R_L = R_th; use P_max = V_th²/(4·R_th) |
| "Use superposition" explicitly | One source at a time | Kill others: V sources short, I sources open |
| A bridge with no series/parallel pair | Star–delta conversion | Convert one three-terminal group, then reduce |

### 10-minute checklist before the paper
1. Can you state KCL and KVL and write both with correct signs?
2. Can you draw the four source symbols and explain ideal vs. practical behaviour?
3. Can you convert a source in both directions and place the arrow correctly?
4. Can you write a mesh equation with a shared branch without a sign error?
5. Can you write a nodal equation at a node with a voltage source behind a resistor?
6. Can you state both star–delta formulas and the balanced shortcuts?
7. Can you list the three steps of superposition and the power warning?
8. Can you find V_th, R_th, I_N and R_N for a two-source network?
9. Can you derive R_L = R_th and P_max?
10. Can you check a final answer by substituting it back into one KCL or KVL equation?

## Course assignments (Dr. Nirmala K.)
### Assignment 1 — Unit 1: DC circuits
- A1-Q1: Superposition, find voltage across 4 Ω resistor → 28 V
- A1-Q2: Maximum power transfer, state and prove → proof by dP_L/dR_L = 0
- A1-Q3: Norton, current through 3 Ω across A-B → 41/48 A ≈ 0.854 A (same as June 2025 Q2(a))
- A1-Q4: KVL and unknown resistance → scan underdetermined; no defensible numerical answer
- A1-Q5: Current in 10 Ω resistor → 34/47 A ≈ 0.723 A (assumes 20 V positive at top, 2 A arrow right)
- A1-Q6: Equivalent resistance across x and y → 595/22 Ω ≈ 27.05 Ω
- A1-Q7: Current through 1 Ω by Thevenin → 11/32 A ≈ 0.344 A (assumes 1 V positive at bottom-left)

### Assignment 2 — Thevenin, Norton, maximum power and nodal
- A2-Q1: Thevenin through 30 Ω → conditional 7/3 A ≈ 2.33 A (13 A downward, 50 V positive at top)
- A2-Q2: Norton through 10 Ω → −79/47 A ≈ −1.68 A (10 V and 20 V positive at top; 20 V source in series with 10 Ω branch)
- A2-Q3: Maximum power in a bridge → R_L = 125/6 Ω ≈ 20.83 Ω; P_max = 5/6 W ≈ 0.833 W
- A2-Q4: Maximum power with source in load branch → R = 49 Ω; P_max = 16/49 W ≈ 0.327 W (assumes 2 V positive on left)
- A2-Q5: Nodal analysis, current through 1 Ω → 4 A downward

### Teacher's Unit 1 practice question bank (15 questions)
Selected questions with unambiguous diagrams:
- **QB-2:** Nodal analysis, current in 5 Ω → 14/15 A ≈ 0.933 A
- **QB-4:** Star to delta → R_AB = 22/3 Ω, R_BC = 22 Ω, R_CA = 11 Ω (for 2, 4, 6 Ω legs)
- **QB-7:** Nodal analysis, current in 15 Ω → 0.25 A from B to A
- **QB-8:** Source transformation → I = 3 A downward
- **QB-11:** Find R from a branch current → R = 20/3 Ω ≈ 6.67 Ω
- **QB-13/14:** Source conversion → I_s = 4 A in parallel with 5 Ω; arrow points to + terminal
- **QB-15:** Nodal analysis, find V_A → 8/7 V ≈ 1.143 V (7 V_A = 8)

### Questions with ambiguous scans (no fake numerical answer)
- **A1-Q4:** Right end of R3 cut off; circuit underdetermined
- **A1-Q5:** Answer depends on 20 V positive at top and 2 A arrow right
- **A2-Q1:** 13 A arrow/50 V polarity unclear; conditional 7/3 A if 13 A downward and 50 V positive top
- **A2-Q2:** 20 V source in series with 10 Ω branch; −79/47 A under stated polarities

## June 2025 NEP paper — Module I answers
| Question | Answer | Marks |
|----------|--------|-------|
| Q1(a) | Star → Delta: R_AB = 22/3 Ω, R_BC = 22 Ω, R_CA = 11 Ω | 3 |
| Q2(a) | Norton, current through 3 Ω A→B → 41/48 A ≈ 0.854 A | 10 |
| Q4(a) | Nodal, current through 4 Ω → 0.75 A from B to A (5 A arrow up) or 1.75 A from A to B (5 A arrow down) | 5 |
| Q6(a) | Source transformation, current through 8 Ω → 1.5 A downward | 6 |

## Practice — Basic / Exam-level / Challenging
### Basic (B1–B8)
- B1: Definitions (KCL, KVL, ideal/practical sources, MPT)
- B2: Ohm's law and power → I = 4 A, P = 96 W
- B3: Series resistance and parallel pair → R = 6 Ω, V_parallel = 4 V, I_6Ω = 2/3 A, I_3Ω = 4/3 A
- B4: Series–parallel reduction → I_total = 3 A, V_parallel = 6 V, I_6Ω = 1 A
- B5: KVL in series circuit → I = 2 A, V_3Ω = 6 V, V_5Ω = 10 V, V_2Ω = 4 V
- B6: Voltage divider and power → V_L = 7.5 V, P_L = 7.5 W
- B7: Source transformation both directions → (a) 3 A ∥ 10 Ω, (b) 30 V in series with 10 Ω
- B8: Balanced star–delta → (a) 27 Ω each, (b) 4 Ω each, (c) R_Δ = 3 R_Y; R_Y = R_Δ/3

### Exam-level (E1–E8)
- E1: Mesh analysis with shared branch → I_1 = 3.2 A, I_2 = 0.4 A, shared = 2.8 A
- E2: Nodal analysis with two shunts → V_A = 4.5 V
- E3: Nodal analysis with two voltage sources → V_A = 14 V, I_6Ω = 2.333 A downward
- E4: Thevenin and resistive load → V_th = 12 V, R_th = 4 Ω, I_L = 2 A, P_L = 8 W
- E5: Norton equivalent → I_N = 6 A, R_N = 2 Ω, I_L = 2 A
- E6: Maximum power transfer → R_L = 2 Ω, P_max = 18 W
- E7: Equivalent resistance → R_AB = 16/3 Ω ≈ 5.33 Ω
- E8: Current division → I_6Ω = 2 A downward

### Challenging (C1–C4)
- C1: Two-stage ladder and Thevenin → V_th = 20 V, R_th = 2 Ω, I_L = 4 A, P_L = 48 W
- C2: Thevenin with current source, then maximum power → V_th = 8 V, R_th = 2 Ω, R_L = 2 Ω, P_max = 8 W
- C3: Nodal analysis with three parallel paths → V_A = 120/13 V ≈ 9.23 V, source current = 70/13 A ≈ 5.38 A, P_4Ω = 3600/169 W ≈ 21.3 W
- C4: Balanced bridge → I_source = 3.75 A, I_5Ω = 0 A (bridge balanced: 2/4 = 4/8)

## Full Answer Key
Tables covering Basic / Exam-level / Challenging answers, Assignment 1 & 2 answer index, Teacher's QB answer index, June 2025 NEP paper Module I answers.

## Revision Sheet — Last-minute revision sheet
### Formula sheet
- Ohm's law: V = IR
- Power: P = VI = I²R = V²/R
- Series: R_eq = R_1 + R_2 + …
- Parallel: 1/R_eq = 1/R_1 + 1/R_2 + … (product/sum for two)
- Voltage divider: V_2 = V_total × R_2/(R_1 + R_2)
- Current divider: I_1 = I_total × R_2/(R_1 + R_2)
- Source transformation: V_s = I_s · R; I_s = V_s/R
- KCL: ΣI_in = ΣI_out
- KVL: ΣV_rises = ΣV_drops
- Star → Δ: R_AB = P/R_C etc., P = R_A·R_B + R_B·R_C + R_C·R_A
- Δ → Star: R_A = R_AB·R_CA/S etc., S = R_AB + R_BC + R_CA
- Thevenin: V_th = open-circuit; R_th = sources dead
- Norton: I_N = short-circuit; R_N = R_th
- Maximum power: R_L = R_th; P_max = V_th²/(4·R_th)

### Sign and unit discipline
- Mark every source's + and − before writing an equation.
- Choose mesh currents all clockwise (or all anticlockwise), keep the choice.
- For nodal analysis, mark reference node with 0 V; write currents as (V_node − V_neighbour)/R for leaving currents.
- A current source fixes the current in its branch, not the voltage across it.
- A voltage source fixes the voltage between its terminals, not the current through it.
- Carry units through arithmetic: Ω × A = V; V × A = W; V²/Ω = W.
- A negative answer is information, not an error: actual direction opposite to assumed arrow.
- Never add powers from superposition.

### Method chooser
See the table under "Choosing a method under exam pressure" above.

### Ten-minute checklist before the paper
See the checklist above.

## References and attribution
See `Source_Index.md` for full list. Key points:
- OpenStax §10.1/§10.3 quotations short and attributed, CC BY 4.0 / CC BY-NC-SA 4.0.
- Kuphaldt Chapter 10 released for free distribution.
- Dr. Nirmala K. course documents identified as `<span class="tag c">Course</span>`.
- June 2025 NEP paper (N10415) identified as `<span class="tag q">Paper</span>`.
- C-scheme 58654 papers flagged as different course/scheme.
- No quotation is invented; no source cited for a claim it does not make.

## What this page does not include
- Dependent sources, supernodes or supermeshes (explicitly excluded by syllabus "only independent sources"; "no super node and super mesh").
- C-scheme 58654 papers as ESC102 questions.
- Teacher assignments or practice bank as university papers.
- Modules 2–6.