---
role: proof
locale: en
of_concept: estimates-for-z1-z2-and-chord
source_book: gtm041
source_chapter: "5"
source_section: "5.6"
---

For $|z_1|^2$ we have
$$
|z_1|^2 = \frac{k^4 + k^2 k_1^2}{(k^2 + k_1^2)^2} = \frac{k^2}{k^2 + k_1^2}.
$$
There is a similar formula for $|z_2|^2$. This proves the modulus formulas
$$
|z_1(h, k)| = \frac{k}{\sqrt{k^2 + k_1^2}}, \qquad |z_2(h, k)| = \frac{k}{\sqrt{k^2 + k_2^2}}.
$$

To prove the chord estimate, note that if $z$ is on the chord, then $|z| \leq \max(|z_1|, |z_2|)$, so it suffices to prove that
$$
|z_1| < \frac{\sqrt{2}\, k}{N} \quad \text{and} \quad |z_2| < \frac{\sqrt{2}\, k}{N}.
$$

Since $h_1/k_1$, $h/k$, $h_2/k_2$ are consecutive in $F_N$, we have the Farey neighbor property $kk_1 \geq N$ and $kk_2 \geq N$ (with appropriate bounds). Consequently,
$$
|z_1| = \frac{k}{\sqrt{k^2 + k_1^2}} \leq \frac{k}{\sqrt{2kk_1}} = \sqrt{\frac{k}{2k_1}} \leq \sqrt{\frac{k^2}{2N}} < \frac{\sqrt{2}\, k}{N}
$$
for sufficiently large $N$, and similarly for $|z_2|$. Since $|z| \leq \max(|z_1|, |z_2|)$, the bound $|z| < \sqrt{2}k/N$ holds for all $z$ on the chord. The chord length is at most $|z_1| + |z_2| < 2\sqrt{2}k/N$.
