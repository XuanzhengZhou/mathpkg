---
role: proof
locale: en
of_concept: gauss-sum-legendre-symbol
source_book: gtm007
source_chapter: "I"
source_section: "§3"
---

Since $\Omega$ is of characteristic $p$, the Frobenius map $t \mapsto t^p$ is a field automorphism. Applying it to the Gauss sum:
$$y^p = \sum_{x \in F_l} \left( \frac{x}{l} \right)^p w^{xp} = \sum_{x \in F_l} \left( \frac{x}{l} \right) w^{xp}.$$

Since $\left( \frac{x}{l} \right) \in \{\pm 1\} \subset F_p$, it is fixed by Frobenius. Now let $z = xp$; as $x$ runs over $F_l$, the product $xp$ runs over $F_l$ (multiplication by $p$ is invertible mod $l$ since $p \neq l$). Thus:
$$y^p = \sum_{z \in F_l} \left( \frac{z p^{-1}}{l} \right) w^z = \sum_{z \in F_l} \left( \frac{z}{l} \right) \left( \frac{p^{-1}}{l} \right) w^z = \left( \frac{p}{l} \right) \sum_{z \in F_l} \left( \frac{z}{l} \right) w^z = \left( \frac{p}{l} \right) y,$$
since $\left( \frac{p^{-1}}{l} \right) = \left( \frac{p}{l} \right)$ (the Legendre symbol is multiplicative and $(\pm 1)^{-1} = \pm 1$). Dividing by $y$ (which is nonzero since $y^2 = (-1)^{\varepsilon(l)}l \neq 0$), we obtain $y^{p-1} = \left( \frac{p}{l} \right)$.
