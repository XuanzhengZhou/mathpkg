---
role: proof
locale: en
of_concept: tor-vanishes-for-projectives
source_book: gtm004
source_chapter: "III"
source_section: "8"
---

# Proof that Tor Vanishes for Projective Modules (Proposition 8.1)

If $A$ (or $B$) is projective, then

$$
\operatorname{Tor}_\varepsilon^\Lambda(A, B) = 0 = \overline{\operatorname{Tor}}_\eta^\Lambda(A, B).
$$

**Proof.** We prove the statement for $\operatorname{Tor}_\varepsilon^\Lambda(A, B)$ when $A$ is projective; the other cases are analogous.

Let $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A$ be a projective presentation of $A$. Since $A$ is projective, the short exact sequence $0 \rightarrow R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A \rightarrow 0$ splits, i.e., there exists $\kappa : P \rightarrow R$ with $\kappa \mu = 1_R$.

Tensoring with $B$, we obtain

$$
\kappa \mu \otimes 1_B = (\kappa \otimes 1_B)(\mu \otimes 1_B) = 1_R \otimes 1_B = 1_{R \otimes_\Lambda B}.
$$

Thus $\mu \otimes 1_B : R \otimes_\Lambda B \rightarrow P \otimes_\Lambda B$ is a split monomorphism. But $\operatorname{Tor}_\varepsilon^\Lambda(A, B)$ is defined as the kernel of $\mu \otimes 1_B$:

$$
\operatorname{Tor}_\varepsilon^\Lambda(A, B) = \ker(\mu \otimes 1_B : R \otimes_\Lambda B \rightarrow P \otimes_\Lambda B).
$$

Since $\mu \otimes 1_B$ is monic, $\ker(\mu \otimes 1_B) = 0$, hence $\operatorname{Tor}_\varepsilon^\Lambda(A, B) = 0$.

The case where $B$ is projective follows by symmetry, using a projective presentation $S \rightarrow Q \rightarrow B$ and the definition of $\overline{\operatorname{Tor}}_\eta^\Lambda(A, B)$.
