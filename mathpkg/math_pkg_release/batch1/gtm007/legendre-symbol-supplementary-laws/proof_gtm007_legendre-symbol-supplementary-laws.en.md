---
role: proof
locale: en
of_concept: "$C"
source_book: gtm007
source_chapter: "I"
source_section: "3.2"
---
(i) is trivial.

(ii) follows from $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2} = (-1)^{\varepsilon(p)}$.

For (iii): let $\alpha$ be a primitive 8th root of unity in an algebraic closure $\Omega$ of $\mathbb{F}_p$. Set $y = \alpha + \alpha^{-1}$. From $\alpha^4 = -1$, we have $\alpha^2 + \alpha^{-2} = 0$, so $y^2 = 2$. Now $y^p = \alpha^p + \alpha^{-p}$.

If $p \equiv \pm 1 \pmod{8}$, then $\alpha^p = \alpha$ or $\alpha^{-1}$, so $y^p = \alpha + \alpha^{-1} = y$, hence $y^{p-1} = 1$, giving $\left(\frac{2}{p}\right) = 1$. If $p \equiv \pm 5 \pmod{8}$, then $\alpha^p = \alpha^{5} = -\alpha$ (or $-\alpha^{-1}$), so $y^p = -y$, giving $y^{p-1} = -1$ and $\left(\frac{2}{p}\right) = -1$. Thus $\left(\frac{2}{p}\right) = (-1)^{\omega(p)}$.
