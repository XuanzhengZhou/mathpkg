---
role: proof
locale: en
of_concept: theorem-9-29-k-1-k-2-k-1-k-2-t-1
source_book: gtm008
source_chapter: "5"
source_section: "5 For each formula"
---
If $k_1 \neq k_2$ and $\beta \triangleq \max(\rho(k_1), \rho(k_2))$ then by symmetry we can assume $(\exists k)[k \in k_1 \land k \notin k_2]$.

Then $\rho(k) < \beta$, and

$$[\![k_1 = k_2]\!]_{\mathbf{T}_{\alpha}} = \prod_{t \in T_{\

Case 1. $\beta_3 \leq \beta_1 \wedge \beta_3 \leq \beta_2$. Obvious from Definition 9.27.6.

Case 2. $\beta_1 < \beta_3 \vee \beta_2 < \beta_3$. From Theorem 9.28, 1 is equivalent to:

2. $[t_3 = t_2][t_2 = t_1] \leq [t_3 = t_1]$.

Consequently, if 1 is proved for $\alpha_1 \leq \alpha_3$ then 1 also holds for $\alpha_3 \leq \alpha_1$. Therefore we may assume $\alpha_1 \leq \alpha_3$ and hence $\beta_2 \neq \beta_3$. Thus we need only consider $\beta_1 < \beta_3$. Then $\beta_1 = \max(\alpha_1, \alpha_2) < \beta_2 = \beta_3 = \alpha_3$.

First of all we assume that $t_i$ is defined over $T_\alpha$ for $i = 1, 2, 3$. (That this is really the case will be shown a little later.)

Let $b = [t_1 = t_2][t_2 = t_3]$. Then for $t \in T_{\alpha_3} = T_{\beta_3}$

$$b[t \in t_1] = b \sum_{t' \in T_{\alpha_1}} [t = t'] [t' \in t_1]$$

(since $t_1$ is defined over $T_{\alpha_1}$)

$$= [t_2 = t_3] \sum_{t' \in T_{\alpha_1}} [t_1 = t_2][t = t'] [t' \in t_1]$$

$$= [t_2 = t_3] \sum_{t' \in T_{\alpha}} \prod_{s \in T_{\beta_1}} [s \in t_1 \leftrightarrow s \in t_2][t = t'] [t' \in t_1]$$

$$\leq \sum_{t' \in T_{\alpha_1}} [t_2

Therefore $b \leq [t \in t_1 \leftrightarrow t \in t_3]$ for all $t \in T_{\beta_3}$.

We next wish to show that if $\beta_1 < \beta_3$ then $t_i$ is defined over $T_\alpha$. We first prove that if $\rho(\underline{k}) \leq \rho(t_3)$ then $k$ is defined over $T_{\rho(\underline{k})}$.

$$[t \in \underline{k}] = \sum_{k' \in k} [t = \underline{k'}] [\underline{k'} \in \underline{k}]$$
$$\leq \sum_{t' \in T_{\rho(\underline{k})}} [t = t'] [\underline{t'} \in \underline{k}]$$
(since $k \subseteq T_{\rho(\underline{k})}$)

$$= \sum_{t' \in T_{\rho(\underline{k})}} [t = t'] \sum_{k' \in k} [\underline{t'} = \underline{k'}]$$
$$\leq \sum_{t' \in T_{\rho(\underline{k})}} \sum_{k' \in k} [t = \underline{k'}]$$
(by the induction hypothesis)

$$= \sum_{k' \in k} [t = \underline{k'}] = [t \in \underline{k}]$$.

i.e., $[t \in \underline{k}] = \sum_{t' \in T_{\rho(\underline{k})}} [t = t'] [\underline{t'} \in \underline{k}]$.

Next we show that if $t = \hat{x}^\beta \varphi(x^\beta)$ for some $\beta \leq \alpha_3$ then $t$ is defined over $T_\beta$.

$$[t_0 \in t] = \sum_{t' \in T_\beta} [t_0 = t'] [\varphi(t')]$$
$$\leq \sum_{t' \in T_\beta} [t_0 = t'] \sum_{t' \in T

Proof.

1. $$[t_1 = t_2] [t_2 \in t_3] \leq \sum_{t \in T_\alpha} [t_1 = t_2] [t = t_2] [t \in t_3]$$
$$\leq \sum_{t \in T_\alpha} [t = t_1] [t \in t_3]$$
$$= [t_1 \in t_3]$$  (by Theorem 9.31).

2. $$[t_1 = t_2] [t_3 \in t_1] = [t_1 = t_2] \sum_{t \in T_{\rho(t_1)}} [t = t_3] [t \in t_1]$$
$$= \sum_{t \in T_{\rho(t_1)}} [t = t_3] \prod_{s \in T_{\beta_1}} [s \in t_1 \leftrightarrow s \in t_2] [t \in t_1],$$
where $\beta_1 = \max(\rho(t_1), \rho(t_2))$
$$\leq \sum_{t \in T_{\rho(t_1)}} [t = t_3] [t \in t_2]$$
$$\leq \sum_{t \in T_\alpha} [t = t_3] [t \in t_2],$  (since $\rho(t_1) < \alpha$)
$$= [t_3 \in t_2].$$

3 and 4 follow from Theorem 9.30.

Remark. We have now proved that $T_\alpha$ is a B-valued structure. (See Definition 6.5)
