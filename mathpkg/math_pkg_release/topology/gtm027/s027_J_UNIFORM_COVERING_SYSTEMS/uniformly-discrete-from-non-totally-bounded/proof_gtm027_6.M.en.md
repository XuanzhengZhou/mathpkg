---
role: proof
locale: en
of_concept: uniformly-discrete-from-non-totally-bounded
source_book: gtm027
source_chapter: "6"
source_section: "M"
---

# Proof of Uniformly Discrete Subsets from Non-Totally Bounded Sets

Let $A$ be a subset of a uniform space $(X, \mathfrak{U})$ which is not totally bounded.

By definition of total boundedness, there exists a member $U$ of $\mathfrak{U}$ such that $A$ cannot be covered by finitely many $U$-small sets. That is, there is no finite subset $\{x_1, \ldots, x_n\} \subset A$ with $A \subset \bigcup_{i=1}^n U[x_i]$.

Choose a symmetric $V \in \mathfrak{U}$ such that $V \circ V \circ V \subset U$.

Construct $B = \{x_n : n \in \omega\}$ inductively: Choose $x_0 \in A$ arbitrarily. Having chosen $x_0, \ldots, x_{n-1}$, since $A$ cannot be covered by $\bigcup_{i=0}^{n-1} U[x_i]$, there exists $x_n \in A \setminus \bigcup_{i=0}^{n-1} U[x_i]$.

For any $i < j$, we have $x_j \notin U[x_i]$, which means $(x_i, x_j) \notin U$. Since $V \circ V \circ V \subset U$, this implies $V[x_i] \cap V[x_j] = \emptyset$. Indeed, if $z \in V[x_i] \cap V[x_j]$, then $(x_i, z) \in V$ and $(z, x_j) \in V$, hence $(x_i, x_j) \in V \circ V$, contradicting $(x_i, x_j) \notin U \supset V \circ V \circ V$.

Moreover, by the metrization lemma for uniform spaces, there exists a pseudo-metric $d$ in the gage of $\mathfrak{U}$ such that $d(x, y) \geq 1$ for distinct $x, y \in B$. (The construction uses the fact that $V$ defines a uniform cover, and the pseudo-metric is built from this cover.)

Such a set $B$ is called *uniformly discrete*.
