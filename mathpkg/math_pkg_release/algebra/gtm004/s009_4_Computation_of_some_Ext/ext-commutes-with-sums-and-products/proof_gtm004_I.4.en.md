---
role: proof
locale: en
of_concept: ext-commutes-with-sums-and-products
source_book: gtm004
source_chapter: "I"
source_section: "4. Computation of some Ext-Groups"
---

# Proof of Lemma 4.1

## Statement

1. $\operatorname{Ext}_A\left(\bigoplus_i A_i, B\right) \cong \prod_i \operatorname{Ext}_A(A_i, B)$,
2. $\operatorname{Ext}_A\left(A, \prod_j B_j\right) \cong \prod_j \operatorname{Ext}_A(A, B_j)$.

## Proof of (i)

We prove assertion (i), leaving the dual assertion (ii) to the reader.

For each $i$ in the index set, choose a projective presentation

$$R_i \longrightarrow P_i \longrightarrow A_i \longrightarrow 0$$

of $A_i$, where $P_i$ is projective and $R_i \to P_i$ is a monomorphism with image $\ker(P_i \to A_i)$. Taking the direct sum over $i$ yields the exact sequence

$$\bigoplus_i R_i \longrightarrow \bigoplus_i P_i \longrightarrow \bigoplus_i A_i \longrightarrow 0,$$

which is a projective presentation of $\bigoplus_i A_i$, since a direct sum of projective modules is projective and the direct sum of exact sequences is exact.

Now apply the functor $\operatorname{Hom}_A(-, B)$ to this projective presentation. By the definition of $\operatorname{Ext}$ via a projective presentation (Proposition 2.6), we obtain the exact sequence

$$\operatorname{Hom}_A\!\left(\bigoplus_i P_i, B\right) \longrightarrow \operatorname{Hom}_A\!\left(\bigoplus_i R_i, B\right) \longrightarrow \operatorname{Ext}_A\!\left(\bigoplus_i A_i, B\right) \longrightarrow 0.$$

By the universal property of the direct sum, there is a natural isomorphism

$$\operatorname{Hom}_A\!\left(\bigoplus_i P_i, B\right) \cong \prod_i \operatorname{Hom}_A(P_i, B),$$

and similarly for $R_i$ in place of $P_i$. Under these isomorphisms the above exact sequence becomes

$$\prod_i \operatorname{Hom}_A(P_i, B) \;\xrightarrow{\;\prod_i \alpha_i^*\;}\; \prod_i \operatorname{Hom}_A(R_i, B) \longrightarrow \operatorname{Ext}_A\!\left(\bigoplus_i A_i, B\right) \longrightarrow 0,$$

where $\alpha_i: R_i \to P_i$ is the inclusion in the chosen projective presentation and $\alpha_i^* = \operatorname{Hom}_A(\alpha_i, B)$.

On the other hand, for each individual $A_i$ we have the defining exact sequence

$$\operatorname{Hom}_A(P_i, B) \xrightarrow{\alpha_i^*} \operatorname{Hom}_A(R_i, B) \longrightarrow \operatorname{Ext}_A(A_i, B) \longrightarrow 0,$$

so that $\operatorname{Ext}_A(A_i, B) \cong \operatorname{coker}(\alpha_i^*)$. Taking the product over $i$ of these exact sequences, we obtain

$$\prod_i \operatorname{Hom}_A(P_i, B) \xrightarrow{\prod_i \alpha_i^*} \prod_i \operatorname{Hom}_A(R_i, B) \longrightarrow \prod_i \operatorname{Ext}_A(A_i, B) \longrightarrow 0.$$

Thus both $\operatorname{Ext}_A(\bigoplus_i A_i, B)$ and $\prod_i \operatorname{Ext}_A(A_i, B)$ appear as the cokernel of the same map $\prod_i \alpha_i^*$. By the uniqueness of the cokernel (up to canonical isomorphism), we conclude

$$\operatorname{Ext}_A\!\left(\bigoplus_i A_i, B\right) \;\cong\; \prod_i \operatorname{Ext}_A(A_i, B).$$

## Proof of (ii)

The proof of (ii) is dual. For each $j$, choose an injective presentation of $B_j$:

$$0 \longrightarrow B_j \longrightarrow Q_j \longrightarrow S_j \longrightarrow 0$$

where $Q_j$ is injective. Apply $\operatorname{Hom}_A(A, -)$ and argue dually, using the fact that

$$\operatorname{Hom}_A\!\left(A, \prod_j Q_j\right) \cong \prod_j \operatorname{Hom}_A(A, Q_j)$$

since the product in the second argument of Hom is preserved. This yields

$$\operatorname{Ext}_A\!\left(A, \prod_j B_j\right) \cong \prod_j \operatorname{Ext}_A(A, B_j).$$
