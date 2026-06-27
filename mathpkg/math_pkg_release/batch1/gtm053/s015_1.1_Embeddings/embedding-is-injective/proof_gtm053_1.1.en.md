---
role: proof
locale: en
of_concept: embedding-is-injective
source_book: gtm053
source_chapter: "1"
source_section: "1.1"
---

**Proof.** Let $h : A \rightarrow B$ be an embedding between $L$-structures. Suppose $h(a_1) = h(a_2)$ for some $a_1, a_2 \in A$. We need to show $a_1 = a_2$.

Consider the equality relation on $A$. The formula $x_1 = x_2$ is an atomic formula in the language $L$ (every first-order language includes equality). Since $A \vDash a_1 = a_1$, we have in particular that the pair $(a_1, a_2)$ satisfies the same atomic formula $x_1 = x_2$ in $A$ as $(h(a_1), h(a_2))$ does in $B$, because $h(a_1) = h(a_2)$ by assumption.

More rigorously, consider the binary relation symbol for equality. Since $h$ preserves all relation symbols, and equality is logically treated as a binary relation preserved under embeddings, we have $A \vDash a_1 = a_2$ if and only if $B \vDash h(a_1) = h(a_2)$. Since $h(a_1) = h(a_2)$, the right-hand side holds, and therefore $A \vDash a_1 = a_2$, i.e., $a_1 = a_2$.

Hence $h$ is injective. $\square$
