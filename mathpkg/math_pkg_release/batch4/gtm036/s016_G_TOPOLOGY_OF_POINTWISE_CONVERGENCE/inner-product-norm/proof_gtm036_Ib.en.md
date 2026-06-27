---
role: proof
locale: en
of_concept: inner-product-norm
source_book: gtm036
source_chapter: "I"
source_section: "I(b)"
---

To verify $\|x\| = \sqrt{(x,x)}$ is a norm:
- $\|x\| \geq 0$ and $\|x\| = 0 \iff (x,x) = 0 \iff x = 0$ (positive definiteness).
- $\|\lambda x\| = \sqrt{(\lambda x, \lambda x)} = \sqrt{|\lambda|^2 (x,x)} = |\lambda| \|x\|$ (absolute homogeneity).
- Triangle inequality: $\|x+y\|^2 = (x+y, x+y) = (x,x) + (x,y) + (y,x) + (y,y) = \|x\|^2 + 2\operatorname{Re}(x,y) + \|y\|^2 \leq \|x\|^2 + 2\|x\|\|y\| + \|y\|^2 = (\|x\| + \|y\|)^2$, using CBS.

The polarization identity is verified by expanding each term:
$$
\begin{aligned}
\|x+y\|^2 &= (x+y, x+y) = \|x\|^2 + (x,y) + (y,x) + \|y\|^2 \\
\|x-y\|^2 &= \|x\|^2 - (x,y) - (y,x) + \|y\|^2 \\
\|x+iy\|^2 &= \|x\|^2 + (x,iy) + (iy,x) + \|y\|^2 = \|x\|^2 - i(x,y) + i(y,x) + \|y\|^2 \\
\|x-iy\|^2 &= \|x\|^2 + i(x,y) - i(y,x) + \|y\|^2
\end{aligned}
$$

Then $\|x+y\|^2 - \|x-y\|^2 + i\|x+iy\|^2 - i\|x-iy\|^2 = 2(x,y) + 2(y,x) + i[-i(x,y) + i(y,x)] - i[i(x,y) - i(y,x)] = 2(x,y) + 2(y,x) + (x,y) - (y,x) + (x,y) - (y,x) = 4(x,y)$.
