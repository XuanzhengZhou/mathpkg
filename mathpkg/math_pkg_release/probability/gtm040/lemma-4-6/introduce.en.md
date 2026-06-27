---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $\{x_n\}$ be a Markov chain with starting distribution $\pi$, let $q$ be a statement relative to $\mathcal{F}_{n-1}$, let $r$ be a statement relative to $\mathcal{T}_{n+1} \cap \mathcal{F}$, and suppose $\Pr_{\pi}[q \wedge x_n = i] >

Case 2: $r$ is of the form $x_{n+1} = c_{n+1} \wedge \cdots \wedge x_m = c_m$, $m > n$. We have

$$\Pr_{\pi}[r \mid q \wedge x_n = i]$$

$$= \Pr_{\pi}[x_{n+1} = c_{n+1} \mid q \wedge x_n = i]$$

$$\times \Pr_{\pi}[x_{n+2} = c_{n+2} \mid q \wedge x_n = i \wedge x_{n+1} = c_{n+1}]$$

$$\times \cdots \times \Pr_{\pi}[x_m = c_m \mid q \wedge x_n = i \wedge \cdots \wedge x_{m-1} = c_{m-1}]$$

The general factor on the right is

$$\Pr_{\pi}[x_{n+k+1} = c_{n+k+1} \mid q \wedge x_n = i \wedge \cdots \wedge x_{n+k} = c_{n+k}]$$

First, suppose that none of these factors is zero. Then we may apply Case 1 with $n + k$ in place of $n$ and $q \wedge x_n = i \wedge \cdots \wedge x_{n+k-1} = c_{n+k-1}$ in place of $q$. The $q$'s drop out of the conditions, and the product of the new conditional probabilities is $\Pr_{\pi}[r \mid x_n = i]$.

Next, suppose that at least one of the factors is zero; let the first such factor from the left be

$$\Pr_{\pi}[x_{n+k+1} = c_{n+k+1} \mid q \wedge x_n = i \wedge \cdots \wedge x_{n+k} = c_{n+k}]$$

We must show that $\Pr_{\pi}[r \mid x_n = i] = 0$. If $k = 0$, then by Case 1

$$0 = \Pr_{\pi}[x_{n+1} = c_{n+1} \

Lemma 4-7: Let $\{x_n\}$ be a Markov chain with starting distribution $\pi$, let $q$ be a statement relative to $\mathcal{F}_n$, let $r$ be a statement relative to $\mathcal{T}_n$, and suppose $\Pr_\pi[q \wedge x_n = i] > 0$. Then

$$\Pr_\pi[r \mid q \wedge x_n = i] = \Pr_\pi[r \mid x_n = i] = \Pr_i[r']$$

where $\omega \in R$ if and only if $\omega_n \in R'$.
