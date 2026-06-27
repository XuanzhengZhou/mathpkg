---
role: proof
locale: en
of_concept: center-is-subring
source_book: gtm013
source_chapter: "1"
source_section: "1.10"
---

To verify $\operatorname{Cen} R$ is a subring, check closure. For $r, s \in \operatorname{Cen} R$ and any $x \in R$:

$$(r - s)x = rx - sx = xr - xs = x(r - s),$$
$$(rs)x = r(sx) = r(xs) = (rx)s = (xr)s = x(rs).$$

Also $1 \cdot x = x \cdot 1$ for all $x$, so $1 \in \operatorname{Cen} R$. Hence $\operatorname{Cen} R$ is a subring. By definition elements of $\operatorname{Cen} R$ commute with each other, so $\operatorname{Cen} R$ is commutative. If $R = \operatorname{Cen} R$, then $R$ is commutative; conversely, if $R$ is commutative, every element is central, so $R = \operatorname{Cen} R$.
