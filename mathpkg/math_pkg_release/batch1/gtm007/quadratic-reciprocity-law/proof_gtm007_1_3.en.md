---
role: proof
locale: en
of_concept: quadratic-reciprocity-law
source_book: gtm007
source_chapter: "I"
source_section: "3"
---

Let $l$ and $p$ be distinct odd primes. Let $\Omega$ be an algebraic closure of $\mathbb{F}_p$ and let $w \in \Omega$ be a primitive $l$-th root of unity. Define the Gauss sum:
\[
y = \sum_{x \in \mathbb{F}_l} \left(\frac{x}{l}\right) w^x.
\]
One computes $y^2 = (-1)^{\varepsilon(l)}l$ in $\mathbb{F}_p$ (Lemma 1, by evaluating $\sum_{u \in \mathbb{F}_l} C_u w^u$ with $C_u = \sum_{t \in \mathbb{F}_l} \left(\frac{1-ut^{-1}}{l}\right)$).

Now compute $y^p$ in two ways. On one hand, by the Frobenius map in characteristic $p$:
\[
y^p = \sum_{x \in \mathbb{F}_l} \left(\frac{x}{l}\right)^p w^{xp} = \sum_{x \in \mathbb{F}_l} \left(\frac{x}{l}\right) w^{xp}.
\]
Substituting $z = xp$ and noting that $\left(\frac{zp^{-1}}{l}\right) = \left(\frac{z}{l}\right)\left(\frac{p^{-1}}{l}\right) = \left(\frac{z}{l}\right)\left(\frac{p}{l}\right)$ (since $\left(\frac{p^{-1}}{l}\right) = \left(\frac{p}{l}\right)$), we get $y^p = \left(\frac{p}{l}\right) y$.

On the other hand, $y^p = y(y^2)^{(p-1)/2} = y((-1)^{\varepsilon(l)}l)^{(p-1)/2} = y(-1)^{\varepsilon(l)\varepsilon(p)} \left(\frac{l}{p}\right)$. Comparing the two expressions gives:
\[
\left(\frac{p}{l}\right) = (-1)^{\varepsilon(l)\varepsilon(p)} \left(\frac{l}{p}\right),
\]
which is the quadratic reciprocity law.
