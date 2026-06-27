---
role: proof
locale: en
of_concept: subgroup-criterion
source_book: gtm028
source_chapter: "I"
source_section: "2. Groups"
---

**Necessity:** If $H_0$ is the set of elements of a subgroup $H$, then for any $a, b \in H$, we have $b^{-1} \in H$ (closure under inverses) and hence $ab^{-1} \in H$ (closure under multiplication). Thus $ab^{-1} \in H_0$.

**Sufficiency:** Assume $H_0 \neq \emptyset$ and $a, b \in H_0 \implies ab^{-1} \in H_0$.

First, $H_0$ contains the identity $e$ of $G$: pick any $a \in H_0$ (possible since $H_0 \neq \emptyset$); then $e = a \cdot a^{-1} \in H_0$ by the condition with $b = a$.

Second, $H_0$ is closed under inverses: if $a \in H_0$, then $a^{-1} = e \cdot a^{-1} \in H_0$ by the condition with $a = e, b = a$.

Third, $H_0$ is closed under multiplication: if $a, b \in H_0$, then $b^{-1} \in H_0$ (just shown), so $a \cdot b = a \cdot (b^{-1})^{-1} \in H_0$ by the condition.

Thus $H_0$ is a group with respect to the operation in $G$, and it is a subgroup of $G$.
