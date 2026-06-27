---
role: proof
locale: en
of_concept: antoine-path-contraction
source_book: gtm047
source_chapter: '18'
source_section: Section 22
---

**Proof.** Here and hereafter, if $f$ is a mapping $A \to B$, then $|f|$ denotes the image $f(A)$. Let

$$A_i = \operatorname{Cl}\left[ D_i - \left(C_{i-1} \cup C_{i+1}\right) \right],$$

as in the definition of $T_2$. Suppose (without loss of generality) that $p$ is a PL mapping, and let

$$\phi: [0, 1]^2 \to \mathbf{R}^3 - T_2$$

be a PL contraction of $p$ to $e$. We can choose $|p|$ and $|\phi|$ in general position relative to $A_i$, in the sense that there is a triangulation $K$ of $[0, 1]^2$ such that if $\sigma^2 \in K$, and $\phi(\sigma^2)$ intersects $A_i$, then $\phi|\sigma^2$ is a simplicial homeomorphism, and $A_i$ contains no vertex of $\phi(\sigma^2)$. Let

$$J = \phi^{-1}(A_i \cap |\phi|).$$

Now the set $\phi(J) = A_i \cap |\phi|$ may be an arbitrary $1$-dimensional polyhedron in $A_i$ (except, of course, that it cannot have any isolated points). But $J$ itself, in $[0, 1]^2$, is a finite union of disjoint polygons. The reason is that $J$ contains no vertex of $K$, so that each nonempty intersection $J \cap \sigma^2$ is a linear interval, joining two points of $\operatorname{Bd} \sigma^2$ and containing no vertex of $\sigma^2$. Thus if $\sigma^2_1 \cap \sigma^2_2 = \sigma^1$, and $P \in \sigma^1 \cap J$, then [the proof continues with a geometric elimination argument removing polygons from $J$ one by one, modifying $\phi$ to avoid $A_i$, ultimately producing a contraction of $p$ in $\mathbf{R}^3 - T_1$].
