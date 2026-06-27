---
role: proof
locale: en
of_concept: corollary-11-9-cardinal-preservation-chain-condition
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of V = L and the CH"
---

**Proof.** We first show that $\lambda$ is a cardinal in $M[G]$. Suppose otherwise. Then there exist $f \in M[G]$ and $\lambda_0 < \lambda$ such that $f: \lambda_0 \xrightarrow{\text{onto}} \lambda$.

As in the proof of Theorem 11.8, for each $\alpha < \lambda_0$ let $S_\alpha = \{\beta < \lambda \mid (\exists q \leq p)\,\varphi(q, \alpha, \beta)\}$ where $p \in G$ forces $f$ to be onto. Then

$$\lambda \leq \bigcup_{\alpha < \lambda_0} S_\alpha.$$

Each $S_\alpha$ has size $< \lambda$ by the $\lambda$-chain condition on $P$ (otherwise we would obtain an antichain of size $\geq \lambda$). Since $\lambda_0 < \lambda$ and $\lambda$ is regular in $M$, the union has size $< \lambda$, contradicting $\lambda \leq \bigcup S_\alpha$.

Thus $\lambda$ remains a cardinal in $M[G]$.

Now, using the argument of Theorem 11.8, if $\mu \geq \lambda$ is a cardinal in $M[G]$, then $(\mu^+)^M$ is also a cardinal in $M[G]$; and conversely, any cardinal $\mu \geq \lambda$ in $M$ remains a cardinal in $M[G]$, by the same antichain argument. $\square$
