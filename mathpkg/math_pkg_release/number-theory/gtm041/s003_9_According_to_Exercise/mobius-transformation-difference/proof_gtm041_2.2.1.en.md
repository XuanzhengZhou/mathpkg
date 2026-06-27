---
role: proof
locale: en
of_concept: mobius-transformation-difference
source_book: gtm041
source_chapter: "2"
source_section: "2.1"
---

Compute directly:
$$f(w) - f(z) = \frac{aw+b}{cw+d} - \frac{az+b}{cz+d} = \frac{(aw+b)(cz+d) - (az+b)(cw+d)}{(cw+d)(cz+d)}.$$

Expand the numerator:
\begin{align*}
(aw+b)(cz+d) - (az+b)(cw+d) &= awcz + awd + bcz + bd - azcw - azd - bcw - bd \\
&= a(wcz - zcw) + ad(w - z) + bc(z - w) \\
&= ad(w-z) - bc(w-z) \\
&= (ad-bc)(w-z).
\end{align*}

Thus $f(w) - f(z) = \frac{(ad-bc)(w-z)}{(cw+d)(cz+d)}$. If $ad-bc = 0$, then $f(w) = f(z)$ for all $w,z$, so $f$ is constant.
