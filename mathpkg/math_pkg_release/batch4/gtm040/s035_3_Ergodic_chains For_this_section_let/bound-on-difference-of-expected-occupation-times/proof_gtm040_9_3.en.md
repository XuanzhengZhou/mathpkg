---
role: proof
locale: en
of_concept: bound-on-difference-of-expected-occupation-times
source_book: gtm040
source_chapter: "9"
source_section: "3"
---

Summing over the powers of $P$ in Lemma 6-34, we obtain

$$N_{ij}^{(n)} = \sum_{k=0}^{\infty} F_{ij}^{(k)} N_{jj}^{(n-k)},$$

where we use the convention $N_{jj}^{(m)} = 0$ if $m < 0$. Since $\sum_{k=0}^{\infty} F_{ij}^{(k)} = H_{ij} = 1$, we have

$$N_{jj}^{(n)} - N_{ij}^{(n)} = \sum_{k=0}^{\infty} F_{ij}^{(k)} [N_{jj}^{(n)} - N_{jj}^{(n-k)}].$$

Now $N_{jj}^{(n)} - N_{jj}^{(n-k)} \geq 0$ for $k \geq 0$, which proves the lower bound $0 \leq N_{jj}^{(n)} - N_{ij}^{(n)}$. For the upper bound, note that $N_{jj}^{(n)} - N_{jj}^{(n-k)} \leq k$ for $0 \leq k \leq n$, and $N_{jj}^{(n)} \leq M_{jj}$. Hence

$$N_{jj}^{(n)} - N_{ij}^{(n)} \leq \sum_{k=0}^{\infty} k F_{ij}^{(k)} = M_{ij}.$$

For the limit, as $n \to \infty$, we use the fact that $N_{jj}^{(n)} - N_{jj}^{(n-k)} \to k\alpha_j$ by the ergodic theorem, and dominated convergence yields

$$\lim_{n \to \infty} [N_{jj}^{(n)} - N_{ij}^{(n)}] = \sum_{k=0}^{\infty} F_{ij}^{(k)} \cdot k\alpha_j = M_{ij}\alpha_j.$$
