---
role: proof
locale: en
of_concept: corollary-analytic-disk-l
source_book: gtm011
source_chapter: "1"
source_section: "1.11"
---

The result is trivial if $f'(0) = 0$, so assume $f'(0) \neq 0$. Define

$$g(z) = \frac{f(Rz) - f(0)}{R f'(0)}.$$

Then $g$ is analytic on a region containing $\bar{D}$ where $D = B(0; 1)$, and $g(0) = 0$, $g'(0) = 1$. By Proposition 1.10 and the definition of Bloch's constant $L$, the image $g(D)$ contains a disk of radius at least $L$. Translating this back to $f$ via the scaling $z \mapsto Rz$, we obtain that $f(B(0; R))$ contains a disk of radius $R|f'(0)| L$.
