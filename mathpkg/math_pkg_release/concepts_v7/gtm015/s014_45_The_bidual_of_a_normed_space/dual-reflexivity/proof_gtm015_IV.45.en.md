---
role: proof
locale: en
of_concept: dual-reflexivity
source_book: gtm015
source_chapter: "IV"
source_section: "45"
---

# Proof of Reflexivity of the Dual Space

We prove: A Banach space $E$ is reflexive if and only if its dual $E'$ is reflexive.

**($\Rightarrow$) Suppose $E$ is reflexive.** Let $\Phi \in E'''$. We must show $\Phi$ is the canonical image of some $f \in E'$. Consider the restriction of $\Phi$ to $E_0$ (the canonical image of $E$ in $E''$). Since $E$ is reflexive, $E_0 = E''$, so $\Phi$ is a continuous linear functional on $E''$. Define $f \in E'$ by $f(x) = \Phi(x'')$ for all $x \in E$ (where $x''$ is the canonical image of $x$ in $E''$). Then one verifies that $f'' = \Phi$, proving $E'$ is reflexive.

More structurally: Let $J_E: E \to E''$ be the canonical embedding. If $J_E$ is surjective, then the double dual $J_E'': E'' \to E^{(iv)}$ coupled with the adjoint $(J_E)': E''' \to E'$ yields that the canonical embedding $J_{E'}: E' \to E'''$ is surjective. Indeed, $J_{E'} = (J_E)' \circ J_{E''}$, and since $J_E$ is bijective, $(J_E)'$ is bijective. Alternatively, the natural map $E''' \to E'$ given by restriction to $E$ (under the identification $E'' = E$) gives the inverse of $J_{E'}$.

**($\Leftarrow$) Suppose $E'$ is reflexive.** Then by the forward direction applied to $E'$, we know $E''$ is reflexive. The canonical image $E_0$ of $E$ in $E''$ is a closed linear subspace of the reflexive space $E''$ (closed because $E$ is complete and the embedding is isometric). By Exercise 45.5 (a closed subspace of a reflexive space is reflexive), $E_0$ is reflexive. Since the canonical map $E \to E_0$ is an isometric isomorphism, $E$ is reflexive. $\square$
