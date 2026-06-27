---
role: proof
locale: en
of_concept: cech-cohomology-vanishing-flabby
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---
We proceed by induction on $\ell$: Let $\xi \in Z^{\ell}(\mathfrak{U}, \mathcal{S})$, $\ell \geqslant 1$. If $U \subset X$ is open, then we set $U \cap \mathfrak{U} := \{U \cap U_{\iota} \neq \emptyset : U_{\iota} \in \mathfrak{U}\}$ and
$$(\xi | U)(\iota_0, \ldots, \iota_{\ell}) := \xi(\iota_0, \ldots, \iota_{\ell}) | U \cap U_{\iota_0 \ldots \iota_{\ell}}.$$
With this notation we have $\xi | U \in Z^{\ell}(U \cap \mathfrak{U}, \mathcal{S})$.

For arbitrary $x_0 \in X$, there is an $\iota_0 \in I$ and an open neighborhood $U(x_0) \subset U_{\iota_0}$. But then $U \in U \cap \mathfrak{U}$, so $H^{\ell}(U \cap \mathfrak{U}, \mathcal{S}) = 0$ for $\ell \geqslant 1$, and there is an $\eta \in C^{\ell-1}(U \cap \mathfrak{U}, \mathcal{S})$ with $\delta \eta = \xi | U$.

If $V \subset X$ is an open set for which there is an $\eta' \in C^{\ell-1}(V \cap \mathfrak{U}, \mathcal{S})$ with $\delta \eta' = \xi | V$, we set
$$s := (\eta - \eta') | U \cap V \in Z^{\ell-1}(U \cap V \cap \mathfrak{U}, \mathcal{S}).$$

If $\ell = 1$, then $s$ lies in $\Gamma(U \cap V, \mathcal{S})$, and since $\mathcal{S}$ is flabby, we can extend $s$ to an $\hat{s} \in \Gamma(V, \mathcal{S})$. Then set
$$s^*(x) := \begin{cases} \eta(x) & \text{for } x \in U \\ (\eta' + \hat{s})(x) & \text{for } x \in V \end{cases}$$
which gives an $\eta^* \in C^{\ell-1}((U \cup V) \cap \mathfrak{U}, \mathcal{S})$ with $\delta \eta^* = \xi | (U \cup V)$.

If $\ell > 1$, then by the induction hypothesis $H^{\ell-1}((U \cap V) \cap \mathfrak{U}, \mathcal{S}) = 0$, so there is a $t \in C^{\ell-2}((U \cap V) \cap \mathfrak{U}, \mathcal{S})$ with $\delta t = s$. Extend $t$ using flabbiness of $\mathcal{S}$ to glue $\eta$ and $\eta'$ similarly.

By Zorn's lemma, we obtain a global trivialization, showing $Z^{\ell}(\mathfrak{U}, \mathcal{S}) = B^{\ell}(\mathfrak{U}, \mathcal{S})$ for $\ell \geqslant 1$, hence $H^{\ell}(\mathfrak{U}, \mathcal{S}) = 0$.
