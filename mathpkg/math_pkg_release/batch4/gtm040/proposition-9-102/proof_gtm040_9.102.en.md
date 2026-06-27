---
role: proof
locale: en
of_concept: proposition-9-102
source_book: gtm040
source_chapter: "9"
source_section: "102"
---

**Proof:** Choose an arbitrary point as the reference state 0. Then, by Lemma 9-100, there is either a one-point set or a set in $\mathcal{L}_0$ which has non-zero capacity.

If $k(\{1\}) > 0$ for some state, then we may choose 0 and 1 as indicated, since $k(E) \geq k(\{1\}) > 0$ if $1 \in E$. If $k(\{1\}) < 0$ for some state, then use 1 as a new reference point, and $k'(\{0\}) = -k(\{1\}) > 0$. Hence we simply interchange the roles of 0 and 1.

Otherwise $k(E) \neq 0$ for some $E \in \mathcal{L}_0$. Then $k(E) > 0$. Let $E$ be a set in $\mathcal{L}_0$ with positive capacity and containing as few states as possible, let

on each path. The capacity inequalities follow from the fact that the time to enter all of $n$ sets is no greater than the time to enter the intersection; hence the time to reach 0 from the intersection is no greater than the time to reach 0 after all $n$ sets are entered. We also see why $k(E) > 0$, if $E$ has more than one state.

Corollary 9-104: $(\lambda^E M)_j = (\hat{\lambda}^E \hat{M})_j$ for all $j \in E$.

Proof: Choose $j \in E$ as reference point. Then

$$(\lambda^E M)_j = k(E) = \hat{k}(E) = (\hat{\lambda}^E \hat{M})_j.$$

Proposition 9-105: In an infinite ergodic chain $K + k1\alpha$ has negative entries for each $k$.

Proof:

$$(K + k1\alpha)_{jj} = G_{0j} - C_{0j} + k\alpha_j$$

$$= \left( -\frac{C_{0j} - G_{0j}}{\alpha_j} + k \right)\alpha_j.$$

Hence

$$\lim_j \frac{(K + k1\alpha)_{jj}}{\alpha_j} = -\infty$$ by Proposition 9-63.

Proposition 9-106: Let $\{E_n\}$ be an increasing sequence of finite sets with union the set of all states $S$. Then $\lim_{n \to \infty} k(E_n) < +\infty$ if and only if the chain is strong ergodic. In a strong ergodic chain, $k(E) = M_{\alpha0} - M_{\alphaE}$, and hence $\hat{M}_{\alphaE} = M_{\alphaE}$.

Proof: $k(E) = M_{\alpha}[t_0 - t_E]$ and therefore

$$\sum_{i \in E} \alpha_i M_{i0} \leq k(E) \leq M_{\alpha0}.$$
