---
role: proof
locale: en
of_concept: chevalley-eilenberg-resolution
source_book: gtm004
source_chapter: "VII"
source_section: "4"
---

# Proof of the Chevalley–Eilenberg Resolution

**Theorem 4.2.** The complex

$$C: \cdots \to C_n \xrightarrow{d_n} C_{n-1} \to \cdots \to C_0 \xrightarrow{\varepsilon} K \to 0$$

is a $\mathfrak{g}$-projective resolution of the trivial $\mathfrak{g}$-module $K$, where:

- $C_n = U\mathfrak{g} \otimes_K E_n \mathfrak{g}$, with $E_n \mathfrak{g}$ the $n$-th exterior power of $\mathfrak{g}$ over $K$,
- $C_0 = U\mathfrak{g}$,
- $\varepsilon : U\mathfrak{g} \to K$ is the augmentation (killing the augmentation ideal),
- $d_n$ is defined by the explicit formula

$$d_n \langle x_1, \ldots, x_n \rangle = \sum_{i=1}^{n} (-1)^{i+1} x_i \langle x_1, \ldots, \hat{x}_i, \ldots, x_n \rangle + \sum_{1 \leq i < j \leq n} (-1)^{i+j} \langle [x_i, x_j], x_1, \ldots, \hat{x}_i, \ldots, \hat{x}_j, \ldots, x_n \rangle.$$

**Proof.** The proof proceeds in several steps.

**(a)** Each $C_n$ is a free $U\mathfrak{g}$-module (hence $\mathfrak{g}$-projective), since $C_n = U\mathfrak{g} \otimes_K E_n \mathfrak{g}$ where $E_n \mathfrak{g}$ is a $K$-vector space.

**(b)** Construction of the $\theta$-map. For $y \in \mathfrak{g}$, define $\theta(y) : C_n \to C_n$ by

$$\theta(y) \langle x_1, \ldots, x_n \rangle = -y \langle x_1, \ldots, x_n \rangle + \sum_{i=1}^{n} \langle x_1, \ldots, [y, x_i], \ldots, x_n \rangle.$$

One proves $\theta([x, y]) = \theta(x) \theta(y) - \theta(y) \theta(x)$ by direct computation using the Jacobi identity.

**(c)** Construction of $d_n$. The differentials $d_n$ are constructed inductively to satisfy

$$\sigma(y) d_{n-1} + d_n \sigma(y) = -\theta(y), \tag{4.4}$$

where $\sigma(y)$ denotes the left multiplication action of $y$ via $U\mathfrak{g}$. Starting from $d_0 = 0$ and $d_1 \langle x \rangle = x \cdot 1$, one defines $d_n$ on $\sigma(x_1) \langle x_2, \ldots, x_n \rangle$ by

$$d_n \sigma(x_1) \langle x_2, \ldots, x_n \rangle = (-\theta(x_1) - \sigma(x_1) d_{n-1}) \langle x_2, \ldots, x_n \rangle.$$

The explicit formula given above indeed satisfies this inductive definition.

**(d)** $d^2 = 0$. Using (4.4), one proves $d_{n-1} d_n = 0$ by induction:

$$\begin{aligned}
d_{n-1} d_n \sigma(x_1) \langle \cdots \rangle &= -d_{n-1}(\theta(x_1) + \sigma(x_1) d_{n-1}) \langle \cdots \rangle \\
&= (-d_{n-1} \theta(x_1) + \theta(x_1) d_{n-1} + \sigma(x_1) d_{n-2} d_{n-1}) \langle \cdots \rangle \\
&= 0
\end{aligned}$$

by the commutation $\theta(y) d_n = d_n \theta(y)$ (proved separately) and the induction hypothesis $d_{n-2} d_{n-1} = 0$.

**(e)** Exactness. The exactness of $C$ as a complex of $K$-vector spaces is proved via a filtration argument. Choose a basis $\{e_i\}_{i \in J}$ of $\mathfrak{g}$ with $J$ simply ordered. Define the filtration $F_p C$ by the number $m$ of $U\mathfrak{g}$-factors in the basis representation (4.8). Let $W^p = F_p C / F_{p-1} C$.

By Lemma 4.1, each $W^p$ is exact (via an explicit contracting homotopy $\Sigma$). The short exact sequence of complexes

$$0 \to F_{p-1} C \to F_p C \to W^p \to 0$$

induces a long exact homology sequence showing $H_n(F_{p-1} C) \cong H_n(F_p C)$ for all $n$, $p \geq 1$. Since $F_0 C \cong 0 \to K \xrightarrow{1} K \to 0$ has trivial homology, induction yields $H_n(F_p C) = 0$ for all $n$, $p$. Taking the union $C = \bigcup_p F_p C$, we conclude $H_n(C) = 0$ for all $n$. $\square$
