---
role: proof
locale: en
of_concept: bound-on-average-valence
source_book: gtm054
source_chapter: "Chapter VII"
source_section: "Section 34"
---

**Case 1:** $\iota \leq 2$. Using C9 to eliminate $\nu_0$ from C8 we obtain

$$\frac{1}{\rho} \geq \frac{1}{G(\gamma)} + \frac{2 - \iota}{2\nu_1}.$$

If $\iota = 0$ or $1$, then $\rho < G(\gamma) \leq \{G(\gamma)\} = H(\gamma, \iota)$. If $\iota = 2$, then $\frac{1}{\rho} \geq \frac{1}{G(\gamma)}$, so $\rho \leq G(\gamma) < [G(\gamma) + 1] = H(\gamma, 2)$ by C5.

**Case 2:** $\iota > 2$. Using C9 to eliminate $\nu_1$ from C8, we obtain C10:

$$\rho \leq G(\gamma)\left(1 + \frac{\iota - 2}{\nu_0}\right).$$

Define the function $f(x) = G(\gamma)(1 + ((\iota - 2)/x))$ for all real $x > 0$. Since $f$ is a decreasing function, there exists a least $H_0 \in \mathbb{N}$ such that $f(H_0 + 1) < H_0$. We assert that $\rho < H_0$: if $\nu_0 \leq H_0$, then $\rho < \nu_0 \leq H_0$; while if $\nu_0 > H_0$, then $\nu_0 \geq H_0 + 1$, and by C10, $\rho \leq f(\nu_0) \leq f(H_0 + 1) < H_0$. It remains only to show that $H_0 = H(\gamma, \iota)$, which follows from the definition of $H(\gamma, \iota)$ as exactly this minimal $H_0$.
