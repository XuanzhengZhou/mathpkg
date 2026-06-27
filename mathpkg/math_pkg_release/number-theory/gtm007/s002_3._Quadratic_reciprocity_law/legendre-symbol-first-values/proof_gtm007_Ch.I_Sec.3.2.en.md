---
role: proof
locale: en
of_concept: legendre-symbol-first-values
source_book: gtm007
source_chapter: "I"
source_section: "§3.2"
---

Only the last deserves a proof. If $\alpha$ denotes a primitive 8th root of unity in an algebraic closure $\Omega$ of $\mathbb{F}_p$, the element $y = \alpha + \alpha^{-1}$ verifies $y^2 = 2$ (from $\alpha^4 = -1$ it follows that $\alpha^2 + \alpha^{-2} = 0$). We have
$$y^p = \alpha^p + \alpha^{-p}.$$

If $p \equiv \pm 1 \pmod{8}$, then $y^p = \alpha + \alpha^{-1} = y$, hence $y^{p-1} = 1$ and $2^{(p-1)/2} = y^{p-1} = 1$, so $\left(\frac{2}{p}\right) = 1$.

If $p \equiv \pm 3 \pmod{8}$, then $\alpha^p = \alpha^3$ (since $\alpha^8=1$), so $y^p = \alpha^3 + \alpha^{-3}$. Using $\alpha^4 = -1$, we get $\alpha^3 = -\alpha^{-1}$ and $\alpha^{-3} = -\alpha$, hence $y^p = -(\alpha + \alpha^{-1}) = -y$. Thus $y^{p-1} = -1$ and $2^{(p-1)/2} = -1$, so $\left(\frac{2}{p}\right) = -1$.

Recalling the definition of $\omega(p)$, this yields $\left(\frac{2}{p}\right) = (-1)^{\omega(p)}$.
