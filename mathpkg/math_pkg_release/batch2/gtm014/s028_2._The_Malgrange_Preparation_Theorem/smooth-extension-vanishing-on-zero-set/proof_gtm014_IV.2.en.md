---
role: proof
locale: en
of_concept: smooth-extension-vanishing-on-zero-set
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

The proof proceeds by induction on $k$.

**Base case $k = 0$:** $P_0(z) \equiv 1$, so we only need a smooth extension $\tilde{G}(z, x)$ such that $\tilde{G}(t, x) = G(t, x)$ for real $t$ and $\partial \tilde{G}/\partial \bar{z}$ vanishes to infinite order for real $t$. Writing $z = s + it$, we have
$$i \frac{\partial}{\partial \bar{z}} = \frac{\partial}{\partial t} + i \frac{\partial}{\partial s}.$$
The existence follows from Lemma 2.7 by taking $X = -i(\partial/\partial s)$, since we need to solve $\partial \tilde{G}/\partial \bar{z} = 0$ to infinite order on $\{t = 0\}$.

**Inductive step:** Assume the result for $k - 1$. We construct smooth functions $E(z, x, \lambda)$ and $F(z, x, \lambda)$ satisfying:
- (i) $E$ and $F$ agree to infinite order on $\{P_k(z, \lambda) = 0\}$,
- (ii) $F$ is an extension of $G$.

Introduce coordinates $(z, x, u, \lambda')$ where $u = P_k(z, \lambda)$. In these coordinates, $\partial/\partial \bar{z}$ becomes $\partial/\partial \bar{z} + (\overline{\partial P_k/\partial z})(\partial/\partial \bar{u})$. The problem reduces to finding $E$ such that:
- (a) $E = F$ to infinite order on $\{u = 0\}$,
- (b) $(\partial/\partial \bar{z} + (\overline{\partial P_k/\partial z})(\partial/\partial \bar{u}))E = 0$ to infinite order on $\{u = 0\}$.

Let $X = -(\overline{\partial P_k/\partial z})^{-1}(\partial/\partial \bar{z})$. (The zeroes of $\partial P_k/\partial z$ are handled separately using the induction hypothesis.) The problem becomes: find smooth $E$ satisfying (a) and
$$\partial E/\partial \bar{z} = XE \quad \text{to infinite order on } \{u = 0\}.$$

This admits a formal solution analogous to Lemma 2.7:
$$E = \sum_{l=0}^{\infty} \frac{(\bar{u})^l}{l!} \rho(\mu_l |\bar{u}|^2) X^l M(z, x, \lambda)$$
where $M$ is obtained from $F$ via the inductive hypothesis and satisfies $\partial M/\partial \bar{z} = 0$ to infinite order on $\{\partial P_k/\partial z = 0\}$. This guarantees $X^l M$ is smooth for all $l$. Choosing $\mu_l \to \infty$ sufficiently rapidly makes the RHS a smooth function of $(z, x, u, \lambda)$, completing the induction.
