---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

In any

PROOF: By Lemma 9-62,

$$\frac{M_{ji}}{M_{ij}} = \frac{i \hat{\lambda}_j}{j \hat{\lambda}_i}.$$

By Proposition 9-60 the numerator tends to 0 and the denominator tends to 1. Hence the first assertion follows. Therefore, for all but finite many states $j$,

$$2M_{ij} \geq M_{ji} + M_{ij} \geq \bar{M}_{jj} = \frac{1}{\alpha_j}.$$

Since $\sum \alpha_j < \infty$, $\alpha_j \to 0$ and $M_{ij} \to \infty$. Finally

$$(C_{ij} - G_{ij})/\alpha_j = M_{ij} - \frac{i \nu_j}{\alpha_j} = M_{ij} - \frac{1}{\alpha_j} i \lambda_j i N_{jj}$$

$$= M_{ij} - i \lambda_j S_{ij} = M_{ij} - i \lambda_j (M_{ij} + M_{ji})$$

$$= M_{ij} \left[ 1 - i \lambda_j \left( 1 + \frac{M_{ji}}{M_{ij}} \right) \right].$$

The factor in brackets tends to 1 since $i \lambda_j \to 0$ and $M_{ji}/M_{ij} \to 0$. Thus the third assertion of the proposition follows from the fact that $M_{ij} \to \infty$.

Corollary 9-64: In any infinite noncyclic ergodic chain, $C \neq G$.

PROOF: If $C = G$, then $(C_{ij} - G_{ij})/\alpha_j = 0$ for every $j$.

On the other hand, there are many finite ergodic chains with $C = G$. An example is

$$P = \begin{pmatrix} 1 - a & a \\ a & 1 - a \end{pmatrix}$$

for $0 < a < 1$.

4. Classes of ergodic chains

Let $P$ be a recurrent chain. In this section we shall investigate the finiteness of the $r$th

Let 0 be a distinguished state and write

$$P = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \begin{pmatrix} P_{00} & U \\ R & Q \end{pmatrix} \text{ and } \alpha = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \begin{pmatrix} \alpha_0 & \bar{\alpha} \end{pmatrix}.$$

The chain $^0P$ obtained from $P$ by making 0 absorbing is an absorbing chain and has $N = \sum Q^k$ as its fundamental matrix. The time to absorption $a$ in the chain $^0P$ is the same as the time $t_0$ to reach 0 in the chain $P$. As in Section 8-8 we let $a^{(r)}$ be a column vector indexed by the transient states of $^0P$ and satisfying

$$a_i^{(r)} = M_i[t_0^r] = M_{i0}^{(r)}.$$

Since $M_{00}^{(r)} = 0$, Proposition 8-68 enables us to compute any column of $M^{(r)}$. From the relation $c_0^{(r)} = \bar{\alpha} a^{(r)}$ we also have a formula for the computation of $c^{(r)}$. An easy calculation gives $b_0^{(r)}$ in terms of $a^{(m)}$ with $m \leq r$:

$$b_0^{(r)} = M_0[\bar{t}_0^r] = \sum_k P_{0k} M_k[(t_0 + 1)^r]$$

$$= P_{00} + \sum_{k \neq 0} P_{0k} \sum_{m=0}^{r} \binom{r}{m} M_k[t_0^m]$$

$$= P_{00} + \sum_{m=0}^{r} \binom{r}{m} Ua^{(m)}.$$

The first three propositions to follow give conditions for the finiteness of $M^{(r)}$, $b^{(r)}$, and $c^{(r)}$.
