---
role: proof
locale: en
of_concept: proposition-9-65
source_book: gtm040
source_chapter: "9"
source_section: "65"
---

Proof:

$$M_\pi[t_i^r t_{i,j}^s] = \sum_{m,n} \Pr_\pi[t_i = m \wedge t_{i,j} = n] m^r n^s$$

$$= \sum_{m,n} \Pr_\pi[t_i = m] \Pr_\pi[t_{i,j} = n \mid t_i = m] m^r n^s$$

$$= \sum_{m,n} \Pr_\pi[t_i = m] \Pr_i[t_j = n] m^r n^s$$

by the strong Markov property

$$= \sum_m \Pr_\pi[t_i = m] m^r \left( \sum_n \Pr_i[t_j = n] n^s \right)$$

$$= M_\pi[t_i^r] M_i[t_j^s].$$

Proposition 9-67: The vector $b^{(r)}$ is finite-valued if and only if $M^{(r)}$ is finite-valued.

Proof: By definition $b^{(r)} = M_j[\bar{t}_j^r]$. Let $t = \min(t_i, \bar{t}_j)$ for $i \neq j$, and let $u = \bar{t}_j - t$ (or $0$ if $t = \infty$). Then $\bar{t}_j = t + u \geq u$, so that

$$b^{(r)} \geq M_j[u^r]$$

$$= \sum_k \Pr_j[x_t = k] M_k[\bar{t}_j^r] \text{ by Theorem 4-11}$$

$$\geq \Pr_j[x_t = i] M_i[\bar{t}_j^r]$$

$$= j\bar{H}_{ji}

Proposition 9-68: If $b_0^{(r)} < \infty$ for some state 0, then $b_j^{(r)} < \infty$ for all $j$.

Proof: The proof is by induction on $r$. For $r = 0$, $b_j^{(0)} = 1$, and the result is trivial. Suppose that the result holds for $r \leq n$ and that $b_0^{(n+1)} < \infty$. Then $b_0^{(r)} < \infty$ for $r \leq n$, so that $b_j^{(r)} < \infty$ for $r \leq n$ by inductive assumption. By Proposition 9-67, $M^{(r)}$ is finite-valued for $r \leq n$, and by Proposition 9-65, $c_0^{(r)} < \infty$ for $r \leq n$. Thus for $j \neq 0$

$$c_j^{(n)} = \sum_k \alpha_k M_k[t_j^n]$$
$$\leq \sum_k \alpha_k M_k[(t_0 + t_{0,j})^n] \quad \text{since } t_j \leq t_0 + t_{0,j}$$
$$= \sum_k \alpha_k \sum_{r=0}^{n} \binom{n}{r} M_k[t_0^r t_{0,j}^{n-r}]$$
$$= \sum_k \alpha_k \sum_{r=0}^{n} \binom{n}{r} M_k^{(r)} M_{0j}^{(n-r)}$$
$$= \sum_{r=0}^{n} \binom{n}{r} c_0^{(r)} M_{0j}^{(n-r)} < \infty.$$

Therefore $b^{(n+1)} < \infty$ by Proposition 9-65.

Finally we show the connection between the moments in $P$ and those in $\hat{P}$.

Lemma 9-69: $\bar{F}_{00}^{(n)} = \hat{\bar{F}}_{00}^{(n)}$ in a recurrent chain.

Proof: By Lemma 6-34, for $n \geq 1

For the second assertion,

$$\alpha_i \Pr_i[t_0 = m] = \sum \alpha_i P_{ik_1} P_{k_1k_2} \dots P_{k_{m-1}0}$$

$$= \sum \alpha_0 \hat{P}_{0k_{m-1}} \dots \hat{P}_{k_2k_1} \hat{P}_{k_1i},$$

where each of the sums is taken over the denumerable number of sequences $k_1, \dots, k_{m-1}$ with each $k_j$ different from 0. Hence for $m > 0$,

$$\sum_i \alpha_i \Pr_i[t_0 = m] = \alpha_0 \sum \hat{P}_{0k_{n-1}} \dots \hat{P}_{k_2k_1}$$

$$= \alpha_0(1 - \hat{H}_{00}^{(m-1)})$$

$$= \alpha_0(1 - \bar{H}_{00}^{(m-1)}) \quad \text{by Lemma 9-69}$$

$$= \sum_i \alpha_i \Pr_i[\hat{t}_0 = m] \quad \text{by symmetry.}$$

If we multiply through by $m^r$ and sum on $m$, we obtain $c_0^{(r)} = \hat{c}_0^{(r)}$.

We thus arrive at a hierarchy of recurrent chains:
