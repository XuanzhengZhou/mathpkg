---
role: proof
locale: en
of_concept: systems-theorem-for-markov-chains-probability
source_book: gtm040
source_chapter: "4"
source_section: "5"
---

By the first hypothesis, $\Pr_{\pi}[p \land t = \infty] = 0$, so we may condition on $t < \infty$ without loss. Then

$$\Pr_{\pi}[p] = \sum_{k} \Pr_{\pi}[\omega \in P \land x_t = k]$$
$$= \sum_{k} \Pr_{\pi}[\omega_t \in P' \land x_t = k]$$
$$= \sum_{k} \Pr_{\pi}[x_t = k] \Pr_{\pi}[\omega_t \in P' \mid x_t = k]$$
$$= \sum_{k} \Pr_{\pi}[x_t = k] \Pr_k[p'] \qquad \text{by Theorem 4-9}.$$

The second equality uses the correspondence between $p$ and $p'$ (hypothesis 2): $\omega \in P$ is equivalent to $\omega_t \in P'$ when $t(\omega) < \infty$. The final equality applies the strong Markov property (Theorem 4-9) with the identically true statement as $q$, which gives $\Pr_{\pi}[\omega_t \in P' \mid x_t = k] = \Pr_k[p']$.
