---
role: proof
locale: en
of_concept: closed-subspace-reflexive-equivalence
source_book: gtm015
source_chapter: "IV"
source_section: "45"
---

# Proof of Equivalent Conditions for Closed Subspaces of Reflexive Spaces

Let $M$ be a linear subspace of a reflexive Banach space $E$. We prove the equivalence of:
(a) $M$ is closed;
(b) $M$ is weakly closed;
(c) $M = {}^\perp(M^\perp)$;
(d) $M_0 = (M^\perp)^\perp$, where $M_0$ is the image of $M$ under the canonical embedding $x \mapsto x''$.

**(a) $\Rightarrow$ (d):** If $M$ is closed, then $M$ is a reflexive Banach space (as a closed subspace of a reflexive space, see 45.5). Its dual is $M' \cong E'/M^\perp$. Under the canonical embedding, the image $M_0$ of $M$ in $M''$ is all of $M''$. One checks that $(M^\perp)^\perp$ in $E''$ corresponds exactly to $M_0$.

**(d) $\Rightarrow$ (c):** If $M_0 = (M^\perp)^\perp$, then applying the pre-annihilator (in $E$) to both sides yields $M = {}^\perp(M^\perp)$, since $M$ is the preimage of $M_0$ under the canonical embedding (which is injective).

**(c) $\Rightarrow$ (b):** The set ${}^\perp(M^\perp)$ is always weakly closed, being the intersection of kernels of the weak* continuous functionals in $M^\perp$. Since $M = {}^\perp(M^\perp)$ by hypothesis, $M$ is weakly closed.

**(b) $\Rightarrow$ (a):** A weakly closed set is always norm-closed (since the weak topology is coarser than the norm topology). $\square$
