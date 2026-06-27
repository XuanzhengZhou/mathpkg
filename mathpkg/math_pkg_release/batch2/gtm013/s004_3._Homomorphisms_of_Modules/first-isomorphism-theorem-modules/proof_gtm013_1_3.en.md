---
role: proof
locale: en
of_concept: first-isomorphism-theorem-modules
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.** Define $\bar{f}: M / \text{Ker}\, f \to \text{Im}\, f$ by $\bar{f}(x + \text{Ker}\, f) = f(x)$. This map is well-defined because if $x + \text{Ker}\, f = y + \text{Ker}\, f$, then $x - y \in \text{Ker}\, f$, so $f(x) = f(y)$. It is clearly a homomorphism since
$$\bar{f}((x + \text{Ker}\, f) + (y + \text{Ker}\, f)) = \bar{f}(x + y + \text{Ker}\, f) = f(x + y) = f(x) + f(y) = \bar{f}(x + \text{Ker}\, f) + \bar{f}(y + \text{Ker}\, f),$$
and similarly for scalar multiplication.

The map $\bar{f}$ is surjective onto $\text{Im}\, f$ by definition. It is injective because if $\bar{f}(x + \text{Ker}\, f) = 0$, then $f(x) = 0$, so $x \in \text{Ker}\, f$, whence $x + \text{Ker}\, f = 0 + \text{Ker}\, f$. Thus $\bar{f}$ is an isomorphism. $\square$
