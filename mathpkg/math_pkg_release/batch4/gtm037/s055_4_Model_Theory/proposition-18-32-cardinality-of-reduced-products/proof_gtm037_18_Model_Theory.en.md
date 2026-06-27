---
role: proof
locale: en
of_concept: proposition-18-32-cardinality-of-reduced-products
source_book: gtm037
source_chapter: "18"
source_section: "Model Theory"
---

Let $\varphi$ be a sentence (involving equality only) which holds in a structure $\mathfrak{A}$ exactly when $|\mathfrak{A}| = n$. Such a sentence exists: it asserts that there are exactly $n$ distinct elements, i.e.,

$$\exists v_0 \cdots \exists v_{n-1} \left( \bigwedge_{i < j < n} v_i \neq v_j \land \forall w \bigvee_{i < n} w = v_i \right).$$

By assumption, $\{i \in I : |A_i| = n\} \in F$, so the set of indices where $\mathfrak{A}_i \models \varphi$ belongs to $F$. By Łoś's Theorem (Corollary 18.30), the reduced product $P_{i \in I} \mathfrak{A}_i / F$ also satisfies $\varphi$, and therefore $|P_{i \in I} A_i / F| = n$.
