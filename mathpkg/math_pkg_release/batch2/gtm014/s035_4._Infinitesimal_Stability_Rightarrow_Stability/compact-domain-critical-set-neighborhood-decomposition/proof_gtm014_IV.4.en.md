---
role: proof
locale: en
of_concept: compact-domain-critical-set-neighborhood-decomposition
source_book: gtm014
source_chapter: "IV"
source_section: "4"
---

We claim that there exist open sets $U_1, \ldots, U_N$ in $X$; $V_1, \ldots, V_N$ in $Y$; and $\varepsilon > 0$ satisfying:

(a) $f(\Sigma_q) \subset \bigcup_{i=1}^{N} W_i$, where $W_i \subset Y$ are suitable coordinate neighborhoods;

(b) $\overline{W}_i \subset V_i$;

(c) For all $v \in \mathbf{R}^k$ with $|v| < \varepsilon$, the deformation $F$ satisfies appropriate estimates on $U_i \times B_\varepsilon(0)$.

To construct this covering, note that since $f$ is infinitesimally stable, the modules $A_F^{p}$ are finitely generated over $C^\infty_{(q,0)}(Y \times \mathbf{R}^k)$ for each $p \in \Sigma_q$. By Theorem 4.4, for each finite set $S = \Sigma_q \cap U$ contained in a sufficiently small open set $U$, the deformation vector field $\tau_F$ can be expressed as $\tau_F = (dF)(\zeta_S) + F^*\eta_S$ with $\zeta_S, \eta_S$ having zero $\mathbf{R}^k$-components on a neighborhood of $S \times \{0\}$.

The compactness of $X$ implies that $\Sigma$ is compact (each $\Sigma_q$ is finite by Lemma 1.8, and $f$ is proper since $X$ is compact). Choose a finite subcover $\{U_i \times V_i\}_{i=1}^{N}$ of $\Sigma \times \{0\}$ in $X \times Y$ such that on each $U_i$, the deformation $F$ restricts to a situation where Theorem 4.4 applies to the finite set $S_i = \Sigma \cap U_i$.

On each $U_i \times B_\varepsilon(0)$, we obtain vector fields $\zeta_i$ on $U_i \times \mathbf{R}^k$ and $\eta_i$ on $V_i \times \mathbf{R}^k$ with vanishing $\mathbf{R}^k$-components satisfying $\tau_F = (dF)(\zeta_i) + F^*\eta_i$. Using a partition of unity subordinate to the cover $\{U_i\}$, these local vector fields are patched together to produce global vector fields $\zeta$ on $X \times \mathbf{R}^k$ and $\eta$ on $Y \times \mathbf{R}^k$.

Setting $B = \bigcup_{i=1}^{N} (U_i \times B_\varepsilon(0))$, which is an open neighborhood of $\Sigma \times \{0\}$ in $X \times \mathbf{R}^k$, the patched vector fields satisfy $\tau_F = (dF)(\zeta) + F^*\eta$ on $B$, with the $\mathbf{R}^k$-components of $\zeta$ and $\eta$ vanishing on $B$ by construction.
