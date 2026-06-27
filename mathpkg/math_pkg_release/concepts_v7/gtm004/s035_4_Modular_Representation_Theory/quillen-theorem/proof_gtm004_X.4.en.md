---
role: proof
locale: en
of_concept: quillen-theorem
source_book: gtm004
source_chapter: "X. Survey of Some Applications"
source_section: "4. Modular Representation Theory"
---

# Proof of Theorem 4.2 (Quillen) — Krull Dimension and $p$-Rank

Let $G$ be a finite group and let $k$ be a field of characteristic $p$. Denote by $H^*(G, k)$ the cohomology ring of $G$ with coefficients in the trivial module $k$.

Recall that the Krull dimension $c(G)$ of $H^*(G, k)$ may be defined via the rate of growth of the sequence

$$d_n = \dim_k H^n(G, k), \quad n = 0, 1, 2, \ldots$$

The growth of a sequence $\{s_n\}$ of integers is the least nonnegative integer $c$ such that there exists a constant $C$ with

$$s_n \leq C n^{c-1}$$

for all $n \geq 0$. One takes $c(G) = \operatorname{growth}(\{d_n\})$.

**Theorem 4.2 (Quillen).** The Krull dimension $c(G)$ of $H^*(G, k)$ equals the maximum of the Krull dimensions $c(E)$ of $H^*(E, k)$, where $E$ runs through the elementary abelian $p$-subgroups of $G$.

*Proof (sketch).* The proof, due to Quillen [Q], is a major result that settled a conjecture of Atiyah and Swan. The argument proceeds via two main steps.

First, for an elementary abelian $p$-group $E$ of order $p^n$, one computes directly that $c(E) = n$. This can be seen from the structure of the cohomology ring $H^*(E, k)$: when $p \neq 2$, the even-dimensional part $H^{2*}(E, k)$ is a polynomial ring in $n$ variables, which has Krull dimension $n$; when $p = 2$, $H^*(E, k)$ itself is a polynomial ring in $n$ variables.

Second, for an arbitrary finite group $G$, one uses the restriction maps

$$\operatorname{res}_{G, E}: H^*(G, k) \longrightarrow H^*(E, k)$$

for each elementary abelian $p$-subgroup $E \leq G$. The key point of Quillen's theorem is that these restriction maps collectively detect the Krull dimension: the kernel of the product map

$$H^*(G, k) \longrightarrow \prod_E H^*(E, k)$$

is nilpotent. Consequently, the Krull dimension of $H^*(G, k)$ equals the maximal Krull dimension among the $H^*(E, k)$. Since $c(E) = \operatorname{rank}(E)$, the maximum over all elementary abelian $p$-subgroups equals the $p$-rank of $G$, i.e., the maximal rank of an elementary abelian $p$-subgroup of $G$. $\square$

Thus Quillen's theorem identifies a purely group-theoretic invariant — the $p$-rank — with the algebraic invariant $c(G)$ from the cohomology ring.
