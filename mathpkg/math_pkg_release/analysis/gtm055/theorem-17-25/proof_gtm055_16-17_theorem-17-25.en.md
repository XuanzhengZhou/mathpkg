---
role: proof
locale: en
of_concept: theorem-17-25
source_book: gtm055
source_chapter: "16-17"
source_section: "Section 18_Section_18"
---

Proof. Let $\gamma$ be a fixed oriented envelope of $\sigma_{\mathcal{A}}(x_0)$ in $U$, let $W_\gamma$ denote the range of $\gamma$, and let $V = \{\lambda \in U : w_\gamma(\lambda) = 1\}$. Then $V$ is an open neighborhood of $\sigma_{\mathcal{A}}(x_0)$ so, by Proposition 12.14, $\sigma_{\mathcal{A}}(x_n) \subset V$ for all sufficiently large $n$, and $f_n(x_n)$ is defined for all such positive integers $n$ (since $\gamma$ is also an oriented envelope of $\sigma_{\mathcal{A}}(x_n)$ in $U$). Moreover, the (continuous) function $\|R_{x_0}(\lambda)\|$ is bounded on $W_\gamma$, whence it follows (Prob. 12K) that for each positive number $\varepsilon$ there exists a positive $\delta$ such that if $\|y - (\lambda - x_0)\| < \delta$ with $\lambda$ in $W_\gamma$, then $\|y^{-1} - R_{x_0}(\lambda)\| < \varepsilon$. If $n_0$ is chosen so that $\|x_n - x_0\| < \delta$ for $n > n_0$, then $\|(\lambda - x_n) - (\lambda - x_0)\| = \|x_n - x_0\| < \delta$ for all $\lambda$, and therefore $\|R_{x_n}(\lambda) - R_{x_0}(\lambda)\| < \varepsilon$ uniformly on $W_\gamma$. Hence the sequence $\{f_nR_{x_n}\}$ converges uniformly to $f_0R_{x_0}$ on $W_\gamma$, and therefore

$$f_0

which $f \circ g$ is defined and locally analytic, so $(f \circ g)(x)$ is also defined. Finally, to establish the desired equality, we first choose an oriented envelope $\gamma_1$ of $g(\sigma_{\mathcal{A}}(x))$ in $\tilde{U}$, and denote by $V$ the (open) set $\{\lambda \in \tilde{U}: w_{\gamma_1}(\lambda) = 1\}$. Next we choose an oriented envelope $\gamma_2$ of $\sigma_{\mathcal{A}}(x)$ in the open set $\{\lambda \in U: g(\lambda) \in V\}$. Then $\sigma_{\mathcal{A}}(g(x))$ and the range of $\gamma_1$ are disjoint, so

$$f(g(x)) = \frac{1}{2\pi i} \int_{\gamma_1} f(\zeta) R_{g(x)}(\zeta) d\zeta$$

$$= \frac{1}{2\pi i} \int_{\gamma_1} \left[ f(\zeta) \frac{1}{2\pi i} \int_{\gamma_2} \frac{R_x(\lambda)}{\zeta - g(\lambda)} d\lambda \right] d\zeta$$

$$= \frac{1}{2\pi i} \int_{\gamma_2} \left[ \frac{1}{2\pi i} \int_{\gamma_1} \frac{f(\zeta)}{\zeta - g(\lambda)} d\lambda \right] R_x(\lambda) d\lambda$$

$$= \frac{1}{2\pi i} w_{\gamma_1}(g(\lambda)) f(g(\lambda)) R_x(\lambda) d\lambda$$

$$= (f \circ g)(x)$$

since $w_{\gamma_1}(g(\lambda)) = 1$ for all $\lambda$ in the range of $\gamma_2$. (The interchange of the order of integration is justified in Problem R.)

The Riesz–Dunford functional calculus had its origin in the study of the algebra $\mathbb{C}_{n,n}$ of complex matrices, and was pursued further by Riesz, Dunford, and others, principally as a tool in the study

$(S(\mathcal{M}) \subset \mathcal{M})$, a fact expressed by saying that $\mathcal{M}$ is invariant under $S$, or is an invariant subspace of $S$. Thus $\mathcal{M}$ is invariant under every bounded operator on $\mathcal{E}$ that commutes with $T$, a fact expressed by saying that $\mathcal{M}$ is hyperinvariant for $T$, or is a hyperinvariant subspace of $T$. Similarly, of course, the subspace $\mathcal{N}$ is hyperinvariant for $T$. Thus, for example, if $S$ is any analytic function of $T$, then $\mathcal{M}$ and $\mathcal{N}$ are both invariant under $S$. In particular, $\mathcal{M}$ and $\mathcal{N}$ are invariant under $T$ itself, and we may and do define operators $A$ and $B$ in $\mathcal{L}(\mathcal{M})$ and $\mathcal{L}(\mathcal{N})$, respectively, by setting

$$A = T | \mathcal{M} \quad \text{and} \quad B = T | \mathcal{N}.$$

(Thus $T(y + z) = Ay + Bz$ for all $y$ in $\mathcal{M}$ and $z$ in $\mathcal{N}$.)

Suppose now that $\alpha$ is a complex number such that $\alpha \notin \sigma(A) \cup \sigma(B)$. Then setting

$$S(y + z) = (\alpha - A)^{-1}y + (\alpha - B)^{-1}z, \quad y \in \mathcal{M}, \quad z \in \mathcal{N},$$

defines a bounded operator on $\mathcal{E}$ (indeed,

$$\| S(y + z) \| \leq \| (\alpha - A)^{-1} \| \| y \| + \| (\alpha - B)^{-1} \| \| z \|,$$

so

$$\| S \| \leq \| (\alpha - A)^{-1} \| \| P \| + \| (\alpha - B)^{-1} \| \| 1 - P \|,$$

and it is obvious that $S = (\alpha - T)^{-1}$. Thus

$$
