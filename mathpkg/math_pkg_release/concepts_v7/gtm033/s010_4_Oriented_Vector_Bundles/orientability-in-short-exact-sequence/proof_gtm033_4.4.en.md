---
role: proof
locale: en
of_concept: orientability-in-short-exact-sequence
source_book: gtm033
source_chapter: "4"
source_section: "4. Oriented Vector Bundles"
---

# Proof of Lemma 4.1 (Orientability in Short Exact Sequence)

Let

$$0 \to \xi' \xrightarrow{\alpha} \xi \xrightarrow{\beta} \xi'' \to 0$$

be a short exact sequence of vector bundles over a common base space $B$. For each $x \in B$, the fibre sequence

$$0 \to \xi'_x \xrightarrow{\alpha_x} \xi_x \xrightarrow{\beta_x} \xi''_x \to 0$$

is a short exact sequence of finite-dimensional real vector spaces.

**Construction of the orientation on the middle term.** Suppose $\xi'$ and $\xi''$ are orientable, with orientations $\omega' = \{\omega'_x\}_{x \in B}$ and $\omega'' = \{\omega''_x\}_{x \in B}$ respectively. For each $x \in B$, the orientation $\omega'_x \oplus \omega''_x$ of the fibre $\xi_x$ is defined as follows: choose an oriented basis $(e_1, \ldots, e_k)$ representing $\omega'_x$ and an oriented basis $(f_1, \ldots, f_m)$ representing $\omega''_x$. Lift each $f_j$ to a vector $\tilde{f}_j \in \xi_x$ with $\beta_x(\tilde{f}_j) = f_j$. Then

$$(e_1, \ldots, e_k, \tilde{f}_1, \ldots, \tilde{f}_m)$$

is a basis of $\xi_x$. Its orientation is independent of the choices of lifts, because any two lifts differ by an element of $\ker \beta_x = \operatorname{im} \alpha_x$, which only changes the basis by a triangular transformation with unit determinant. We set

$$\omega_x := \omega'_x \oplus \omega''_x.$$

**Coherence.** The family $\omega = \{\omega_x\}_{x \in B}$ is coherent. Indeed, over a sufficiently small open set $U \subset B$, the exact sequence admits simultaneous local trivializations of $\xi'$, $\xi$, and $\xi''$ such that $\alpha$ and $\beta$ correspond to the standard inclusion and projection of $\mathbb{R}^k$ into $\mathbb{R}^{k+m}$ and onto $\mathbb{R}^m$ respectively. In such a trivialization, the orientation $\omega_x$ is the constant standard orientation of $\mathbb{R}^{k+m}$, which is coherent. Hence $\omega$ is an orientation of $\xi$.

**Determination of the third orientation.** The same construction shows that any two of the orientations $\omega, \omega', \omega''$ determine the third uniquely:

- If $\xi$ and $\xi''$ are oriented, then $\xi' \cong \ker \beta$ inherits an orientation $\omega' = \omega / \omega''$ obtained by taking a basis of $\xi_x$ representing $\omega_x$, projecting to $\xi''_x$, and declaring the kernel orientation to be the one that, when summed with $\omega''_x$, yields $\omega_x$.
- If $\xi$ and $\xi'$ are oriented, the quotient $\xi'' \cong \xi / \alpha(\xi')$ inherits the quotient orientation $\omega'' = \omega / \omega'$.

**Conclusion.** Two of the bundles $\xi, \xi', \xi''$ are orientable if and only if the third is orientable. In particular, if two are orientable, specifying orientations on any two uniquely determines an orientation on the third via the $\oplus$ and $/$ operations described above.

QED
