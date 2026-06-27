---
role: proof
locale: en
of_concept: isekis-transformation-formula
source_book: gtm041
source_chapter: "3"
source_section: "3.5"
---

Given $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ in $\Gamma$, with $c > 0$, and given $\tau$ with $\operatorname{Im}(\tau) > 0$, choose $z, h, k$, and $H$ as follows:

$$k = c, \quad h = -d, \quad H = a, \quad z = -i(c\tau + d).$$

Then $\operatorname{Re}(z) > 0$, and the condition $ad - bc = 1$ implies $-hH - bk = 1$, so $(h, k) = 1$ and $hH \equiv -1 \pmod{k}$. Now $b = -(hH + 1)/k$ and $iz = c\tau + d$, so

$$\tau = \frac{iz - d}{c} = \frac{iz + h}{k}$$

and hence

$$a\tau + b = H \frac{iz + h}{k} - \frac{hH + 1}{k} = \frac{iz}{k} \left( H + \frac{i}{z} \right).$$

Therefore, since $c\tau + d = iz$, we have

$$\frac{a\tau + b}{c\tau + d} = \frac{\frac{iz}{k}(H + i/z)}{iz} = \frac{H}{k} + \frac{i}{kz}.$$

This transformation is exactly the change of variables needed to connect the two $\lambda$-series in Iseki's formula. The full proof of Lemma 2 (establishing the equality of the two series with the correction terms) proceeds via Iseki's $\Lambda$-function and contour integration, as developed in the remainder of Section 3.5 (see Iseki's formula for $\Lambda(\alpha,\beta,z)$).
