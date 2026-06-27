---
role: proof
locale: en
of_concept: progenerator-endomorphism-equivalence
source_book: gtm013
source_chapter: "6"
source_section: "22"
---

**(a) $\Rightarrow$ (b).** This is immediate from (22.2). If $R \approx S$, then by Morita's Theorem there exists a bimodule ${}_S P_R$ such that $P_R$ is a progenerator and the equivalence $F \cong (P \otimes_R -)$ yields $S \cong \operatorname{End}({}_S S) \cong \operatorname{End}(F({}_R R)) = \operatorname{End}({}_S P)$. Since ${}_S P_R$ is balanced (22.2.2), we have $S \cong \operatorname{End}(P_R)$.

**(b) $\Rightarrow$ (a).** We may assume that $S = \operatorname{End}(P_R)$. By (17.8), since $P_R$ is a generator, it is balanced and finitely generated projective over $S = \operatorname{End}(P_R)$. Then also since ${}_S P_R$ is balanced and $P_R$ is finitely generated projective, an application of (17.7) gives us that ${}_S P$ is a generator. Now (22.2) applies and $R$ and $S$ are equivalent via $F = (P \otimes_R -)$ and $G = \operatorname{Hom}_S(P, -)$.

**(a) $\Leftrightarrow$ (c).** By symmetry.
