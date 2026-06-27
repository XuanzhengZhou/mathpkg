---
role: proof
locale: en
of_concept: boolean-valued-bounded-quantifier
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The formulas follow directly from the definition of the Boolean values for quantifiers and the Boolean-valued membership relation.

**Part 1.** By definition of the existential quantifier:
$$[\![(\exists x \in u) \varphi(x)]\!] = [\![\exists x (x \in u \wedge \varphi(x))]\!]$$
$$= \sum_{x \in V^{(B)}} [\![x \in u \wedge \varphi(x)]\!]$$
$$= \sum_{x \in V^{(B)}} [\![x \in u]\!] \cdot [\![\varphi(x)]\!].$$

By Definition 13.3, $[\![x \in u]\!] = \sum_{y \in \mathcal{D}(u)} u(y) \cdot [\![x = y]\!]$. Substituting:
$$= \sum_{x \in V^{(B)}} \sum_{y \in \mathcal{D}(u)} u(y) \cdot [\![x = y]\!] \cdot [\![\varphi(x)]\!]$$
$$= \sum_{y \in \mathcal{D}(u)} u(y) \cdot \sum_{x \in V^{(B)}} [\![x = y]\!] \cdot [\![\varphi(x)]\!]$$
$$= \sum_{y \in \mathcal{D}(u)} u(y) \cdot [\![\varphi(y)]\!]$$
where the last equality follows from the substitution property (Theorem 13.5): $\sum_x [\![x = y]\!] \cdot [\![\varphi(x)]\!] = [\![\varphi(y)]\!]$.

**Part 2.** Dually, $[\![(\forall x \in u) \varphi(x)]\!] = [\![\forall x (x \in u \rightarrow \varphi(x))]\!]$
$$= \prod_{x \in V^{(B)}} ([\![x \in u]\!] \Rightarrow [\![\varphi(x)]\!])$$
$$= \prod_{x \in V^{(B)}} \left( \sum_{y \in \mathcal{D}(u)} u(y) \cdot [\![x = y]\!] \Rightarrow [\![\varphi(x)]\!] \right).$$

By Boolean algebra, $(\sum_y u(y) \cdot [\![x = y]\!]) \Rightarrow [\![\varphi(x)]\!] = \prod_y (u(y) \cdot [\![x = y]\!] \Rightarrow [\![\varphi(x)]\!])$. Taking the product over $x$ and using the substitution property as above yields:
$$= \prod_{y \in \mathcal{D}(u)} (u(y) \Rightarrow [\![\varphi(y)]\!]).$$
