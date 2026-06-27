---
role: proof
locale: en
of_concept: r-relation-via-transition-probabilities
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** Suppose $n \geq 0$ is the smallest exponent for which $(P^n)_{ij} > 0$. Then $F^{(n)}_{ij} = (P^n)_{ij} > 0$, and since $H_{ij} = \sum_n F^{(n)}_{ij}$, we have $H_{ij} > 0$, hence $R(i,j)$.

Conversely, if $R(i,j)$, then $H_{ij} > 0$. Since $H_{ij} = \sum_{n} F^{(n)}_{ij}$, there exists some $n$ with $F^{(n)}_{ij} > 0$. By definition, $F^{(n)}_{ij} \leq (P^n)_{ij}$, hence $(P^n)_{ij} > 0$.
