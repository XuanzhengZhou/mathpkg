---
role: proof
locale: en
of_concept: realization-of-homology-via-free-chain-complexes
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "2. The Künneth Theorem"
---

# Proof of Realization of Graded Modules as Homology of Free Chain Complexes

**Proposition 2.2.** Let $\Lambda$ be a principal ideal domain and let $\{H_p\}_{p \in \mathbb{Z}}$ be a graded $\Lambda$-module, with each $H_p$ a finitely generated $\Lambda$-module. Then there exists a free chain complex $C$ over $\Lambda$ such that $H_p(C) \cong H_p$ for all $p$.

**Proof.** For each $p$, let
$$0 \to R_p \to F_p \to H_p \to 0$$
be a free presentation of $H_p$, where $F_p$ and $R_p$ are free $\Lambda$-modules.

Define the chain complex $C$ by setting
$$C_p = F_p \oplus R_{p-1},$$
with differential $\partial_p: C_p \to C_{p-1}$ given by
$$\partial_p(x, y) = (y, 0), \quad x \in F_p, \; y \in R_{p-1}.$$

Let us verify the chain complex condition: for any $(x, y) \in C_p$,
$$\partial_{p-1}\partial_p(x, y) = \partial_{p-1}(y, 0) = (0, 0),$$
so $\partial \partial = 0$.

Now compute the cycles and boundaries:
- The kernel of $\partial_p$ consists of those $(x, y) \in F_p \oplus R_{p-1}$ with $y = 0$. Hence $Z_p(C) = F_p \oplus 0 \cong F_p$.
- The image of $\partial_{p+1}$ consists of those $(y, 0) \in F_p \oplus R_{p-1}$ with $y \in R_p$ (since $R_p$ is the second component of $C_{p+1} = F_{p+1} \oplus R_p$, and $\partial_{p+1}(x, y) = (y, 0)$). Hence $B_p(C) = R_p \oplus 0 \cong R_p$.

Therefore
$$H_p(C) = Z_p(C)/B_p(C) \cong F_p/R_p \cong H_p,$$
as required.
