---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

If $\mu \in \mathcal{E}_Q$, then there are strictly positive functions $g_{(n,i)}$ and $h_{(n,i)}$ ($n \in \mathbb{Z}, i \in S$) such that

(1) $g_{(n+1,i_{n+1})} = \sum_{i_n \in S} g_{(n,i_n)}Q_{i_ni_{n+1}}$,

(2) $h(n,i_n) = \sum_{

and

$$\mu_{n+2}^{n+2}(\iota) = \frac{Q_{k0}Q_{00}}{(Q^2)_{k0}} = \frac{P_{n+1,k0}P_{n+2,00}}{(P_{n+1}P_{n+2})_{k0}}$$

whenever $i_n = j$, $i_{n+1} = k$, $i_{n+2} = i_{n+3} = 0$. Let $\bar{h}_{(n,j)} = (Q^2)_{j0}/(P_nP_{n+1})_{j0}$, $c_n = Q_{00}/P_{n+1,00}$. Then dividing the first equation by the second and rearranging terms,

$$\frac{P_{n,jk}}{Q_{jk}} = \frac{1}{c_{n+1}} \frac{\bar{h}_{(n+1,k)}}{\bar{h}_{(n,j)}}.$$

Choose $\bar{c}_n$, $n \in \mathbb{Z}$, so that $\bar{c}_0 = 1$ and $\bar{c}_{n-1}/\bar{c}_n = c_n$. Now define $h_{(n,j)} = \bar{c}_n \bar{h}_{(n,j)}$ to get

$$P_{n,jk} = Q_{jk}h_{(n+1,k)}/h_{(n,j)}$$

as desired. Equation (2) follows immediately from the fact that $P_n$ is a transition matrix. If we define $g_{(n,j)} = \pi_{n,j}/h_{(n,j)}$, then (3) holds because $\pi_n$ is a probability measure, while the equation $\pi_n P_n = \pi_{n+1}$ implies (1). It therefore remains only to derive the representation of $g$ and $h$ as ratio limits of powers of $Q$. To this end, choose $\Lambda(n)$ and $k_n$ as in the proof of the previous theorem. Then for $m > 0$,

$$\Pr[x_m = i_m \mid x_0 = 0] = \lim_{n \to \infty} \

are space-time harmonic for sums of independent random variables. By analogy to Example 6 of Section 10-13, one can show that the extreme such functions are of the form $c^m t^i$ for some $c > 0, t > 0$ ($q_i > 0$ excludes degenerate solutions). Thus,

$$g_{(0,t)} h_{(0,t)} = \int_0^\infty \int_0^\infty [s^i t^i] d\nu(s) d\mu(t)$$

for some measures $\nu$ and $\mu$ on $(0, \infty)$. It follows that

$$\sum_{i \in \mathbb{Z}} g_{(0,t)} h_{(0,t)} = \int_0^\infty \int_0^\infty \left[ 1 + \sum_{i=1}^{\infty} (st)^i + \sum_{i=1}^{\infty} \frac{1}{(st)^i} \right] d\nu(s) d\mu(t)$$

$$= \infty,$$

since one of the two infinite sums must diverge for any given $s$ and $t$. This contradicts equation (3) of Theorem 12-37, so $\mathcal{E}_Q$ is empty. $\mathcal{G}_Q$ is therefore empty by Theorem 12-28.

If $Q > 0$ is an ergodic transition matrix, then there is a unique probability measure $\alpha > 0$ such that $\alpha Q = \alpha$. In this case $\mathcal{G}_Q$ clearly contains the stationary process with

$$\pi_{n,i} = \alpha_i \quad \text{and} \quad P_{n,ij} = Q_{ij} \quad \text{for all } n \in \mathbb{Z}.$$

Thus, whenever $Q' \approx Q$ for some ergodic $Q$, then $|\mathcal{G}_{Q'}| \neq 0$. Our next goal is to show that when $S$ is finite $\mathcal{G}_{Q'}$ contains exactly one Markov field for any $Q' > 0$, and that this field is a stationary Markov chain on $\mathbb{Z}$. The first step is contained in

But this contradicts the definition of $\bar{c}$ once we normalize $Q' \bar{h}$. Hence $\bar{c} \bar{h} = Q' \bar{h} > 0$, which shows that $\bar{h} > 0$.

Theorem 12-40: If $S$ is finite, then $|\mathcal{G}_{Q'}| = 1$. $\mathcal{G}_{Q'}$ consists of the Markov chain with transition matrix $Q$ and stationary measure $\alpha$, where $Q$ is defined as in Lemma 12-39 and $\alpha$ is the regular probability measure for $Q$.
