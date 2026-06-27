---
role: proof
locale: en
of_concept: equivalence-of-finite-b-and-m-moments
source_book: gtm040
source_chapter: "9"
source_section: "4"
---

By definition $b^{(r)} = M_j[\bar{t}_j^r]$. Let $t = \min(t_i, \bar{t}_j)$ for $i \neq j$, and let $u = \bar{t}_j - t$ (or $0$ if $t = \infty$). Then $\bar{t}_j = t + u \geq u$, so that

$$b^{(r)} \geq M_j[u^r] = \sum_k \Pr_j[x_t = k] \, M_k[\bar{t}_j^r] \quad \text{by Theorem 4-11}$$
$$\geq \Pr_j[x_t = i] \, M_i[\bar{t}_j^r] = \,^{j}\!\bar{H}_{ji} \, M_i[\bar{t}_j^r].$$

Since $^{j}\!\bar{H}_{ji} > 0$ for a recurrent chain, finiteness of $b^{(r)}_j$ implies finiteness of $M_i[\bar{t}_j^r]$, which in turn implies finiteness of $M^{(r)}$. The converse direction follows from $b^{(r)}_j \leq \sum_i P_{ji} M_i[(\bar{t}_j + 1)^r]$ and the binomial expansion.
