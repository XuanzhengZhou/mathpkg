---
role: proof
locale: en
of_concept: compact-set-neighborhood-urysohn
source_book: gtm027
source_chapter: "5"
source_section: "Locally Compact Spaces"
---

# Proof of Neighborhood Extension for Closed Compact Sets with Urysohn Function (Theorem 18)

Let $U$ be a neighborhood of a closed compact subset $A$ of a regular locally compact topological space $X$.

**Part 1: Existence of the closed compact neighborhood $V$.**

For each point $x$ of $A$, by Theorem 17 (closed compact neighborhoods form a base), there exists a neighborhood $W_x$ of $x$ which is a closed compact subset of $U$. Since $A$ is compact, it may be covered by a finite number of such neighborhoods: $A \subset W_{x_1} \cup \cdots \cup W_{x_n}$. Let

$$V = W_{x_1} \cup \cdots \cup W_{x_n}.$$

Then $V$ is a finite union of closed compact sets, hence $V$ is closed and compact. Moreover, $A \subset V \subset U$ and $V$ is a neighborhood of $A$. This establishes the first claim.

**Part 2: Existence of the Urysohn function $f$.**

Since $V$ is compact and regular (being a subspace of a regular space), $V$ is normal by Theorem 5.10. Hence there exists a continuous function $g: V \to [0,1]$ such that $g$ is identically zero on the closed set $A$ and identically one on $V \setminus V^0$, where $V^0$ denotes the interior of $V$. Define a function $f: X \to [0,1]$ by

$$f(x) = \begin{cases} g(x), & x \in V \\ 1, & x \in X \setminus V \end{cases}$$

To verify continuity of $f$, observe that $V^0$ and $X \setminus V$ are separated sets (since $V$ is closed, $X \setminus V$ is open and disjoint from $V^0 \subset V$, and the closure of $V^0$ in $X \setminus V$ is contained in $V \cap (X \setminus V) = \emptyset$). The function $f$ is continuous on the closed set $V$ (where it agrees with $g$) and on $X \setminus V^0$ (where it is constant 1 — on $X \setminus V$ it is 1 by definition, and on $V \setminus V^0$ it agrees with $g$). Since $X = V \cup (X \setminus V^0)$ and $f$ is continuous on each of these closed sets and they agree on their intersection, $f$ is continuous on $X$. (An equivalent verification via Problem 3.B: a function is continuous if it is continuous on each member of a closed cover.)

Thus $f$ is a continuous function on $X$ to $[0,1]$ such that $f = 0$ on $A$ and $f = 1$ on $X \setminus V$. $\square$
