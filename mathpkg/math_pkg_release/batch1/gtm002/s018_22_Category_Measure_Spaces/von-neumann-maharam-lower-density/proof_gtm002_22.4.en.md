---
role: proof
locale: en
of_concept: von-neumann-maharam-lower-density
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

The proof of this theorem in full generality is not given in the present text. As stated in the book:

> We shall not prove this theorem in general. We are primarily interested in the Lebesgue measure space, and we have already seen that in this case the Lebesgue density theorem defines such a mapping (Theorem 3.21).

The theorem is due to von Neumann and Maharam [19]. An alternative proof has been given by A. and C. Ionescu Tulcea [15]. The construction uses transfinite induction or the Stone representation theorem for Boolean algebras to build a lifting of the measure algebra $S / \mathcal{N}$ to $S$.

For the Lebesgue measure space on $\mathbb{R}^n$, the Lebesgue density theorem (Theorem 3.21) provides an explicit lower density:
$$\phi(A) = \{x \in \mathbb{R}^n : d(x, A) = 1\},$$
where $d(x, A) = \lim_{r \to 0} \frac{m(A \cap B_r(x))}{m(B_r(x))}$ is the metric density of $A$ at $x$.

**References:**
- [15] Ionescu Tulcea, A. and C.: On the lifting property I. J. Math. Anal. Appl. 3, 537--546 (1961).
- [19] von Neumann, J. and Maharam, D.: On the existence of a lower density. In: J. von Neumann, Collected Works, Vol. IV, pp. 403--406. Pergamon Press, Oxford, 1961.
