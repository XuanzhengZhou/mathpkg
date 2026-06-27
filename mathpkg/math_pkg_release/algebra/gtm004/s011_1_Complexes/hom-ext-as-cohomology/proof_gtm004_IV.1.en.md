---
role: proof
locale: en
of_concept: hom-ext-as-cohomology
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "1. Complexes"
---

# Proof of Hom and Ext as Cohomology of a Cochain Complex

Let $A, B$ be $\Lambda$-modules and let

$$
R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A \to 0
$$

be a projective presentation of $A$ (i.e. an exact sequence with $P$ projective). Apply the contravariant functor $\operatorname{Hom}_\Lambda(-, B)$ to obtain the cochain complex $C$:

$$
0 \longrightarrow \operatorname{Hom}_\Lambda(A, B) \xrightarrow{\varepsilon^*} \operatorname{Hom}_\Lambda(P, B) \xrightarrow{\mu^*} \operatorname{Hom}_\Lambda(R, B) \longrightarrow 0,
$$

concentrated in degrees $0$ and $1$: set

$$
C^0 = \operatorname{Hom}_\Lambda(P, B), \quad C^1 = \operatorname{Hom}_\Lambda(R, B), \quad \delta^0 = \mu^*, \quad C^n = 0 \text{ for } n \neq 0, 1.
$$

Since $\operatorname{Hom}_\Lambda(-, B)$ is left exact, the sequence

$$
0 \to \operatorname{Hom}_\Lambda(A, B) \xrightarrow{\varepsilon^*} \operatorname{Hom}_\Lambda(P, B) \xrightarrow{\mu^*} \operatorname{Hom}_\Lambda(R, B)
$$

is exact. Hence $\varepsilon^*$ is injective and $\operatorname{im} \varepsilon^* = \ker \mu^*$.

**Cohomology in degree 0:**

$$
H^0(C) = \frac{\ker \delta^0}{\operatorname{im} \delta^{-1}} = \frac{\ker \mu^*}{0} = \ker \mu^* \cong \operatorname{Hom}_\Lambda(A, B),
$$

the isomorphism being $\varepsilon^*$.

**Cohomology in degree 1:**

$$
H^1(C) = \frac{\ker \delta^1}{\operatorname{im} \delta^0} = \frac{\operatorname{Hom}_\Lambda(R, B)}{\operatorname{im} \mu^*} = \operatorname{coker} \mu^*.
$$

By the characterization of $\operatorname{Ext}$ in terms of a projective presentation (Section III.2), we have $\operatorname{coker} \mu^* \cong \operatorname{Ext}_\Lambda^1(A, B)$. Thus

$$
H^1(C) \cong \operatorname{Ext}_\Lambda^1(A, B).
$$

**Cohomology for $n \neq 0, 1$:** $H^n(C) = 0$ since $C^n = 0$.

Similarly, using an injective presentation $B \to I \to S$ and applying $\operatorname{Hom}_\Lambda(A, -)$, one obtains a cochain complex $C'$ with

$$
H^0(C') \cong \operatorname{Hom}_\Lambda(A, B), \qquad H^1(C') \cong \operatorname{Ext}_\Lambda^1(A, B), \qquad H^n(C') = 0 \text{ for } n \neq 0, 1.
$$

In both cases the cohomology is independent of the chosen resolution; this follows from the comparison theorem for projective (resp. injective) resolutions and will be fully generalized in Sections 4 and 5.
