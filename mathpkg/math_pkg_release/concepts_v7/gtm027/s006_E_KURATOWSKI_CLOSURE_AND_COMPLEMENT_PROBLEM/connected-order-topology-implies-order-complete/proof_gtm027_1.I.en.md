---
role: proof
locale: en
of_concept: connected-order-topology-implies-order-complete
source_book: gtm027
source_chapter: "1"
source_section: "I"
---

# Proof that Connected Order Topology Implies Order-Complete

**Theorem.** If $X$, with the order topology, is connected, then $X$ is order-complete (that is, each nonempty subset with an upper bound has a supremum).

*Proof.* Suppose $X$ is connected in the order topology but not order-complete. Then there exists a nonempty subset $S \subseteq X$ with an upper bound but no supremum.

Let $U$ be the set of all upper bounds of $S$, and let $V = X \setminus U$ (the set of points that are not upper bounds of $S$).

Since $S \neq \emptyset$, $V$ is nonempty (any element of $S$ belongs to $V$). Since $S$ has an upper bound, $U$ is nonempty.

We show both $U$ and $V$ are open in the order topology:

- **$U$ is open:** Let $x \in U$. Since $x$ is an upper bound of $S$ but not the supremum (none exists), $x$ is not the least upper bound. Hence there exists an upper bound $y < x$. Then the interval $(y, \infty) = \{z \in X : z > y\}$ is open, contains $x$, and is contained in $U$ (any $z > y$ is also an upper bound of $S$).

- **$V$ is open:** Let $x \in V$. Then $x$ is not an upper bound of $S$, so there exists $s \in S$ with $x < s$. The interval $(-\infty, s) = \{z \in X : z < s\}$ is open, contains $x$, and is contained in $V$ (no point $z < s$ can be an upper bound of $S$, since $s \in S$).

Thus $U$ and $V$ form a disconnection of $X$ — contradiction. Therefore $X$ must be order-complete. $\square$
