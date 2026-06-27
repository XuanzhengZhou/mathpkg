---
role: proof
locale: en
of_concept: smooth-mapping-space-is-frechet-manifold
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

It is easy to check that $C^\infty(X, Y)$ is a Hausdorff space. Let $f \in C^\infty(X, Y)$. We wish to produce an open neighborhood $U_f$ of $f$ which is homeomorphic to an open subset $V_f$ of a Frechet space. We do this via tubular neighborhoods.

Let $X_f = \operatorname{graph}(f) \subset X \times Y$. Since $X_f$ is a submanifold of $X \times Y$, we may apply the tubular neighborhood theorem (II, Theorem 7.2) to find a tubular neighborhood $Z$ of $X_f$ with projection $\pi: Z \to X_f$. Let $V_f$ be an open neighborhood of the zero section in $C^\infty(Z)$, the space of smooth sections of the tubular neighborhood $Z$ viewed as a fiber bundle over $X_f$.

Since $\pi: Z \to X_f$ is smooth, the pushforward $\pi_*: C^\infty(X, Z) \to C^\infty(X, X_f)$ is continuous (II, Proposition 3.5). The inverse image $(\pi_*)^{-1}(\operatorname{Diff}(X, X_f))$ is an open neighborhood of the inclusion $i_f: X \hookrightarrow X_f$ (since $\operatorname{Diff}(X, X_f)$ is open in $C^\infty(X, X_f)$). This neighborhood is homeomorphic to $V_f$ via the exponential map of the tubular neighborhood, establishing the Frechet manifold structure.
