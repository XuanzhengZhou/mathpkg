---
role: proof
locale: en
of_concept: finite-language-back-and-forth
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

For each $i \leq n$ let

$$I_i = \{(x, y) : x \in {}^i A,\; y \in {}^i B,\; \text{and for all atomic } \varphi \text{ with } \operatorname{Fv}\varphi \subseteq \{v_0,\ldots,v_{i-1}\},\; \mathfrak{A} \models \varphi[x] \text{ iff } \mathfrak{B} \models \varphi[y]\}.$$

[The proof constructs the $(n+1)$-sequence by defining each $I_i$ as the set of pairs of $i$-tuples that satisfy the same atomic formulas. The back-and-forth extension property (condition (3)) is verified using the hypothesis that $\mathfrak{A}$ and $\mathfrak{B}$ agree on all $\Delta_n^n$ sentences, together with the finiteness of the relational language. The finite language condition ensures that there are only finitely many atomic types to consider, allowing the back-and-forth construction to proceed through all $n+1$ levels.]
