---
role: proof
locale: en
of_concept: projections-as-extreme-points
source_book: gtm003
source_chapter: "5"
source_section: "5.5"
---

Let $p$ be a projection in $A$. Then $p$ is the unit of $pAp$; because $pAp$ is hereditary in $A$ by (5.1), we have $[0, p] = \{x \in A : 0 \leq x \leq p\}$ contained in $pAp$. Thus it suffices to show that $p$ is an extreme point of the unit ball of $pAp$ intersected with $(pAp)_+$, which is the order interval $[0, p]$ in $pAp$.

If $p = \frac{1}{2}(x + y)$ with $x, y \in [0, p]$, then $0 \leq p - x = y - p \leq p$, so $p - x \in pAp$. Since $p$ is the unit of $pAp$, we have $\|p - x\| \leq 1$. But also $\|x\| \leq 1$, and $p = \frac{1}{2}(x + (2p - x))$ forces $\|p - x\| = 0$, so $x = p = y$.

This shows that any projection $q \leq p$ is an extreme point of $[0, p]$. The converse follows similarly.
