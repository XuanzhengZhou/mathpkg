---
role: proof
locale: en
of_concept: ext-vanishes-for-integers
source_book: gtm004
source_chapter: "I"
source_section: "4. Computation of some Ext-Groups"
---

# Proof: $\operatorname{Ext}(\mathbb{Z}, B) = 0$ for any abelian group $B$

Here $\operatorname{Ext}$ denotes $\operatorname{Ext}_{\mathbb{Z}}$, the Ext functor over the ring of integers. Recall that $\operatorname{Hom}$ stands for $\operatorname{Hom}_{\mathbb{Z}}$.

## Statement

For any abelian group $B$,

$$\operatorname{Ext}(\mathbb{Z}, B) = 0.$$

In particular, $\operatorname{Ext}(\mathbb{Z}, \mathbb{Z}) = 0$ and $\operatorname{Ext}(\mathbb{Z}, \mathbb{Z}_q) = 0$ for any integer $q$.

## Proof

The group $\mathbb{Z}$ is a projective $\mathbb{Z}$-module (indeed, it is free of rank $1$, and free modules are projective). By Proposition 2.6, if the first argument of $\operatorname{Ext}$ is projective, then $\operatorname{Ext}$ vanishes. More explicitly:

A projective presentation of $\mathbb{Z}$ is simply

$$0 \longrightarrow 0 \longrightarrow \mathbb{Z} \xrightarrow{\;\mathrm{id}\;} \mathbb{Z} \longrightarrow 0,$$

since the identity map $\mathbb{Z} \to \mathbb{Z}$ is an epimorphism with zero kernel, and $\mathbb{Z}$ itself is projective. Applying $\operatorname{Hom}(-, B)$ to this presentation yields

$$\operatorname{Hom}(\mathbb{Z}, B) \longrightarrow \operatorname{Hom}(0, B) = 0 \longrightarrow \operatorname{Ext}(\mathbb{Z}, B) \longrightarrow 0.$$

But the first map $\operatorname{Hom}(\mathbb{Z}, B) \to 0$ is surjective (its image is $0$, which is all of the codomain), so the cokernel is $0$. Hence

$$\operatorname{Ext}(\mathbb{Z}, B) = 0.$$

Equivalently, one may appeal directly to Proposition 2.6, which states that $\operatorname{Ext}(P, B) = 0$ whenever $P$ is a projective module. Since $\mathbb{Z}$ is projective, the result follows immediately.
