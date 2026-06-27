---
role: proof
locale: en
of_concept: bound-variable-decomposition
source_book: gtm037
source_chapter: "10"
source_section: "Elements of Logic"
---

Induction on $\varphi$. If $\varphi$ is atomic, the statement holds vacuously. For compound formulas, the induction steps follow from the structure of formula construction. In particular, if $\varphi$ is $\forall \beta \chi$ and $\alpha$ occurs bound in $\chi$, by the induction hypothesis there exists a subformula $\forall \alpha \psi$ occurring in $\chi$ with the required property. If $\alpha$ does not occur bound in $\chi$, then $\forall \beta \chi$ itself (with $\beta = \alpha$) provides the required decomposition.
