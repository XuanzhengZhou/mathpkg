---
role: proof
locale: en
of_concept: koszul-resolution
source_book: gtm004
source_chapter: "VII"
source_section: "7"
---

# Proof of the Koszul Resolution

**Proposition 7.2 (Koszul).** Let $P = K[x_1, \ldots, x_m]$ be the polynomial ring in $m$ variables over a field $K$, regarded as a graded $K$-algebra. Let $D_n = P \otimes_K E_n \mathfrak{a}$, where $\mathfrak{a}$ is the $K$-vector space with basis $\{x_1, \ldots, x_m\}$ (regarded as an abelian Lie algebra), and let $d_n : D_n \to D_{n-1}$ be defined by

$$d_n(p \otimes \langle x_{j_1}, \ldots, x_{j_n} \rangle) = \sum_{i=1}^{n} (-1)^{i+1} p x_{j_i} \otimes \langle x_{j_1}, \ldots, \hat{x}_{j_i}, \ldots, x_{j_n} \rangle,$$

where $j_1 < j_2 < \cdots < j_n$. Then

$$D : 0 \to D_m \to D_{m-1} \to \cdots \to D_0 \xrightarrow{\varepsilon} K \to 0$$

is a $P$-free resolution of $K$ (regarded as graded $P$-module via the augmentation $\varepsilon$).

**Proof.** Note that $P$ may be regarded as the universal enveloping algebra of the abelian Lie algebra $\mathfrak{a}$ (where $x_1, \ldots, x_m$ form a $K$-basis of $\mathfrak{a}$ and $[x_i, x_j] = 0$ for all $i, j$). The Lie algebra resolution for $\mathfrak{a}$ given by Theorem 4.2 reduces to the Koszul complex because all Lie brackets vanish, so the second sum in the formula for $d_n$ disappears.

Explicitly, since $\mathfrak{a}$ is abelian, $U\mathfrak{a} = P$ and the exterior powers $E_n \mathfrak{a}$ are free $K$-modules of rank $\binom{m}{n}$. The differential simplifies to

$$d_n(p \otimes \langle x_{j_1}, \ldots, x_{j_n} \rangle) = \sum_{i=1}^{n} (-1)^{i+1} p x_{j_i} \otimes \langle x_{j_1}, \ldots, \hat{x}_{j_i}, \ldots, x_{j_n} \rangle.$$

The exactness follows from Theorem 4.2, since the Chevalley–Eilenberg complex for an abelian Lie algebra is automatically exact (the subquotients $W^p$ are still exact via the same homotopy construction).

A direct proof can be given by constructing a contracting homotopy similar to the one used in Lemma 4.1 (see Exercise 7.1). $\square$

**Remark.** The Koszul resolution is the standard tool for computing Tor over polynomial rings. It shows that $\operatorname{Tor}_n^P(K, K) \cong E_n \mathfrak{a}$ and that the global dimension of $P$ is exactly $m$.
