---
role: proof
locale: en
of_concept: proposition-10-14
source_book: gtm055
source_chapter: "10-11"
source_section: "Section 12_Section_12"
---

Proof. If $\mu$ is a signed Borel measure on $X$, and if $K$ is a compact subset of $X$, then both $\mu_+(K)$ and $\mu_-(K)$ must be finite, since $\mu(K) = \mu_+(K) - \mu_-(K)$ is. But then $|\mu|(K) = \mu_+(K) + \mu_-(K) < +\infty$ (Prob. 8U). Hence $\mu_+$, $\mu_-$ and $|\mu|$ are Borel measures on $X$. If $\xi$ is a complex Borel measure on $X$, then $v_1 = \text{Re} \xi$ and $v_2 = \text{Im} \xi$ are clearly signed Borel measures such that both $v_1(X)$ and $v_2(X)$ are finite (since $\xi(X) = v_1(X

converges uniformly on $X \setminus Z$ to the sum $1/(\varphi(x) - \lambda)$ for each $\lambda$ in $D_r(\lambda_0)$, and we may therefore integrate the series (3) term by term, thus obtaining the power series expansion

$$\int_X \frac{d\xi(x)}{\varphi(x) - \lambda} = \sum_{n=0}^{\infty} \alpha_n(\lambda - \lambda_0)^n$$

on $D_r(\lambda_0)$, where $\alpha_n = \int_X d\xi(x)/(\varphi(x) - \lambda_0)^{n+1}$, $n \in \mathbb{N}_0$.

In particular, if $\xi$ is a complex Borel measure on $\mathbb{C}$ itself, then

$$h(\lambda) = \int_{\mathbb{C}} \frac{d\xi(\zeta)}{\zeta - \lambda}$$

is a locally analytic function on the complement $U$ of the support of $\xi$ (see Problem P). The function $h$ is usually called the Cauchy transform of the measure $\xi$.
