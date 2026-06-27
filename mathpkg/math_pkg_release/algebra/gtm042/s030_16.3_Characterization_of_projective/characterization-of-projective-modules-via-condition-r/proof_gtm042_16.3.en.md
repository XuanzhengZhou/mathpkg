---
role: proof
locale: en
of_concept: characterization-of-projective-modules-via-condition-r
source_book: gtm042
source_chapter: "16"
source_section: "16.3"
---

By Proposition 44 it is enough to prove that
$$e(P_A^+(\mathbf{G})) = e(P_A(\mathbf{G})) \cap R_{K'}^+(\mathbf{G})$$
when $K$ is sufficiently large, in which case condition (R) just means that $d$ maps $R_{K'}^+(\mathbf{G})$ onto $R_{k'}^+(\mathbf{G})$.

Now let $x \in e(P_A(\mathbf{G})) \cap R_{K'}^+(\mathbf{G})$. Since $x \in e(P_A(\mathbf{G}))$, we can write $x$ as
$$x = \sum_{E \in S_k} n_E \, e([\tilde{P}_E]),$$
where $\tilde{P}_E$ denotes a projective $A[G]$-module whose reduction modulo $\mathfrak{m}$ is the projective envelope $P_E$ of $E$ (cf. 14.4). We must show that the integers $n_E$ are nonnegative.

By condition (R), for each $E \in S_k$ there exists $z_E \in R_{K'}^+(\mathbf{G})$ such that $d(z_E) = [E]$. Since $x \in R_{K'}^+(\mathbf{G})$, we have $\langle x, z_E \rangle_{K'} \geqslant 0$. On the other hand, the fact that $d$ and $e$ are adjoint shows that $\langle x, z_E \rangle_{K'} = n_E$. In particular $n_E$ is nonnegative, and the proof is complete.
