---
role: proof
locale: en
of_concept: finiteness-of-all-b-moments
source_book: gtm040
source_chapter: "9"
source_section: "4"
---

The proof is by induction on $r$. For $r = 0$, $b_j^{(0)} = 1$, and the result is trivial. Suppose that the result holds for $r \leq n$ and that $b_0^{(n+1)} < \infty$. Then $b_0^{(r)} < \infty$ for $r \leq n$, so that $b_j^{(r)} < \infty$ for $r \leq n$ by inductive assumption. By Proposition 9-67, $M^{(r)}$ is finite-valued for $r \leq n$, and by Proposition 9-65, $c_0^{(r)} < \infty$ for $r \leq n$. Thus for $j \neq 0$

$$c_j^{(n)} = \sum_k \alpha_k M_k[t_j^n] \leq \sum_k \alpha_k M_k[(t_0 + t_{0,j})^n] \quad \text{since } t_j \leq t_0 + t_{0,j}$$
$$= \sum_k \alpha_k \sum_{r=0}^{n} \binom{n}{r} M_k[t_0^r t_{0,j}^{n-r}]$$
$$= \sum_k \alpha_k \sum_{r=0}^{n} \binom{n}{r} M_k^{(r)} M_{0j}^{(n-r)}$$
$$= \sum_{r=0}^{n} \binom{n}{r} c_0^{(r)} M_{0j}^{(n-r)} < \infty.$$

Therefore $b^{(n+1)} < \infty$ by Proposition 9-65.
