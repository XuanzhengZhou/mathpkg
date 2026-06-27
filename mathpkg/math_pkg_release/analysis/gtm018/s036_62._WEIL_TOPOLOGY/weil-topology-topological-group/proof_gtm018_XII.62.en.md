---
role: proof
locale: en
of_concept: weil-topology-topological-group
source_book: gtm018
source_chapter: "XII"
source_section: "62"
---

We verify that $N$ satisfies the neighborhood axioms (a)--(e) for a base at the identity of a topological group.

**(a)** Separation: Suppose $x_0 \in X$, $x_0 \neq e$, and that $E$ is a measurable set of positive, finite measure such that $\rho(x_0E, E) > 0$. If $\epsilon$ is a positive number such that $0 < \epsilon < \rho(x_0E, E)$, then $\epsilon < 2\mu(E)$. It follows that if $N = \{x : \rho(xE, E) < \epsilon\}$, then $N \in N$, and clearly $x_0 \notin N$. Thus distinct points can be separated.

**(b)** Intersection: If $N$ and $M$ are in $N$, then by Theorem A, there exist sets $A$ and $B$ in $A$ such that $A \subset N$ and $B \subset M$. By Theorem D, there exists a set $C$ in $A$ such that $C \subset A \cap B$; by Theorem B, we obtain a set $K$ in $N$ such that $K \subset C \subset A \cap B \subset N \cap M$.

**(c)** Conjugation invariance: If $N = \{x : \rho(xE, E) < \epsilon\} \in N$ and $x \in X$, then $xNx^{-1} = \{x y x^{-1} : \rho(yE, E) < \epsilon\} = \{z : \rho(x^{-1}z x E, E) < \epsilon\} = \{z : \rho(z(xE), xE) < \epsilon\}$. Applying Theorem B to the set $(xE)(xE)^{-1}$ in $A$, we may find a set $M$ in $N$ such that

$$M \subset (xE)(xE)^{-1} = xEE^{-1}x^{-1} \subset xNx^{-1}.$$

Thus $N$ is invariant under inner automorphisms up to containment.

**(d)** Continuity of multiplication: If $N = \{x : \rho(xE, E) < \epsilon\} \in N$ and $x_0 \in N$, then $\rho(x_0E, E) < \epsilon$. Since $\epsilon < 2\mu(E)$, it follows that $\epsilon - \rho(x_0E, E) < 2\mu(x_0E)$ and hence that if

$$M = \{x : \rho(x x_0 E, x_0 E) < \epsilon - \rho(x_0E, E)\},$$

then $M \in N$. Since

$$Nx_0^{-1} = \{x x_0^{-1} : \rho(xE, E) < \epsilon\} = \{x : \rho(x x_0 E, E) < \epsilon\},$$

we have, for every $x$ in $M$,

$$\rho(x x_0 E, E) \leq \rho(x x_0 E, x_0 E) + \rho(x_0 E, E) < (\epsilon - \rho(x_0 E, E)) + \rho(x_0 E, E) = \epsilon.$$

This implies that $x \in N x_0^{-1}$ and hence that $M x_0 \subset N$, establishing continuity of multiplication at $e$.

Thus $N$ satisfies all the axioms for a neighborhood base at the identity of a topological group.
