---
role: proof
locale: en
of_concept: hom-interchange-isomorphism
source_book: gtm013
source_chapter: "20"
source_section: "20.7"
---

Define $\eta: \operatorname{Hom}_R(M, \operatorname{Hom}_S(N, U)) \to \operatorname{Hom}_S(N, \operatorname{Hom}_R(M, U))$ by $[\eta(\gamma)](n): m \mapsto [\gamma(m)](n)$. 

First, verify that $\eta(\gamma)(n) \in \operatorname{Hom}_R(M, U)$: for $r \in R$,
$$[\eta(\gamma)(n)](rm) = [\gamma(rm)](n) = [r \cdot \gamma(m)](n) = r \cdot [\gamma(m)](n) = r \cdot [\eta(\gamma)(n)](m).$$

Next, $\eta(\gamma): N \to \operatorname{Hom}_R(M, U)$ is $S$-linear: for $s \in S$,
$$[\eta(\gamma)(ns)](m) = [\gamma(m)](ns) = [\gamma(m)](n)s = [\eta(\gamma)(n)](m)s.$$

The inverse of $\eta$ is given by $[\eta^{-1}(\alpha)](m): n \mapsto [\alpha(n)](m)$ for $\alpha \in \operatorname{Hom}_S(N, \operatorname{Hom}_R(M, U))$. One verifies similarly that $\eta^{-1}(\alpha)(m) \in \operatorname{Hom}_S(N, U)$ and that $\eta^{-1}(\alpha)$ is $R$-linear. Clearly $\eta \circ \eta^{-1} = 1$ and $\eta^{-1} \circ \eta = 1$.

Naturality in $M$, $N$, and $U$ follows from the functoriality of Hom and the definition of $\eta$, verified by straightforward diagram chases. The details are left as an exercise in the text.
