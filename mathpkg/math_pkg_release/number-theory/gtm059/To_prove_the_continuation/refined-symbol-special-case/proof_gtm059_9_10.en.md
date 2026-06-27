---
role: proof
locale: en
of_concept: refined-symbol-special-case
source_book: gtm059
source_chapter: "9"
source_section: "10"
---

First observe that the elements $-x_n$ form a vector
$$(-x_n - x_n) = T(X)Z,$$
i.e., is the norm of the corresponding tensor. Instead of using Lemma 3.2 (which relied on DL 5.1), we may now use directly the more precise relation DL 6 which gives an equality implying the stronger statement:
$$\begin{bmatrix} v, a_n \\ v, a_n \end{bmatrix} = \frac{1}{2} T_a(a_n) T_a(a_n - a_n)$$
$$= \frac{1}{2} T_a(a_n) T_a(a_n - a_n)$$
$$= \frac{1}{2} T_a(a_n - a_n)$$
$$= [v, -a_n].$$

The value $d_{n-1} - a_n$ is here taken to be specifically $(1)^{n+1} \|U\|_2 (U, a_n)$, rather than defined only up to a constant factor.

As an example, taking $A = \mathbb{G}_m$ to be the formal multiplicative group, the theorem yields another reciprocity law of Artin-Hasse type:
$$[v, -a_n] = Q^{n-1}$$
where
$$[v, -a_n] = \frac{1}{p^{n-1}} T_a\left(\frac{1}{p} \log(1 + x)\right),$$
$x_n = \zeta - 1$, and $\zeta$ is a primitive $p^{n-1}$-th root of unity.
