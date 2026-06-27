---
role: proof
locale: en
of_concept: bounded-partial-sums-convergence
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

Assume $|A_{m,p}| \leq K$ for all $m, p$. By Abel\'s lemma (Lemma 2),
$$
S_{m,m'} = \sum_{n=m}^{m'} \frac{a_n}{n^s} = \sum_{n=m}^{m'-1} A_{m,n}\left(\frac{1}{n^s} - \frac{1}{(n+1)^s}\right) + A_{m,m'}\frac{1}{m'^s}.
$$
We may assume $s$ is real (by Proposition 6 on uniform convergence in angular domains). Then $1/n^s - 1/(n+1)^s > 0$ and telescoping gives
$$
|S_{m,m'}| \leq \frac{K}{m^s},
$$
which tends to $0$ as $m \to \infty$ when $s > 0$. The convergence follows.
