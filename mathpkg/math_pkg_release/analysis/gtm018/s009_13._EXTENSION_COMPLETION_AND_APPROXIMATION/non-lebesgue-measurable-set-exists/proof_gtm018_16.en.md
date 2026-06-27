---
role: proof
locale: en
of_concept: non-lebesgue-measurable-set-exists
source_book: gtm018
source_chapter: "III. Extension of Measures"
source_section: "§16. Non Measurable Sets"
---

Define $x \sim y$ iff $x - y \in A$ (the dense subgroup from Theorem C). Using the Axiom of Choice, let $E_0$ contain exactly one element from each equivalence class.

If $E_0$ were measurable, its measure must be zero: for any compact $F \subset E_0$, $D(F) \cap A = \varnothing$ (equivalent elements differ by members of $A$), so by Theorem B, $\mu(F) = 0$. Hence $\mu_*(E_0) = 0$.

But distinct elements $a_1,a_2 \in A$ give disjoint translates $E_0 + a_1$ and $E_0 + a_2$, and $\{E_0 + a : a \in A\}$ covers $\mathbb{R}$. Measurability would imply all translates have the same measure as $E_0$, giving $\mu(\mathbb{R}) = 0$, contradiction.
