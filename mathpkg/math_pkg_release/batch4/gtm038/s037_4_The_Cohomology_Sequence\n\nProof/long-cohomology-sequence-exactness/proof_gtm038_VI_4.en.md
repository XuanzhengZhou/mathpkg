---
role: proof
locale: en
of_concept: long-cohomology-sequence-exactness
source_book: gtm038
source_chapter: "VI. Cohomology Theory"
source_section: "4. The Cohomology Sequence"
---

**Proof.**

a. The sequence

$$0 \to \Gamma(X, \mathcal{S}^*) \xrightarrow{\varphi_*} \Gamma(X, \mathcal{S}) \xrightarrow{\psi_*} \Gamma(X, \mathcal{S}^{**})$$

is exact, since $\Gamma$ is a left exact functor (Theorem 1.7).

b. The cohomology sequence is exact at $H^i(X, \mathcal{S}^*)$, $i \geqslant 1$:

1. $\bar{\varphi} \circ \partial = 0$ by Theorem 4.3.
2. If $\xi \in Z^i(X, \mathcal{S}^*)$ and

$$0 = \bar{\varphi} \circ q_i^*(\xi) = q_i \circ (W_i\varphi)_*(\xi^*)$$

for a representative $\xi^* \in Z^i(X, \mathcal{S}^*)$, then there exists an $\eta_0 \in \Gamma(X, \mathcal{S}_{i-1})$ with $d\eta_0 = (W_i\varphi)_*(\xi^*)$.

Set $\xi_0 := (W_i\psi)_*(\eta_0)$. Then

$$d\xi_0 = d \circ (W_i\psi)_*(\eta_0) = (W_{i+1}\psi)_* \circ d(\eta_0) = (W_{i+1}\psi)_* \circ (W_i\varphi)_*(\xi^*) = (W_{i+1}(\psi \circ \varphi))_*(\xi^*) = 0.$$

Therefore $\xi_0 \in Z^i(X, \mathcal{S}^{**})$ and

$$\bar{\psi} \circ q_i(\eta_0) = q_i^{**} \circ (W_i\psi)_*(\eta_0) = q_i^{**}(\xi_0).$$

Thus $\partial(q_i^{**}\xi_0) = q_i^*(\xi)$.

c. The cohomology sequence is exact at $H^i(X, \mathcal{S})$, $i \geqslant 1$:

1. $\bar{\psi} \circ \bar{\varphi} = 0$ by Theorem 4.3.
2. If $\xi \in Z^i(X, \mathcal{S})$ and $\bar{\psi} \circ q_i(\xi) = 0$, then $q_i^{**} \circ (W_i\psi)_*(\xi) = 0$. Hence there exists $\eta_0 \in \Gamma(X, \mathcal{S}_{i-1}^{**})$ with $d\eta_0 = (W_i\psi)_*(\xi)$.

Since the canonical resolution $\mathfrak{W}(\mathcal{S})$ is exact and $\mathfrak{W}(\mathcal{S}^{**})$ is exact, and since $(W_{i-1}\psi)_*$ is surjective (by the properties of the canonical resolution), there exists $\eta \in \Gamma(X, \mathcal{S}_{i-1})$ with $(W_{i-1}\psi)_*(\eta) = \eta_0$.

Then

$$(W_i\psi)_*(\xi - d\eta) = (W_i\psi)_*(\xi) - (W_i\psi)_* \circ d(\eta) = d\eta_0 - d \circ (W_{i-1}\psi)_*(\eta) = d\eta_0 - d\eta_0 = 0.$$

Since the sequence $O \to \mathfrak{W}(\mathcal{S}^*) \to \mathfrak{W}(\mathcal{S}) \to \mathfrak{W}(\mathcal{S}^{**}) \to O$ is exact (Theorem 1.6), there exists $\sigma \in \Gamma(X, \mathcal{S}_i^*)$ with $(W_i\varphi)_*(\sigma) = \xi - d\eta$.

Then $d\sigma = d(\xi - d\eta) = 0$ since $d\xi = 0$ and $dd\eta = 0$. Therefore $\sigma \in Z^i(X, \mathcal{S}^*)$ and

$$\bar{\varphi} \circ q_i^*(\sigma) = q_i \circ (W_i\varphi)_*(\sigma) = q_i(\xi - d\eta) = q_i(\xi).$$

d. The cohomology sequence is exact at $H^i(X, \mathcal{S}^{**})$, $i \geqslant 1$:

1. $\partial \circ \bar{\psi} = 0$ by Theorem 4.3.
2. If $\xi^{**} \in Z^i(X, \mathcal{S}^{**})$ and $\partial(q_i^{**}\xi^{**}) = 0$, then by definition of $\partial$, there exists $\eta \in \Gamma(X, \mathcal{S}_{i-1}^{**})$ and $\xi \in Z^i(X, \mathcal{S})$ with $(W_i\psi)_*(\xi) = \eta_0$ (where $d\eta_0 = \xi^{**}$ in the appropriate sense).

More precisely, from $\partial(q_i^{**}\xi^{**}) = 0$ we obtain the existence of $\eta_0 \in \Gamma(X, \mathcal{S}_{i-1})$ with $d\eta_0 = (W_i\varphi)_*(\sigma)$ for some $\sigma$, and the surjectivity of $(W_{i-1}\psi)_*$ gives $\eta \in \Gamma(X, \mathcal{S}_{i-1}^{**})$ with $(W_{i-1}\psi)_*(\eta_0) = \eta$.

Then $\eta = d\sigma$, and

$$d(\eta_0 - (W_i\varphi)_*\sigma) = 0, \quad (W_i\psi)_*(\eta_0 - (W_i\varphi)_*\sigma) = \xi;$$

therefore

$$\bar{\psi} \circ q_i(\eta_0 - (W_i\varphi)_*\sigma) = q_i^{**} \circ (W_i\psi)_*(\eta_0 - (W_i\varphi)_*\sigma) = q_i^{**}\xi.$$

Hence $\operatorname{Ker} \partial \subset \operatorname{Im} \bar{\psi}$, and the proof is complete.
