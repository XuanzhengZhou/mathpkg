---
role: proof
locale: en
of_concept: semisimple-group-zero-nilradical
source_book: gtm021
source_chapter: "13"
source_section: "Correspondence Between Groups and Lie Algebras"
---
Let $R(G)$ be the radical of $G$ (maximal closed connected solvable normal subgroup). Since $G$ is semisimple, $R(G) = \{e\}$.

Consider any commutative normal subgroup -- its Lie algebra would be an abelian ideal, hence contained in the nilradical. If $n$ is a nonzero nilpotent ideal of $\mathfrak{g}$, let $H$ be the corresponding connected subgroup with $\mathfrak{h} = n$. Since $n$ is an ideal, Theorem 13.3 implies $H \trianglelefteq G$. Moreover, $n$ is nilpotent, and by the correspondence, $H$ would be a nilpotent (hence solvable) normal subgroup, contradicting semisimplicity of $G$ unless $n = 0$.

More precisely: The center $\mathfrak{z}(\mathfrak{g})$ is an abelian ideal, and by Theorem 13.4(b), its corresponding group is $Z(G)^\circ$, which is a normal commutative subgroup. Semisimplicity forces $Z(G)^\circ = \{e\}$, hence $\mathfrak{z} = 0$.

Similarly, the nilradical of $\mathfrak{g}$ is also an ideal (including the center, since it is commutative, as part of the center). Its corresponding group would be a normal nilpotent subgroup, contradicting semisimplicity. Hence the nilradical is zero.
