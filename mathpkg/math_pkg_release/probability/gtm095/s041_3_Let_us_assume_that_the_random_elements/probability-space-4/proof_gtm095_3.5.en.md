---
role: proof
locale: en
of_concept: probability-space-4
source_book: gtm095
source_chapter: "3"
source_section: "5"
---

# Proof of Corollary (Lévy–Prokhorov Upper Bound via Coupling)

Let $X$ and $\tilde{X}$ be random elements defined on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with values in a separable metric space $(E, \mathcal{E}, \rho)$. Let $P_X$ and $P_{\tilde{X}}$ be their probability distributions. Then

$$L(P_X, P_{\tilde{X}}) \leq d_{\mathbb{P}}(X, \tilde{X}),$$

where $L$ is the Lévy–Prokhorov metric and

$$d_{\mathbb{P}}(X, \tilde{X}) = \inf\{\varepsilon > 0 : \mathbb{P}(\rho(X, \tilde{X}) \geq \varepsilon) \leq \varepsilon\}$$

is the Ky Fan distance (distance in probability).

*Proof.* This follows directly from Theorem 4 (the coupling bound). By definition of the Lévy–Prokhorov metric,

$$L(P_X, P_{\tilde{X}}) = \inf\{\varepsilon > 0 : P_X(F) \leq P_{\tilde{X}}(F^\varepsilon) + \varepsilon \text{ for all closed } F \subset E\},$$

where $F^\varepsilon = \{x \in E : \rho(x, F) < \varepsilon\}$ is the $\varepsilon$-neighborhood of $F$.

Theorem 4 states that for any coupling $(X, \tilde{X})$ on a common probability space with marginal distributions $P_X$ and $P_{\tilde{X}}$,

$$L(P_X, P_{\tilde{X}}) \leq \inf\{\varepsilon > 0 : \mathbb{P}(\rho(X, \tilde{X}) \geq \varepsilon) \leq \varepsilon\} = d_{\mathbb{P}}(X, \tilde{X}).$$

The crux of the proof is the elementary set inclusion: for any closed $F \subset E$ and any $\varepsilon > 0$,

$$\{X \in F\} \subseteq \{\tilde{X} \in F^\varepsilon\} \cup \{\rho(X, \tilde{X}) \geq \varepsilon\}.$$

Taking probabilities yields

$$P_X(F) = \mathbb{P}(X \in F) \leq \mathbb{P}(\tilde{X} \in F^\varepsilon) + \mathbb{P}(\rho(X, \tilde{X}) \geq \varepsilon) = P_{\tilde{X}}(F^\varepsilon) + \mathbb{P}(\rho(X, \tilde{X}) \geq \varepsilon).$$

If $\mathbb{P}(\rho(X, \tilde{X}) \geq \varepsilon) \leq \varepsilon$, then $P_X(F) \leq P_{\tilde{X}}(F^\varepsilon) + \varepsilon$ for every closed $F$, which by definition implies $L(P_X, P_{\tilde{X}}) \leq \varepsilon$. Taking the infimum over all such $\varepsilon$ completes the proof.

$\square$

**Remark.** The preceding proof shows that the bound is valid whenever we can exhibit, on any probability space $(\Omega^*, \mathcal{F}^*, \mathbb{P}^*)$, random elements $X$ and $\tilde{X}$ with values in $E$ whose distributions coincide with $P$ and $\tilde{P}$. The procedure of constructing $\Omega^*, \mathcal{F}^*, \mathbb{P}^*$ and $X, \tilde{X}$ for given $P, \tilde{P}$ is called *coupling*. The trivial choice of the product measure $\mathbb{P}^* = P \otimes \tilde{P}$ generally does not yield a good estimate, which motivates the search for optimal couplings. In fact, there exist couplings attaining equality: $L(P, \tilde{P}) = \inf d_{\mathbb{P}^*}(X, \tilde{X})$, where the infimum is over all couplings.
