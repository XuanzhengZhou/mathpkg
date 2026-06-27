---
role: proof
locale: en
of_concept: no-line-fully-in-unital
source_book: gtm006
source_chapter: "2"
source_section: "8"
---

*Proof.* Suppose such a line $\langle v \rangle + \langle w \rangle$ exists, so that every point $\langle xv + yw \rangle$ lies in $\mathcal{U}$. Then in the equation
$$x^{1+\phi}(v A v'^{\phi}) + x^{\phi} y (v A w'^{\phi}) + x y^{\phi} (w A v'^{\phi}) + y^{1+\phi} (w A w'^{\phi}) = 0$$
all pairs $(x,y)$ are solutions. Setting $y = 1$, we obtain an equation of the form $(*)$ of Lemma 2.44 satisfied for all $x$, which by Lemma 2.45 implies that all coefficients $a, b, c$ vanish, provided $K \neq \text{GF}(4)$. But $a = v A v'^{\phi} = 0$ means $\langle v \rangle$ is an absolute point, and similarly $c = 0$ gives $\langle w \rangle$ absolute. Then $b = v A w'^{\phi} = 0$ implies both $\langle v \rangle$ and $\langle w \rangle$ lie on the line $\langle A w'^{\phi} \rangle$, the image of $\langle w \rangle$ under the polarity. This forces the line $\langle v \rangle + \langle w \rangle$ to be absolute (the unique line through two absolute points on a common absolute line). But then the line intersects $\mathcal{U}$ in exactly one point (its absolute pole), contradicting the assumption that all its points are in $\mathcal{U}$. $\square$
