---
role: proof
locale: en
of_concept: well-founded-direct-limit-existence
source_book: gtm001
source_chapter: "17"
source_section: "17.2"
---

Let $I = \{\langle \eta, \alpha, Q \rangle \mid \eta < \mu \wedge \alpha < \kappa \wedge \alpha \leq \eta \wedge Q \text{ is a finite subset of } \eta\}$. For each $i = \langle \eta, \alpha, Q \rangle \in I$, set $\eta_i = \eta$, $\alpha_i = \alpha$, $Q_i = Q$. Define the ordering on $I$ by:

$$i < j \leftrightarrow \eta_i \leq \eta_j \wedge \alpha_i \leq \alpha_j \wedge Q_i \subseteq Q_j \wedge \eta_i \in Q_j,$$
$$i \leq j \leftrightarrow i < j \vee i = j.$$

For each $i \in I$, let $X_i = M^{\eta_i}(\alpha_i \cup Q_i)$ and let $\rho_i: \delta_i \rightarrow X_i$ be the collapsing map. Set $P_i = (\rho_i^{-1})^* Q_i$. When $i \leq j$, define $\pi_{ij} = \rho_j^{-1} \circ \rho_i$. Then $\Pi = \langle \langle \delta_i, \alpha_i, P_i \rangle, \pi_{ij} \rangle_{i,j \in I}$ is a $\kappa$-direct limit system whose limit is $\mu$, and well-foundedness follows from the hypothesis on order types.
