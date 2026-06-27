---
role: proof
locale: en
of_concept: u-duality-between-reflexive-modules
source_book: gtm013
source_chapter: "23"
source_section: "23.1"
---
Let $R$ and $S$ be rings and let ${}_R U_S$ be a bimodule. Set
$$H' = \operatorname{Hom}_R(-, U): {}_R \mathcal{M} \to \mathcal{M}_S, \qquad H'' = \operatorname{Hom}_S(-, U): \mathcal{M}_S \to {}_R \mathcal{M}.$$

For each ${}_R M$, define the evaluation map $\sigma_M: M \to H''H'(M)$ via
$$\sigma_M(x)(f) = f(x)$$
for $x \in M$, $f \in H'(M) = \operatorname{Hom}_R(M, U)$. Similarly, for each $N_S$, define $\sigma_N: N \to H' H''(N)$ via
$$\sigma_N(y)(g) = g(y)$$
for $y \in N$, $g \in H''(N) = \operatorname{Hom}_S(N, U)$. These are natural homomorphisms (see Section 20), i.e., they define natural transformations
$$\sigma: 1_{{}_R \mathcal{M}} \to H''H', \qquad \sigma: 1_{\mathcal{M}_S} \to H' H''.$$

Now let ${}_R \mathcal{R}[U]$ and $\mathcal{R}_S[U]$ be the full subcategories of ${}_R \mathcal{M}$ and $\mathcal{M}_S$ whose objects are the $U$-reflexive modules. By the definition of $U$-reflexive modules, the evaluation maps $\sigma_M$ and $\sigma_N$ are isomorphisms precisely for $M \in {}_R \mathcal{R}[U]$ and $N \in \mathcal{R}_S[U]$. Thus $H''H' \cong 1_{{}_R \mathcal{R}[U]}$ and $H'H'' \cong 1_{\mathcal{R}_S[U]}$ on these subcategories. By (20.14), $H'$ and $H''$ restrict to functors between ${}_R \mathcal{R}[U]$ and $\mathcal{R}_S[U]$, and the natural isomorphisms above establish that they form a duality.
