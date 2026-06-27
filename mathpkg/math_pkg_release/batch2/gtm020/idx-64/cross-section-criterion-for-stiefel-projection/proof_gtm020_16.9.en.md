---
role: proof
locale: en
of_concept: cross-section-criterion-for-stiefel-projection
source_book: gtm020
source_chapter: "16"
source_section: "9"
---

**Proof.** If $s$ is a cross section of $q$, then by (9.3) there exists a map $f : S^{n-1} \to \mathbf{R}P^{n-1}/\mathbf{R}P^{n-\rho(n)-2}$ such that the composition $\theta \circ f : S^{n-1} \to V_{\rho(n)+1}(\mathbf{R}^n)$ is homotopic to $s$. After composing with the projection $q : V_{\rho(n)+1}(\mathbf{R}^n) \to S^{n-1}$, we obtain
\[
q \circ \theta \circ f \simeq q \circ s = \mathrm{id}_{S^{n-1}}.
\]
But $q \circ \theta$ factors through the projection $\pi : \mathbf{R}P^{n-1}/\mathbf{R}P^{n-\rho(n)-2} \to \mathbf{R}P^{n-1}/\mathbf{R}P^{n-2} = S^{n-1}$. Hence $\pi \circ f \simeq \mathrm{id}_{S^{n-1}}$, so $\pi \circ f$ has degree $1$.

Conversely, suppose there exists a map $f : S^{n-1} \to \mathbf{R}P^{n-1}/\mathbf{R}P^{n-\rho(n)-2}$ such that $\pi \circ f$ is homotopic to the identity on $S^{n-1}$. Composing $f$ with $\theta$ yields a map
\[
s' = \theta \circ f : S^{n-1} \to V_{\rho(n)+1}(\mathbf{R}^n)
\]
such that $q \circ s' \simeq \mathrm{id}_{S^{n-1}}$. Since $q$ is a fibre map (it is the projection of a fibre bundle), this homotopy lifts into $V_{\rho(n)+1}(\mathbf{R}^n)$, which defines a genuine cross section of $q$.
