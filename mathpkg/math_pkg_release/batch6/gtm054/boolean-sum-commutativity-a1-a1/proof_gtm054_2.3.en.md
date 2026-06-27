---
role: proof
locale: en
of_concept: boolean-sum-commutativity-a1-a1
source_book: gtm054
source_chapter: "2"
source_section: "IIA"
---

Clearly $\varnothing \in \mathcal{E}(U)$. If $U = \varnothing$, then $\mathcal{E}(U) = \{\varnothing\} = \mathcal{P}(U)$. We suppose $U \neq \varnothing$.

By IC5, if $S, T \in \mathcal{E}(U)$, then $S + T \in \mathcal{E}(U)$; also $0S = \varnothing$ and $1S = S$ belong to $\mathcal{E}(U)$. Since $\mathcal{E}(U)$ is closed with respect to $+$ and scalar multiplication, $\mathcal{E}(U)$ is a subspace of $\mathcal{P}(U)$.

Select $x_0 \in U$. One can easily verify that if $\mathcal{B} = \{\{x_0, x\}: x \in U + \{x_0\}\}$, then $\mathcal{B}$ is independent and $|\mathcal{B}| = |U| - 1$. Hence $\dim(\mathcal{E}(U)) \geq |U| - 1$. However, since $U \neq \varnothing$, $\mathcal{E}(U) \neq \mathcal{P}(U)$, so $\dim(\mathcal{E}(U)) < \dim(\mathcal{P}(U)) = |U|$.

The following corollary offers a different approach to Exercise IC23.
