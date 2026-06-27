---
role: proof
locale: en
of_concept: convergence-in-product-topology
source_book: gtm027
source_chapter: "3"
source_section: "Product Spaces"
---

# Proof of Convergence in the Product Topology

**Theorem.** A net $\{S_n, n \in D\}$ in a product space $\bigwedge\{X_a : a \in A\}$ converges to a point $s$ if and only if $\{P_a(S_n), n \in D\}$ converges to $P_a(s)$ for each $a$ in $A$.

*Proof.* ($\Rightarrow$) If the net converges to $s$ in the product topology, then since each projection $P_a$ is continuous, it follows from condition (f) of Theorem 1 that $\{P_a(S_n), n \in D\}$ converges to $P_a(s)$ for each $a$.

($\Leftarrow$) Conversely, suppose that for each $a$ in $A$, $\{P_a(S_n), n \in D\}$ converges to $P_a(s)$. Let $U$ be a neighborhood of $s$ in the product topology. Then $U$ contains a basic open set of the form

$$
\bigcap_{a \in F} P_a^{-1}[U_a] = \{y : y_a \in U_a \text{ for each } a \in F\},
$$

where $F$ is a finite subset of $A$ and $U_a$ is an open neighborhood of $P_a(s)$ in $X_a$ for each $a \in F$.

For each $a \in F$, the coordinate net $\{P_a(S_n), n \in D\}$ converges to $P_a(s)$, so it is eventually in $U_a$. Consequently $\{S_n, n \in D\}$ is eventually in $P_a^{-1}[U_a]$ for each $a \in F$, and hence $\{S_n, n \in D\}$ must eventually be in each finite intersection of sets of the form $P_a^{-1}[U_a]$. Since the family of such finite intersections is a base for the neighborhood system of $s$ in the product topology, $\{S_n, n \in D\}$ converges to $s$. $\square$
