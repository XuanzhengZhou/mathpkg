---
role: proof
locale: en
of_concept: gauss-sum-squared
source_book: gtm007
source_chapter: "I"
source_section: "§3"
---

We have
$$y^2 = \sum_{x, z} \left( \frac{xz}{l} \right) w^{x+z} = \sum_{u \in F_l} w^u \left( \sum_{t \in F_l} \left( \frac{t(u-t)}{l} \right) \right).$$

Now if $t \neq 0$:
$$\left( \frac{t(u-t)}{l} \right) = \left( \frac{-t^2}{l} \right) \left( \frac{1-ut^{-1}}{l} \right) = (-1)^{\varepsilon(l)} \left( \frac{1-ut^{-1}}{l} \right),$$
and
$$(-1)^{\varepsilon(l)} y^2 = \sum_{u \in F_l} C_u w^u,$$
where
$$C_u = \sum_{t \in F_l} \left( \frac{1-ut^{-1}}{l} \right).$$

If $u = 0$, $C_0 = \sum_{t \in F_l} \left( \frac{1}{l} \right) = l-1$; otherwise $s = 1-ut^{-1}$ runs over $F_l - \{1\}$, and we have
$$C_u = \sum_{s \in F_l} \left( \frac{s}{l} \right) - \left( \frac{1}{l} \right) = -\left( \frac{1}{l} \right) = -1,$$
since in $F_l^*$ there are as many squares as non squares. Hence $\sum_{u \in F_l} C_u w^u = l-1 - \sum_{u \in F_l^*} w^u = l$, which proves the lemma.
