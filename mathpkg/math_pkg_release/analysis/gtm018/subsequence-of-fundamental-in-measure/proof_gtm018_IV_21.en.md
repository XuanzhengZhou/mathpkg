---
role: proof
locale: en
of_concept: subsequence-of-fundamental-in-measure
source_book: gtm018
source_chapter: "IV"
source_section: "21"
---
**Proof.** For each $k$, choose $\bar{n}(k)$ such that if $n,m \geq \bar{n}(k)$, then
$$\mu(\{x : |f_n(x) - f_m(x)| \geq 1/2^k\}) < 1/2^k.$$
Set $n_1 = \bar{n}(1)$, $n_2 = (n_1+1) \cup \bar{n}(2)$, $n_3 = (n_2+1) \cup \bar{n}(3)$, etc., so $n_1 < n_2 < \cdots$. Define
$$E_k = \{x : |f_{n_k}(x) - f_{n_{k+1}}(x)| \geq 1/2^k\}.$$
For $k \leq i \leq j$ and $x \notin E_k \cup E_{k+1} \cup \cdots$,
$$|f_{n_i}(x) - f_{n_j}(x)| \leq \sum_{m=i}^{\infty} |f_{n_m}(x) - f_{n_{m+1}}(x)| < 1/2^{i-1}.$$
Thus $\{f_{n_i}\}$ is uniformly fundamental on $X - (E_k \cup E_{k+1} \cup \cdots)$, and
$$\mu(E_k \cup E_{k+1} \cup \cdots) \leq \sum_{m=k}^{\infty} \mu(E_m) < 1/2^{k-1} \to 0,$$
proving almost uniform fundamentality.
