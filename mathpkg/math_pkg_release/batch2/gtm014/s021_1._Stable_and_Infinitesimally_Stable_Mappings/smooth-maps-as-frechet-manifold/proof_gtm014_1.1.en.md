---
role: proof
locale: en
of_concept: smooth-maps-as-frechet-manifold
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

**Proof.** It is easy to check that $C^\infty(X, Y)$ is a Hausdorff space. Let $f \in C^\infty(X, Y)$. We wish to produce an open neighborhood $U_f$ of $f$ which is homeomorphic to an open subset $V_f$ of a Fr\'{e}chet space. We do this via a tubular neighborhood.

Let $X_f = \operatorname{graph}(f) \subset X \times Y$. $X_f$ is a submanifold of $X \times Y$, so we may apply the tubular neighborhood theorem (II, 7.2) to find a tubular neighborhood $Z$ of $X_f$ with projection $\pi: Z \to X_f$. Then $V_f$ will be an open neighborhood of the zero section in $C^\infty(Z)$, the space of smooth sections of the normal bundle.

Since $\pi: Z \to X_f$ is smooth, the induced map $\pi_*: C^\infty(X, Z) \to C^\infty(X, X_f)$ is continuous (II, Proposition 3.5). The preimage $(\pi_*)^{-1}(\operatorname{Diff}(X, X_f))$ is an open set in $C^\infty(X, Z)$ containing the zero section. By identifying $\operatorname{Diff}(X, X_f)$ with an open subset of $C^\infty(X, X_f)$ and using the homeomorphism between $C^\infty(X, X_f)$ and an open subset of $C^\infty(X, Y)$ via the tubular neighborhood identification, we obtain the desired Fr\'{e}chet manifold chart around $f$.
