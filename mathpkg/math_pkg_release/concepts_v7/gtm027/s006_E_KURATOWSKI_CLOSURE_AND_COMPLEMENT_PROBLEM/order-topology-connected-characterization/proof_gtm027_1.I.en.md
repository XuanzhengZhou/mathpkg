---
role: proof
locale: en
of_concept: order-topology-connected-characterization
source_book: gtm027
source_chapter: "1"
source_section: "I"
---

# Proof of Characterization of Connectedness in Order Topology

**Theorem.** Let $X$ be a linearly ordered set with the order topology. Then $X$ is connected if and only if $X$ is order-complete and has no gaps.

*Proof.* Recall definitions:
- $X$ is **order-complete** if every nonempty subset with an upper bound has a supremum.
- $X$ has a **gap** if there exist $a, b \in X$ with $a < b$ such that there is no $c \in X$ with $a < c < b$.

### ($\Rightarrow$) Connectedness implies order-complete and no gaps.

**No gaps:** Suppose there is a gap between $a$ and $b$. Then $X = (-\infty, b) \cup (a, +\infty)$, and both sets are open in the order topology. They are nonempty (containing $a$ and $b$ respectively), disjoint, and their union is $X$. Hence $X$ is disconnected — contradiction.

**Order-complete:** Suppose $S \subseteq X$ is nonempty and bounded above but has no supremum. Let $U$ be the set of all upper bounds of $S$ and $V = X \setminus U$. Both $U$ and $V$ are open in the order topology (if $S$ has no supremum, every upper bound has a smaller upper bound, and every non-upper bound is strictly less than some upper bound). Both are nonempty, disjoint, and cover $X$, so $X$ is disconnected — contradiction.

### ($\Leftarrow$) Order-complete and no gaps implies connected.

Suppose $X$ is order-complete and has no gaps, but is disconnected. Then $X = U \cup V$ where $U, V$ are nonempty, disjoint, and open. Pick $a \in U$, $b \in V$. Without loss, assume $a < b$.

Define $S = \{x \in U : x < b\}$. Since $a \in S$, $S \neq \emptyset$, and $b$ is an upper bound for $S$. By order-completeness, $c = \sup S$ exists.

Consider $c$: Since $U$ and $V$ cover $X$, either $c \in U$ or $c \in V$.

- If $c \in U$: Then $c < b$ (otherwise $c \geq b$ would contradict $c \in U$). Since $U$ is open in the order topology and there are no gaps, there exists $d > c$ with $d \in U$ and $d < b$. But then $d \in S$ and $d > \sup S$ — contradiction.

- If $c \in V$: Since $V$ is open, there exists an interval around $c$ contained in $V$. In particular, there exists $e < c$ with $(e, c] \subseteq V$. But $c = \sup S$, so there exists $s \in S$ with $e < s \leq c$. Then $s \in V \cap U$ — contradiction.

Both cases lead to contradiction, so $X$ is connected. $\square$
