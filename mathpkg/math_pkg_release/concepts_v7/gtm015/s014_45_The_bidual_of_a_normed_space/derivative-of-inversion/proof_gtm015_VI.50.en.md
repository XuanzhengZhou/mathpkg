---
role: proof
locale: en
of_concept: derivative-of-inversion
source_book: gtm015
source_chapter: "VI"
source_section: "50"
---

# Proof of the Derivative of the Inversion Map

Let $A$ be a Banach algebra with unity $1$, and let $U$ be the group of invertible elements. For $x \in U$, we compute
$$\lim_{h \to 0} \frac{(x + h1)^{-1} - x^{-1}}{h},$$
where $h \in \mathbb{C}$ (note: $h1$ denotes the scalar multiple of the unity).

If $0 < |h| < \|x^{-1}\|^{-1}$, then
$$\|(x + h1) - x\| = |h| < \|x^{-1}\|^{-1},$$
so $x + h1$ is invertible by (50.5). Now compute:
$$(x + h1)^{-1} - x^{-1} = (x + h1)^{-1}[x - (x + h1)]x^{-1} = -h (x + h1)^{-1} x^{-1}.$$

Therefore,
$$\frac{1}{h}\left[(x + h1)^{-1} - x^{-1}\right] = -(x + h1)^{-1} x^{-1}.$$

As $h \to 0$, we have $x + h1 \to x$ in $A$, and by the continuity of inversion (Theorem 50.7), $(x + h1)^{-1} \to x^{-1}$. Hence
$$\lim_{h \to 0} \frac{(x + h1)^{-1} - x^{-1}}{h} = -x^{-1} x^{-1} = -(x^{-1})^2.$$

Thus the inversion map is differentiable (in the sense of complex-differentiable functions between Banach spaces), with derivative $-x^{-2}$ at $x \in U$. This is the Banach algebra analog of the elementary calculus formula $\frac{d}{dx}(x^{-1}) = -x^{-2}$. $\square$
