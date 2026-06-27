---
role: proof
locale: en
of_concept: lemma-4-1-exactness-of-subquotient
source_book: gtm004
source_chapter: "VII"
source_section: "4"
---

# Proof of Lemma 4.1: Contracting Homotopy for the Subquotient Complex $W^p$

Let $\{e_i\}$, $i \in J$, be a $K$-basis of $\mathfrak{g}$ with $J$ simply ordered. By the Birkhoff–Witt Theorem, the elements

$$e_{k_1} \cdots e_{k_m} \langle e_{l_1}, \ldots, e_{l_n} \rangle$$

with $k_1 \leq k_2 \leq \cdots \leq k_m$ and $l_1 < l_2 < \cdots < l_n$ form a $K$-basis of $C_n$.

Define the filtration subcomplexes $F_p C$ as follows: $(F_p C)_{-1} = K$, and for $n \geq 0$, $(F_p C)_n$ is the subspace of $C_n$ spanned by those basis elements (4.8) with $m \leq p$. Let $W^p = F_p C / F_{p-1} C$ be the subquotient complex.

**Lemma 4.1.** $W^p$ is exact for all $p \geq 1$.

**Proof.** We define a $K$-linear contracting homotopy $\Sigma$ on $W^p$ as follows:

- $\Sigma_{-1} : K \to W_0^p$ is given by $\Sigma_{-1}(1_K) = 1 \langle \rangle$ (the empty bracket in degree 0).
- For $n \geq 0$, define $\Sigma_n : W_n^p \to W_{n+1}^p$ on the basis elements by

$$\Sigma_n\bigl(e_{k_1} \cdots e_{k_m} \langle e_{l_1}, \ldots, e_{l_n} \rangle\bigr) = \begin{cases}
0, & \text{if } k_m \leq l_n \text{ in } J \text{ (in particular if } m = 0\text{);} \\
(-1)^n e_{k_1} \cdots e_{k_m} \langle e_{l_1}, \ldots, e_{l_n}, e_{k_m} \rangle, & \text{if } k_m > l_n.
\end{cases}$$

One verifies the homotopy identities:

$$\varepsilon \Sigma_{-1} = 1_K, \quad d_{n+1} \Sigma_n + \Sigma_{n-1} d_n = 1_{W_n^p} \quad (n \geq 0).$$

The verification is a direct computation using the explicit formula for $d_n$ and the ordering of the basis. The key observation is that when $k_m > l_n$, the term $\langle e_{l_1}, \ldots, e_{l_n}, e_{k_m} \rangle$ has its indices in strictly increasing order (since $l_n < k_m$), and the sign $(-1)^n$ compensates for the position of the new element.

Thus $\Sigma$ is a contracting homotopy, which implies $H_n(W^p) = 0$ for all $n$, i.e., $W^p$ is exact. $\square$
