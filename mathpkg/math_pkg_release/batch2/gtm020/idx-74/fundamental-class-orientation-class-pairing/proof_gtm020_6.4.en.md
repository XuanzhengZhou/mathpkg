---
role: proof
locale: en
of_concept: fundamental-class-orientation-class-pairing
source_book: gtm020
source_chapter: "6"
source_section: "6.4"
---

We have the following commutative diagram where $f_x: M \to M \times M$ is defined by $f_x(y) = (x, y)$:

\[
\begin{array}{ccc}
H^*(D(\tau), D_0(\tau)) & \xleftarrow{h_t^*} & H^*(M \times M, M \times M - \Delta) & \xrightarrow{j^*} & H^*(M \times M) \\[4pt]
\downarrow & & \downarrow & & \downarrow \\[4pt]
H^*(D(\tau)_x, D_0(\tau)_x) & \xleftarrow{\approx} & H^*(M, M - \{x\}) & \xrightarrow{j^*} & H^*(M)
\end{array}
\]

In $H^*(D(\tau)_x, S(\tau)_x)$ we have $\exp_x^*(\bar{\omega}_x) = j_x^*(U)$. Consequently,
$$\langle (\exp_x^*)^{-1} j_x^*(U), \omega_x \rangle = 1$$
and
$$\langle j^*(\exp_x^*)^{-1} j_x^*(U), \omega_M \rangle = 1$$
for the pairing $H^n(M) \otimes H_n(M) \to R$.

By naturality of the construction and the definition $U_M = j^* ((h_t)^*)^{-1}(U)$, the evaluation $\langle U_M, 1 \times \omega_M \rangle$ corresponds to the above local pairing, yielding
$$\langle U_M, 1 \times \omega_M \rangle = 1.$$
