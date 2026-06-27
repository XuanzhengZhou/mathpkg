---
role: proof
locale: en
of_concept: equivalence-class-type-homogeneity
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** Suppose $i$ and $j$ communicate, so $R(i,j)$ and $R(j,i)$ both hold. If $i$ is recurrent, then by Lemma 4-23 applied to $R(i,j)$, we have $H_{ji} = 1$ and $H_{ij} = 1$. Since $H_{ji} = 1$, state $j$ is almost surely reached from itself (via $i$), implying $\bar{H}_{jj} = 1$, so $j$ is recurrent. The same argument with the roles reversed shows that if $j$ is recurrent then $i$ is recurrent. Therefore, either both are recurrent or both are transient.
