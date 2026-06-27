---
role: proof
locale: en
of_concept: global-infinitesimal-stability-multijet-criterion
source_book: gtm014
source_chapter: "V"
source_section: "§1"
---

**Proof of Theorem 1.6.**

*Necessity.* If $f$ is infinitesimally stable then condition $(\dagger)$ follows directly from the definition, as any global solution $\tau = (df)(\zeta) + f^*\eta$ restricts to a simultaneous solution at any finite set $S \subset f^{-1}(q)$, and passage to $m$-jets yields the stated equality.

*Sufficiency.* Assume $f$ satisfies $(\dagger)$. Let $\Sigma$ be the set of critical points of $f$ in $X$ (points where $(df)_p$ is not surjective), and let $\Sigma_q = \Sigma \cap f^{-1}(q)$. By Lemma 1.9, $|\Sigma_q| \leq m$ for each $q$. In particular, $\Sigma_q$ is a finite set with at most $m$ points.

Let $\tau$ be a vector field along $f$, i.e., $\tau \in C^\infty(f^*TY)$. We must produce $\zeta \in C^\infty(TX)$ and $\eta \in C^\infty(TY)$ such that $\tau = (df)(\zeta) + f^*\eta$.

**Step 1: Near the critical set.** For each $q \in f(\Sigma)$, the set $S = \Sigma_q$ has $|S| \leq m \leq m+1$, so condition $(\dagger)$ together with Proposition 1.5 implies that $f$ is simultaneously locally infinitesimally stable at the points of $S$. Thus, for each $q \in f(\Sigma)$, there exist a neighborhood $W_q$ of $q$ in $Y$, neighborhoods $U_p$ of each $p \in \Sigma_q$ in $X$ (with $\overline{U}_p$ pairwise disjoint), a vector field $\zeta_q$ defined on $\bigcup_{p \in \Sigma_q} U_p$, and a vector field $\eta_q$ defined on $W_q$ such that
\[
\tau = (df)(\zeta_q) + f^*\eta_q \quad \text{on } \bigcup_{p \in \Sigma_q} U_p.
\]

Cover $\Sigma$ by finitely many such neighborhoods (possible since $X$ is compact, hence $\Sigma$ is compact). Let $\{W_i\}_{i=1}^{N}$ be the corresponding finite cover of $f(\Sigma)$ and $\{U_i\}_{i=1}^{N}$ the corresponding open sets in $X$ with $f^{-1}(\overline{W}_i) \cap \Sigma \subset U_i$. Let $\{\rho_i\}$ be a partition of unity on $Y$ subordinate to $\{W_i\}$ and set $\eta = \sum_{i=1}^{N} \rho_i \eta_i$. Choose $\zeta$ on a neighborhood of $\Sigma$ extending the local $\zeta_i$ appropriately using a partition of unity on $X$. Then we obtain
\[
\tau = (df)(\zeta) + f^*\eta \quad \text{on a neighborhood of } \Sigma.
\]

Thus we may assume, by subtracting $(df)(\zeta) + f^*\eta$ from $\tau$, that $\tau \equiv 0$ on a neighborhood $U$ of $\Sigma$ in $X$.

**Step 2: Off the critical set.** If $\dim X < \dim Y$, then $\Sigma = X$ and we are finished. In the case $\dim X \geq \dim Y$, the map $f$ is a submersion on $X \setminus \Sigma$. By III, Proposition 2.1, all submersions are infinitesimally stable (the proof given there does not use compactness of $X$). Hence there exists a vector field $\zeta$ on $X \setminus \Sigma$ such that $(df)(\zeta) = \tau$ there.

Choose a smooth function $\rho: X \to \mathbf{R}$ which is $0$ on a neighborhood of $\Sigma$ and $1$ off $U$. Then $\rho\zeta$ extends to a globally defined smooth vector field on $X$, and
\[
(df)(\rho\zeta) = \rho \cdot (df)(\zeta) = \rho \cdot \tau = \tau
\]
since $\operatorname{supp} \tau \subset X \setminus U$. Thus we have constructed the required $\zeta$ (and $\eta \equiv 0$ in this region), completing the proof. $\square$
