---
role: proof
locale: en
of_concept: simply-connected-analytic-logarithm
source_book: gtm011
source_chapter: "IV"
source_section: "6.17"
---

Since $f$ never vanishes, $\frac{f'}{f}$ is analytic on $G$. By Corollary 6.16 (simply connected implies primitive exists), $\frac{f'}{f}$ must have a primitive $g_1$ on $G$. Define $h(z) = \exp g_1(z)$; then $h$ is analytic and never vanishes. Consider the quotient $\frac{f}{h}$, which is also analytic on $G$. Its derivative is

$$\frac{h(z)f'(z) - h'(z)f(z)}{h(z)^2}.$$

But $h' = g_1' h = \frac{f'}{f} h$, so $h f' - f h' = h f' - f \cdot \frac{f'}{f} h = 0$. Hence the derivative of $\frac{f}{h}$ is identically zero, so $\frac{f}{h}$ is a constant $c$ for all $z$ in $G$. That is,

$$f(z) = c \exp g_1(z) = \exp[g_1(z) + c']$$

for some $c'$ with $e^{c'} = c$. Now define $g(z) = g_1(z) + c' + 2\pi i k$ for an appropriate integer $k$ so that $g(z_0) = w_0$. This completes the proof.
