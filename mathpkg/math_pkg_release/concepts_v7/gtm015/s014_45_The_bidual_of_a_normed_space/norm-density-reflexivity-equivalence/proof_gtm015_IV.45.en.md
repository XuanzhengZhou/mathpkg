---
role: proof
locale: en
of_concept: norm-density-reflexivity-equivalence
source_book: gtm015
source_chapter: "IV"
source_section: "45"
---

# Proof of Norm Density of the Canonical Image and Reflexivity

We prove equivalence of:
(a) $E_0$ (the canonical image of $E$ in $E''$) is norm-dense in $E'$;
(b) the completion $\widehat{E}$ of $E$ is reflexive;
(c) $E'$ is reflexive.

**(a) $\Rightarrow$ (b):** The completion $\widehat{E}$ is a Banach space containing $E$ as a dense subspace. The bidual of $\widehat{E}$ is the same as the bidual of $E$ (since $E' \cong \widehat{E}'$ isometrically). If $E_0$ is norm-dense in $E''$, then the canonical embedding of $\widehat{E}$ into $(\widehat{E})'' = E''$ has dense range. Since $\widehat{E}$ is complete, its image in $E''$ is closed. A dense closed subspace must be the whole space, so $\widehat{E}$ is reflexive.

**(b) $\Rightarrow$ (c):** If $\widehat{E}$ is reflexive, then $\widehat{E}' \cong E'$ is also reflexive (by Exercise 45.7: a Banach space is reflexive iff its dual is reflexive).

**(c) $\Rightarrow$ (a):** Suppose $E'$ is reflexive. Let $J: E \to E''$ be the canonical embedding, and let $J': E''' \to E'$ be the dual map. Since $E'$ is reflexive, the canonical embedding $E' \to E'''$ is surjective. The composition yields that $J$ has dense range in the weak* topology (by Goldstine's theorem, 45.3). But since $E'$ is reflexive, the weak* topology on $E''$ coincides with the weak topology, and $J(E)$ being weak* dense plus the reflexivity of $E'$ implies $J(E)$ is actually norm-dense in $E''$. $\square$
