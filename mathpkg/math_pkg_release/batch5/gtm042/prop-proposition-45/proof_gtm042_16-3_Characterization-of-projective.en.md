---
role: proof
locale: en
of_concept: prop-proposition-45
source_book: gtm042
source_chapter: "16.3"
source_section: "Characterization of projective"
---

By prop. 44 it is enough to prove that

$$e(P_A^+(\mathbf{G})) = e(P_A(\mathbf{G})) \cap R_{K'}^+(\mathbf{G})$$

when $K$ is sufficiently large, in which case condition (R) just means that $d$ maps $R_{K'}^+(\mathbf{G})$ onto $R_{k'}^+(\mathbf{G})$. Now let

$$x \in e(P_A(\mathbf{G})) \cap R_{K'}^+(\mathbf{G})$$.

Since $x \in e(P_A(\mathbf{G}))$, we can write $x$ as

$$x = \sum_{E \in S_k} n_E e([\tilde{P}_E])$$,

where $\tilde{P}_E$ denotes a projective A[G]-module whose reduction mod. $m$ is the projective envelope $P_E$ of $E$ (cf. 14.4). We must show that the integers $n_E$ are nonnegative. By (R), for each $E \in S_k$ there exists $z_E \in R_{K'}^+(\mathbf{G})$ such that $d(z_E) = [E]$. Since $x \in R_{k'}^+(\mathbf{G})$, we have $\langle x, z_E \rangle_K \geqslant 0$. On the other hand, the fact that $d$ and $e$ are adjoint shows that $\langle x, z_E \rangle_K = n_E$. In particular $n_E$ is non-negative, and the proof is complete.

Combining prop. 45 and th.

16.6. Show that, for $K$ sufficiently large, condition (R) is equivalent to the condition $e(P_A^+(G)) = e(P_A(G)) \cap R_K^+(G)$. (Observe that an element $x$ of $P_k(G)$ belongs to $P_k^+(G)$ if and only if $\langle x, y \rangle_k \geq 0$ for all $y \in R_k^+(G)$.)

16.7. Take for $G$ the group $SL(V)$ where $V$ is a vector space of dimension 2 over the field $F_p = Z/pZ$. Show that the natural representations of $G$ in the $i$th symmetric powers $V_i$ of $V$ are absolutely irreducible for $i < p$. (Since the number of $p$-regular classes of $G$ is $p$, it follows that these are, up to isomorphism, all the irreducible representations of $G$, cf. 18.2, cor. 2 to th. 42.) Give examples where these representations cannot be lifted to characteristic zero even over a sufficiently large field $K$. (For $p = 7$, $i = 4$, we have $\dim V_i = 5$, and 5 does not divide the order of $G$; hence $V_i$ cannot be lifted.)

16.4 Examples of projective $A[G]$-modules: irreducible representations of defect zero

In this section we assume that $K$ is sufficiently large.
