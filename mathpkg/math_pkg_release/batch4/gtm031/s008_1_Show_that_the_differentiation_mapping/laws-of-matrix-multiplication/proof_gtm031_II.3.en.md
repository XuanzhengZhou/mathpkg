---
role: proof
locale: en
of_concept: laws-of-matrix-multiplication
source_book: gtm031
source_chapter: "II"
source_section: "3"
---

The laws follow from the corresponding laws for linear transformations via the matrix correspondence. Alternatively, they can be verified algebraically.

**Associativity**: $((\alpha)(\beta))(\gamma) = (\alpha)((\beta)(\gamma))$ because the $(i,\ell)$-entry of both sides is $\sum_{j,k} \alpha_{ij} \beta_{jk} \gamma_{k\ell}$, which is well-defined by associativity of multiplication and distributivity in $\Delta$.

**Left distributivity**: For matrices of compatible sizes,
$$([(\alpha) + (\beta)](\gamma))_{ik} = \sum_j (\alpha_{ij} + \beta_{ij})\gamma_{jk} = \sum_j (\alpha_{ij}\gamma_{jk} + \beta_{ij}\gamma_{jk}) = \sum_j \alpha_{ij}\gamma_{jk} + \sum_j \beta_{ij}\gamma_{jk} = ((\alpha)(\gamma) + (\beta)(\gamma))_{ik}.$$

**Right distributivity**: Similarly,
$$((\alpha)[(\beta) + (\gamma)])_{ik} = \sum_j \alpha_{ij}(\beta_{jk} + \gamma_{jk}) = \sum_j (\alpha_{ij}\beta_{jk} + \alpha_{ij}\gamma_{jk}) = \sum_j \alpha_{ij}\beta_{jk} + \sum_j \alpha_{ij}\gamma_{jk} = ((\alpha)(\beta) + (\alpha)(\gamma))_{ik}.$$
