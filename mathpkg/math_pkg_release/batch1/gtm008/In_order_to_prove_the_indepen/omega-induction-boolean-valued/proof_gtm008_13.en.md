---
role: proof
locale: en
of_concept: omega-induction-boolean-valued
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

Using the result of Example 4:
$$[\![0 \in a \land (\forall x \in a)[x + 1 \in a]]\!] \leq [\![\check{n} \in a]\!] \quad \text{for every } n \in \omega.$$

Therefore:
$$[\![0 \in a \land (\forall x \in a)[x + 1 \in a]]\!] \leq \prod_{n \in \omega} [\![\check{n} \in a]\!]$$
(since the left-hand side is bounded by each factor, it is bounded by the product).

By definition of the subset relation in $V^{(B)}$:
$$\prod_{n \in \omega} [\![\check{n} \in a]\!] = [\![(\forall x \in \check{\omega})[x \in a]]\!] = [\![\check{\omega} \subseteq a]\!].$$

Thus the implication holds with Boolean value $1$.
