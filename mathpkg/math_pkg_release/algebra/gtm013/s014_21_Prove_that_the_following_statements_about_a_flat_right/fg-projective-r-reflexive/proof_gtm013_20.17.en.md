---
role: proof
locale: en
of_concept: fg-projective-r-reflexive
source_book: gtm013
source_chapter: "20"
source_section: "20.17"
---

Suppose $P$ is a finitely generated projective left $R$-module. Then by (17.3), there exist $P'$ and $n$ such that $P \oplus P' \cong {}_R R^{(n)}$.

By (4.11), the left multiplication map $\lambda: R \to \operatorname{End}(R_R)$ is an isomorphism. So by (20.15), ${}_R R$ is $R$-reflexive. Then by (20.13), ${}_R R^{(n)}$ is $R$-reflexive, and since $P$ is a direct summand of ${}_R R^{(n)}$, $P$ is $R$-reflexive by (20.13) again. This proves (1).

For (2):
$$P^* \oplus P'^* \cong (P \oplus P')^* \cong (R^{(n)})^* \cong (R^*)^{(n)} \cong R^{(n)},$$

so $P^*$ is a direct summand of a finitely generated free right $R$-module, hence is finitely generated and projective. This proves (2).
