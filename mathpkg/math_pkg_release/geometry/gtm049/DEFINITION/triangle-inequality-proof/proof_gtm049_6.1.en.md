---
role: proof
locale: en
of_concept: triangle-inequality-for-euclidean-distance
source_book: gtm049
source_chapter: "VI"
source_section: "6.1"
---

**Proof.** For any $a, b \in V$,

$$\|a + b\|^2 = \sigma(a + b, a + b) = \|a\|^2 + \|b\|^2 + 2\sigma(a, b).$$

By Schwarz's inequality (Lemma 1), $\sigma(a, b) \leq \|a\| \|b\|$. Therefore

$$\|a + b\|^2 \leq \|a\|^2 + \|b\|^2 + 2\|a\| \|b\| = (\|a\| + \|b\|)^2.$$

Taking square roots gives $\|a + b\| \leq \|a\| + \|b\|$, which is equivalent to

$$d(a, c) = \|a - c\| = \|(a - b) + (b - c)\| \leq \|a - b\| + \|b - c\| = d(a, b) + d(b, c).$$
