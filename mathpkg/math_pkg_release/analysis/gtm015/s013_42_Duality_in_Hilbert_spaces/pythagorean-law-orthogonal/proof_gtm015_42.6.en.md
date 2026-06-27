---
role: proof
locale: en
of_concept: pythagorean-law-orthogonal
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.6"
---

# Proof of Pythagorean Law for Orthogonal Vectors

**Lemma.** If $x$ and $y$ are orthogonal vectors in an inner product space, then $\|x + y\|^2 = \|x\|^2 + \|y\|^2$.

*Proof.* By definition of orthogonality, $(x|y) = 0$ and $(y|x) = 0$. Expanding the norm as an inner product:

$$\begin{aligned}
\|x + y\|^2 &= (x+y|x+y) \\
&= (x|x) + (x|y) + (y|x) + (y|y) \\
&= \|x\|^2 + 0 + 0 + \|y\|^2 \\
&= \|x\|^2 + \|y\|^2.
\end{aligned}$$
