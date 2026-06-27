---
role: proof
locale: en
of_concept: lemma-9-3
source_book: gtm040
source_chapter: "9"
source_section: "1. Potentials"
---

By Lemma 9-2,
$$0 \leq N_{jj}^{(n)} - N_{ij}^{(n)} \leq c \quad \text{for all } n.$$
Hence
$$0 \leq 1 - \frac{N_{ij}^{(n)}}{N_{jj}^{(n)}} \leq \frac{c}{N_{jj}^{(n)}}.$$
Since $i$ and $j$ communicate and the chain is recurrent, $N_{jj}^{(n)} \to \infty$ as $n \to \infty$. Therefore $N_{ij}^{(n)} / N_{jj}^{(n)} \to 1$ when $H_{ij} = 1$ (the recurrent case), and more generally the limit is $H_{ij}$. The second inequality follows from duality and the fact that $N_{ij}^{(n)} \alpha_i = N_{ji}^{(n)} \alpha_j$ in the dual chain.
