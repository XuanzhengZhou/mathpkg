---
role: proof
locale: en
of_concept: normalizer-theorem-borel
source_book: gtm021
source_chapter: "23"
source_section: "23.2"
---
We are given a Borel subgroup $B$, with normalizer $N$ (where $B = N^\circ$, thanks to Lemma 23.1). To show that $N = B$, we proceed by induction on $\dim G$. It is clear that $R(G)$ lies in all Borel subgroups of $G$ (cf. Exercise 21.6), so we may assume without loss of generality that $G$ is positive dimensional and semisimple.

Consider a line $D$ whose isotropy group in $G$ is precisely $M$ (Theorem 11.2). Let $\chi: M \rightarrow G_m$ be the associated character. Then $\chi$ is trivial on $(M, M)$ as well as on the unipotent group $B_u$; so $\chi$ is trivial on $B$. If $0 \neq v \in V$ spans $D$, this implies that $\rho$ induces a morphism $G/B \rightarrow Y = \text{orbit of } v$ under $\rho(G)$. Since $G/B$ is complete, its image $Y$ is closed in $V$ (hence affine) as well as complete, by (21.1)(b). But then $Y$ is a point (21.1)(c). Therefore $G = M$. Since $G$ is connected and $[M:B] < \infty$ (Lemma 23.1), this forces $G = B$, which is absurd.
