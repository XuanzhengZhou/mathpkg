---
role: proof
locale: en
of_concept: legendre-symbol-formulas
source_book: gtm007
source_chapter: "I"
source_section: "3"
---

(i) $1^{(p-1)/2} = 1$, so $\left(\frac{1}{p}\right) = 1$.

(ii) $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2} = (-1)^{\varepsilon(p)}$ by definition of the Legendre symbol.

(iii) Let $\alpha$ be a primitive 8th root of unity in an algebraic closure $\Omega$ of $\mathbb{F}_p$. Then $\alpha^4 = -1$, so $\alpha^2 + \alpha^{-2} = 0$. Set $y = \alpha + \alpha^{-1}$. Then $y^2 = \alpha^2 + 2 + \alpha^{-2} = 2$. Now $y^p = \alpha^p + \alpha^{-p}$. If $p \equiv \pm 1 \pmod{8}$, then $p = 8k \pm 1$, so $y^p = \alpha^{\pm 1} + \alpha^{\mp 1} = y$, hence $y^{p-1} = 1$, so $2^{(p-1)/2} = y^{p-1} = 1$. If $p \equiv \pm 5 \pmod{8}$, then $p = 8k \pm 3$ (since $\pm 5 \equiv \mp 3 \bmod 8$), and $y^p = \alpha^{\pm 3} + \alpha^{\mp 3}$. Since $(\alpha^3 + \alpha^{-3}) + (\alpha + \alpha^{-1}) = 0$ (as $\alpha^2 + \alpha^{-2} = 0$ implies $(\alpha + \alpha^{-1})(\alpha^2 - 1 + \alpha^{-2}) = 0$, but $\alpha^2 - 1 + \alpha^{-2} = -1 - 1 = -2 \neq 0$), we get $y^p = -y$, so $y^{p-1} = -1$, giving $\left(\frac{2}{p}\right) = -1$. Thus $\left(\frac{2}{p}\right) = (-1)^{\omega(p)}$.
