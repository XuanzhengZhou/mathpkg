---
role: proof
locale: en
of_concept: trigonometric-product-formula
source_book: gtm007
source_chapter: "I"
source_section: "§3 Appendix"
---

This is elementary. First, prove that $\sin (mx)/\sin (x)$ is a polynomial of degree $(m-1)/2$ in $\sin^2 x$ (this follows by induction using the addition formulas for sine, or by expressing $\sin(mx)$ as the imaginary part of $e^{imx} = (\cos x + i\sin x)^m$, which yields $\sin(mx) = \sin x \cdot P(\sin^2 x)$ for some polynomial $P$).

Then remark that this polynomial has for roots the $\sin^2 \frac{2\pi j}{m}$ with $1 \leq j \leq (m-1)/2$, since $\sin(m \cdot \frac{2\pi j}{m}) = \sin(2\pi j) = 0$ while $\sin(2\pi j/m) \neq 0$ for these values of $j$.

The factor $(-4)^{(m-1)/2}$ is obtained by comparing coefficients of $e^{i(m-1)x}$ on both sides: on the left, $\sin(mx)/\sin x = (e^{imx} - e^{-imx})/(e^{ix} - e^{-ix}) = e^{i(m-1)x} + e^{i(m-3)x} + \dots + e^{-i(m-1)x}$; on the right, expanding the product $\prod (\sin^2 x - \sin^2 \frac{2\pi j}{m})$ and comparing the leading term yields the coefficient.
