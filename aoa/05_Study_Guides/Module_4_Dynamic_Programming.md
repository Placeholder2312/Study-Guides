# AOA — Module 4: Dynamic Programming

**B.E. Computer Science (AI & ML) · Semester III · Course 2023113 · NEP 2020**
**Module IV · 8 teaching hours · Course outcome CO4**
End-semester pattern: 6 questions of 20 marks · Q1 compulsory · answer any 3 · 2 hours

This guide is written for the day before the examination. Every algorithm is presented in the same order: the problem, the idea, how to recognise it, how it works, reproducible pseudocode, a worked example, a full trace, the complexity, and the mistakes that cost marks. The practice set is at the end, with a separate fully worked answer key.

> **How to use this guide.** Read Sections 1–6 once, copying each recurrence by hand. Then close the guide and reproduce the five tables — multistage cost table, Floyd matrices, knapsack table, TSP `g` table, LCS `c` table — on blank paper. Finally answer the practice questions without looking at the key.

---

## Syllabus and scope

> **Official syllabus — University of Mumbai, 6.21 (N) B.E. AI & ML, Sem III & IV, 2025–26, page 23.**
> **Module IV — Dynamic Programming Approach:** General Method, Multistage graphs, All pair shortest path: Floyd Warshall Algorithm, 0/1 knapsack Problem, Travelling Salesperson problem, Longest common subsequence.
> **Self-learning Topics:** Bellman Ford Algorithm, real life applications of all algorithms.
> **Hours:** 8 · **CO mapping:** CO4 — "Develop solutions using Dynamic Programming and examine its complexity."

| Prescribed topic | What you must be able to do | Section |
|---|---|---|
| General method | State the two DP properties, write the four-step method, compare DP with greedy and divide-and-conquer. | 1 |
| Multistage graphs | Write the backward recurrence and compute the cost and decision tables for a staged graph. | 2 |
| All pairs shortest path (Floyd–Warshall) | Run the pivot loop and produce D⁰ … Dⁿ. | 3 |
| 0/1 knapsack | Build the `m[i, w]` table, give the recurrence and reconstruct the chosen items. | 4 |
| Travelling salesperson problem | Use `g(i, S)`, fill the table by increasing set size and read off the tour. | 5 |
| Longest common subsequence | Build the `c` table, trace the arrows and print an LCS. | 6 |

**Not in Module IV.** Matrix-chain multiplication, optimal binary search trees and assembly-line scheduling are not prescribed here. Bellman–Ford appears only as a self-learning topic. Do not spend revision time on the others unless your teacher covered them in class.

---

## 1 — The general method

### 1.1 The problem DP solves

Dynamic programming solves an **optimisation problem**: one that asks for a maximum or a minimum — the cheapest path, the largest profit, the longest common subsequence, the shortest tour. A brute-force solution enumerates every possibility and is usually exponential. DP replaces enumeration with a table of smaller answers.

### 1.2 The idea

Break the problem into smaller versions of itself, solve each distinct smaller version **once**, store the answer, and reuse it. The two properties that make this legal are:

| Property | Meaning | Test question |
|---|---|---|
| **Optimal substructure** | An optimal solution to the whole problem can be built from optimal solutions to its subproblems. | If I knew the best answer for the smaller problem, could I combine it into the best answer for the bigger one? |
| **Overlapping subproblems** | The same subproblem is needed again and again by different branches of the recursion. | Does a plain recursive solution recompute the same argument more than once? |

> **Teacher's slide 3.** Dynamic Programming is used to solve optimisation problems. Break the complex problem into simpler subproblems, find the optimal solution to these subproblems, store the results (memoisation), reuse the stored results so that the same subproblem is not calculated more than once, and finally compute the result of the complex problem. It applies to problems with two properties: overlapping subproblems and optimal substructure.

> **Teacher's slide 4 — examples given in class.**
> **Optimal substructure:** in the shortest path problem, the shortest path to a destination depends on the shortest path to an intermediate vertex.
> **Overlapping subproblems:** in the Fibonacci sequence, values such as `fib(n-2)` are computed multiple times.

The **principle of optimality** is the sentence that earns the first mark: *whatever the first decision is, the remaining decisions must themselves be optimal for the state that results from the first decision.*

### 1.3 How to recognise a DP problem

- The question says "maximum", "minimum", "longest", "shortest", "number of ways" or "optimal".
- A locally best choice is not obviously safe — 0/1 knapsack is the standard trap.
- The same smaller case would be needed repeatedly.
- The question names Floyd–Warshall, LCS, TSP by DP, multistage graph, or says "using dynamic programming".
- The input has a natural sequence, grid, capacity or set that can index a table.

### 1.4 How it works — the six-step method

For **every** DP answer, write these six headings. Even if an arithmetic slip occurs, the method marks are secure.

1. **State.** Define exactly what one table entry means, including its indices and units. Example: "`m[i, w]` is the maximum profit obtainable from a subset of items 1…i using capacity at most `w`."
2. **Recurrence and base cases.** Express a state using smaller states. Write the first row and first column explicitly.
3. **Computation order.** Choose an order in which every state is ready before it is used — increasing `i`, increasing `w`, increasing set size, or increasing stage index.
4. **Final answer.** State which cell (or which minimum over a row) is the answer, with its unit.
5. **Reconstruction.** Walk backwards through the table to recover the chosen items, path or subsequence, not just the value.
6. **Complexity.** Give time and space with one line of reasoning based on the table size.

### 1.5 Pseudocode template

```
DP-SOLVE(input)
  allocate table T with the dimensions implied by the state
  initialise the base row, column or diagonal
  for each state in a valid computation order:
      T[state] = min or max over choices of (local cost + T[smaller state])
  answer = T[final state]
  reconstruct choices by walking backwards from the final state
  return answer, choices
```

### 1.6 Worked example — Fibonacci

`fib(n) = fib(n-1) + fib(n-2)`, with `fib(0) = 0` and `fib(1) = 1`.

```
fib(5) = fib(4) + fib(3)
       = (fib(3)+fib(2)) + (fib(2)+fib(1))
       = ...
```

`fib(2)` is computed three times and `fib(3)` twice. The DP table removes the repetition:

| n | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| fib(n) | 0 | 1 | 1 | 2 | 3 | 5 |

Time Θ(n), space Θ(n), or Θ(1) if only the last two values are kept.

### 1.7 Top-down and bottom-up

| Style | How it works | Use |
|---|---|---|
| **Top-down (memoisation)** | Write the natural recursion; before computing a state, check a table; store the result after computing it. | Useful for TSP's `g(i,S)` while learning. |
| **Bottom-up (tabulation)** | Fill the table from the smallest states upwards with loops; no recursion. | All five exam algorithms in this module. |

In the examination, write the bottom-up version: it is shorter, it displays the table, and it makes the complexity obvious.

### 1.8 Dynamic programming compared with greedy

> **Teacher's slide 16 — comparison table given in class.**
> **Greedy:** generates only one decision sequence; makes stepwise decisions on local information; does not consider results from subproblems while making locally optimal decisions; determines the first choice before computing any subproblem. Examples: playing cricket, Dijkstra's algorithm, fractional knapsack.
> **Dynamic programming:** may generate multiple decision sequences; cannot produce stepwise decisions based on local information alone; makes globally optimal decisions that depend on the sub-sequences of decisions obtained by solving subproblems; computes the subproblems before making the first choice. Examples: playing chess, Bellman–Ford, 0/1 knapsack.

| Question to ask | Greedy | Dynamic programming |
|---|---|---|
| Can a locally best choice be wrong later? | No — that is the greedy-choice property. | Yes — so all candidates are compared. |
| Are subproblems overlapping? | Usually irrelevant. | Yes, and storing them is the point. |
| Typical complexity | O(n log n) after sorting. | Polynomial in the table size, e.g. O(nM) or O(n²2ⁿ). |
| Example | Fractional knapsack. | 0/1 knapsack. |

A one-mark contrast: **greedy commits to one choice without looking ahead; DP compares every choice using the stored answers to subproblems.**

### 1.9 Common mistakes in the general method

- Calling any recursive solution "dynamic programming" without a stored table.
- Forgetting to state the meaning of the state.
- Writing a recurrence but not the base cases.
- Filling the table in an order that uses a cell before it is computed.
- Giving only the optimal value, not the reconstruction the question asked for.
- Claiming DP is always faster. 0/1 knapsack is O(nM), which is **pseudo-polynomial** — not polynomial in the number of bits of `M`.

---

## 2 — Multistage graphs

### 2.1 The problem

A **multistage graph** is a directed graph whose vertices are partitioned into `k ≥ 2` stages `S₁, S₂, …, Sₖ`. Every edge goes from a vertex in `Sᵢ` to a vertex in `Sᵢ₊₁`. There is one source (in `S₁`) and one sink (in `Sₖ`). Each edge has a cost. Find a path from source to sink of minimum total cost.

### 2.2 The idea

Any optimal source-to-sink path must leave the source by some edge and then follow an optimal path from that next vertex to the sink. That is optimal substructure. The same suffix is needed by several prefixes, which is why one table serves all of them.

Define `cost(i, j)` = minimum cost from vertex `j` in stage `i` to the sink. Then

```
cost(k, j) = 0                                   for the sink j in stage k
cost(i, j) = min over edges (j, l) with l in stage i+1 of [ c(j, l) + cost(i+1, l) ]
```

The answer is `cost(1, source)`. The vertex `l` that attains the minimum is stored in `D[j]` so the path can be reconstructed.

### 2.3 How to recognise it

- The graph is drawn in vertical columns labelled stages.
- Every edge points from one column to the next; no edge stays in a column or skips a column.
- The question says "multistage", "stages", "source to sink", "minimum cost path".
- If edges may go backwards or stay within a stage, it is a general shortest-path problem, not this algorithm.

### 2.4 How it works

1. Number the stages from 1 (source) to `k` (sink).
2. Set `cost(k, sink) = 0`.
3. Process stages from `k−1` down to 1. For each vertex `j` in the current stage, try every edge `(j, l)` to the next stage, add the already-computed `cost(i+1, l)`, and keep the smallest.
4. Record the winning next vertex in `D[j]`.
5. The answer is `cost(1, source)`. Follow `D` from the source to the sink to print the path.

The computation is **backward**: the sink is solved first. A forward version is also possible: define `f(i, j)` as the minimum cost from the source to vertex `j` in stage `i`, compute stages 1 to `k`, and read `f(k, sink)`. Both are O(V + E). The backward version is the one used in the slides and the one that gives the decision table directly.

### 2.5 Pseudocode

```
MULTISTAGE(G, stages, c)
  // G has vertices 1..n; stage 1 contains the source 1; stage k contains the sink n
  cost[k][n] = 0
  for i = k-1 down to 1:
      for each vertex j in stage[i]:
          cost[i][j] = INFINITY
          for each edge (j, l) with l in stage[i+1]:
              if c[j][l] + cost[i+1][l] < cost[i][j]:
                  cost[i][j] = c[j][l] + cost[i+1][l]
                  D[j] = l
  print "minimum cost =", cost[1][1]
  v = 1
  while v != n:
      print v, "->"
      v = D[v]
  print n
```

### 2.6 Worked example — twelve vertices, five stages

The class graph has 12 vertices in five stages:

- `S₁ = {1}`, `S₂ = {2,3,4,5}`, `S₃ = {6,7,8}`, `S₄ = {9,10,11}`, `S₅ = {12}`.
- Edges and costs: 1–2 = 9, 1–3 = 7, 1–4 = 3, 1–5 = 2; 2–6 = 4, 2–7 = 2, 2–8 = 1; 3–6 = 2, 3–7 = 7; 4–8 = 11; 5–7 = 11, 5–8 = 8; 6–9 = 6, 6–10 = 5; 7–9 = 4, 7–10 = 3; 8–10 = 5, 8–11 = 6; 9–12 = 4, 10–12 = 2, 11–12 = 5.

![Figure 1 — the twelve-vertex five-stage graph](figure:multistage)

**Stage 4.** Every vertex in stage 4 has one edge to the sink:

| j | edge | cost(4, j) | D[j] |
|---|---|---|---|
| 9 | 9→12, 4 | 4 | 12 |
| 10 | 10→12, 2 | 2 | 12 |
| 11 | 11→12, 5 | 5 | 12 |

**Stage 3.** Add the edge cost to the stage-4 cost:

| j | candidates | minimum | D[j] |
|---|---|---|---|
| 6 | 6–9: 6+4 = 10; 6–10: 5+2 = 7 | **7** | 10 |
| 7 | 7–9: 4+4 = 8; 7–10: 3+2 = 5 | **5** | 10 |
| 8 | 8–10: 5+2 = 7; 8–11: 6+5 = 11 | **7** | 10 |

**Stage 2.**

| j | candidates | minimum | D[j] |
|---|---|---|---|
| 2 | 2–6: 4+7 = 11; 2–7: 2+5 = 7; 2–8: 1+7 = 8 | **7** | 7 |
| 3 | 3–6: 2+7 = 9; 3–7: 7+5 = 12 | **9** | 6 |
| 4 | 4–8: 11+7 = 18 | **18** | 8 |
| 5 | 5–7: 11+5 = 16; 5–8: 8+7 = 15 | **15** | 8 |

**Stage 1.**

| j | candidates | minimum | D[j] |
|---|---|---|---|
| 1 | 1–2: 9+7 = 16; 1–3: 7+9 = 16; 1–4: 3+18 = 21; 1–5: 2+15 = 17 | **16** | 2 |

The minimum cost is **16**. Following `D`: 1 → 2 → 7 → 10 → 12, with cost 9 + 2 + 3 + 2 = 16.

**Tie note.** `1 → 3 → 6 → 10 → 12` also costs 7 + 2 + 5 + 2 = 16. The table records `D[1] = 2` only because the candidates are examined in increasing order and `<` keeps the first minimum. In an examination, state the tie: *the optimal cost is 16, and one optimal path is 1–2–7–10–12; 1–3–6–10–12 is an equally optimal path.* A complete answer mentions both.

### 2.7 Full trace

| Stage | Vertex | Computation | cost | D |
|---|---|---|---|---|
| 5 | 12 | base | 0 | — |
| 4 | 9 | 4 + 0 | 4 | 12 |
| 4 | 10 | 2 + 0 | 2 | 12 |
| 4 | 11 | 5 + 0 | 5 | 12 |
| 3 | 6 | min(6+4, 5+2) | 7 | 10 |
| 3 | 7 | min(4+4, 3+2) | 5 | 10 |
| 3 | 8 | min(5+2, 6+5) | 7 | 10 |
| 2 | 2 | min(4+7, 2+5, 1+7) | 7 | 7 |
| 2 | 3 | min(2+7, 7+5) | 9 | 6 |
| 2 | 4 | 11 + 7 | 18 | 8 |
| 2 | 5 | min(11+5, 8+7) | 15 | 8 |
| 1 | 1 | min(9+7, 7+9, 3+18, 2+15) | 16 | 2 |

### 2.8 Complexity

Each edge is examined exactly once. With adjacency lists, time is **Θ(V + E)**; with an adjacency matrix and the usual scan of the next stage, **Θ(k·n²)** worst case. Space is **Θ(V)** for the cost and decision arrays. For a dense layered graph, `E` can be Θ(n²), so the matrix version is not a slowdown in the worst case.

### 2.9 Common mistakes

- Using forward greedy and never reconsidering an earlier choice.
- Forgetting the base case `cost(k, sink) = 0`.
- Adding `cost(i, j)` to itself, or using `cost(i, l)` instead of `cost(i+1, l)`.
- Processing stages from the source downwards while the recurrence needs the next stage.
- Reading the cost from the table but not reconstructing the path, when the question asks for the path.
- Reporting only one path when two are optimal, or claiming the other is wrong.

---

## 3 — All pairs shortest path: Floyd–Warshall

### 3.1 The problem

Given a directed graph with `n` vertices and edge weights that may be negative (but no negative cycle), compute the shortest distance from every vertex to every other vertex. The output is an `n × n` matrix `D` where `D[i][j]` is the minimum cost of a path from `i` to `j`.

### 3.2 The idea

Number the vertices `1…n`. Let `D⁽ᵏ⁾[i][j]` be the shortest path from `i` to `j` that uses only vertices from `{1, …, k}` as intermediate vertices. Then either the path does not use `k`, or it is a shortest path from `i` to `k` followed by a shortest path from `k` to `j`:

```
D⁽ᵏ⁾[i][j] = min( D⁽ᵏ⁻¹⁾[i][j],  D⁽ᵏ⁻¹⁾[i][k] + D⁽ᵏ⁻¹⁾[k][j] )
D⁽⁰⁾[i][j] = weight(i, j)     if the edge exists
D⁽⁰⁾[i][i] = 0
D⁽⁰⁾[i][j] = ∞               otherwise
```

After `k = n`, `D⁽ⁿ⁾` is the all-pairs answer. The third vertex `k` is called the **pivot**.

### 3.3 How to recognise it

- "All pairs shortest path", "distance matrix", "every pair".
- A matrix is given, and the question asks for a sequence of matrices `D¹, D², …`.
- Edge weights may be negative; no negative cycle is stated.
- Contrast: a single source with non-negative weights is Dijkstra; a single source with negative edges is Bellman–Ford.

### 3.4 How it works

1. Initialise `D` from the weight matrix, with 0 on the diagonal and ∞ where there is no edge.
2. For `k = 1` to `n` (the pivot):
   for every `i`, for every `j`, replace `D[i][j]` with `min(D[i][j], D[i][k] + D[k][j])`.
3. After the last pivot, `D[i][j]` is the shortest distance.

The three loops can be written in place. This is valid because `D[i][k]` and `D[k][j]` do not change during pivot `k`: a shortest path from `i` to `k` using `k` as an intermediate would repeat `k`, which cannot improve a path without a negative cycle. Some textbooks keep a previous matrix `D⁽ᵏ⁻¹⁾` to make this argument explicit; both versions produce the same result.

**Path reconstruction.** Keep a `next` matrix. Initially `next[i][j] = j` if the edge `i→j` exists. Whenever `D[i][j]` improves through pivot `k`, set `next[i][j] = next[i][k]`. Then the path from `i` to `j` is `i`, `next[i][j]`, `next[next[i][j]][j]`, … until `j`.

### 3.5 Pseudocode

```
FLOYD-WARSHALL(W, n)
  D = W                                  // D[i][i] = 0, D[i][j] = infinity if no edge
  for i = 1 to n:
      for j = 1 to n:
          if i != j and W[i][j] < infinity: next[i][j] = j
  for k = 1 to n:
      for i = 1 to n:
          for j = 1 to n:
              if D[i][k] + D[k][j] < D[i][j]:
                  D[i][j] = D[i][k] + D[k][j]
                  next[i][j] = next[i][k]
  return D, next

PRINT-PATH(i, j)
  if D[i][j] == infinity: print "no path"
  else:
      print i
      while i != j:
          i = next[i][j]
          print i
```

### 3.6 Worked example — four vertices

Weight matrix (∞ means no direct edge):

```
       1    2    3    4
1      0    8    ∞    1
2      ∞    0    1    ∞
3      4    ∞    0    ∞
4      ∞    2    9    0
```

**Initial matrix D⁰**

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 0 | 8 | ∞ | 1 |
| **2** | ∞ | 0 | 1 | ∞ |
| **3** | 4 | ∞ | 0 | ∞ |
| **4** | ∞ | 2 | 9 | 0 |

**Pivot k = 1.** Paths that may now pass through vertex 1. The only improvements use row 1 and column 1:

- `D[3][2] = min(∞, 4 + 8) = 12`
- `D[3][4] = min(∞, 4 + 1) = 5`

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 0 | 8 | ∞ | 1 |
| **2** | ∞ | 0 | 1 | ∞ |
| **3** | 4 | 12 | 0 | 5 |
| **4** | ∞ | 2 | 9 | 0 |

**Pivot k = 2.** Improvements:

- `D[1][3] = min(∞, 8 + 1) = 9`
- `D[4][3] = min(9, 2 + 1) = 3`

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 0 | 8 | 9 | 1 |
| **2** | ∞ | 0 | 1 | ∞ |
| **3** | 4 | 12 | 0 | 5 |
| **4** | ∞ | 2 | 3 | 0 |

**Pivot k = 3.** Improvements:

- `D[2][1] = min(∞, 1 + 4) = 5`
- `D[2][4] = min(∞, 1 + 5) = 6`
- `D[4][1] = min(∞, 3 + 4) = 7`

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 0 | 8 | 9 | 1 |
| **2** | 5 | 0 | 1 | 6 |
| **3** | 4 | 12 | 0 | 5 |
| **4** | 7 | 2 | 3 | 0 |

**Pivot k = 4.** Improvements:

- `D[1][2] = min(8, 1 + 2) = 3`
- `D[1][3] = min(9, 1 + 3) = 4`
- `D[3][2] = min(12, 5 + 2) = 7`

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 0 | **3** | **4** | 1 |
| **2** | 5 | 0 | 1 | 6 |
| **3** | 4 | **7** | 0 | 5 |
| **4** | 7 | 2 | 3 | 0 |

For example, `D[2][4] = 6` is realised by 2 → 3 → 1 → 4: 1 + 4 + 1 = 6. Check with the `next` matrix: `next[2][4] = 3` (set at pivot 3), `next[3][4] = 1` (set at pivot 1), `next[1][4] = 4`. Path: 2, 3, 1, 4. ✓

`D[4][1] = 7` is realised by 4 → 2 → 3 → 1: 2 + 1 + 4 = 7. ✓

### 3.7 Full trace

| Pivot | Cells improved | D after the pivot (rows 1–4) |
|---|---|---|
| 0 | initial | `[0,8,∞,1] [∞,0,1,∞] [4,∞,0,∞] [∞,2,9,0]` |
| 1 | D[3][2]=12, D[3][4]=5 | `[0,8,∞,1] [∞,0,1,∞] [4,12,0,5] [∞,2,9,0]` |
| 2 | D[1][3]=9, D[4][3]=3 | `[0,8,9,1] [∞,0,1,∞] [4,12,0,5] [∞,2,3,0]` |
| 3 | D[2][1]=5, D[2][4]=6, D[4][1]=7 | `[0,8,9,1] [5,0,1,6] [4,12,0,5] [7,2,3,0]` |
| 4 | D[1][2]=3, D[1][3]=4, D[3][2]=7 | `[0,3,4,1] [5,0,1,6] [4,7,0,5] [7,2,3,0]` |

### 3.8 Complexity

Three nested loops, each of length `n`: **Θ(n³)** time. The matrix is `n²`: **Θ(n²)** space. For comparison, running Dijkstra `n` times from each source with a binary heap is O(n·(E log V)) and is faster on sparse graphs with non-negative weights; Bellman–Ford from each source is O(n·V·E) and handles negative edges. Floyd–Warshall is the simplest all-pairs method and handles negative edges.

### 3.9 Common mistakes

- Putting `k` in the innermost loop. The pivot must be the **outer** loop; otherwise intermediate vertices are combined incorrectly.
- Using the original matrix for both terms while updating in place, without checking that the in-place argument is valid. (It is valid for this recurrence, but the reason must be understood.)
- Using a finite "large" number and adding to it, producing a false path. Guard with `if D[i][k] < ∞ and D[k][j] < ∞`.
- Forgetting `D[i][i] = 0` and `D[i][j] = ∞` for missing edges.
- Claiming the algorithm works with a negative cycle. It does not: distances would decrease forever. Detect a negative cycle by checking for a negative diagonal after the run.
- Reconstructing a path from the final matrix alone. Keep the `next` (or predecessor) matrix during the updates.

---

## 4 — 0/1 knapsack

### 4.1 The problem

Given `n` items, each with a positive integer weight `wᵢ` and profit `pᵢ`, and a knapsack of capacity `M`, choose a subset of the items so that the total weight is at most `M` and the total profit is maximum. Each item is taken **once** — that is the "0/1" part.

### 4.2 The idea

Consider the items one at a time. For item `i` there are only two decisions: leave it out, or take it (if it fits). If we take it, the remaining capacity is `w − wᵢ` and the remaining items are `1…i−1`. The best profit for that smaller problem is already in the table. Define

```
m[i, w] = maximum profit using a subset of items 1…i with capacity at most w
```

Then

```
m[0, w] = 0                         for every w
m[i, 0] = 0                         for every i
m[i, w] = m[i-1, w]                 if wᵢ > w
m[i, w] = max( m[i-1, w],  pᵢ + m[i-1, w - wᵢ] )    if wᵢ ≤ w
```

The answer is `m[n, M]`. The same item is never reused because the second term uses row `i−1`, not row `i`.

### 4.3 How to recognise it

- A capacity, a budget, a weight limit, or a time limit.
- Each item can be chosen once ("0/1"), not in fractions, not repeatedly.
- The question asks for maximum profit or minimum cost with a constraint.
- If fractions are allowed, use the greedy ratio method, not this DP. If unlimited copies are allowed, use the unbounded recurrence `m[i, w] = max(m[i-1,w], pᵢ + m[i, w-wᵢ])`.

### 4.4 How it works

1. Create a table with `n+1` rows (0…n) and `M+1` columns (0…M).
2. Fill row 0 and column 0 with 0.
3. For `i = 1…n` and `w = 0…M`, apply the recurrence.
4. The answer is the bottom-right cell.
5. To reconstruct, start at `(n, M)` and move upwards: if `m[i][w] ≠ m[i-1][w]`, item `i` was taken; subtract `wᵢ` from `w` and move to row `i−1`. Otherwise move to row `i−1` without subtracting.

Computation order is **row by row, left to right**: every cell uses the row above (already complete) and a cell to the left in the row above (also complete).

### 4.5 Pseudocode

```
KNAPSACK-01(w[1..n], p[1..n], M)
  for w = 0 to M: m[0][w] = 0
  for i = 1 to n: m[i][0] = 0
  for i = 1 to n:
      for w = 0 to M:
          if w[i] > w:
              m[i][w] = m[i-1][w]
          else:
              m[i][w] = max(m[i-1][w], p[i] + m[i-1][w - w[i]])
  // reconstruction
  w = M
  for i = n down to 1:
      if m[i][w] != m[i-1][w]:
          x[i] = 1
          w = w - w[i]
      else:
          x[i] = 0
  return m[n][M], x
```

### 4.6 Worked example — four items, capacity 5

`n = 4`, `M = 5`, weights `(2, 3, 4, 5)`, profits `(3, 4, 5, 6)`.

Base: row 0 is all zeros, column 0 is all zeros.

**Row 1 (item 1: w = 2, p = 3).** For `w < 2`, copy row 0. For `w ≥ 2`, compare "leave" (0) with "take" (3 + 0 = 3).

| i \ w | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 3 | 3 | 3 | 3 |

**Row 2 (item 2: w = 3, p = 4).**

- `w = 2`: leave 3; take does not fit → 3.
- `w = 3`: max(leave 3, 4 + m[1][0] = 4) = 4.
- `w = 4`: max(3, 4 + m[1][1] = 4) = 4.
- `w = 5`: max(3, 4 + m[1][2] = 7) = 7.

| i \ w | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 3 | 3 | 3 | 3 |
| 2 | 0 | 0 | 3 | 4 | 4 | 7 |

**Row 3 (item 3: w = 4, p = 5).**

- `w = 4`: max(4, 5 + m[2][0] = 5) = 5.
- `w = 5`: max(7, 5 + m[2][1] = 5) = 7.

| i \ w | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 3 | 3 | 3 | 3 |
| 2 | 0 | 0 | 3 | 4 | 4 | 7 |
| 3 | 0 | 0 | 3 | 4 | 5 | 7 |

**Row 4 (item 4: w = 5, p = 6).**

- `w = 5`: max(leave 7, 6 + m[3][0] = 6) = 7.

| i \ w | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 3 | 3 | 3 | 3 |
| 2 | 0 | 0 | 3 | 4 | 4 | 7 |
| 3 | 0 | 0 | 3 | 4 | 5 | 7 |
| 4 | 0 | 0 | 3 | 4 | 5 | **7** |

The maximum profit is **7**.

**Reconstruction.** Start at `m[4][5] = 7`. `m[3][5] = 7`, so item 4 is not taken; move to `(3,5)`. `m[2][5] = 7`, so item 3 is not taken; move to `(2,5)`. `m[1][5] = 3 ≠ 7`, so item 2 is taken; `w = 5 − 3 = 2`, move to `(1,2)`. `m[0][2] = 0 ≠ 3`, so item 1 is taken; `w = 0`. Therefore `X = (1, 1, 0, 0)`, total weight 5, profit 7.

### 4.7 Full trace

| Cell | Leave | Take | m[i][w] | Decision |
|---|---|---|---|---|
| m[1][2] | 0 | 3 + 0 = 3 | 3 | take |
| m[1][5] | 0 | 3 + 0 = 3 | 3 | take |
| m[2][3] | 3 | 4 + 0 = 4 | 4 | take |
| m[2][4] | 3 | 4 + 0 = 4 | 4 | take |
| m[2][5] | 3 | 4 + 3 = 7 | 7 | take |
| m[3][4] | 4 | 5 + 0 = 5 | 5 | take |
| m[3][5] | 7 | 5 + 0 = 5 | 7 | leave |
| m[4][5] | 7 | 6 + 0 = 6 | 7 | leave |

### 4.8 Complexity

Time **Θ(nM)**: `n(M+1)` cells, constant work per cell. Space **Θ(nM)** for the full table. If only the value is needed, two rows (or one row scanned right-to-left) give **Θ(M)** space:

```
for i = 1 to n:
    for w = M down to w[i]:
        dp[w] = max(dp[w], p[i] + dp[w - w[i]])
```

The reverse scan is essential: scanning left to right would allow the same item to be taken repeatedly. Reconstructing the chosen items with Θ(M) space requires a divide-and-conquer technique; in the examination, keep the full table.

`O(nM)` is **pseudo-polynomial**: it is polynomial in the numeric value of `M`, not in the number of bits used to write `M`. 0/1 knapsack is NP-hard, so no genuinely polynomial algorithm is known. Saying "O(nM), which is pseudo-polynomial" is a strong answer.

### 4.9 Common mistakes

- Using `m[i][w−wᵢ]` instead of `m[i−1][w−wᵢ]` — that solves the unbounded knapsack.
- Forgetting row 0 or column 0.
- Using the fractional-knapsack greedy ratio on a 0/1 instance.
- Filling the table column by column without checking that the required cells exist (the recurrence is fine either way, but the row-by-row presentation is easier to mark).
- Reconstructing by comparing `m[i][w]` with `m[i][w−1]` instead of `m[i−1][w]`.
- Reporting the profit but not the selected items or the total weight.
- Writing "O(nM) polynomial" without the pseudo-polynomial qualification.

---

## 5 — Travelling salesperson problem by dynamic programming

### 5.1 The problem

A salesperson starts at city 1, must visit every other city exactly once, and must return to city 1. The cost of travelling from city `i` to city `j` is `c(i, j)`. Find a tour of minimum total cost.

The graph is usually complete: there is a cost for every ordered pair of distinct cities. If some direct route is missing, set its cost to ∞. The matrix need not be symmetric.

### 5.2 The idea

Fix the starting city, 1. Suppose the salesperson is at city `i` and the set `S` of cities still to be visited is known. The cheapest way to finish does not depend on how the salesperson reached `i` — only on `i` and `S`. That is the state. Define

```
g(i, S) = minimum cost of a path that starts at i, visits every city in S exactly once,
          and ends at city 1
```

where `i ∉ S` and `S ⊆ {2, 3, …, n}`. Then

```
g(i, ∅) = c(i, 1)                                      base case: go straight home
g(i, S) = min over j in S of [ c(i, j) + g(j, S − {j}) ]
```

The answer is

```
min over j in {2,…,n} of [ c(1, j) + g(j, {2,…,n} − {j}) ]
```

The set `S` is stored as a bitmask: bit `j−2` is 1 when city `j` is still to be visited.

### 5.3 How to recognise it

- "Visit every city exactly once and return to the start."
- A cost matrix between cities, and `n` is small (typically ≤ 15).
- The question says "using dynamic programming" or gives the recurrence `g(i, S)`.
- Brute force would try `(n−1)!` tours; DP reduces this to about `n²2ⁿ`.
- If the question asks only for a lower bound or a search tree, it may be branch and bound (Module V), not this DP.

### 5.4 How it works

1. Write the base values `g(i, ∅) = c(i, 1)` for every city `i ≠ 1`.
2. Process subsets by **increasing size**: all singletons, then all pairs, then all triples, and so on. A state of size `s` uses states of size `s−1`, which are already complete.
3. For each state `(i, S)`, try every `j ∈ S`, add `c(i, j)` to `g(j, S−{j})`, and keep the smallest. Store the winning `j`.
4. Combine at the start: try every first city `j`, add `c(1, j)` to `g(j, {2…n}−{j})`, and take the minimum.
5. Reconstruct the tour by following the stored choices.

### 5.5 Pseudocode

```
TSP-DP(c, n)
  // cities are 1..n; city 1 is the start; S is a bitmask over cities 2..n
  for i = 2 to n:
      g[i][0] = c[i][1]
      choice[i][0] = 1
  for size = 1 to n-2:
      for every subset S of {2..n} with |S| = size:
          for every i in {2..n} with i not in S:
              g[i][S] = INFINITY
              for every j in S:
                  candidate = c[i][j] + g[j][S without j]
                  if candidate < g[i][S]:
                      g[i][S] = candidate
                      choice[i][S] = j
  best = INFINITY
  full = {2, 3, ..., n}
  for j = 2 to n:
      candidate = c[1][j] + g[j][full without j]
      if candidate < best:
          best = candidate
          first = j
  return best, first, choice
```

### 5.6 Worked example — four cities

Cost matrix (the matrix used in Assignment 4 and in the IAT-2 question bank):

| from \ to | A | B | C | D |
|---|---|---|---|---|
| **A** | 0 | 4 | 2 | 1 |
| **B** | 4 | 0 | 13 | 9 |
| **C** | 2 | 13 | 0 | 8 |
| **D** | 1 | 9 | 8 | 0 |

Write A = 1, B = 2, C = 3, D = 4, and start at A.

**Base: `S = ∅`.**

| State | Computation | Value | Path |
|---|---|---|---|
| g(B, ∅) | c(B, A) | 4 | B–A |
| g(C, ∅) | c(C, A) | 2 | C–A |
| g(D, ∅) | c(D, A) | 1 | D–A |

**Size 1.**

| State | Candidates | Minimum | Path |
|---|---|---|---|
| g(B, {C}) | 13 + g(C, ∅) = 13 + 2 = 15 | **15** | B–C–A |
| g(B, {D}) | 9 + g(D, ∅) = 9 + 1 = 10 | **10** | B–D–A |
| g(C, {B}) | 13 + g(B, ∅) = 13 + 4 = 17 | **17** | C–B–A |
| g(C, {D}) | 8 + g(D, ∅) = 8 + 1 = 9 | **9** | C–D–A |
| g(D, {B}) | 9 + g(B, ∅) = 9 + 4 = 13 | **13** | D–B–A |
| g(D, {C}) | 8 + g(C, ∅) = 8 + 2 = 10 | **10** | D–C–A |

**Size 2.**

| State | Candidates | Minimum | Path |
|---|---|---|---|
| g(B, {C,D}) | via C: 13 + g(C,{D}) = 13 + 9 = 22; via D: 9 + g(D,{C}) = 9 + 10 = 19 | **19** via D | B–D–C–A |
| g(C, {B,D}) | via B: 13 + g(B,{D}) = 13 + 10 = 23; via D: 8 + g(D,{B}) = 8 + 13 = 21 | **21** via D | C–D–B–A |
| g(D, {B,C}) | via B: 9 + g(B,{C}) = 9 + 15 = 24; via C: 8 + g(C,{B}) = 8 + 17 = 25 | **24** via B | D–B–C–A |

**Size 3 — the answer.**

| First city j | Candidate | Value |
|---|---|---|
| B | c(A,B) + g(B,{C,D}) = 4 + 19 | **23** |
| C | c(A,C) + g(C,{B,D}) = 2 + 21 | **23** |
| D | c(A,D) + g(D,{B,C}) = 1 + 24 | **25** |

The minimum tour cost is **23**. There are two optimal tours:

- via B: A → B → D → C → A, cost 4 + 9 + 8 + 2 = 23;
- via C: A → C → D → B → A, cost 2 + 8 + 9 + 4 = 23.

The table stores the first minimum (`B`) because the loop examines B before C, but both must be reported.

### 5.7 Full trace

| Subset size | States computed | Values |
|---|---|---|
| 0 | g(B,∅), g(C,∅), g(D,∅) | 4, 2, 1 |
| 1 | g(B,{C}), g(B,{D}), g(C,{B}), g(C,{D}), g(D,{B}), g(D,{C}) | 15, 10, 17, 9, 13, 10 |
| 2 | g(B,{C,D}), g(C,{B,D}), g(D,{B,C}) | 19, 21, 24 |
| 3 | start combination at A | 23 |

A useful check: `g(C, {B,D})` must use the already-computed `g(D, {B}) = 13` and `g(B, {D}) = 10`; it does not recompute those paths. This is the overlapping-subproblem saving.

### 5.8 Complexity

Number of states: for each of the `n` cities, `2ⁿ⁻¹` subsets that do not contain it, so about `n·2ⁿ⁻¹`. Each state scans up to `n` choices. Time **O(n²2ⁿ)**; space **O(n·2ⁿ)** for the table (and the choice table). Brute force is `(n−1)!`, which is far larger: for `n = 10`, `9! = 362,880` tours versus roughly `10²·2¹⁰ ≈ 10⁵` states.

### 5.9 Common mistakes

- Using `g(j, S)` instead of `g(j, S−{j})`; the next city must be removed from the remaining set.
- Forgetting the base case `g(i, ∅) = c(i, 1)` — the return to the start.
- Forgetting the final edge from the start to the first city in the answer combination.
- Processing subsets in numeric order rather than by size; a pair may then be used before it is computed.
- Using a visited mask that includes the start city or the current city.
- Reporting only the cost when the question asks for the tour.
- Treating a missing edge as cost 0 instead of ∞.
- Confusing this DP (Module IV) with the branch-and-bound TSP (Module V). The DP fills a table of exact values; branch and bound searches a tree of partial tours with lower bounds.

---

## 6 — Longest common subsequence

### 6.1 The problem

A **subsequence** of a string is obtained by deleting zero or more characters without changing the order of the remaining characters. It is **not** a substring: the characters need not be contiguous. Given two strings `X[1…m]` and `Y[1…n]`, find a longest string that is a subsequence of both.

Example: `X = ACADB`, `Y = CBDA`. The string `CA` is a subsequence of both (take A, C in X and C, A in Y), and no common subsequence has length 3. So the LCS length is 2. `CB` is another LCS of the same length.

### 6.2 The idea

Look at the last characters. Let `c[i][j]` be the length of an LCS of the prefixes `X[1…i]` and `Y[1…j]`.

- If `X[i] = Y[j]`, that character can end an LCS: `c[i][j] = c[i−1][j−1] + 1`.
- If they differ, the last character of one prefix cannot be in the LCS, so drop one of them: `c[i][j] = max(c[i−1][j], c[i][j−1])`.

Base cases: `c[0][j] = 0` and `c[i][0] = 0`, because an empty prefix has no common subsequence.

Optimal substructure holds because an LCS of the prefixes contains an LCS of the smaller prefixes. Overlapping subproblems occur because `c[i−1][j]` and `c[i][j−1]` both depend on `c[i−1][j−1]`.

### 6.3 How to recognise it

- Two sequences or strings, and the word "common subsequence".
- "Longest", with deletions allowed but order preserved.
- The question asks for a table, arrows, or a reconstruction.
- Distinguish from longest common **substring** (contiguous), which uses a different recurrence (`c[i][j] = c[i−1][j−1] + 1` on a match, else 0, and the answer is the maximum cell, not the bottom-right cell).
- Also used for `diff`, DNA alignment and version control.

### 6.4 How it works

1. Draw a table with `m+1` rows and `n+1` columns. Row/column 0 is the empty prefix.
2. Fill row by row, left to right.
3. On a match, take the diagonal and add 1; on a mismatch, take the larger of the cell above and the cell to the left.
4. The bottom-right cell is the LCS length.
5. Reconstruct: start at `(m, n)` and move backwards. On a match, output the character and move diagonally. On a mismatch, move towards the larger neighbour; on a tie, move left (any consistent tie-break gives a valid LCS).

### 6.5 Pseudocode

```
LCS-LENGTH(X[1..m], Y[1..n])
  for i = 0 to m: c[i][0] = 0
  for j = 0 to n: c[0][j] = 0
  for i = 1 to m:
      for j = 1 to n:
          if X[i] == Y[j]:
              c[i][j] = c[i-1][j-1] + 1
              b[i][j] = "diagonal"
          else if c[i-1][j] >= c[i][j-1]:
              c[i][j] = c[i-1][j]
              b[i][j] = "up"
          else:
              c[i][j] = c[i][j-1]
              b[i][j] = "left"
  return c, b

PRINT-LCS(b, X, i, j)
  if i == 0 or j == 0: return
  if b[i][j] == "diagonal":
      PRINT-LCS(b, X, i-1, j-1)
      print X[i]
  else if b[i][j] == "up":
      PRINT-LCS(b, X, i-1, j)
  else:
      PRINT-LCS(b, X, i, j-1)
```

The reconstruction above prints the LCS in forward order because the recursive call happens before the `print`.

### 6.6 Worked example — X = ACADB, Y = CBDA

Rows are prefixes of X, columns are prefixes of Y.

| c | — | C | B | D | A |
|---|---|---|---|---|---|
| **—** | 0 | 0 | 0 | 0 | 0 |
| **A** | 0 | 0 | 0 | 0 | 1 |
| **C** | 0 | 1 | 1 | 1 | 1 |
| **A** | 0 | 1 | 1 | 1 | 2 |
| **D** | 0 | 1 | 1 | 2 | 2 |
| **B** | 0 | 1 | 2 | 2 | 2 |

Selected cells:

- `c[2][1]`: C = C → `c[1][0] + 1 = 1`.
- `c[3][4]`: A = A → `c[2][3] + 1 = 1 + 1 = 2`.
- `c[4][3]`: D = D → `c[3][2] + 1 = 1 + 1 = 2`.
- `c[5][2]`: B = B → `c[4][1] + 1 = 1 + 1 = 2`.
- `c[5][3]`: B ≠ D → max(c[4][3] = 2, c[5][2] = 2) = 2.

The LCS length is **2**.

Reconstruction with the rule "on a tie, move up":

- `(5,4)`: B ≠ A, `c[4][4] = 2`, `c[5][3] = 2` → up to `(4,4)`.
- `(4,4)`: D ≠ A, `c[3][4] = 2`, `c[4][3] = 2` → up to `(3,4)`.
- `(3,4)`: A = A → output **A**, go to `(2,3)`.
- `(2,3)`: C ≠ D, `c[1][3] = 0`, `c[2][2] = 1` → left to `(2,2)`.
- `(2,2)`: C ≠ B, `c[1][2] = 0`, `c[2][1] = 1` → left to `(2,1)`.
- `(2,1)`: C = C → output **C**, go to `(1,0)`; stop.

Output in reverse is A, C; forward is **CA**.

If ties are broken by moving left instead, the same table yields **CB**. Both are correct. State the tie-break rule you use.

### 6.7 Worked example 2 — X = SAVANT, Y = ADVENT

| c | — | A | D | V | E | N | T |
|---|---|---|---|---|---|---|---|
| **—** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **S** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **A** | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| **V** | 0 | 1 | 1 | 2 | 2 | 2 | 2 |
| **A** | 0 | 1 | 1 | 2 | 2 | 2 | 2 |
| **N** | 0 | 1 | 1 | 2 | 2 | 3 | 3 |
| **T** | 0 | 1 | 1 | 2 | 2 | 3 | 4 |

The LCS length is **4**. Reconstructing with the left-on-tie rule:

- `(6,6)`: T = T → **T**; `(5,5)`.
- `(5,5)`: N = N → **N**; `(4,4)`.
- `(4,4)`: A ≠ E, tie at 2 → left; `(4,3)`.
- `(4,3)`: A ≠ V, `c[3][3] = 2 > c[4][2] = 1` → up; `(3,3)`.
- `(3,3)`: V = V → **V**; `(2,2)`.
- `(2,2)`: A ≠ D, tie at 0 → left; `(2,1)`.
- `(2,1)`: A = A → **A**; `(1,0)`; stop.

Output **AVNT**, length 4.

### 6.8 Complexity

The table has `(m+1)(n+1)` cells, each filled in constant time: **Θ(mn)** time. Space is **Θ(mn)** for the table and arrows. If only the length is required, two rows (or two columns) suffice, giving **Θ(min(m, n))** space. Recovering the actual subsequence in linear space needs Hirschberg's divide-and-conquer variant; that is beyond the syllabus, but mentioning it is a bonus.

### 6.9 Common mistakes

- Solving longest common **substring** instead of subsequence.
- Using `c[i−1][j−1] + 1` on a mismatch (that is the substring recurrence).
- Reading the answer from the last cell of the wrong dimension, or from the maximum interior cell.
- Off-by-one indexing: `X[i]` in the recurrence corresponds to row `i`, but row 0 is the empty prefix.
- Reconstructing forward from `(1,1)` without stored arrows; backtracking from `(m,n)` is the reliable method.
- Forgetting that the answer is a string, not only its length.
- Claiming the LCS is unique. It often is not.

---

## 7 — Choosing and comparing the five algorithms

| Algorithm | Problem | State | Recurrence | Computation order | Time | Space |
|---|---|---|---|---|---|---|
| Multistage graph | Cheapest source-to-sink path in a layered DAG | `cost(i,j)` | `min(c(j,l) + cost(i+1,l))` | stages backwards | Θ(V+E) | Θ(V) |
| Floyd–Warshall | All-pairs shortest paths | `D[i][j]` | `min(D[i][j], D[i][k]+D[k][j])` | pivot `k` outermost | Θ(n³) | Θ(n²) |
| 0/1 knapsack | Maximum profit within capacity | `m[i,w]` | `max(leave, take)` | rows `i`, then `w` | Θ(nM) | Θ(nM) |
| TSP by DP | Minimum Hamiltonian tour | `g(i,S)` | `min(c(i,j)+g(j,S−{j}))` | subset size increasing | O(n²2ⁿ) | O(n2ⁿ) |
| LCS | Longest common subsequence | `c[i][j]` | match: diagonal + 1; else max(up, left) | rows, then columns | Θ(mn) | Θ(mn) |

**How to choose in an exam.**

- Layered graph with a source and a sink → multistage.
- "All pairs", matrix output, negative edges → Floyd–Warshall.
- Capacity with each item once → 0/1 knapsack.
- Visit every city and return, small `n` → TSP DP.
- Two strings and a common subsequence → LCS.

**DP, divide and conquer, greedy — one table.**

| | Divide and conquer | Dynamic programming | Greedy |
|---|---|---|---|
| Subproblems | Independent, non-overlapping | Overlapping | Usually one choice at each step |
| Direction | Top-down recursion | Bottom-up table (or memoised) | One pass after sorting or a priority rule |
| Correctness | Combining optimal subsolutions | Principle of optimality + table | Greedy-choice property + optimal substructure |
| Examples | Merge sort, binary search, quick sort | All five algorithms in this module | Fractional knapsack, Dijkstra, Prim, Kruskal |
| Failure mode | — | Large table, pseudo-polynomial | A locally best choice that is globally wrong |

The classic contrast: **fractional knapsack is greedy; 0/1 knapsack is DP.** The greedy ratio can leave capacity wasted, and taking a high-ratio item may block a better combination.

---

## 8 — Self-learning topics

### 8.1 Bellman–Ford algorithm

> **Supplementary clarification.** The official syllabus lists Bellman–Ford under self-learning. The derivation below is added for completeness and is not claimed to be taught in the Module 4 slide deck.

Bellman–Ford finds shortest paths from **one source** in a graph that may contain negative edges. It repeatedly **relaxes** every edge: if `d[u] + w(u,v) < d[v]`, update `d[v]`.

```
BELLMAN-FORD(V, E, source)
  for each vertex v: d[v] = INFINITY
  d[source] = 0
  for pass = 1 to |V|-1:
      for each edge (u, v, w):
          if d[u] + w < d[v]:
              d[v] = d[u] + w
  for each edge (u, v, w):
      if d[u] + w < d[v]:
          report "negative cycle reachable from the source"
  return d
```

Why `|V|−1` passes: a shortest path without a cycle has at most `|V|−1` edges, and one pass guarantees at least one more edge of every shortest path is correct. If an edge can still be relaxed on pass `|V|`, the improvement must come from a cycle, and that cycle has negative weight.

**Small example.** Vertices 1–4; edges 1→2 (4), 1→3 (5), 2→3 (−3), 3→4 (2). Source 1.

| Pass | d[1] | d[2] | d[3] | d[4] | Relaxations |
|---|---|---|---|---|---|
| 0 | 0 | ∞ | ∞ | ∞ | initial |
| 1 | 0 | 4 | 1 | 3 | 1→2, 2→3 improves 5 to 1, 3→4 |
| 2 | 0 | 4 | 1 | 3 | none |
| 3 | 0 | 4 | 1 | 3 | none |

Distances: `0, 4, 1, 3`. Complexity **O(VE)**. With a negative cycle (for example, adding 4→2 with weight −5), pass 4 would improve `d[2]` again, and the algorithm reports the cycle.

**Comparison with Floyd–Warshall.** Bellman–Ford is single-source with negative edges and detects negative cycles; Floyd–Warshall is all-pairs and also assumes no negative cycle. Dijkstra is faster (O(E log V)) but fails on negative edges because it finalises a vertex too early.

### 8.2 Real-life applications

| Algorithm | Real-life use |
|---|---|
| Multistage graph | Stage-wise project planning, resource allocation across phases, assembly-line costs |
| Floyd–Warshall | Road-network distance tables, routing tables, transitive closure, game-map all-pairs distances |
| 0/1 knapsack | Budget selection, cargo loading, exam revision with limited hours, feature selection |
| TSP by DP | Delivery-route planning for a small number of stops, PCB drilling, warehouse picking |
| LCS | `diff` and version control, DNA/protein alignment, plagiarism detection, autocomplete |
| Bellman–Ford | Distance-vector routing (RIP), currency-arbitrage detection, network fault analysis |

---

## 9 — Practice questions

Attempt these on blank paper. The fully worked answer key follows in Section 10. Each question states its provenance; none of these is a University examination paper.

### Q1 — Multistage graph

*Class example (Module 4 slide deck).* For the twelve-vertex graph in Figure 1, with stages `{1}`, `{2,3,4,5}`, `{6,7,8}`, `{9,10,11}`, `{12}`, compute `cost(1,1)`. Give the cost table and one optimal path.

### Q2 — Floyd–Warshall

*Worked example from the Module 4 slide deck.* For the weight matrix

```
      1    2    3    4
1     0    8    ∞    1
2     ∞    0    1    ∞
3     4    ∞    0    ∞
4     ∞    2    9    0
```

compute `D⁴`. Hence give the shortest path and distance from 2 to 4, and from 4 to 3.

### Q3 — 0/1 knapsack

*Assignment 4, Q2 (course assignment — not a University paper).* `n = 4`, `M = 5`, weights `(2, 3, 4, 5)`, profits `(3, 4, 5, 6)`. Build the DP table, give the maximum profit, and reconstruct the chosen items.

### Q4 — Travelling salesperson problem

*Assignment 4, Q3 (course assignment — not a University paper); also in the IAT-2 question bank.* For the cost matrix

```
      A    B    C    D
A     0    4    2    1
B     4    0   13    9
C     2   13    0    8
D     1    9    8    0
```

find an optimal tour using the DP recurrence `g(i, S)`. Show the `g` table and the tour.

### Q5 — Longest common subsequence (1)

*Preliminary (internal) examination — not a University paper.* Find an LCS of `X = SAVANT` and `Y = ADVENT`, and give its length. Show the `c` table.

### Q6 — Longest common subsequence (2)

*IAT-2 question bank (teacher's revision sheet) — not a University paper.* Find an LCS of `X = AMERICA` and `Y = ARMENIA`, and give its length. Show the `c` table.

### Q7 — 0/1 knapsack (2)

*IAT-2 question bank (teacher's revision sheet) — not a University paper.* `n = 4`, `M = 8`, weights `(3, 4, 6, 5)`, profits `(2, 3, 1, 4)`. Build the DP table and give the optimal selection and profit.

### Q8 — 0/1 knapsack (3)

*Preliminary (internal) examination — not a University paper.* Capacity `M = 15`; seven items with weights `(2, 3, 5, 7, 1, 4, 1)` and profits `(10, 5, 15, 7, 6, 10, 3)`. Find the maximum profit and the selected items.

### Q9 — Conceptual

*IAT-2 style theory question — not a University paper.* (a) State the principle of optimality. (b) Explain overlapping subproblems using the 0/1 knapsack recurrence. (c) Give three differences between dynamic programming and the greedy method.

### Q10 — Bellman–Ford (self-learning)

*Self-learning topic from the official syllabus.* For the graph with edges 1→2 (4), 1→3 (5), 2→3 (−3), 3→4 (2), run Bellman–Ford from vertex 1. Show the passes and the final distances. How would you detect a negative cycle?

### Q11 — LCS (3)

*Class practice from the Module 4 slide deck.* Find the LCS length of `X = ACBAED` and `Y = ABCABE`, and give one LCS.

---

## 10 — Answer key

### A1 — Multistage graph

Base: `cost(5,12) = 0`.

| Stage | Vertex | Computation | cost | D |
|---|---|---|---|---|
| 4 | 9 | 4 + 0 | 4 | 12 |
| 4 | 10 | 2 + 0 | 2 | 12 |
| 4 | 11 | 5 + 0 | 5 | 12 |
| 3 | 6 | min(6+4, 5+2) | 7 | 10 |
| 3 | 7 | min(4+4, 3+2) | 5 | 10 |
| 3 | 8 | min(5+2, 6+5) | 7 | 10 |
| 2 | 2 | min(4+7, 2+5, 1+7) | 7 | 7 |
| 2 | 3 | min(2+7, 7+5) | 9 | 6 |
| 2 | 4 | 11 + 7 | 18 | 8 |
| 2 | 5 | min(11+5, 8+7) | 15 | 8 |
| 1 | 1 | min(9+7, 7+9, 3+18, 2+15) | 16 | 2 |

**Answer:** minimum cost **16**, via `1 → 2 → 7 → 10 → 12`. The path `1 → 3 → 6 → 10 → 12` also costs 16.

### A2 — Floyd–Warshall

The four matrices are in Section 3.6. The final matrix is

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 0 | 3 | 4 | 1 |
| **2** | 5 | 0 | 1 | 6 |
| **3** | 4 | 7 | 0 | 5 |
| **4** | 7 | 2 | 3 | 0 |

**2 → 4:** distance **6**, path 2 → 3 → 1 → 4 (1 + 4 + 1). **4 → 3:** distance **3**, path 4 → 2 → 3 (2 + 1). The `next` matrix: `next[2][4] = 3`, `next[3][4] = 1`, `next[1][4] = 4`; `next[4][3] = 2`, `next[2][3] = 3`.

### A3 — 0/1 knapsack, M = 5

| i \ w | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 3 | 3 | 3 | 3 |
| 2 | 0 | 0 | 3 | 4 | 4 | 7 |
| 3 | 0 | 0 | 3 | 4 | 5 | 7 |
| 4 | 0 | 0 | 3 | 4 | 5 | 7 |

**Answer:** maximum profit **7**, items **1 and 2** (`X = 1,1,0,0`), weight 2 + 3 = 5.

Reconstruction: `m[4][5] = 7 = m[3][5]` → item 4 out; `m[3][5] = 7 = m[2][5]` → item 3 out; `m[2][5] = 7 ≠ m[1][5] = 3` → item 2 in, `w = 2`; `m[1][2] = 3 ≠ m[0][2] = 0` → item 1 in, `w = 0`.

### A4 — TSP, four cities

| State | Value | State | Value |
|---|---|---|---|
| g(B,∅) | 4 | g(C,∅) | 2 |
| g(D,∅) | 1 | g(B,{C}) | 15 |
| g(B,{D}) | 10 | g(C,{B}) | 17 |
| g(C,{D}) | 9 | g(D,{B}) | 13 |
| g(D,{C}) | 10 | g(B,{C,D}) | 19 |
| g(C,{B,D}) | 21 | g(D,{B,C}) | 24 |

At the start: `4 + 19 = 23`, `2 + 21 = 23`, `1 + 24 = 25`. **Optimal cost 23.** Tours: **A → B → D → C → A** and **A → C → D → B → A**.

### A5 — LCS, SAVANT / ADVENT

The `c` table is in Section 6.7. Length **4**. One LCS: **AVNT**. Reconstruct from `(6,6)` as shown there: T, N, V, A.

### A6 — LCS, AMERICA / ARMENIA

| c | — | A | R | M | E | N | I | A |
|---|---|---|---|---|---|---|---|---|
| **—** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **A** | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **M** | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 2 |
| **E** | 0 | 1 | 1 | 2 | 3 | 3 | 3 | 3 |
| **R** | 0 | 1 | 2 | 2 | 3 | 3 | 3 | 3 |
| **I** | 0 | 1 | 2 | 2 | 3 | 3 | 4 | 4 |
| **C** | 0 | 1 | 2 | 2 | 3 | 3 | 4 | 4 |
| **A** | 0 | 1 | 2 | 2 | 3 | 3 | 4 | 5 |

Length **5**. Reconstruction from `(7,7)`: A = A → **A**; `(6,6)` C ≠ I → up (4 = 4); `(5,6)` I = I → **I**; `(4,5)` R ≠ N, `c[3][5] = 3 = c[4][4]` → up; `(3,5)` E = E → **E**; `(2,4)` M ≠ E, `c[1][4] = 1 < c[2][3] = 2` → left; `(2,3)` M = M → **M**; `(1,2)` A ≠ R, tie → left; `(1,1)` A = A → **A**; stop. Forward: **A M E I A** (length 5).

### A7 — 0/1 knapsack, M = 8

| i \ w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | 0 | 0 | 0 | 2 | 3 | 3 | 3 | 5 | 5 |
| 3 | 0 | 0 | 0 | 2 | 3 | 3 | 3 | 5 | 5 |
| 4 | 0 | 0 | 0 | 2 | 3 | 4 | 4 | 5 | 6 |

**Answer:** profit **6**, items **1 and 4** (`X = 1,0,0,1`), weight 3 + 5 = 8. Reconstruction: `m[4][8] = 6 ≠ m[3][8] = 5` → item 4 in, `w = 3`; `m[3][3] = m[2][3]` → item 3 out; `m[2][3] = m[1][3]` → item 2 out; `m[1][3] = 2 ≠ m[0][3] = 0` → item 1 in, `w = 0`.

### A8 — 0/1 knapsack, M = 15

The final row of the table (capacity 0 to 15) is

| w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| m[7][w] | 0 | 6 | 10 | 16 | 19 | 19 | 21 | 26 | 31 | 34 | 34 | 36 | 41 | 44 | 44 | **46** |

**Answer:** maximum profit **46**, items **1, 2, 3, 5, 6**, with total weight 2 + 3 + 5 + 1 + 4 = 15. The corresponding profits are 10 + 5 + 15 + 6 + 10 = 46. (Items 4 and 7 are left out: item 4 weighs 7 and adds 7, which would displace a better combination; item 7 adds only 3.)

### A9 — Conceptual

**(a) Principle of optimality.** In an optimal sequence of decisions, whatever the first decision is, the remaining decisions must be optimal with respect to the state produced by the first decision. Equivalently, an optimal solution contains optimal solutions to its subproblems.

**(b) Overlapping subproblems in knapsack.** The recurrence `m[i][w] = max(m[i−1][w], pᵢ + m[i−1][w−wᵢ])` asks for `m[i−1][w]` and for a cell in the same previous row. Different items and capacities request the same earlier cells repeatedly; the table computes each `(i,w)` once and reuses it. A plain recursion would recompute the same `(i,w)` from many branches.

**(c) DP versus greedy.**

1. Greedy commits to one locally best choice; DP compares all choices using stored subproblem answers.
2. Greedy needs the greedy-choice property; DP needs optimal substructure and overlapping subproblems.
3. Greedy is usually faster (often O(n log n)); DP is usually polynomial in the table size but can be pseudo-polynomial (knapsack) or exponential (TSP).
4. Example: fractional knapsack is greedy; 0/1 knapsack is DP.

### A10 — Bellman–Ford

Initial `d = [0, ∞, ∞, ∞]`.

| Pass | Edge relaxations that change a value | d after the pass |
|---|---|---|
| 1 | 1→2 (d₂ = 4); 2→3 (d₃ = 1, better than 5); 3→4 (d₄ = 3) | 0, 4, 1, 3 |
| 2 | none | 0, 4, 1, 3 |
| 3 | none | 0, 4, 1, 3 |

**Answer:** `d = [0, 4, 1, 3]`. With `|V| = 4`, three passes suffice. To detect a negative cycle, run one more pass over all edges; if any edge can still be relaxed, a negative cycle is reachable from the source.

### A11 — LCS, ACBAED / ABCABE

The LCS length is **4**. Any one of **ABAE**, **ACAE**, **ACBE** is correct. For example, `ACAE` is at positions 1, 2, 4, 5 in `ACBAED` and 1, 3, 4, 6 in `ABCABE`. The full `c` table ends at `c[6][6] = 4`.

---

## 11 — Common mistakes across the module

| Trap | What the examiner expects |
|---|---|
| Writing "DP" without a state definition | A sentence defining each index and the value stored |
| Omitting base cases | The first row, column or stage written explicitly |
| Filling in a wrong order | A stated order (rows, stages, subset size) with a reason |
| Giving only the optimal value | Reconstruction of items, path or subsequence |
| Adding the same edge twice | Check each recurrence term against the table |
| Using a greedy choice in 0/1 knapsack | Compare leave/take, or state why greedy fails |
| Confusing LCS with substring | Order preserved, gaps allowed |
| Forgetting the TSP return edge | Base case `g(i, ∅) = c(i, 1)` and the final `c(1, j)` |
| Calling Floyd–Warshall O(n²) | Three nested loops: O(n³) |
| Calling knapsack polynomial | O(nM) is pseudo-polynomial |
| Reporting one optimal tour when two exist | State both, or say "one optimal tour is …" |
| Quoting a number without its unit | "16 cost units", "7 profit", "length 2" |

---

## 12 — Last-minute revision sheet

**General.** DP = optimal substructure + overlapping subproblems + table. State, recurrence, base, order, answer, reconstruction, complexity. Top-down = memoisation; bottom-up = tabulation.

**Multistage graph.**
`cost(i,j) = min_{edge j→l} [c(j,l) + cost(i+1,l)]`, `cost(k,sink) = 0`.
Class graph: **cost 16**, path **1–2–7–10–12**; also 1–3–6–10–12. Time Θ(V+E), space Θ(V).

**Floyd–Warshall.**
`D[i][j] = min(D[i][j], D[i][k] + D[k][j])`, pivot `k` outermost. Θ(n³), Θ(n²). Negative edges allowed; no negative cycles. Final matrix for the class example:

```
0 3 4 1
5 0 1 6
4 7 0 5
7 2 3 0
```

**0/1 knapsack.**
`m[i][w] = max(m[i−1][w], pᵢ + m[i−1][w−wᵢ])` if `wᵢ ≤ w`, else `m[i−1][w]`.
Class example: **profit 7**, items 1 and 2. Θ(nM) time and space; O(M) space with a right-to-left 1-D array; pseudo-polynomial.

**TSP by DP.**
`g(i,S) = min_{j∈S} [c(i,j) + g(j,S−{j})]`, `g(i,∅) = c(i,1)`.
Class matrix: **23**, tours **A–B–D–C–A** and **A–C–D–B–A**. O(n²2ⁿ) time, O(n2ⁿ) space.

**LCS.**
Match: `c[i][j] = c[i−1][j−1] + 1`. Mismatch: `max(c[i−1][j], c[i][j−1])`.
`ACADB` / `CBDA` → length **2** (`CA` or `CB`). `SAVANT` / `ADVENT` → **AVNT**, length 4. `AMERICA` / `ARMENIA` → **AMEIA**, length 5. Θ(mn).

**Bellman–Ford (self-learning).** Relax all edges `|V|−1` times; O(VE); a further relaxation means a negative cycle.

**Numbers to remember:** 16 (multistage), 23 (TSP), 7 (knapsack M=5), 2 (LCS ACADB/CBDA), 4 (SAVANT/ADVENT), 5 (AMERICA/ARMENIA), 46 (knapsack M=15).

---

## 13 — References and attribution

**Official syllabus.**
University of Mumbai, Faculty of Science and Technology, *6.21 (N) B.E. Artificial Intelligence and Machine Learning, Semester III and Semester IV*, 2025–26, page 23 (Module IV). PDF: `https://mu.ac.in/old/wp-content/uploads/2025/06/6.21-N-B.E.-AI-ML-sem-III-IV.pdf`.

**Course material inspected.**
- Module 4 slide deck: `Module 4 Dynamic Programming (UPDATED)16 sept.pptx (1).pdf` — used for the general method, the 12-vertex multistage example, the greedy comparison, the TSP matrix and the LCS examples. Some matrices in the deck are images; values were re-derived and checked independently.
- `Assignment No 4 AOA.docx` — knapsack (`n=4, M=5`) and TSP matrix.
- `PRELIMS AOA.docx` — LCS `SAVANT`/`ADVENT` and the seven-item knapsack.
- `IAT-2 Question Bank (2025-26) (FINAL) (1).pdf` and `IAT-2 Question Bank (2026-27) (FINAL) (1).docx` — LCS and knapsack practice. These are teacher revision sheets, not University papers.

**Standard references for further reading (not quoted page-by-page).**
- T. H. Cormen, C. E. Leiserson, R. L. Rivest and C. Stein, *Introduction to Algorithms*, 3rd edition, MIT Press.
- E. Horowitz, S. Sahni and S. Rajasekaran, *Computer Algorithms*, 2nd edition, Universities Press.

**Attribution.** All explanations, tables, pseudocode, worked traces and diagrams in this guide were written for this study guide. The class examples are attributed above. Passages marked **Supplementary clarification** are added by the guide author and are not claimed to be part of the slide deck. No question in this guide is labelled a University examination question; the provenance of each practice question is stated at the question.

