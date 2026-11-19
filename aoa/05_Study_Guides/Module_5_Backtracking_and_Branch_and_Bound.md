# AOA — Module 5: Backtracking and Branch and Bound

**B.E. Computer Science (AI & ML) · Semester III · Course 2023113 · NEP 2020**
**Module V · 7 teaching hours**
End-semester pattern: 6 questions of 20 marks · Q1 compulsory · answer any 3 · 2 hours

This guide covers the complete prescribed Module V: the general backtracking method, N-queens, sum of subsets, graph colouring, the general branch-and-bound method, the travelling salesperson problem and the 15-puzzle problem. Every algorithm is presented as problem → idea → recognition → method → pseudocode → worked trace → complexity → mistakes. Practice questions and a separate worked answer key are at the end.

---

## Syllabus and scope

> **Official syllabus — University of Mumbai, 6.21 (N) B.E. AI & ML, Sem III & IV, 2025–26, page 23.**
> **Module V — Backtracking and Branch and Bound:** General Method, Backtracking: N-queen problem, Sum of subsets, Graph coloring. Branch and Bound: Travelling Salesperson Problem, 15 Puzzle problem.
> **Hours:** 7 · **CO mapping as printed:** CO1.

> **A note on the CO number.** The syllabus table prints CO1 for Module V, while CO5 is the outcome that describes "Backtracking and Branch and Bound". This guide follows the printed module content and does not silently change the syllabus. If an examination question asks for the CO mapping, quote the printed table and add the discrepancy.

| Prescribed topic | What you must be able to do | Section |
|---|---|---|
| General method (backtracking) | Draw a state-space tree, define promising and non-promising nodes, write the control abstraction. | 1 |
| N-queens | Place queens row by row, write the bounding test, trace 4-queens and 8-queens. | 2 |
| Sum of subsets | Write the inclusion/exclusion tree with the two pruning tests, trace a full example. | 3 |
| Graph colouring | Test a colour assignment, trace the search, state the complexity. | 4 |
| General method (branch and bound) | Explain live/dead/expanded nodes, bounds, incumbent, FIFO/LIFO/LC search. | 5 |
| TSP by branch and bound | Reduce the cost matrix, compute child bounds, expand in best-bound order. | 6 |
| 15-puzzle by branch and bound | Define `c(x) = f(x) + g(x)`, expand the least-cost live node, trace to the goal. | 7 |

**Not in Module V.** The syllabus does not prescribe the 8-puzzle separately, the assignment problem, or knapsack by branch and bound. They may be used as illustrations, but do not present them as prescribed topics. Backtracking for the Hamiltonian cycle and the m-colouring decision problem are standard extensions; graph colouring is the prescribed version.

---

## 1 — The general method of backtracking

### 1.1 The problem

Backtracking solves **constraint satisfaction** and **combinatorial optimisation** problems: choose values for `n` variables `x₁, x₂, …, xₙ` from finite domains so that a set of constraints is satisfied, and possibly so that an objective is optimised. Examples: place `n` queens, choose a subset with a given sum, colour a graph, find a Hamiltonian tour.

A brute-force method generates all `|D₁| × |D₂| × … × |Dₙ|` tuples and tests each one. Backtracking builds the tuple **one component at a time** and abandons a partial tuple as soon as it cannot be completed.

### 1.2 The idea

The search is a **depth-first traversal of a state-space tree**:

- The root is the empty assignment.
- A node at level `i` fixes `x₁ … xᵢ`.
- An edge from level `i−1` to level `i` chooses a value for `xᵢ`.
- A node is **promising** if it can still be extended to a complete solution; otherwise it is **non-promising** and its whole subtree is **pruned**.
- When a node has no promising child, the search **backtracks** to its parent and tries the next value.

The test that decides whether a partial assignment is promising is the **bounding function** (also called the feasibility test). For N-queens it is the column/diagonal test; for sum of subsets it is `s ≤ m` and `s + remaining ≥ m`; for graph colouring it is "no neighbour has the same colour".

### 1.3 How to recognise it

- "Find all solutions", "find one solution", "place n queens", "subset with sum", "colour the graph".
- The answer is a tuple `(x₁, …, xₙ)` and the constraints can be checked incrementally.
- A greedy or DP solution is not obvious, and the search space is a tree of choices.
- The question says "state-space tree", "promising", "pruning" or "backtracking".

### 1.4 How it works

1. Define the solution as a tuple and the domain of each component.
2. Define a test `PROMISING(k)` that checks the partial tuple `x₁ … xₖ` against all constraints involving those components.
3. Start with `k = 1`. Try each value in the domain.
4. If the partial tuple is promising, recurse to `k+1`. If `k = n`, a solution is found: print it.
5. If no value works, return to `k−1` and try its next value.
6. For optimisation, keep the best complete solution found so far and add a bound to prune subtrees that cannot beat it.

### 1.5 Pseudocode — recursive control abstraction

```
BACKTRACK(k)
  for each value v in domain[k]:
      if PROMISING(k, v):
          x[k] = v
          if k == n:
              process the solution x[1..n]
          else:
              BACKTRACK(k+1)
  // returning from the loop means no value worked: backtrack to level k-1
```

The iterative version keeps an explicit stack; the recursive version is what examiners expect because it shows the tree directly.

### 1.6 Worked example — a tiny state-space tree

Variables `x₁, x₂` with domain `{0, 1}` and the constraint `x₁ ≠ x₂`. The tree has a root, two level-1 nodes and four leaves. The branch `x₁ = 1, x₂ = 1` is non-promising and pruned; the other two leaves are solutions `(0,1)` and `(1,0)`. The search visits `(0,0)`, `(0,1)`, `(1,0)`, `(1,1)` in depth-first order and prunes only the last. For a small tree the saving is invisible; for N-queens it is enormous.

### 1.7 Complexity

Worst case the tree has `b^d` nodes, where `b` is the branching factor and `d` the depth, so time is **O(b^d)**; pruning reduces the constant and often the exponent in practice, but does not change the worst-case bound. Space is **O(d)** for the recursion stack plus the solution array. This is why backtracking can handle `n = 8` queens but not `n = 30`.

### 1.8 Common mistakes

- Calling a full enumeration "backtracking" without pruning.
- Testing a constraint only at the leaf; the point is to test it as early as possible.
- Forgetting to undo the assignment when returning (`x[k] = 0`), so later branches see stale values.
- Pruning a node that is actually completable (an incorrect bounding function).
- Not distinguishing "no solution in this subtree" from "no solution at all".
- Reporting the number of nodes visited when the question asks for the number of solutions.

---

## 2 — N-queens problem

### 2.1 The problem

Place `n` queens on an `n × n` chessboard so that no two queens attack each other: no two share a row, a column or a diagonal. The `n`-queens problem asks for all such placements; the 8-queens instance is the classic.

### 2.2 The idea

Place **one queen per row**, left to right. Then the row constraint is automatic. Let `x[i]` be the column of the queen in row `i`. When placing the queen in row `k` at column `j`, the partial assignment is promising if for every earlier row `i < k`:

```
x[i] ≠ j                  (different column)
|x[i] − j| ≠ k − i        (different diagonal)
```

The first test catches columns; the second catches both diagonals in one expression. If either fails, the square is attacked and the search tries the next column.

### 2.3 How to recognise it

- "Queens", "chessboard", "no two attack", "place n queens".
- A tuple of column positions, one per row.
- The constraints are local and incremental — exactly the backtracking pattern.
- Variants: count the solutions, print the first solution, or place `n` rooks (columns only).

### 2.4 How it works

1. Start at row `k = 1`.
2. For `j = 1 … n`, test `PLACE(k, j)` against rows `1 … k−1`.
3. If promising, set `x[k] = j` and recurse to row `k+1`.
4. When `k = n+1`, a complete placement is found; print `x[1..n]`.
5. If no column works, return to row `k−1` and continue its loop.

### 2.5 Pseudocode

```
NQUEENS(k, n, x)
  for j = 1 to n:
      if PLACE(k, j):
          x[k] = j
          if k == n:
              print x[1..n]
          else:
              NQUEENS(k+1, n, x)

PLACE(k, j)
  for i = 1 to k-1:
      if x[i] == j or abs(x[i] - j) == k - i:
          return false
  return true
```

For a single solution, replace the `print` with a global flag and stop the recursion once the flag is set.

### 2.6 Worked example — four queens

Rows are 1–4, columns 1–4. The trace below is the actual depth-first search.

| Step | Action | Reason | Result |
|---|---|---|---|
| 1 | Q1 = 1 | first column | promising |
| 2 | Q2 = 1 | same column as Q1 | rejected |
| 3 | Q2 = 2 | diagonal with Q1 (|2−1| = 1 = 2−1) | rejected |
| 4 | Q2 = 3 | column free, diagonals free | promising |
| 5 | Q3 = 1 | same column as Q1 | rejected |
| 6 | Q3 = 2 | diagonal with Q2 (|2−3| = 1) | rejected |
| 7 | Q3 = 3 | same column as Q2 | rejected |
| 8 | Q3 = 4 | diagonal with Q2 (|4−3| = 1) | rejected → backtrack to Q2 |
| 9 | Q2 = 4 | column free | promising |
| 10 | Q3 = 1 | same column as Q1 | rejected |
| 11 | Q3 = 2 | column is free; diagonals with Q2 (|2−4| = 2) and Q1 (|2−1| = 1) are clear | promising |
| 12 | Q4 = 1 | same column as Q1 | rejected |
| 13 | Q4 = 2 | same column as Q3 | rejected |
| 14 | Q4 = 3 | diagonal with Q3 (|3−2| = 1 = 4−3) | rejected |
| 15 | Q4 = 4 | same column as Q2 | rejected → backtrack to Q3 |
| 16 | Q3 = 3 | diagonal with Q2 (|3−4| = 1) | rejected |
| 17 | Q3 = 4 | same column as Q2 | rejected → backtrack to Q2 |
| 18 | Q2 has no more columns | backtrack to Q1 | — |
| 19 | Q1 = 2 | next column | promising |
| 20 | Q2 = 1 | diagonal with Q1 (|1−2| = 1) | rejected |
| 21 | Q2 = 2 | same column as Q1 | rejected |
| 22 | Q2 = 3 | diagonal with Q1 (|3−2| = 1) | rejected |
| 23 | Q2 = 4 | column and diagonals free | promising |
| 24 | Q3 = 1 | free with Q1 and Q2 | promising |
| 25 | Q4 = 1 | same column as Q3 | rejected |
| 26 | Q4 = 2 | same column as Q1 | rejected |
| 27 | Q4 = 3 | free with Q1, Q2, Q3 (check diagonals) | **solution (2, 4, 1, 3)** |

The solution is shown in Figure 1: row 1 column 2, row 2 column 4, row 3 column 1, row 4 column 3.

![Figure 1 — the first 4-queens solution, (2, 4, 1, 3)](figure:board4)

The first branch `Q1 = 1` is exhausted without a solution: step 8 kills `Q2 = 3`, and steps 14–17 kill `Q2 = 4`. That is 17 steps with no solution. Backtracking then tries `Q1 = 2`, and the solution appears at step 27. The ability to abandon a whole subtree at step 8 and again at step 17 is the point of the method.

### 2.7 The 8-queens instance

The same algorithm with `n = 8` has **92 solutions**. A naive enumeration would examine `8⁸ = 16,777,216` tuples; the column and diagonal tests prune almost all of them. The first solution found by the standard column order is `(1, 5, 8, 6, 3, 7, 2, 4)`. The counting variant is a common examination question; the answer 92 is worth memorising, and the method is more important than the number.

### 2.8 Complexity

The tree has at most `n!` leaves (one queen per row, distinct columns), so the worst-case time is **O(n!)**, with pruning reducing the actual count. Space is **O(n)** for `x[1..n]` and the recursion stack. The `PLACE` test is O(n), so a naive bound is O(n·n!), but the pruning dominates.

### 2.9 Common mistakes

- Placing more than one queen in a row or forgetting that one queen per row is the modelling choice.
- Testing only columns and forgetting diagonals.
- Using `abs(x[i] − j) == k − i` with rows counted from 0 in one place and 1 in another.
- Not undoing `x[k]` on backtracking (with the recursive formulation this is automatic, but the iterative version needs it).
- Printing partial boards as solutions.
- Using a 2-D board when a 1-D array `x[row] = column` is enough; examiners reward the smaller representation.

---

## 3 — Sum of subsets

### 3.1 The problem

Given `n` positive weights `w₁ … wₙ` and a target `m`, find every subset whose sum is exactly `m`. This is the subset-sum problem, a special case of 0/1 knapsack with `pᵢ = wᵢ` and the profit required to equal the capacity.

### 3.2 The idea

Build the subset one weight at a time. At level `i` decide whether to **include** `wᵢ` (`xᵢ = 1`) or **exclude** it (`xᵢ = 0`). Maintain:

- `s` — the sum of the weights chosen so far;
- `r` — the sum of the weights still available (from `i` to `n`).

A node is promising only if both tests hold:

```
s + w[i] ≤ m          (taking the next weight does not overshoot)  -- checked before the include branch
s + r ≥ m             (the remaining weights can still reach m)
```

The second test is the bounding function: if even taking everything that remains cannot reach `m`, the subtree is dead. The first test prunes overshoots. Sorting the weights in increasing order makes the pruning more effective and is good practice, but the correctness does not depend on it.

### 3.3 How to recognise it

- "Subset with sum", "subset sum", "exact sum", "target".
- Positive weights and a target; each weight used at most once.
- The answer is a family of subsets, or a yes/no decision.
- A DP table is possible (O(nm)); backtracking is asked when the question says "state-space tree", "pruning" or "all subsets".

### 3.4 How it works

1. Sort the weights (optional but recommended) and compute the total.
2. Start with `s = 0`, `r = total`, `i = 1`.
3. Include branch: if `s + wᵢ ≤ m`, set `xᵢ = 1`, recurse with `s + wᵢ`, `r − wᵢ`.
4. Exclude branch: recurse with the same `s`, `r − wᵢ`.
5. Before either branch, if `s = m`, record the solution. If `s + r < m` or `i > n`, prune.
6. Undo `xᵢ` after the include branch.

### 3.5 Pseudocode

```
SUBSET-SUM(i, s, r)
  // x[1..n] is the current choice; r is the sum of w[i..n]
  if s == m:
      print x[1..n]
      return
  if i > n or s + r < m:
      return
  if s + w[i] <= m:                 // include w[i]
      x[i] = 1
      SUBSET-SUM(i+1, s + w[i], r - w[i])
  x[i] = 0                          // exclude w[i]
  SUBSET-SUM(i+1, s, r - w[i])
```

This version prints a solution as soon as `s = m` and does not explore its extensions; that is correct because all weights are positive, so extending an exact sum would overshoot.

### 3.6 Worked example — n = 4, m = 17, w = (2, 7, 8, 15)

Total `r = 32`. The trace below is the complete depth-first search.

| Step | Level | Decision | s | r after | Test | Result |
|---|---|---|---|---|---|---|
| 1 | 1 | include 2 | 2 | 30 | 2 + 30 ≥ 17 | promising |
| 2 | 2 | include 7 | 9 | 23 | 9 + 23 ≥ 17 | promising |
| 3 | 3 | include 8 | 17 | 15 | s = m | **solution {2, 7, 8}** |
| 4 | 3 | exclude 8 | 9 | 15 | 9 + 15 ≥ 17 | promising |
| 5 | 4 | include 15 | 24 | 0 | 24 > 17 | prune (overshoot) |
| 6 | 4 | exclude 15 | 9 | 0 | 9 + 0 < 17 | prune |
| 7 | 2 | exclude 7 | 2 | 23 | 2 + 23 ≥ 17 | promising |
| 8 | 3 | include 8 | 10 | 15 | 10 + 15 ≥ 17 | promising |
| 9 | 4 | include 15 | 25 | 0 | 25 > 17 | prune |
| 10 | 4 | exclude 15 | 10 | 0 | 10 < 17 | prune |
| 11 | 3 | exclude 8 | 2 | 15 | 2 + 15 = 17 | promising |
| 12 | 4 | include 15 | 17 | 0 | s = m | **solution {2, 15}** |
| 13 | 4 | exclude 15 | 2 | 0 | 2 < 17 | prune |
| 14 | 1 | exclude 2 | 0 | 30 | 0 + 30 ≥ 17 | promising |
| 15 | 2 | include 7 | 7 | 23 | 7 + 23 ≥ 17 | promising |
| 16 | 3 | include 8 | 15 | 15 | 15 + 15 ≥ 17 | promising |
| 17 | 4 | include 15 | 30 | 0 | 30 > 17 | prune |
| 18 | 4 | exclude 15 | 15 | 0 | 15 < 17 | prune |
| 19 | 3 | exclude 8 | 7 | 15 | 7 + 15 ≥ 17 | promising |
| 20 | 4 | include 15 | 22 | 0 | 22 > 17 | prune |
| 21 | 4 | exclude 15 | 7 | 0 | 7 < 17 | prune |
| 22 | 2 | exclude 7 | 0 | 23 | 0 + 23 ≥ 17 | promising |
| 23 | 3 | include 8 | 8 | 15 | 8 + 15 ≥ 17 | promising |
| 24 | 4 | include 15 | 23 | 0 | 23 > 17 | prune |
| 25 | 4 | exclude 15 | 8 | 0 | 8 < 17 | prune |
| 26 | 3 | exclude 8 | 0 | 15 | 0 + 15 < 17 | prune |

**Solutions:** `{2, 7, 8}` and `{2, 15}`. Both sum to 17. The second is easy to miss if the search stops after the first solution; the question "find all subsets" requires continuing the traversal.

### 3.7 Complexity

The tree has at most `2ⁿ` leaves and `2ⁿ⁺¹ − 1` nodes, so the worst case is **O(2ⁿ)** time and **O(n)** space for the recursion. The bounding tests do not change the worst case (if every subset is promising) but prune heavily in typical instances. The DP alternative is O(nm) time and O(nm) or O(m) space, which is better when `m` is small; backtracking is the prescribed method and is preferable when the question asks for all subsets or a search tree.

### 3.8 Common mistakes

- Forgetting to subtract the weight from `r` on both branches.
- Testing `s + r ≥ m` only after recursing, not before.
- Using `s + w[i] ≤ m` on the exclude branch as well.
- Recording a solution and then continuing to extend it (positive weights mean it cannot reach `m` again).
- Sorting the weights but then reporting the subset in sorted order without mapping back to the original indices.
- Missing the `{2, 15}` solution because the first solution ended the search.

---

## 4 — Graph colouring

### 4.1 The problem

Given an undirected graph `G = (V, E)` and `m` colours, assign a colour to every vertex so that no two adjacent vertices have the same colour. This is the **m-colouring decision problem**; the optimisation version asks for the smallest `m` (the chromatic number).

### 4.2 The idea

Colour the vertices in a fixed order, one at a time. Let `x[i]` be the colour of vertex `i`, with `x[i] ∈ {1, …, m}`. When colouring vertex `k`, the partial assignment is promising if no neighbour of `k` among vertices `1 … k−1` already has the chosen colour:

```
for every edge (k, j) with j < k:  x[j] ≠ c
```

If a colour fails, try the next one. If all `m` colours fail, backtrack.

### 4.3 How to recognise it

- "Colour the graph", "m colours", "no two adjacent", "map colouring", "register allocation".
- The graph is small, and the question asks for a state-space tree or a trace.
- The decision version is `m`-colouring; the optimisation version asks for the minimum `m`.
- A greedy colouring may use more colours than necessary; backtracking finds a valid assignment or proves that none exists.

### 4.4 How it works

1. Order the vertices `1 … n`.
2. Start with vertex 1 and colour 1.
3. For the next vertex, try colours `1 … m`; keep a colour if no earlier neighbour has it.
4. If a colour works, move to the next vertex. If none works, backtrack.
5. When all vertices are coloured, print the colouring. To find the minimum `m`, try `m = 1, 2, …` until a colouring exists.

### 4.5 Pseudocode

```
M-COLOURING(k, n, m, x, adj)
  for c = 1 to m:
      if SAFE(k, c):
          x[k] = c
          if k == n:
              print x[1..n]
          else:
              M-COLOURING(k+1, n, m, x, adj)
          x[k] = 0

SAFE(k, c)
  for j = 1 to k-1:
      if adj[k][j] == 1 and x[j] == c:
          return false
  return true
```

### 4.6 Worked example — five vertices, three colours

Graph edges: 1–2, 1–3, 2–3, 2–4, 2–5, 3–5, 4–5. Colour with `m = 3`. The graph and the final colouring are shown in Figure 2.

![Figure 2 — the five-vertex graph, coloured with three colours](figure:graph5)

Trace:

| Step | Vertex | Try colour | Conflict | Result |
|---|---|---|---|---|
| 1 | 1 | 1 | none | x1 = 1, promising |
| 2 | 2 | 1 | adjacent to 1 (colour 1) | reject |
| 3 | 2 | 2 | none | x2 = 2, promising |
| 4 | 3 | 1 | adjacent to 1 (colour 1) | reject |
| 5 | 3 | 2 | adjacent to 2 (colour 2) | reject |
| 6 | 3 | 3 | none | x3 = 3, promising |
| 7 | 4 | 1 | adjacent to 2 (colour 2) only | x4 = 1, promising |
| 8 | 5 | 1 | adjacent to 1 (colour 1) | reject |
| 9 | 5 | 2 | adjacent to 2 (colour 2) | reject |
| 10 | 5 | 3 | adjacent to 3 (colour 3) | reject → backtrack to 4 |
| 11 | 4 | 1 | undo | backtrack |
| 12 | 4 | 2 | adjacent to 2 (colour 2) | reject |
| 13 | 4 | 3 | none (neighbours 2 and 5; 5 uncoloured) | x4 = 3, promising |
| 14 | 5 | 1 | neighbours 2 (2), 3 (3), 4 (3); 1 is free | **x5 = 1, solution** |

**Solution:** `(1, 2, 3, 3, 1)`. Check every edge: 1–2 (1,2), 1–3 (1,3), 2–3 (2,3), 2–4 (2,3), 2–5 (2,1), 3–5 (3,1), 4–5 (3,1). All differ.

The dead end at step 10 is the heart of the example: colouring vertex 4 with 1 looked locally fine, but it consumed the only colour that vertex 5 could use. Backtracking changes vertex 4 to 3 and succeeds.

### 4.7 Complexity

The tree has at most `mⁿ` leaves, so the worst case is **O(mⁿ)** time and **O(n)** space. The `SAFE` test is O(n), so a naive bound is O(n·mⁿ); the pruning is what makes the search practical. Deciding whether a graph is `m`-colourable is NP-complete for `m ≥ 3`, so no polynomial algorithm is known.

### 4.8 Common mistakes

- Checking only the neighbours with a smaller index when the graph is directed; for undirected graphs the earlier-neighbour test is sufficient.
- Testing an edge twice and reporting a false conflict.
- Forgetting to reset `x[k] = 0` after the loop.
- Claiming the first colouring found is optimal. It is valid; optimality requires trying smaller `m` or adding an objective.
- Confusing `m` (number of colours) with `n` (number of vertices).
- Using a greedy colouring and calling it backtracking.

---

## 5 — The general method of branch and bound

### 5.1 The problem

Branch and bound solves **combinatorial optimisation** problems: find the minimum-cost (or maximum-profit) feasible solution among exponentially many candidates. Unlike plain backtracking, it uses a numeric **bound** at each node to discard subtrees that cannot contain a better solution than the best one already found.

### 5.2 The idea

The search is again a state-space tree, but each node carries:

- a **cost** or **bound** — an optimistic estimate of the best completion reachable from this node;
- a flag for whether the node is **live** (generated, not yet expanded), **expanded** (its children have been generated) or **dead** (killed);
- the **incumbent** — the cost of the best complete solution found so far.

For a minimisation problem:

- A node is killed if `bound ≥ incumbent` (it cannot improve the best known solution).
- A node is also killed if it is infeasible.
- The search continues until the live set is empty or the best live bound is not less than the incumbent.

The **expansion strategy** decides which live node to expand next:

| Strategy | Live set | Order | Also called |
|---|---|---|---|
| **FIFO** | queue | breadth-first | BFS branch and bound |
| **LIFO** | stack | depth-first | DFS branch and bound |
| **LC** | priority queue on bound | best-bound first | least-cost search, best-first |

LC search usually examines the fewest nodes, but it needs a priority queue and more memory. DFS needs only a stack and is the easiest to trace by hand; FIFO is rarely the best but is easy to explain.

### 5.3 How to recognise it

- "Minimise cost", "maximise profit", "find the optimal tour", "15-puzzle".
- The question mentions bounds, reduced cost matrices, an incumbent, live/dead nodes, or least-cost search.
- A complete enumeration is too large, but a good optimistic estimate is available.
- If the question only asks for feasibility and uses a boolean promising test, it is backtracking, not branch and bound.

### 5.4 How it works

1. Build the root and compute its bound.
2. Put the root in the live set. Set the incumbent to ∞ (minimisation) or −∞ (maximisation).
3. While the live set is non-empty:
   - remove a live node according to the strategy;
   - if its bound cannot beat the incumbent, kill it;
   - if it is a complete solution and better than the incumbent, update the incumbent;
   - otherwise generate its children, compute each child's bound, and insert the promising children into the live set.
4. Stop when the live set is empty, or when the best live bound is not better than the incumbent (nothing left can improve it).
5. Return the incumbent and the corresponding solution.

### 5.5 Pseudocode — least-cost branch and bound

```
LC-BRANCH-AND-BOUND(root)
  incumbent = INFINITY
  best = null
  live = priority queue ordered by bound
  insert root with its bound
  while live is not empty:
      node = remove the live node with the smallest bound
      if node.bound >= incumbent:
          continue                       // cannot improve
      if node is a complete solution:
          if node.cost < incumbent:
              incumbent = node.cost
              best = node
      else:
          for each child of node:
              child.bound = LOWER-BOUND(child)
              if child.bound < incumbent:
                  insert child into live
  return incumbent, best
```

For maximisation, reverse the inequalities and initialise the incumbent to −∞.

### 5.6 A small illustration

A minimisation tree has root bound 10, children with bounds 12 and 14, and a first complete solution of cost 15. The child with bound 12 is expanded; its children have bounds 16 and 18. Both are killed (`16 ≥ 15`, `18 ≥ 15`). The child with bound 14 is expanded; its children have bounds 13 and 17. The 13 child leads to a solution of cost 13, which becomes the new incumbent. The 17 child is killed. The live set is empty; the answer is 13. The two subtrees with bounds 16 and 18 were never explored. This is the entire idea in one paragraph.

### 5.7 Complexity

Worst case the tree is the full enumeration, exponential in the number of decisions. With a good bound, branch and bound often explores far fewer nodes, but the worst-case bound is unchanged. Space depends on the strategy: O(depth) for DFS, potentially exponential for LC because the live set can grow. For TSP the worst case is O(n!) tours; for the 15-puzzle it is the number of reachable states (about `16!/2`).

### 5.8 Common mistakes

- Using an **upper** bound where a lower bound is required; an optimistic bound must never overestimate the true completion cost for minimisation.
- Pruning with `>` instead of `≥` (or the reverse) and losing the optimal solution.
- Forgetting to update the incumbent when a complete solution is found.
- Expanding a node after it has been killed.
- Calling a feasibility-only search "branch and bound".
- Mixing FIFO and LC in the trace: state the strategy at the start and follow it consistently.

---

## 6 — Travelling salesperson problem by branch and bound

### 6.1 The problem

A salesperson must visit every city exactly once and return to the start, at minimum cost. The cost matrix `C[i][j]` gives the cost of travelling from city `i` to city `j`. The graph is complete; missing edges are represented by ∞.

### 6.2 The idea

Use a **reduced cost matrix** to obtain a lower bound. For each row, subtract its smallest entry from every entry in the row; then for each column, subtract its smallest entry. The sum of all subtracted values is a lower bound on the cost of every tour, because every tour must leave each city once (one entry per row) and enter each city once (one entry per column).

To branch from a node that has fixed the edge `i → j`:

1. Delete row `i` and column `j` (city `i` is left, city `j` is entered).
2. Set `C[j][i] = ∞` to forbid returning to the start before all cities are visited.
3. Reduce the remaining matrix and add the reduction to the parent bound. The result is the child's bound.

A child is killed if its bound is not less than the incumbent. When a node has fixed `n−1` edges, the last edge closes the tour; its cost is the node's bound.

### 6.3 How to recognise it

- A cost matrix and "find the optimal tour".
- The question mentions "reduced cost matrix", "lower bound", "branch and bound", "least-cost search".
- The matrix is small (4–6 cities) so the reduction can be shown by hand.
- If the question asks for the `g(i,S)` DP table, it is Module IV, not this section.

### 6.4 How it works

1. Reduce the original matrix; the root bound is the sum of the reductions.
2. Generate the root's children, one for each possible first city `j` (edges `A → j`). For each, delete row A and column j, forbid `j → A`, reduce, and add the reduction to the root bound.
3. Insert the children into a least-cost live set.
4. Repeatedly remove the live node with the smallest bound.
5. If its bound is not less than the incumbent, kill it.
6. If it fixes `n−1` edges, close the tour and update the incumbent.
7. Otherwise branch on the next city, computing each child's bound as above.
8. Stop when the live set is empty. The incumbent is the optimal cost.

### 6.5 Pseudocode

```
REDUCE(M)
  total = 0
  for each row i:
      r = min(M[i][j] over j)
      if r > 0 and r < INFINITY:
          subtract r from every finite entry of row i
          total = total + r
  for each column j:
      c = min(M[i][j] over i)
      if c > 0 and c < INFINITY:
          subtract c from every finite entry of column j
          total = total + c
  return total

TSP-BB(C, n)
  root.matrix = C
  root.bound = REDUCE(root.matrix)
  live = priority queue containing root
  incumbent = INFINITY
  while live is not empty:
      node = remove live node with smallest bound
      if node.bound >= incumbent: continue
      if node fixes n-1 edges:
          close the tour and update incumbent
      else:
          for each city j not yet visited:
              child = node with edge (current, j) fixed
              delete row current and column j
              set C[j][start] = INFINITY
              child.bound = node.bound + REDUCE(child.matrix)
              if child.bound < incumbent: insert child into live
  return incumbent
```

### 6.6 Worked example — four cities

Cost matrix:

| from \ to | A | B | C | D |
|---|---|---|---|---|
| **A** | ∞ | 4 | 2 | 1 |
| **B** | 4 | ∞ | 13 | 9 |
| **C** | 2 | 13 | ∞ | 8 |
| **D** | 1 | 9 | 8 | ∞ |

**Root reduction.** Row minima: A = 1, B = 4, C = 2, D = 1; subtract them, total 8. Column minima of the reduced matrix: column B has 3, column C has 1; subtract, total 4. Root bound = 8 + 4 = **12**. Reduced matrix:

| | A | B | C | D |
|---|---|---|---|---|
| **A** | ∞ | 0 | 0 | 0 |
| **B** | 0 | ∞ | 8 | 5 |
| **C** | 0 | 8 | ∞ | 6 |
| **D** | 0 | 5 | 6 | ∞ |

**Children of the root.**

- **A → B.** Delete row A and column B; set B → A = ∞. Row minima: B = 5, C = 0, D = 0. Subtract 5 from row B. Column minima: C = 3. Subtract 3 from column C. Reduction = 8; bound = 12 + 8 = **20**.
- **A → C.** Delete row A and column C; set C → A = ∞. Row minima: B = 0, C = 6, D = 0. Subtract 6 from row C. Column minima: B = 5. Subtract 5 from column B. Reduction = 11; bound = 12 + 11 = **23**.
- **A → D.** Delete row A and column D; set D → A = ∞. Row minima: B = 0, C = 0, D = 5. Subtract 5 from row D. Column minima: C = 1. Subtract 1 from column C. Reduction = 6; bound = 12 + 6 = **18**.

Live set: `{AD:18, AB:20, AC:23}`. LC search expands **AD** first.

**Expand AD (bound 18).** Reduced matrix:

| | A | B | C | D |
|---|---|---|---|---|
| **B** | 0 | ∞ | 7 | ∞ |
| **C** | 0 | 8 | ∞ | ∞ |
| **D** | ∞ | 0 | 0 | ∞ |

- **A → D → B.** Delete row D and column B. Row minimum B? Row B has 7 in column C, so subtract 7. Reduction 7; bound = 18 + 7 = **25**.
- **A → D → C.** Delete row D and column C. Row C has 8 in column B, so subtract 8. Reduction 8; bound = 18 + 8 = **26**.

Both children are worse than the current best live bound (20), so they wait.

**Expand AB (bound 20).** Reduced matrix (after the A→B reduction):

| | A | B | C | D |
|---|---|---|---|---|
| **B** | ∞ | ∞ | 0 | 0 |
| **C** | 0 | ∞ | ∞ | 6 |
| **D** | 0 | ∞ | 3 | ∞ |

- **A → B → C.** Delete row B and column C. Row C has 6 in column D, so subtract 6. Reduction 6; bound = 20 + 6 = **26**.
- **A → B → D.** Delete row B and column D. Row D has 3 in column C, so subtract 3. Reduction 3; bound = 20 + 3 = **23**.

**Expand ABD (bound 23).** The only remaining city is C, so the tour is A → B → D → C → A, cost 4 + 9 + 8 + 2 = **23**. The incumbent becomes 23.

**Prune.** AC has bound 23, which is not less than the incumbent 23; ABC has 26; ADB has 25; ADC has 26. All are killed. The live set is empty. The optimal cost is **23**.

The search tree is summarised in Figure 3.

![Figure 3 — least-cost branch and bound tree for the four-city TSP](figure:tsp)

**A second optimal tour.** A → C → D → B → A also costs 2 + 8 + 9 + 4 = 23. It is never generated because AC is pruned once the incumbent is 23. If the tie were broken the other way, AC would be expanded, ACD would complete at 23, and ABD would then be pruned. Either way the optimal cost is 23. State this in the answer.

### 6.7 Full trace

| Step | Live node popped | Bound | Action | New live nodes |
|---|---|---|---|---|
| 1 | root | 12 | expand | AD 18, AB 20, AC 23 |
| 2 | AD | 18 | expand | ADB 25, ADC 26 |
| 3 | AB | 20 | expand | ABC 26, ABD 23 |
| 4 | ABD | 23 | complete tour A-B-D-C-A = 23 | incumbent 23 |
| 5 | AC | 23 | prune (23 ≥ 23) | — |
| 6 | ADB, ADC, ABC | 25, 26, 26 | prune | — |

### 6.8 Complexity

The worst case enumerates all `(n−1)!` tours, so time is **O(n!)**; space for the live set can also be exponential. The reduced-matrix bound is strong, and in practice far fewer nodes are expanded. The reduction itself is O(n²) per node. For comparison, the DP of Module IV is O(n²2ⁿ) and is preferable for `n` up to about 15 when the full table fits; branch and bound is preferable when a good incumbent is found early and memory is limited.

### 6.9 Common mistakes

- Forgetting to set the return edge `j → start` to ∞, so a child closes a subtour too early.
- Adding the row reduction twice, or forgetting the column reduction.
- Treating the reduced-matrix sum as the tour cost rather than a lower bound.
- Killing a node with `bound > incumbent` when the bound equals the incumbent and a tie is acceptable; state the convention.
- Expanding a node whose bound is already ≥ the incumbent.
- Reporting a partial path as a tour.
- Mixing the DP `g(i,S)` table with the B&B reduced matrices.

---

## 7 — The 15-puzzle problem

### 7.1 The problem

A 4 × 4 board contains the tiles 1–15 and one blank. A move slides a tile adjacent to the blank into the blank. Given a start configuration and the goal configuration (tiles in order, blank at the bottom-right), find a shortest sequence of moves.

### 7.2 The idea

Each board configuration is a state; each legal slide is an edge. The search tree is the graph of states. Use **least-cost branch and bound** with the evaluation function

```
c(x) = f(x) + g(x)
```

where `f(x)` is the number of moves already made from the start (the depth, also called `g` in some textbooks) and `g(x)` is a heuristic estimate of the remaining moves. A common estimate is the **number of misplaced tiles**: every tile that is not in its goal position must move at least once. Another is the **Manhattan distance**, the sum of the horizontal and vertical distances of every tile from its goal; it is at least as strong as the misplaced-tile count and is still admissible. The guide uses misplaced tiles because it is easy to compute by hand; state which heuristic you use.

`c(x)` is a lower bound on the cost of any solution through `x`: the moves already made plus at least the remaining moves. Expanding the live node with the smallest `c` is **least-cost search**. When the goal is popped, its `c` is the length of a shortest solution, provided the heuristic never overestimates.

### 7.3 How to recognise it

- A sliding-tile board, a blank, moves up/down/left/right.
- "15-puzzle", "8-puzzle", "shortest sequence of moves".
- The question gives `c(x) = f(x) + g(x)` and asks for the search tree or the sequence.
- If the question asks for a heuristic and its admissibility, this is the section.

### 7.4 How it works

1. Represent a state as a 4 × 4 array (or a string).
2. Compute `g` = number of misplaced tiles (excluding the blank); `f` = depth.
3. Insert the start with `c = f + g`.
4. Pop the live node with the smallest `c`.
5. If it is the goal, stop and output the moves.
6. Otherwise generate the legal moves (2, 3 or 4 depending on the blank), compute each child's `f` and `g`, and insert it with `c = f + g`.
7. Keep a visited set to avoid returning to a state already expanded (optional for a short trace, essential for a real program).

### 7.5 Pseudocode

```
BEST-FIRST-15(start, goal)
  open = priority queue ordered by c = f + g
  insert start with f = 0, g = MISPLACED(start), c = g
  closed = empty set
  while open is not empty:
      node = remove the node with the smallest c
      if node.state == goal:
          return node.moves, node.f
      if node.state in closed: continue
      add node.state to closed
      for each legal move:
          child.state = slide(node.state, move)
          child.f = node.f + 1
          child.g = MISPLACED(child.state)
          child.c = child.f + child.g
          insert child into open
  return failure
```

`MISPLACED(s)` counts tiles `t ≠ 0` with `s[r][c] ≠ goal[r][c]`; for a 4 × 4 board the maximum is 15, so the heuristic is bounded and cheap.

### 7.6 Worked example

Start:

```
1  2  3  4
5  6  7  8
9 10 12  .
13 14 11 15
```

Goal:

```
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15  .
```

**Start.** Misplaced tiles: 12, 11, 15 → `g = 3`; `f = 0`; `c = 3`. The blank is at row 3, column 4. Legal moves: Left (swap 12), Up (swap 8), Down (swap 15).

| Child | Move | Misplaced tiles | g | f | c |
|---|---|---|---|---|---|
| 1 | Left | 11, 15 | 2 | 1 | **3** |
| 2 | Down | 11, 12, 15 | 3 | 1 | **4** |
| 3 | Up | 8, 11, 12, 15 | 4 | 1 | **5** |

The left child has the smallest `c = 3`. Expand it (state `S1`):

```
1  2  3  4
5  6  7  8
9 10  . 12
13 14 11 15
```

From `S1`, the blank is at row 3, column 3. Legal moves: Left (swap 10), Up (swap 7), Down (swap 11), Right (back to start).

| Child | Move | g | f | c |
|---|---|---|---|---|
| S1a | Down (swap 11) | 1 | 2 | **3** |
| S1b | Up (swap 7) | 4 | 2 | 6 |
| S1c | Left (swap 10) | 4 | 2 | 6 |

`S1a` is:

```
1  2  3  4
5  6  7  8
9 10 11 12
13 14  . 15
```

`g = 1` (tile 15), `f = 2`, `c = 3`. Expanding `S1a`, the move Right swaps the blank with 15 and reaches the goal: `g = 0`, `f = 3`, `c = 3`.

**Sequence:** Left, Down, Right — three moves. The search is drawn in Figure 4.

![Figure 4 — least-cost search for the 15-puzzle from the start state](figure:puzzle)

**Why the sequence is optimal.** The start has `g = 3`, so every solution needs at least 3 moves. The search found one in 3 moves, so it is optimal. This is the admissibility argument in one line, and it is worth writing in the examination.

**A caution about the heuristic.** If two tiles are swapped and both are misplaced, the misplaced-tile count is 2, but undoing a swap may take more moves; the estimate is still a lower bound, just weaker than Manhattan distance. The puzzle is solvable only when the permutation parity is even relative to the goal (for a 4 × 4 board); the search itself does not need this check, but a written answer may mention it.

### 7.7 Full trace

| Step | Node popped | f | g | c | Action |
|---|---|---|---|---|---|
| 1 | start | 0 | 3 | 3 | expand: Left, Down, Up |
| 2 | S1 (Left) | 1 | 2 | 3 | expand: Down, Up, Left |
| 3 | S1a (Down) | 2 | 1 | 3 | expand: Right, others |
| 4 | goal (Right) | 3 | 0 | 3 | stop; 3 moves |

The `c` value never decreases below 3, and the goal is reached at 3, so the solution is optimal.

### 7.8 Complexity

The state space has `16!` arrangements, but only half are reachable (about `16!/2 ≈ 1.05 × 10¹³`). The worst-case time and space are exponential. With a good heuristic and a closed set, the search is practical for modest depths; the guide's example is three moves. The heuristic computation is O(16) per node.

### 7.9 Common mistakes

- Using `c = f − g` or `c = g − f`.
- Counting the blank as a misplaced tile.
- Using a heuristic that can overestimate (for example, counting a tile that is one move away as requiring more than one move). An inadmissible heuristic destroys optimality.
- Forgetting the depth term `f` and expanding by `g` alone; that is greedy best-first search, not branch and bound.
- Moving a tile that is not adjacent to the blank, or wrapping around the board edges.
- Reporting the number of nodes expanded instead of the move sequence.
- Not checking that the start state is solvable.

---

## 8 — Backtracking, branch and bound, and dynamic programming

| | Backtracking | Branch and bound | Dynamic programming |
|---|---|---|---|
| Goal | Any or all feasible solutions | Optimal solution | Optimal solution |
| Tree | State-space tree, DFS | State-space tree, any strategy | Table of states, no tree |
| Pruning test | Feasibility (promising) | Numeric bound + incumbent | None; every state is solved |
| Search order | Depth-first | FIFO, LIFO or least-cost | Increasing state size |
| Typical time | O(b^d), often n! or 2ⁿ | O(b^d), pruned | Polynomial or pseudo-polynomial |
| Space | O(d) | O(d) to exponential | Table size |
| Examples | N-queens, sum of subsets, colouring | TSP, 15-puzzle | Multistage, Floyd, knapsack, TSP-DP, LCS |

**The one-sentence distinction.** Backtracking asks *"can this partial assignment be completed?"*; branch and bound asks *"can this partial assignment beat the best solution I already have?"*. The first prunes on feasibility, the second on cost.

**Backtracking versus branch and bound in an answer.** Both build a state-space tree and prune. Backtracking is depth-first and uses a Boolean promising test. Branch and bound maintains an incumbent and a numeric bound, can use best-first order, and is used for optimisation. A question that says "find all solutions" points to backtracking; "find the minimum cost" points to branch and bound.

---

## 9 — Practice questions

Attempt these on blank paper; the worked key follows. Each question states its provenance. None is a University examination paper.

### Q1 — N-queens

*Assignment 5 (course assignment — not a University paper).* Write the backtracking algorithm for the n-queens problem. Explain the state-space tree and the promising test. Trace the first solution for `n = 4`.

### Q2 — Sum of subsets

*Assignment 5 (course assignment — not a University paper).* For `n = 4`, `m = 17`, weights `(2, 7, 8, 15)`, draw the state-space tree and find all subsets that sum to 17. State where pruning occurs.

### Q3 — Sum of subsets (2)

*Preliminary (internal) examination — not a University paper.* For weights `(3, 5, 6, 7, 2)` and target sum 15, find all subsets. Show the pruning tests.

### Q4 — Graph colouring

*Course tutorial example.* For the graph with edges 1–2, 1–3, 2–3, 2–4, 2–5, 3–5, 4–5, find a 3-colouring using backtracking. Show the trace and the backtrack.

### Q5 — 15-puzzle

*Assignment 5 (course assignment — not a University paper).* Explain the branch-and-bound formulation of the 15-puzzle with `c(x) = f(x) + g(x)`. For the start state in Figure 4, compute `c` for the first level and find a shortest move sequence.

### Q6 — TSP by branch and bound

*Preliminary (internal) examination and IAT-2 question bank — not a University paper.* For the cost matrix

```
      A    B    C    D
A     ∞    4    2    1
B     4    ∞   13    9
C     2   13    ∞    8
D     1    9    8    ∞
```

solve the TSP by branch and bound using the reduced cost matrix. Show the root bound, the child bounds, the search order and the optimal tour.

### Q7 — Conceptual

*IAT-2 style theory question — not a University paper.* (a) Distinguish between backtracking and branch and bound. (b) Define live node, dead node, expanded node and incumbent. (c) Why is a lower bound used in a minimisation problem?

### Q8 — 8-queens count

*Preliminary (internal) examination — not a University paper.* How many solutions does the 8-queens problem have? Explain why backtracking examines far fewer than `8⁸` tuples.

---

## 10 — Answer key

### A1 — N-queens

The algorithm is in Section 2.5. The state-space tree has one level per row; a node at level `k` fixes the columns of queens 1…k. A node is promising when `PLACE(k, j)` is true for every earlier row: different column and different diagonal.

For `n = 4`, the first solution is **(2, 4, 1, 3)**: row 1 column 2, row 2 column 4, row 3 column 1, row 4 column 3. The first branch `Q1 = 1` is exhausted without a solution: `Q2 = 3` fails at row 3, and `Q2 = 4` fails at row 4. Backtracking then tries `Q1 = 2` and succeeds. The complete trace is in Section 2.6; the board is Figure 1.

### A2 — Sum of subsets, (2, 7, 8, 15), m = 17

**Solutions:** `{2, 7, 8}` and `{2, 15}`. The full trace is Section 3.6. Pruning occurs when:

- the running sum exceeds 17 (for example, `2 + 7 + 8 + 15 = 32`);
- the running sum plus all remaining weights is below 17 (for example, `9 + 0 = 9` after excluding 8 and 15).

The include branch is taken only when `s + w[i] ≤ 17`. The exclude branch is always tried, but is pruned by `s + r < 17`.

### A3 — Sum of subsets, (3, 5, 6, 7, 2), sum = 15

Sorted weights: `(2, 3, 5, 6, 7)`, total 23. The solutions are:

- **{2, 6, 7}** = 15;
- **{3, 5, 7}** = 15.

Trace of the promising branches (s = running sum, r = remaining):

| Decision | s | r | s + r | Result |
|---|---|---|---|---|
| include 2 | 2 | 21 | 23 | promising |
| include 3 | 5 | 18 | 23 | promising |
| include 5 | 10 | 13 | 23 | promising |
| include 6 | 16 | 7 | 23 | overshoot, prune |
| exclude 6 | 10 | 7 | 17 | promising |
| include 7 | 17 | 0 | 17 | overshoot, prune |
| exclude 7 | 10 | 0 | 10 | prune |
| exclude 5 | 5 | 13 | 18 | promising |
| include 6 | 11 | 7 | 18 | promising |
| include 7 | 18 | 0 | 18 | overshoot, prune |
| exclude 7 | 11 | 0 | 11 | prune |
| exclude 6 | 5 | 7 | 12 | prune |
| exclude 3 | 2 | 18 | 20 | promising |
| include 5 | 7 | 13 | 20 | promising |
| include 6 | 13 | 7 | 20 | promising |
| include 7 | 20 | 0 | 20 | overshoot, prune |
| exclude 7 | 13 | 0 | 13 | prune |
| exclude 6 | 7 | 7 | 14 | prune |
| exclude 5 | 2 | 13 | 15 | **promising: include 6 and 7 → {2, 6, 7}** |
| exclude 2 | 0 | 21 | 21 | promising |
| include 3 | 3 | 18 | 21 | promising |
| include 5 | 8 | 13 | 21 | promising |
| include 6 | 14 | 7 | 21 | promising |
| include 7 | 21 | 0 | 21 | overshoot, prune |
| exclude 7 | 14 | 0 | 14 | prune |
| exclude 6 | 8 | 7 | 15 | **promising: include 7 → {3, 5, 7}** |

The second solution is found after the first, so a search that stops at the first solution would miss it.

### A4 — Graph colouring

The graph is in Section 4.6. The trace gives the colouring **x = (1, 2, 3, 3, 1)**. The key backtrack: with `x4 = 1`, vertex 5 sees colours 1, 2 and 3 on its neighbours 1, 2 and 3 and has no colour; the search undoes `x4`, tries 2 (blocked by vertex 2), then 3, and vertex 5 takes 1. Verify every edge: 1–2 (1,2), 1–3 (1,3), 2–3 (2,3), 2–4 (2,3), 2–5 (2,1), 3–5 (3,1), 4–5 (3,1). All valid.

### A5 — 15-puzzle

`f(x)` is the number of moves from the start, `g(x)` is the number of misplaced tiles, and `c(x) = f(x) + g(x)` is a lower bound on the total moves through `x`. The start has `g = 3`, so `c = 3`; the Left child has `g = 2`, `f = 1`, `c = 3`; its Down child has `g = 1`, `f = 2`, `c = 3`; the Right move reaches the goal with `g = 0`, `f = 3`, `c = 3`. The shortest sequence is **Left, Down, Right** (three moves). The full table is Section 7.6.

### A6 — TSP by branch and bound

Root bound: row minima 1 + 4 + 2 + 1 = 8; column minima 3 + 1 = 4; **root = 12**. Reduced matrix:

```
∞  0  0  0
0  ∞  8  5
0  8  ∞  6
0  5  6  ∞
```

Child bounds: **AB = 20**, **AC = 23**, **AD = 18**. LC order: AD (18), then AB (20). AD's children are ADB = 25 and ADC = 26; AB's children are ABC = 26 and ABD = 23. ABD completes the tour **A → B → D → C → A** with cost 4 + 9 + 8 + 2 = **23**, so the incumbent is 23. AC (23), ABC (26), ADB (25) and ADC (26) are pruned. The optimal cost is **23**; A → C → D → B → A is also optimal. The full reduction is in Section 6.6.

### A7 — Conceptual

**(a) Backtracking versus branch and bound.** Backtracking searches a state-space tree depth-first and prunes a node when it cannot be completed to a feasible solution (a Boolean promising test). Branch and bound searches for an optimum; it maintains an incumbent and a numeric bound, prunes a node when its bound cannot beat the incumbent, and may use FIFO, LIFO or least-cost order. Every branch-and-bound node is also a partial solution, but the pruning criterion is cost, not feasibility.

**(b) Definitions.**
- **Live node:** generated but not yet expanded, and not killed.
- **Dead node:** killed because it is infeasible or its bound cannot beat the incumbent.
- **Expanded node:** a node whose children have been generated.
- **Incumbent:** the cost of the best complete solution found so far.

**(c) Lower bound.** For minimisation, the true completion cost from a node is at least its lower bound. If the lower bound is already ≥ the incumbent, no completion can improve the incumbent, so the subtree can be discarded safely. An admissible (never-overestimating) bound guarantees that the optimal solution is never pruned.

### A8 — 8-queens

There are **92** solutions. A naive enumeration would examine `8⁸ = 16,777,216` tuples, but the search fixes one queen per row, so at most `8! = 40,320` column permutations are possible, and the column/diagonal test rejects most partial permutations after a few rows. The pruning is what makes the search fast; the worst-case bound is still exponential.

---

## 11 — Common mistakes across the module

| Trap | What the examiner expects |
|---|---|
| Calling enumeration "backtracking" | A pruning test applied to partial solutions |
| Forgetting to undo a choice | The sibling branch must see the parent's state |
| Confusing promising with feasible | A partial solution can be promising without being complete |
| Wrong diagonal formula | `abs(x[i] − j) == k − i` |
| Sum of subsets: forgetting `r` | Subtract the weight on both branches |
| Recording a solution then extending it | Positive weights: an exact sum cannot be extended |
| Colouring with too few colours | Check every edge, and try smaller `m` only after a valid colouring |
| Branch and bound: upper vs lower bound | Minimisation needs a lower bound |
| Pruning on `>` when equality is optimal | State the convention; `≥` is usual for minimisation |
| TSP: forgetting the return edge | Set `j → start = ∞` when the edge `start → j` is fixed |
| 15-puzzle: counting the blank | The blank is not a tile |
| Reporting nodes instead of the tour/moves | The question asks for the solution, not the search size |

---

## 12 — Last-minute revision sheet

**Backtracking.** State-space tree; DFS; promising/non-promising; bounding function; backtrack. Time O(b^d), space O(d).

**N-queens.** One queen per row; `x[i]` = column; test `x[i] ≠ j` and `|x[i] − j| ≠ k − i`. 4-queens first solution **(2,4,1,3)**; 8-queens has **92** solutions.

**Sum of subsets.** Include/exclude; prune if `s + w[i] > m` or `s + r < m`. `(2,7,8,15)`, `m = 17` → **{2,7,8}** and **{2,15}**.

**Graph colouring.** `x[k] = c` is promising if no earlier neighbour has colour `c`. The five-vertex example gives **(1,2,3,3,1)**; complexity O(mⁿ).

**Branch and bound.** Live/dead/expanded; incumbent; FIFO, LIFO, LC. Prune if bound ≥ incumbent (minimisation). B&B prunes on cost; backtracking prunes on feasibility.

**TSP by B&B.** Reduce rows then columns; root bound = sum of reductions; child bound = parent bound + child reduction; set the return edge to ∞. Four-city example: root **12**, children **20/23/18**, tour **A–B–D–C–A = 23**; A–C–D–B–A is also 23.

**15-puzzle.** `c(x) = f(x) + g(x)`; `f` = depth, `g` = misplaced tiles (or Manhattan); expand the smallest `c`. Example: start `c = 3`, then Left (c=3), Down (c=3), Right (goal, c=3); sequence **Left, Down, Right**.

**One-line distinctions.**

- Backtracking: "can this be completed?"
- Branch and bound: "can this beat the incumbent?"
- DP: "what is the best value for every state?"

---

## 13 — References and attribution

**Official syllabus.**
University of Mumbai, Faculty of Science and Technology, *6.21 (N) B.E. Artificial Intelligence and Machine Learning, Semester III and Semester IV*, 2025–26, page 23 (Module V). PDF: `https://mu.ac.in/old/wp-content/uploads/2025/06/6.21-N-B.E.-AI-ML-sem-III-IV.pdf`.

**Course material inspected.**
- `Assignment no 5 AoA (1).docx` — 15-puzzle formulation `c(x) = f(x) + g(x)`, 8-queen note and pseudocode, sum of subsets `(2,7,8,15)` with `m = 17`, and the D&C/DP/backtracking comparison table.
- `PRELIMS AOA.docx` — 8-queen, sum of subsets, 15-puzzle and TSP questions.
- `IAT-2 Question Bank (2025-26) (FINAL) (1).pdf` and `IAT-2 Question Bank (2026-27) (FINAL) (1).docx` — TSP branch-and-bound and 15-puzzle practice. These are teacher revision sheets, not University papers.

**Standard references for further reading (not quoted page-by-page).**
- E. Horowitz, S. Sahni and S. Rajasekaran, *Computer Algorithms*, 2nd edition, Universities Press.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest and C. Stein, *Introduction to Algorithms*, 3rd edition, MIT Press.

**Attribution.** All explanations, tables, pseudocode, traces and diagrams were written for this guide. Practice questions state their provenance at the question; none is presented as a University examination paper. The CO-number discrepancy is reported, not resolved silently.
