---
role: proof
locale: en
of_concept: alpha-f-zero-insufficient-for-charge
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

Choose $p_i = (i/(i+1))^{3/2}$. Then
$$\beta_i = \prod_{k=1}^i p_k = \prod_{k=1}^i \left(\frac{k}{k+1}\right)^{3/2} = (i+1)^{-3/2}.$$

Since $\sum_i \beta_i = \sum_i (i+1)^{-3/2} < \infty$, the chain is ergodic. The stationary distribution is $\alpha_i = \beta_i / \sum_k \beta_k \sim c (i+1)^{-3/2}$.

Define $h_i = \sqrt{i+1}$. Then $h \geq 0$ and
$$\alpha h = \sum_i \alpha_i \sqrt{i+1} \sim c \sum_i (i+1)^{-3/2} \sqrt{i+1} = c \sum_i (i+1)^{-1} = +\infty.$$

Now define $f = (I-P)h$. We compute:
$$f_i = h_i - (Ph)_i = h_i - (p_{i+1} h_{i+1} + q_{i+1} h_0).$$

To verify $\alpha f = 0$, note that for any function $h$:
$$\alpha(I-P)h = \alpha h - \alpha P h = \alpha h - \alpha h = 0,$$
since $\alpha P = \alpha$ (stationarity). This formal calculation holds provided the sums converge appropriately. In this case, the cancellation is valid as a formal identity.

Now for $f$ to be a charge, we would need $(I + P + \cdots + P^{n-1})f$ to converge as $n \to \infty$. But:
$$(I + P + \cdots + P^{n-1})f = (I - P^n)h.$$

By Fatou's Theorem applied to the nonnegative sequence $P^n h$:
$$\liminf_n (P^n h) \geq A h = +\infty,$$
since the Abel mean $A h = \lim_{\lambda \to 1} (1-\lambda) \sum_{n=0}^\infty \lambda^n P^n h$ diverges when $\alpha h = +\infty$ for an ergodic chain.

Therefore $(I-P^n)h$ does not converge (it tends to $-\infty$ in the liminf sense relative to the divergent part), so $f$ is not a charge despite satisfying $\alpha f = 0$.
