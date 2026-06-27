---
role: proof
locale: en
of_concept: yoneda-embedding-is-codense
source_book: gtm005
source_chapter: "X"
source_section: "6"
---

A functor $K: A \to C$ is dense if the right Kan extension $\operatorname{Ran}_K K$ is $1_C$, i.e., every object of $C$ is canonically a colimit of objects from $A$.

The Yoneda embedding $Y: D^{\mathrm{op}} \to \mathbf{Set}^{D}$ (note: contravariant version sends $d$ to $D(d, -)$) is dense. Actually, $Y: D \to \mathbf{Set}^{D^{\mathrm{op}}}$ (sending $d$ to $D(-, d)$) is codense: every presheaf $P$ is a colimit of representables:
$$P \cong \varinjlim_{(d, x) \in \int_D P} D(-, d).$$

Proof: This is the co-Yoneda lemma. For each $(d, x)$ with $x \in P(d)$, we have the natural transformation $D(-, d) \Rightarrow P$ corresponding via Yoneda to $x$. These assemble into a cocone over the diagram of representables indexed by $\int_D P$, and the universal property follows from the Yoneda Lemma.
