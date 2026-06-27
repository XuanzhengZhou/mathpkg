---
role: proof
locale: en
of_concept: existence-and-uniqueness-of-lie-parallel-vector-fields
source_book: gtm048
source_chapter: "2"
source_section: "2.0.1"
---

Given $e \in \mathcal{E}$ and $W \in T_{\gamma e} M$, define $W(u) := (\mu_{u-e})_* W$ for all $u \in \mathcal{E}$. By the group property of the flow $\mu$, we have $\mu_{u+s-e} = \mu_s \circ \mu_{u-e}$, hence
$$W(u + s) = (\mu_{u+s-e})_* W = (\mu_s)_* (\mu_{u-e})_* W = (\mu_s)_* W(u),$$
so $W$ is Lie parallel and satisfies $W(e) = (\mu_0)_* W = W$.

For uniqueness, suppose $\tilde{W}$ is another Lie parallel vector field over $\gamma$ with $\tilde{W}(e) = W$. Then for any $u \in \mathcal{E}$, taking $s = u - e$ in the definition,
$$\tilde{W}(u) = \tilde{W}(e + (u-e)) = (\mu_{u-e})_* \tilde{W}(e) = (\mu_{u-e})_* W = W(u).$$
Thus $\tilde{W} = W$. This argument follows Bishop--Goldberg 5.8.1.
