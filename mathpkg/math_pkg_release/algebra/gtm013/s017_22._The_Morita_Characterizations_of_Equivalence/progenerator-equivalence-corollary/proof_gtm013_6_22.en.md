---
role: proof
locale: en
of_concept: progenerator-equivalence-corollary
source_book: gtm013
source_chapter: "6"
source_section: "22"
---

By (17.8), since $P_R$ is a progenerator, ${}_S P_R$ is a faithfully balanced bimodule, where $S = \operatorname{End}(P_R)$. In particular, $S \cong \operatorname{End}(P_R)$ via the natural action. By (22.2), $R$ and $S$ are equivalent via $F = (P \otimes_R -)$ and $G = \operatorname{Hom}_S(P, -)$.

Now, by the natural isomorphisms established in (21.1), we have

$$G \cong \operatorname{Hom}_S(P, -) \cong \operatorname{Hom}_R(\operatorname{Hom}_S(P, S), -) = \operatorname{Hom}_R(P^{\circledast}, -)$$

since $P^{\circledast} = \operatorname{Hom}_R(P, R) \cong \operatorname{Hom}_S(P, S)$ by the balanced property. Furthermore, by the tensor-Hom adjunction and the fact that $P^{\circledast}$ is a progenerator over $R$, we obtain

$$\operatorname{Hom}_R(P^{\circledast}, -) \cong (P \otimes_R -).$$

Similarly, $G \cong (P^{\circledast} \otimes_S -)$. Thus $(P \otimes_R -)$ and $(P^{\circledast} \otimes_S -)$ are inverse equivalences.
