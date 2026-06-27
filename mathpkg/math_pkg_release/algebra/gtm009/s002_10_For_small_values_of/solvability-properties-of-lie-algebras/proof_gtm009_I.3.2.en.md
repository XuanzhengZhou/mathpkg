---
role: proof
locale: en
of_concept: solvability-properties-of-lie-algebras
source_book: gtm009
source_chapter: "I"
source_section: "3.2"
---
(a) From the definition, if $K$ is a subalgebra of $L$, then $K^{(i)} \subset L^{(i)}$. Similarly, if $\phi: L \to M$ is an epimorphism, an easy induction on $i$ shows that $\phi(L^{(i)}) = M^{(i)}$. In both cases, if $L^{(n)} = 0$ for some $n$, then the same holds for the smaller object.

(b) Suppose $(L/I)^{(n)} = 0$. Applying part (a) to the canonical homomorphism $\pi: L \to L/I$, we get $\pi(L^{(n)}) = 0$, or $L^{(n)} \subset I = \operatorname{Ker} \pi$. Now if $I^{(m)} = 0$, the fact that $(L^{(i)})^{(j)} = L^{(i+j)}$ implies that $L^{(n+m)} = 0$ (apply proof of part (a)).

(c) Consider the natural homomorphism $\pi: I+J \to (I+J)/J$. Since $(I+J)/J \cong I/(I \cap J)$ by the second isomorphism theorem, and $I$ is solvable, the quotient $(I+J)/J$ is solvable (as a homomorphic image of $I$). Since $J$ is solvable as well, part (b) applied to $(I+J)$ with ideal $J$ shows that $I+J$ is solvable.
