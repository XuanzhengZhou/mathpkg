---
role: proof
locale: en
of_concept: product-space-projections-oco
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

The statement that $\langle X, T \rangle$ is a topological space is obvious from the definition: each $\tilde{G}_{\alpha}$ is a subset of $X$, and the collection of all such sets is closed under finite intersections (by taking the minimum of the relevant indices).

$p_{\alpha}$ is continuous because the preimage of an open set $G_{\alpha} \subseteq X^{\alpha}$ is exactly $\tilde{G}_{\alpha}$, which is a basic open set in $T$.

$p_{\alpha}$ is open because the image of a basic open set $\tilde{G}_{\beta}$ is either $X^{\alpha}$ (if $\alpha \neq \beta$) or $G_{\alpha}$ (if $\alpha = \beta$), both of which are open in $X^{\alpha}$.

$p_{\alpha}$ is onto since for any $x \in X^{\alpha}$, one can extend $x$ to a function $f$ with domain containing $\alpha$ (by arbitrary choices on other coordinates).

The compatibility $p_{\alpha\beta} \circ p_{\beta} = p_{\alpha}$ holds by definition of the restriction maps $p_{\alpha\beta}$.
