---
role: proof
locale: en
of_concept: tensor-product-character-decomposition-by-weight-multiplicities
source_book: gtm009
source_chapter: "24"
source_section: "Exercises (Ex. 9)"
---

**Proof.** Begin, as in (24.4), with the equation
$$
\operatorname{ch}_{\lambda'} * \omega(\lambda'' + \delta) = \sum_{\lambda \in \Lambda^+} n(\lambda) \, \omega(\lambda + \delta). \tag{2}
$$

Replace $\operatorname{ch}_{\lambda'}$ on the left side by its weight space decomposition $\operatorname{ch}_{\lambda'} = \sum_{\lambda \in \Lambda} m_{\lambda'}(\lambda) \varepsilon_{\lambda}$, and use $\omega(\mu) = \sum_{\sigma \in \mathcal{W}} \operatorname{sn}(\sigma) \varepsilon_{\sigma(\mu)}$ to obtain:
$$
\begin{aligned}
\operatorname{ch}_{\lambda'} * \omega(\lambda'' + \delta)
&= \left( \sum_{\nu \in \Lambda} m_{\lambda'}(\nu) \varepsilon_{\nu} \right) * \left( \sum_{\sigma \in \mathcal{W}} \operatorname{sn}(\sigma) \varepsilon_{\sigma(\lambda'' + \delta)} \right) \\
&= \sum_{\sigma \in \mathcal{W}} \operatorname{sn}(\sigma) \sum_{\nu \in \Lambda} m_{\lambda'}(\nu) \, \varepsilon_{\nu + \sigma(\lambda'' + \delta)}.
\end{aligned}
$$

Since the Weyl group $\mathcal{W}$ permutes the weight spaces of $V(\lambda')$, we have $m_{\lambda'}(\sigma(\nu)) = m_{\lambda'}(\nu)$ for all $\sigma \in \mathcal{W}$. Applying the change of variable $\nu \mapsto \sigma(\nu)$ and using $\sigma^{-1} = \sigma$ for the sign (with $\operatorname{sn}(\sigma^{-1}) = \operatorname{sn}(\sigma)$), the sum becomes:
$$
\sum_{\sigma \in \mathcal{W}} \operatorname{sn}(\sigma) \sum_{\nu \in \Lambda} m_{\lambda'}(\nu) \, \varepsilon_{\sigma(\nu + \lambda'' + \delta)}.
$$

Similarly, the right side of (2) can be expressed as:
$$
\sum_{\sigma \in \mathcal{W}} \operatorname{sn}(\sigma) \sum_{\lambda \in \Lambda^+} n(\lambda) \, \varepsilon_{\sigma(\lambda + \delta)}.
$$

Comparing the two expressions for each $\sigma \in \mathcal{W}$ and each dominant weight, one obtains relations for the coefficients $n(\lambda)$.

Define $t(\mu)$ for $\mu \in \Lambda$ by:
$$
t(\mu) =
\begin{cases}
0 & \text{if } \sigma(\mu) = \mu \text{ for some } \sigma \neq 1 \text{ in } \mathcal{W}, \\
\operatorname{sn}(\sigma) & \text{if the stabilizer of } \mu \text{ in } \mathcal{W} \text{ is trivial and } \sigma(\mu) \text{ is dominant}.
\end{cases}
$$

From Exercise 8, the alternating sum over the Weyl group vanishes for any weight with a nontrivial stabilizer. This implies that when extracting the coefficient of $\varepsilon_{\sigma(\lambda + \delta)}$ from both sides, only those weights $\nu + \lambda'' + \delta$ with trivial stabilizer contribute. Specifically, for each $\nu \in \Pi(\lambda')$ (the set of weights of $V(\lambda')$), the weight $\nu + \lambda'' + \delta$ determines a unique dominant weight $\{\nu + \lambda'' + \delta\}$ in its Weyl group orbit, and the coefficient contributed is $m_{\lambda'}(\nu) \, t(\nu + \lambda'' + \delta)$.

Therefore, equating formal characters:
$$
\operatorname{ch}_{\lambda'} * \operatorname{ch}_{\lambda''} = \sum_{\lambda \in \Pi(\lambda')} m_{\lambda'}(\lambda) \, t(\lambda + \lambda'' + \delta) \, \operatorname{ch}_{\{\lambda + \lambda'' + \delta\} - \delta},
$$
where $\{\mu\}$ denotes the unique dominant weight in the Weyl group orbit of $\mu$, and the formal character $\operatorname{ch}_{\mu}$ for dominant $\mu$ is given by Weyl's formula. $\square$
