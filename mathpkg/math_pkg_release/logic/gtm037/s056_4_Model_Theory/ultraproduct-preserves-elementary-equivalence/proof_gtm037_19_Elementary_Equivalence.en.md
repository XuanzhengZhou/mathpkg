---
role: proof
locale: en
of_concept: ultraproduct-preserves-elementary-equivalence
source_book: gtm037
source_chapter: "19"
source_section: "Elementary Equivalence"
---
Let $\varphi$ be a sentence which holds in $\prod_{i \in I} \mathfrak{A}_i / \bar{F}$. Then by the basic theorem on ultraproducts, $\{i \in I : \mathfrak{A}_i \models \varphi\} \in F$.

But $\{i \in I : \mathfrak{A}_i \models \varphi\} = \{i \in I : \mathfrak{B}_i \models \varphi\}$ by the hypothesis that $\mathfrak{A}_i \equiv_{\text{ee}} \mathfrak{B}_i$ for each $i \in I$.

Therefore, by the basic theorem on ultraproducts again, $\prod_{i \in I} \mathfrak{B}_i / \bar{F} \models \varphi$.

Taking $\neg \varphi$ for $\varphi$, we see that the converse holds also. Hence the two ultraproducts are elementarily equivalent.
