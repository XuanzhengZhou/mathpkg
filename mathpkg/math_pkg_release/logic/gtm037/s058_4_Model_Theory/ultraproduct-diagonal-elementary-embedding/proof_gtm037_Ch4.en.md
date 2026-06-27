---
role: proof
locale: en
of_concept: ultraproduct-diagonal-elementary-embedding
source_book: gtm037
source_chapter: "4"
source_section: "Model Theory"
---

First, $f$ is one-one. For, suppose $fa = fb$. Thus $\langle a : i \in I \rangle \, \overline{F} \, \langle b : i \in I \rangle$, i.e., $\{i \in I : a = b\} \in F$. But $\{i : a = b\}$ is either empty or all of $I$ depending upon whether $a \neq b$ or $a = b$ respectively. Since $\emptyset \notin F$, it follows that $a = b$.

Since $f$ is one-one, we can use the procedure of the proof of Proposition 19.7 to make the image $C$ of $f$ into an $L$-structure, and $f$ into an isomorphism from $\mathfrak{A}$ onto $\mathfrak{C}$. Since $f$ is an isomorphism, it is an elementary embedding. Then by definition, the inclusion map $i : \mathfrak{C} \to I_{\mathfrak{A}/\overline{F}}$ is an embedding. To show $f$ is an elementary embedding of $\mathfrak{A}$ into $I_{\mathfrak{A}/\overline{F}}$, it suffices to show that $i$ is an elementary embedding, which follows from the fact that $f$ is elementary and $i \circ f$ is the canonical embedding, or more directly from Los's theorem applied to the diagonal sequences.
