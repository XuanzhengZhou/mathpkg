---
role: proof
locale: en
of_concept: basis-of-k-forms
source_book: gtm035
source_chapter: "4"
source_section: "4.6"
---

# Proof of Basis of k-Forms

**Lemma 4.6.** Fix $k$. The set of elements

$$e_{i_1} \wedge e_{i_2} \wedge \cdots \wedge e_{i_k}, \quad 1 \leq i_1 < i_2 < \cdots < i_k \leq N,$$

forms a basis for $\wedge^k(V)$.

## Proof

Let $\{e_1, \ldots, e_N\}$ be a basis for $\wedge^1(V) = V^*$. We must show that the stated wedge products form a basis for $\wedge^k(V)$.

**Step 1: Linear independence.** Suppose
$$\sum_{1 \leq i_1 < \cdots < i_k \leq N} c_{i_1 \cdots i_k} \; e_{i_1} \wedge \cdots \wedge e_{i_k} = 0$$
for scalars $c_{i_1 \cdots i_k} \in \mathbb{C}$. Fix a multi-index $J = (j_1, \ldots, j_k)$ with $1 \leq j_1 < \cdots < j_k \leq N$. Let $\{v_1, \ldots, v_N\}$ be the dual basis of $V$ (so that $e_i(v_j) = \delta_{ij}$). Evaluate both sides on $(v_{j_1}, \ldots, v_{j_k})$.

For any ordered $k$-tuple of basis vectors, the determinant-like evaluation gives
$$(e_{i_1} \wedge \cdots \wedge e_{i_k})(v_{j_1}, \ldots, v_{j_k}) = \det\begin{pmatrix}
e_{i_1}(v_{j_1}) & \cdots & e_{i_1}(v_{j_k}) \\
\vdots & \ddots & \vdots \\
e_{i_k}(v_{j_1}) & \cdots & e_{i_k}(v_{j_k})
\end{pmatrix}.$$

This determinant equals $\operatorname{sgn}(\pi)$ if $(i_1, \ldots, i_k)$ is a permutation $\pi$ of $(j_1, \ldots, j_k)$, and $0$ otherwise. Since $i_1 < \cdots < i_k$ and $j_1 < \cdots < j_k$, the only way for $\{i_1, \ldots, i_k\}$ to equal $\{j_1, \ldots, j_k\}$ is if $i_r = j_r$ for all $r$. In that case, the determinant equals $1$.

Hence applying the linear combination to $(v_{j_1}, \ldots, v_{j_k})$ yields $c_{j_1 \cdots j_k} = 0$. Since $J$ was arbitrary, all coefficients vanish, proving linear independence.

**Step 2: Spanning.** Let $\omega \in \wedge^k(V)$. Define coefficients
$$c_{i_1 \cdots i_k} = \omega(v_{i_1}, \ldots, v_{i_k})$$
for $1 \leq i_1 < \cdots < i_k \leq N$. We claim that
$$\omega = \sum_{1 \leq i_1 < \cdots < i_k \leq N} c_{i_1 \cdots i_k} \; e_{i_1} \wedge \cdots \wedge e_{i_k}.$$

Both sides are $k$-linear alternating maps on $V$. By multilinearity, it suffices to verify the equality on $k$-tuples of basis vectors $(v_{j_1}, \ldots, v_{j_k})$ with $j_1 < \cdots < j_k$. Evaluating the right-hand side gives $c_{j_1 \cdots j_k} = \omega(v_{j_1}, \ldots, v_{j_k})$, which matches the left-hand side. For $k$-tuples that are not in strictly increasing order, the alternating property ensures consistency.

Thus the set of strictly increasing wedge products spans $\wedge^k(V)$.

Therefore $\{e_{i_1} \wedge \cdots \wedge e_{i_k} : 1 \leq i_1 < \cdots < i_k \leq N\}$ is a basis for $\wedge^k(V)$. Consequently, $\dim \wedge^k(V) = \binom{N}{k}$. $\square$
