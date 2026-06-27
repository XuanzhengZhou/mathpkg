---
role: proof
locale: en
of_concept: degree-diffeomorphism-homotopic-to-identity
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Theorem 1.3 (Degree of a Diffeomorphism Homotopic to the Identity)

**Theorem statement.** Let $N$ be a compact connected oriented $n$-manifold without boundary. If $h: N \to N$ is a diffeomorphism homotopic to the identity, then $\deg h = 1$.

**Proof.** Since $h$ is homotopic to the identity $\mathrm{id}_N$, Theorem 1.6(a) (homotopy invariance of degree) yields

$$\deg h = \deg(\mathrm{id}_N).$$

It therefore suffices to show that $\deg(\mathrm{id}_N) = 1$. Let $y \in N$ be any point. Then $y$ is a regular value of $\mathrm{id}_N$, and the single preimage $\mathrm{id}_N^{-1}(y) = \{y\}$ consists of one point. The derivative $D(\mathrm{id}_N)_y = \mathrm{id}_{T_y N}$ is the identity map, which is orientation-preserving. Hence the sign at $y$ is $+1$, and

$$\deg(\mathrm{id}_N) = \deg(\mathrm{id}_N, y) = +1.$$

Therefore $\deg h = 1$. The same argument in the nonorientable case (using mod 2 degree) gives $\deg_2 h = 1$.
