---
role: proof
locale: en
of_concept: solvability-properties
source_book: gtm009
source_chapter: "3"
source_section: "3.1"
---

\textbf{Proof.}
(a) If $K$ is a subalgebra of $L$, then $K^{(i)} \subset L^{(i)}$ by definition of the derived series. Similarly, if $\phi: L \rightarrow M$ is an epimorphism, an easy induction on $i$ shows that $\phi(L^{(i)}) = M^{(i)}$. Thus if $L^{(n)} = 0$, then $K^{(n)} = 0$ and $M^{(n)} = 0$.

(b) Suppose $(L/I)^{(n)} = 0$. Apply part (a) to the canonical homomorphism $\pi: L \rightarrow L/I$ to get $\pi(L^{(n)}) = 0$, i.e., $L^{(n)} \subset I = \text{Ker } \pi$. Now if $I^{(m)} = 0$, then using the fact that $(L^{(i)})^{(j)} = L^{(i+j)}$, we obtain $L^{(n+m)} = (L^{(n)})^{(m)} \subset I^{(m)} = 0$. Hence $L$ is solvable.

(c) Since $(I+J)/J \cong I/(I \cap J)$ is a homomorphic image of $I$, it is solvable by (a). Then $J$ is solvable and $(I+J)/J$ is solvable, so by (b) applied to $I+J$ with ideal $J$, we get $I+J$ solvable.
