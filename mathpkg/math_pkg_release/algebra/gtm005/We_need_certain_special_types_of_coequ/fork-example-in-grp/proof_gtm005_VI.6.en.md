---
role: proof
locale: en
of_concept: fork-example-in-grp
source_book: gtm005
source_chapter: "VI"
source_section: "6"
---

In $\mathbf{Grp}$, consider the inclusion $i: N \hookrightarrow G$ of a normal subgroup and the trivial homomorphism $0: N \to G$ (sending all to $1_G$). The coequalizer of $(i, 0)$ is the quotient map $\pi: G \to G/N$.

This fork is split in $\mathbf{Set}$ (not in $\mathbf{Grp}$): choose a set-theoretic section $s: G/N \to G$ (picking coset representatives), giving $\pi \circ s = 1_{G/N}$. In $\mathbf{Grp}$, the fork is a regular epimorphism but not split unless $G \cong N \times (G/N)$ as groups.

Split coequalizers in $\mathbf{Grp}$ correspond to semidirect product decompositions: a fork is split iff the quotient map has a group-theoretic section, in which case $G$ is the semidirect product of the kernel and the image of the section.
