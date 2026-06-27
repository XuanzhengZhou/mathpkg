---
role: proof
locale: en
of_concept: theorem-14-22-homomorphism-properties
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

1 and 2 follow from the $N$-completeness of $h_0$, since
$$h(u) = h(v) \leftrightarrow (\forall x \in \mathcal{D}(u))[h_0([x \in u]) = 1 \rightarrow h(x) \in h(v)]$$
$$\land (\forall x \in \mathcal{D}(v))[h_0([x \in v]) = 1 \rightarrow h(x) \in h(u)]$$
and
$$h(u) \in h(v) \leftrightarrow (\exists y \in \mathcal{D}(v))[h(u) = h(y) \land h_0([y \in u]) = 1].$$

3. Follows by induction on rank$(k)$:
$$h(\check{k}) = \{h(x) \mid x \in \mathcal{D}(\check{k}) \land h_0([x \in \check{k}]) = 1\}$$
$$= \{h(x) \mid (\exists k_1 \in k)[x = \check{k}_1]\} = \{h(\check{k}_1) \mid k_1 \in k\} = k.$$

4-8 follow from the definition of $h$ together with the $N$-completeness of $h_0$ and properties of generic filters. The sum preservation (6) uses the Axiom of Choice in $N$ to ensure the sums are over sets in $N$, which are preserved by the $N$-complete $h_0$. Property 7 is proved by induction on the number of logical symbols in $\varphi$, using 1 and 2 for the base cases and 6 for the induction step. Property 8 uses the definition of $h$ by recursion.
