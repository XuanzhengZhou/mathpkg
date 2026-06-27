---
role: proof
locale: en
of_concept: gauss-sum-square
source_book: gtm007
source_chapter: "I"
source_section: "3"
---

Compute $y^2$:
\[
y^2 = \sum_{x, z \in \mathbb{F}_l} \left(\frac{xz}{l}\right) w^{x+z} = \sum_{u \in \mathbb{F}_l} w^u C_u,
\]
where $C_u = \sum_{t \in \mathbb{F}_l} \left(\frac{t(u-t)}{l}\right)$. For $t \neq 0$, using multiplicativity of the Legendre symbol:
\[
\left(\frac{t(u-t)}{l}\right) = \left(\frac{-t^2}{l}\right) \left(\frac{1-ut^{-1}}{l}\right) = (-1)^{\varepsilon(l)} \left(\frac{1-ut^{-1}}{l}\right).
\]
Thus $(-1)^{\varepsilon(l)} y^2 = \sum_{u \in \mathbb{F}_l} C_u w^u$ with $C_u = \sum_{t \in \mathbb{F}_l} \left(\frac{1-ut^{-1}}{l}\right)$.

If $u = 0$, then $C_0 = \sum_{t \in \mathbb{F}_l} \left(\frac{1}{l}\right) = l \cdot 1 = l-1$ (since $\left(\frac{0}{l}\right) = 0$ and $\left(\frac{1}{l}\right) = 1$). If $u \neq 0$, as $t$ runs over $\mathbb{F}_l^*$, $s = 1-ut^{-1}$ runs over $\mathbb{F}_l \setminus \{1\}$, so $C_u = \sum_{s \in \mathbb{F}_l} \left(\frac{s}{l}\right) - \left(\frac{1}{l}\right) = -1$ (since there are equally many squares and non-squares in $\mathbb{F}_l^*$).

Therefore $\sum_{u \in \mathbb{F}_l} C_u w^u = (l-1) - \sum_{u \in \mathbb{F}_l^*} w^u = l-1 - (-1) = l$. Hence $(-1)^{\varepsilon(l)} y^2 = l$, so $y^2 = (-1)^{\varepsilon(l)} l$.
