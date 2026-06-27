---
role: proof
locale: en
of_concept: stopping-time
source_book: gtm095
source_chapter: "1"
source_section: "3"
---

# Proof of Corollary (Wald's Identities)

**Corollary.** For the martingale $(S_k, \mathcal{D}_k)_{1 \leq k \leq n}$ of Example 1, and any stopping time $\tau$ (with respect to $(\mathcal{D}_k)$), we have the formulas

$$\mathsf{E}\,S_\tau = 0, \quad \mathsf{E}\,S_\tau^2 = \mathsf{E}\,\tau, \tag{11}$$

known as Wald's identities.

**Proof.** Recall the martingale of Example 1: let $\eta_1, \ldots, \eta_n$ be independent random variables with $\mathsf{E}\,\eta_k = 0$ and $|\eta_k| \leq K$ (bounded), and set

$$S_k = \eta_1 + \cdots + \eta_k, \quad \mathcal{D}_k = \mathcal{D}_{\eta_1, \ldots, \eta_k}.$$

Then $(S_k, \mathcal{D}_k)_{1 \leq k \leq n}$ is a martingale.

*First identity.* The optional stopping theorem (Theorem 1 of this section) states that for any martingale $(\xi_k, \mathcal{D}_k)$ and any stopping time $\tau$, we have $\mathsf{E}(\xi_\tau \mid \mathcal{D}_1) = \xi_1$ and consequently $\mathsf{E}\,\xi_\tau = \mathsf{E}\,\xi_1$. Applying this to the martingale $(S_k, \mathcal{D}_k)$ yields

$$\mathsf{E}\,S_\tau = \mathsf{E}\,S_1 = \mathsf{E}\,\eta_1 = 0.$$

*Second identity.* Consider the process $M_k = S_k^2 - \sum_{i=1}^{k} \mathsf{E}[\eta_i^2 \mid \mathcal{D}_{i-1}]$. If the $\eta_i$ are independent with $\mathsf{E}\,\eta_i = 0$ and $\mathsf{E}\,\eta_i^2 = \sigma_i^2$, then

$$\begin{aligned}
\mathsf{E}[S_{k+1}^2 \mid \mathcal{D}_k] &= \mathsf{E}[(S_k + \eta_{k+1})^2 \mid \mathcal{D}_k] \\
&= S_k^2 + 2S_k\,\mathsf{E}[\eta_{k+1} \mid \mathcal{D}_k] + \mathsf{E}[\eta_{k+1}^2 \mid \mathcal{D}_k] \\
&= S_k^2 + \sigma_{k+1}^2,
\end{aligned}$$

since $\mathsf{E}[\eta_{k+1} \mid \mathcal{D}_k] = \mathsf{E}\,\eta_{k+1} = 0$ by independence. Therefore, if we assume the $\eta_i$ are identically distributed with $\mathsf{E}\,\eta_i^2 = \sigma^2$, the process

$$M_k = S_k^2 - k\sigma^2$$

is a martingale with respect to $(\mathcal{D}_k)$. Applying the optional stopping theorem to $M_k$ gives

$$\mathsf{E}\,M_\tau = \mathsf{E}\,M_1 = \mathsf{E}[S_1^2 - \sigma^2] = \mathsf{E}[\eta_1^2] - \sigma^2 = 0.$$

Thus

$$\mathsf{E}[S_\tau^2 - \tau\sigma^2] = 0 \quad \Longrightarrow \quad \mathsf{E}\,S_\tau^2 = \sigma^2\,\mathsf{E}\,\tau.$$

In the special case considered in Example 1 where $\eta_i = \pm 1$ with equal probability (so $\sigma^2 = 1$), this becomes

$$\mathsf{E}\,S_\tau^2 = \mathsf{E}\,\tau.$$

This completes the proof. $\square$
