---
role: proof
locale: en
of_concept: projection-of-open-set
source_book: gtm027
source_chapter: "3"
source_section: "Product Spaces"
---

# Proof of Projection of an Open Set is Open

**Theorem.** For each $c \in A$, the projection $P_c$ of the product space $\bigwedge\{X_a : a \in A\}$ into the $c$-th coordinate space maps open sets to open sets; i.e., projections are open mappings.

*Proof.* A subset $W$ of the product space is open iff it is a union of members of the defining base for the product topology. Since the image of a union is the union of the images, it suffices to prove that the projection of each basic open set is open.

Suppose that $x \in V = \{y : y_a \in U_a \text{ for } a \in F\}$, where $F$ is a finite subset of $A$ and $U_a$ is open in $X_a$ for each $a$ in $F$. We construct a copy of $X_c$ which contains the point $x$. For $z \in X_c$ let

$$
f(z)_c = z, \quad \text{and for } a \neq c: \; f(z)_a = x_a.
$$

Then $P_c \circ f(z) = z$.

If $c \notin F$, then clearly $f[X_c] \subset V$ and $P_c[V] = X_c$, which is open.

If $c \in F$, then $f(z) \in V$ iff $z \in U_c$, and consequently $P_c[V] = U_c$, which is open.

In either case, $P_c[V]$ is open. The theorem follows. $\square$

*(Remark: The function $f$ defined in this proof is a homeomorphism onto its image, a fact that is occasionally useful.)*
