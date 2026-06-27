---
role: proof
locale: en
of_concept: tensor-tor-as-homology
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "1. Complexes"
---

# Proof of Tensor Product and Tor as Homology of a Chain Complex

We give two constructions, using either a projective presentation of $B$ or a projective presentation of $A$; both yield $\operatorname{Tor}_\Lambda(B, A)$ as a homology group.

## Construction via a projective presentation of $B$

Let $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} B \to 0$ be a projective presentation of the right $\Lambda$-module $B$. Apply the covariant functor $- \otimes_\Lambda A$ to obtain the chain complex $D$:

$$
0 \longleftarrow B \otimes_\Lambda A \xleftarrow{\varepsilon \otimes 1} P \otimes_\Lambda A \xleftarrow{\mu \otimes 1} R \otimes_\Lambda A \longleftarrow 0,
$$

concentrated in degrees $0$ and $1$:

$$
D_0 = P \otimes_\Lambda A, \quad D_1 = R \otimes_\Lambda A, \quad \partial_1 = \mu \otimes 1, \quad D_n = 0 \text{ for } n \neq 0, 1.
$$

By the right exactness of $- \otimes_\Lambda A$, the sequence

$$
R \otimes_\Lambda A \xrightarrow{\mu \otimes 1} P \otimes_\Lambda A \xrightarrow{\varepsilon \otimes 1} B \otimes_\Lambda A \longrightarrow 0
$$

is exact. Hence $\varepsilon \otimes 1$ is surjective and $\operatorname{im}(\mu \otimes 1) = \ker(\varepsilon \otimes 1)$.

**Homology in degree 0:**

$$
H_0(D) = \frac{\ker \partial_0}{\operatorname{im} \partial_1} = \frac{D_0}{\operatorname{im}(\mu \otimes 1)} = \frac{P \otimes_\Lambda A}{\ker(\varepsilon \otimes 1)} \cong B \otimes_\Lambda A.
$$

**Homology in degree 1:**

$$
H_1(D) = \frac{\ker \partial_1}{\operatorname{im} \partial_2} = \frac{\ker(\mu \otimes 1)}{0} = \ker(\mu \otimes 1).
$$

By the characterization of $\operatorname{Tor}$ in terms of a projective presentation (Section III.7), we have $\ker(\mu \otimes 1) \cong \operatorname{Tor}_1^\Lambda(B, A)$. Thus

$$
H_1(D) \cong \operatorname{Tor}_1^\Lambda(B, A).
$$

**Homology for $n \neq 0, 1$:** $H_n(D) = 0$ since $D_n = 0$.

## Construction via a projective presentation of $A$

Dually, let $R' \to P' \to A \to 0$ be a projective presentation of the left $\Lambda$-module $A$. Apply $B \otimes_\Lambda -$ to obtain a chain complex $D'$ with

$$
H_0(D') \cong B \otimes_\Lambda A, \qquad H_1(D') \cong \operatorname{Tor}_1^\Lambda(B, A), \qquad H_n(D') = 0 \text{ for } n \neq 0, 1.
$$

The independence of the homology from the chosen projective presentation follows from the comparison theorem and will be fully treated in Sections 4 and 5 on derived functors.
