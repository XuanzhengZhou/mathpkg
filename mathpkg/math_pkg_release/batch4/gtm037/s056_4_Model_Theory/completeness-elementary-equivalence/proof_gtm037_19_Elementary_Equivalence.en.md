---
role: proof
locale: en
of_concept: completeness-elementary-equivalence
source_book: gtm037
source_chapter: "19"
source_section: "Elementary Equivalence"
---
The proof is straightforward. (i) $\Rightarrow$ (ii): Suppose $\Gamma$ is complete and let $\mathfrak{A}, \mathfrak{B}$ be models of $\Gamma$. For any sentence $\varphi$, either $\Gamma \vdash \varphi$ or $\Gamma \vdash \neg \varphi$ by completeness. Hence either $\mathfrak{A} \models \varphi$ and $\mathfrak{B} \models \varphi$, or $\mathfrak{A} \models \neg \varphi$ and $\mathfrak{B} \models \neg \varphi$. In either case $\mathfrak{A} \models \varphi \iff \mathfrak{B} \models \varphi$, so the structures are elementarily equivalent.

(ii) $\Rightarrow$ (i): If any two models of $\Gamma$ are elementarily equivalent, then for each sentence $\varphi$, either all models satisfy $\varphi$ or none do. Thus $\varphi$ is either a semantic consequence of $\Gamma$ or its negation is, establishing completeness.
