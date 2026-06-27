---
role: proof
locale: en
of_concept: quadratic-reciprocity-law
source_book: gtm007
source_chapter: "I"
source_section: "§3"
---

[The main proof uses Gauss sums. Define the Gauss sum $y = \sum_{x \in F_l} \left(\frac{x}{l}\right) w^x$ where $w$ is a primitive $l$-th root of unity in an extension of $F_p$.]

**Lemma 1.** $y^2 = (-1)^{\varepsilon(l)} l$.

*Proof.* We have
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

**Lemma 2.** $-y^{p-1} = \left( \frac{p}{l} \right)$

Since $\Omega$ is of characteristic $p$, we have
$$y^p = \sum_{x \in F_l} \left( \frac{x}{l} \right) w^{xp} = \left( \frac{p}{l} \right) \sum_{z \in F_l} \left( \frac{z}{l} \right) w^z = \left( \frac{p}{l} \right) y.$$

Thus $y^{p-1} = \left( \frac{p}{l} \right)$ in $\Omega$, and since $y^{p-1} \in F_p$, we obtain the result.

Now from Lemma 1, $y^2 = (-1)^{\varepsilon(l)} l$, so:
$$y^{p-1} = (y^2)^{(p-1)/2} = (-1)^{\varepsilon(l)(p-1)/2} l^{(p-1)/2} = (-1)^{\varepsilon(l)\varepsilon(p)} \left( \frac{l}{p} \right).$$

Comparing with Lemma 2 yields:
$$\left( \frac{p}{l} \right) = (-1)^{\varepsilon(l)\varepsilon(p)} \left( \frac{l}{p} \right),$$
which is the quadratic reciprocity law.
