---
role: proof
locale: en
of_concept: order-preserving-preimage-lemma
source_book: gtm043
source_chapter: "13"
source_section: "13.5"
---
Let $(c_n)_{n \in \mathbb{N}}$ be preimages of the elements of $E$, with $c_1$ the specified one. We inductively adjust them.

For $c_n$, compare $I(c_n)$ with previously fixed $I(c_k)$ ($k < n$):
- If $I(c_n) \geq I(c_k)$, replace $c_n$ by $c_n \vee c_k$;
- If $I(c_n) \leq I(c_k)$, replace by $c_n \wedge c_k$.

Since $I$ is absolutely convex, $I(c_n \vee c_k) = I(c_n) \vee I(c_k) = I(c_n)$ when $I(c_n) \geq I(c_k)$, and similarly for meets. So the residue class is preserved, while the adjusted preimages now reflect the order of their images.

After finitely many adjustments per index, we obtain $F = \{c_n'\}$ with the required property.