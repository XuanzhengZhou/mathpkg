---
role: proof
locale: en
of_concept: corollary-1
source_book: gtm026
source_chapter: "1"
source_section: "1.34"
---

1.33 and 1.19. $\square$

1.35 The Composition of Algebraic Functors Need Not Be Algebraic. Let $\mathcal{A}$ be the category of abelian groups with algebraic forgetful functor $V$: $\mathcal{A} \longrightarrow \text{Set}$. Let $\mathcal{P}$ be the full replete subcategory of torsion-free abelian groups (a group is torsion-free if it has no elements of finite order). Then $\mathcal{P}$ is reflective (the reflection of $A$ is $\theta:A \longrightarrow A/C$ where $C$ is the torsion subgroup of $A$—the “$C$” of 2.2.13; since $A$ is abelian, $C$ is simply the subset of elements of finite order). By 1.33, the inclusion functor $U:\mathcal{P} \longrightarrow \mathcal{A}$ is algebraic. Although $UV:\mathcal{P} \longrightarrow \text{Set}$ has a left adjoint (2.2.30), $UV$ is not algebraic. Let 2 be a two-element set and let $(T, \eta, \mu)$ be the algebraic theory in $\text{Set}$ whose algebras are the abelian groups. Then $(2TT, 2T\mu)$ and $(2T, 2

1. If $U$ creates coequalizers of $U$-absolute pairs then $V$ creates coequalizers of $V$-absolute pairs.

2. If $U$ creates limits and if $i$ preserves limits then $V$ creates limits.

3. If $U$ has a left adjoint $F: \mathcal{H} \longrightarrow \mathcal{A}$ and if either $FU: \mathcal{H} \longrightarrow \mathcal{K}$ maps $\mathcal{L}$ into $\mathcal{L}$ or $\mathcal{P}$ is reflective in $\mathcal{A}$ then $V$ has a left adjoint.

1. Let

$$P_1V \xrightarrow{fV} P_2V \xrightarrow{h} L$$

be an absolute coequalizer in $\mathcal{L}$. Then

$$P_1jU \xrightarrow{fjU} P_2jU \xrightarrow{hi} Li$$

is an absolute coequalizer in $\mathcal{H}$ so that there exists a unique lift $\bar{h}: P_2j \longrightarrow \mathcal{A}$ with $\bar{h}U = hi$; and, moreover, $\bar{h} = \text{coeq}(fj, gj)$ in $\mathcal{A}$. As $AU = Li$, $A$ is in $\mathcal{P}$. The rest is clear.

2. The proof is similar to that of (1). Let $D$ be a diagram in $\mathcal{P}$ and let $\psi: L \longrightarrow DV$ be a limit of $DV$. As $i$ preserves limits, $\psi: Li \longrightarrow DjU$ is a limit of $DjU$ in $\mathcal{H}$ and there exist unique lifts $\bar{\psi}: \bar{L} \longrightarrow Dj$ with $\bar{\psi}U = \psi i$; and, moreover, $(\bar{L}, \bar{\psi})$ is a limit of $Dj$. As $\bar{L}U = Li$, $\bar{L}$ is in $\mathcal{P}$. The rest is clear.

3. If $FU$ maps $\mathcal{L}$ into $\mathcal{L
