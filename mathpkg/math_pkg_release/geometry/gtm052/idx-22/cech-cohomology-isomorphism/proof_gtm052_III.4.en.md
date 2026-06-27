---
role: proof
locale: en
of_concept: cech-cohomology-isomorphism
source_book: gtm052
source_chapter: "III"
source_section: "4"
---

For $p = 0$ we have an isomorphism by (4.1). For the general case, embed $\mathcal{F}$ in a flasque, quasi-coherent sheaf $\mathcal{G}$ (3.6), and let $\mathcal{R}$ be the quotient:

$$0 \rightarrow \mathcal{F} \rightarrow \mathcal{G} \rightarrow \mathcal{R} \rightarrow 0.$$

For each $i_0 < \ldots < i_p$, the open set $U_{i_0, \ldots, i_p}$ is affine, since it is an intersection of affine open subsets of a separated scheme (II, Ex. 4.3). Since $\mathcal{F}$ is quasi-coherent, we therefore have an exact sequence

$$0 \rightarrow \mathcal{F}(U_{i_0, \ldots, i_p}) \rightarrow \mathcal{G}(U_{i_0, \ldots, i_p}) \rightarrow \mathcal{R}(U_{i_0, \ldots, i_p}) \rightarrow 0$$

of abelian groups, by (3.5) or (II, 5.6). Taking products, we find that the corresponding sequence of Čech complexes

$$0 \rightarrow C^*(\mathfrak{U}, \mathcal{F}) \rightarrow C^*(\mathfrak{U}, \mathcal{G}) \rightarrow C^*(\mathfrak{U}, \mathcal{R}) \rightarrow 0$$

is exact. Therefore we get a long exact sequence of Čech cohomology groups. Since $\mathcal{G}$ is flasque, its Čech cohomology vanishes for $p > 0$ by (4.2). The result then follows by induction on $p$ using the long exact sequence and the five lemma, comparing the Čech cohomology long exact sequence with the derived functor cohomology long exact sequence.

[Proof truncated in source: the remainder uses that $\check{H}^p(\mathfrak{U}, \mathcal{G}) = 0$ for $p > 0$ when $\mathcal{G}$ is flasque, together with the fact that $H^p(X, \mathcal{G}) = 0$ for $p > 0$ by (2.5), and proceeds by dimension-shifting induction.]
