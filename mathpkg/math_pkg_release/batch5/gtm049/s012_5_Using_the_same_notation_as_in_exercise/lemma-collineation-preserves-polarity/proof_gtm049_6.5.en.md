---
role: proof
locale: en
of_concept: lemma-collineation-preserves-polarity
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

We recall the notation $\sigma^g$ for the transformed bilinear form (defined by $\sigma^g(a, b) = \sigma(ag^{-1}, bg^{-1})$). We also use the notation $d^g$ in the same way and denote by $D^g$ the set of all $d^g$ for $d$ in $D$.

If $M$ is any subspace of $H$, then $M^{\perp(\sigma^g)}$ is the set of all vectors $b$ such that $\sigma^g(M, b) = 0$. Hence $M^{\perp(\sigma^g)}g$ is the set of all vectors $bg$ such that $\sigma(Mg, bg) = 0$. This means that $M^{\perp(\sigma^g)}g = (Mg)^{\perp(\sigma)}$. We thus have the general formula

$$\perp(\sigma^g)\mathcal{P}(g) = \mathcal{P}(g)\perp(\sigma).$$

We conclude that $\mathcal{P}(g)$ preserves $\perp(\sigma)$ if, and only if, $\perp(\sigma^g) = \perp(\sigma)$. This in turn is equivalent to $D^g = D$, as required (since if $\perp(\sigma^g) = \perp(\sigma)$ then $\sigma^g = r^2\sigma$ for some $r > 0$, which means $d^g = rd$, i.e., $D^g = D$).
