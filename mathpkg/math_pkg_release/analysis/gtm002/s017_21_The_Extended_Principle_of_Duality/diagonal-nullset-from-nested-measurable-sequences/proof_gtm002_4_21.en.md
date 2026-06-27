---
role: proof
locale: en
of_concept: diagonal-nullset-from-nested-measurable-sequences
source_book: gtm002
source_chapter: "4"
source_section: "21. The Extended Principle of Duality"
---

Let $I_k = [-k, k]$. For each $i$ and $k$ there is a positive integer $n_k(i)$ such that

$$m(E_{i,n_k(i)} \cap I_k) < 1/(k 2^i).$$

This is possible because $\bigcap_j E_{i,j}$ is a nullset, so for each fixed $i$ and $k$ the measures $m(E_{i,j} \cap I_k)$ tend to $0$ as $j \to \infty$.

Hence

$$m\left(\bigcup_i E_{i,n_k(i)} \cap I_k\right) \leq \sum_i m(E_{i,n_k(i)} \cap I_k) < \sum_i 1/(k 2^i) = 1/k.$$

Put $E = \bigcap_k \bigcup_i E_{i,n_k(i)}$. For any finite interval $I$, we have $I \subset I_k$ for all sufficiently large $k$. Then

$$E \cap I \subset \bigcup_i E_{i,n_k(i)} \cap I_k.$$

Hence $m(E \cap I) < 1/k$ for all sufficiently large $k$. Since $k$ is arbitrary, $m(E \cap I) = 0$. Thus $E \cap I$ is a nullset for every finite interval $I$, and therefore $E$ is a nullset.
