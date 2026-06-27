---
role: proof
locale: en
of_concept: morita-equivalence-symmetry
source_book: gtm013
source_chapter: "6"
source_section: "22"
---

By Morita's Theorem (22.2), $R \approx S$ if and only if there exists a bimodule ${}_S P_R$ such that ${}_S P$ and $P_R$ are progenerators, ${}_S P_R$ is balanced, and the equivalence is given by $F \cong (P \otimes_R -)$ and $G \cong \operatorname{Hom}_S(P, -)$.

Now observe that ${}_S P_R$ is also an $(R^{\text{op}}, S^{\text{op}})$-bimodule ${}_{R^{\text{op}}} P_{S^{\text{op}}}$ with the same additive group but reversed scalar actions. The progenerator and balanced conditions are symmetric: $P_R$ being a progenerator means $P$ is a finitely generated projective generator as a right $R$-module, which translates to ${}_{R^{\text{op}}} P$ being a progenerator. Similarly, ${}_S P$ being a progenerator means ${}P_{S^{\text{op}}}$ is a progenerator. The balanced condition ${}_S P_R$ translates directly.

Thus ${}_{R^{\text{op}}} P_{S^{\text{op}}}$ satisfies the conditions of (22.2) for the opposite rings, giving $R^{\text{op}} \approx S^{\text{op}}$ via $(P \otimes_{R^{\text{op}}} -)$ and $\operatorname{Hom}_{S^{\text{op}}}(P, -)$.

The last statement follows because $\mathbf{M}_R$ is equivalent to ${}_{R^{\text{op}}}\mathbf{M}$, so $R^{\text{op}} \approx S^{\text{op}}$ implies $\mathbf{M}_R \approx \mathbf{M}_S$.
