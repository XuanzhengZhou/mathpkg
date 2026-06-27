---
role: proof
locale: en
of_concept: existence-of-lower-density
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

Oxtoby does not give the full proof in the text, noting: "We shall not prove this theorem in general. We are primarily interested in the Lebesgue measure space, and we have already seen that in this case the Lebesgue density theorem defines such a mapping (Theorem 3.21)."

The proof of Theorem 22.4 in full generality is due to von Neumann and Maharam [19]. An alternative proof was given by A. and C. Ionescu Tulcea [15]. The construction involves a transfinite induction or an application of the Martingale convergence theorem in the case of a separable measure algebra. For the purposes of Chapter 22, the Lebesgue density lower density on $\mathbb{R}$ suffices:

$$\phi(E) = \{x \in \mathbb{R} : \lim_{h \to 0} \frac{m(E \cap [x-h, x+h])}{2h} = 1\},$$

where $m$ is Lebesgue measure. This satisfies all five properties listed in the theorem statement: (1) $\phi(E) \sim E$ by the Lebesgue density theorem; (2) if $E \sim F$ then $m(E \triangle F) = 0$, and the density points coincide; (3) $\phi(\emptyset) = \emptyset$ and $\phi(\mathbb{R}) = \mathbb{R}$; (4) density points of $E \cap F$ are exactly the intersection of density points of $E$ and $F$; (5) monotonicity follows from the definition of density points.
