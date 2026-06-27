---
role: proof
locale: en
of_concept: homotopy-invariance-of-hopf-invariant
source_book: gtm020
source_chapter: "15"
source_section: "1.3"
---

**Proof.** View $f_t$ as a map $f: (S^{2n-1} \times I)_* \to S^n$, where $(S^{2n-1} \times I)_*$ denotes the reduced cylinder $(S^{2n-1} \times I)/(* \times I)$. Define $j_t: S^{2n-1} \to (S^{2n-1} \times I)_*$ by $j_t(x) = [x, t]$, the class of $(x, t)$. Then $j_t$ is a homotopy equivalence (in fact a homotopy inverse of the projection $(x,t) \mapsto x$), and $f_t = f \circ j_t$.

For each $t$, let $k_t: C_{f_t} \to C_f$ be the map of mapping cones induced by the commutative square

\[
\begin{array}{ccc}
S^{2n-1} & \xrightarrow{f_t} & S^n \\
\downarrow j_t & & \downarrow \mathrm{id} \\
(S^{2n-1} \times I)_* & \xrightarrow{f} & S^n
\end{array}
\]

Applying reduced $K$-theory and the exact sequence of the mapping cone, we obtain the commutative diagram

\[
\begin{array}{ccccccc}
0 & \leftarrow & \tilde{K}(S^n) & \xleftarrow{\phi_t} & \tilde{K}(C_{f_t}) & \xleftarrow{\psi_t} & \tilde{K}(S^{2n}) \\
& & \uparrow \mathrm{id} & & \uparrow k_t^* & & \uparrow (S j_t)^* \\
0 & \leftarrow & \tilde{K}(S^n) & \xleftarrow{\phi} & \tilde{K}(C_f) & \xleftarrow{\psi} & \tilde{K}(S^{2n})
\end{array}
\]

Since $j_t$ is a homotopy equivalence, the suspension $S j_t$ is also a homotopy equivalence, so $(S j_t)^*$ is an isomorphism on $\tilde{K}(S^{2n})$. By the five-lemma applied to the exact sequences, $k_t^*: \tilde{K}(C_f) \to \tilde{K}(C_{f_t})$ is an isomorphism of rings.

Now let $a(f) \in \tilde{K}(C_f)$ denote the element corresponding to $\beta_n$ under $\phi$ (for $n$ even; the case $n$ odd is trivial since $h_f = 0$), and let $b(f) = \psi(\beta_{2n})$. By definition,
\[
k_t^* b(f_t) = b(f), \qquad k_t^* a(f_t) = a(f) \pmod{\langle b(f) \rangle}.
\]
Applying $k_t^*$ to the relation $a(f_t)^2 = h(f_t) \, b(f_t)$ yields
\[
a(f)^2 = h(f_t) \, b(f) \quad \text{in } \tilde{K}(C_f).
\]
But $a(f)^2 = h(f) \, b(f)$ by definition of $h(f)$. Since $b(f)$ generates a free $\mathbb{Z}$-submodule and $h(f), h(f_t)$ are integers, we conclude $h(f_t) = h(f)$ for all $t \in I$. In particular, $h(f_0) = h(f_1)$.
