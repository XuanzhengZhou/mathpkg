---
role: proof
locale: en
of_concept: upward-lowenheim-skolem-no-equality
source_book: gtm037
source_chapter: "29"
source_section: "Unusual Logics"
---

Fix $a \in A$ and define $f : B \rightarrow A$ by setting $fx = x$ for $x \in A$ and $fx = a$ for $x \in B \sim A$. For each $m$-ary relational symbol $R$, let

$$R^{\mathfrak{B}} = \{x \in {}^m B : f \circ x \in R^{\mathfrak{A}}\}.$$

This defines the $\mathcal{L}$-structure $\mathfrak{B}$. One easily checks that

(1) for any $x \in {}^\omega B$ and any formula $\varphi$ of $\mathcal{L}$ we have $\mathfrak{B} \models \varphi[x]$ iff $\mathfrak{A} \models \varphi[f \circ x]$.

From (1), $\mathfrak{A} \preceq \mathfrak{B}$ follows immediately.
