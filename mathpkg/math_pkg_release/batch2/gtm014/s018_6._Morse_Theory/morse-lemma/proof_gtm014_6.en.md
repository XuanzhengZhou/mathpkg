---
role: proof
locale: en
of_concept: morse-lemma
source_book: gtm014
source_chapter: "6"
source_section: "6. Morse Theory"
---

The proof proceeds in two parts.

\textbf{Part (a).} A simple calculation using the chain rule gives the result when the Hessian is already diagonal.

\textbf{Part (b).} We prove the general case via a sequence of lemmas (Lemmas 6.10, 6.11, 6.12).

Let $U$ be a coordinate neighborhood of $p$ and $\psi: U \to \mathbb{R}^n$ a chart centered at $p$. Then $d^2(f \circ \psi^{-1})$ is a symmetric, nondegenerate bilinear form on $T_0 \mathbb{R}^n$. Choose a matrix $A$ which diagonalizes this form, i.e.,
$$d^2(f \circ \psi^{-1} \circ A) = \begin{pmatrix} -I_k & 0 \\ 0 & I_{n-k} \end{pmatrix}$$
where $I_s$ is the $s \times s$ identity matrix. Let $\eta = A^{-1} \circ \psi$; $\eta$ is also a chart on $U$.

Now Lemma 6.12 (proved by induction on $r$) provides the required smooth functions $h_i$ and completes the diagonalization, yielding the normal form
$$f(x) = f(p) - (h_1^2(x) + \cdots + h_k^2(x)) + h_{k+1}^2(x) + \cdots + h_n^2(x)$$
in a neighborhood of $p$. Setting $\alpha_i = h_i \circ \eta$ gives the desired coordinate chart.
