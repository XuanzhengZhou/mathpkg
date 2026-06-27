---
role: proof
locale: en
of_concept: mobius-inverse-is-mobius
source_book: gtm041
source_chapter: "2"
source_section: "2.1"
---

Starting from $w = f(z) = \frac{az+b}{cz+d}$, solve for $z$:
\begin{align*}
w(cz+d) &= az+b \\
cwz + dw &= az + b \\
cwz - az &= b - dw \\
z(cw - a) &= b - dw \\
z &= \frac{b - dw}{cw - a} = \frac{dw - b}{-cw + a}.
\end{align*}
Thus $f^{-1}(w) = \frac{dw - b}{-cw + a}$, which has the same form as a Möbius transformation. The determinant of the inverse coefficients is $d(-a) - (-b)(-c) = -da + bc = -(ad-bc) \neq 0$, confirming it is non-degenerate.
