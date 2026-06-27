---
role: proof
locale: en
of_concept: bounded-partial-sums-convergence
source_book: gtm007
source_chapter: "VI"
source_section: "2"
---

Assume $|A_{m,p}| \leq K$ for all $m, p$. Applying Abel's lemma (Lemma 2), we obtain
$$|S_{m,m'}| \leq K\left(\sum_{n=m}^{m'-1}\left|\frac{1}{n^s} - \frac{1}{(n+1)^s}\right| + \left|\frac{1}{m'^s}\right|\right).$$

By Proposition 6, we may suppose $s$ is real. Then the inequality simplifies to
$$|S_{m,m'}| \leq K / m^s,$$
from which convergence for $\Re(s) > 0$ follows immediately.

