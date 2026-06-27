---
role: proof
locale: en
of_concept: systems-theorem-for-markov-chains-expectation
source_book: gtm040
source_chapter: "4"
source_section: "5"
---

If $f$ assumes negative values, we may prove the result for $f^+$ and $f^-$ separately and then subtract. We therefore assume $f \geq 0$.

For each positive integer $m$, partition the range of $f$ into dyadic intervals. Define the statement $p_{j^{(m)}}$ to be $j/2^m \leq f < (j+1)/2^m$ for $1 \leq j < m \cdot 2^m$, let $p_{0^{(m)}}$ be the statement $0 < f < 1/2^m$, and let $p_{m 2^m^{(m)}}$ be the statement $m \leq f$. Define the statements $p'_{j^{(m)}}$ similarly for $f'$. Then $p_{j^{(m)}}$ and $p'_{j^{(m)}}$ satisfy the hypotheses of Theorem 4-10, so that

$$\Pr_{\pi}[p_{j^{(m)}}] = \sum_{k} \Pr_{\pi}[x_t = k] \Pr_k[p'_{j^{(m)}}].$$

Now define the simple function approximation

$$f_m = \sum_{j} \frac{j}{2^m} \cdot \mathbf{1}_{p_{j^{(m)}}},$$

and similarly for $f'_m$. Then $f_m \uparrow f$ and $f'_m \uparrow f'$ pointwise as $m \to \infty$.

Taking expectations:

$$M_{\pi}[f_m] = \sum_j \frac{j}{2^m} \Pr_{\pi}[p_{j^{(m)}}] = \sum_j \frac{j}{2^m} \sum_k \Pr_{\pi}[x_t = k] \Pr_k[p'_{j^{(m)}}] = \sum_k \Pr_{\pi}[x_t = k] M_k[f'_m].$$

Letting $m \to \infty$ and applying the Monotone Convergence Theorem to both sides yields

$$M_{\pi}[f] = \sum_k \Pr_{\pi}[x_t = k] M_k[f'].$$
