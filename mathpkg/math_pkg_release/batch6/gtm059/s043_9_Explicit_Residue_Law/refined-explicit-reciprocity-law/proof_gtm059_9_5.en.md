---
role: proof
locale: en
of_concept: refined-explicit-reciprocity-law
source_book: gtm059
source_chapter: "9"
source_section: "§5"
---

**Proof.** First observe that the elements $-\pi_n$ form a vector of the norm of the tensor algebra. Instead of using Lemma 3.2, which relied on DL 5.1, we may now use directly the more precise relation DL 6 which gives an equality implying the stronger statement:

$$\begin{bmatrix} v, a_n \\ v, a_n \end{bmatrix} = \frac{1}{2} T_a(a_n) T_a(a_n - a_n) = \frac{1}{2} T_a(a_n - a_n) = [v, -a_n].$$

The value $d_{n-1} - a_n$ is here taken to be specifically $(1)^{n+1} \|U\|_2 (U, a_n)$, rather than up to a constant.

**Example 2.** Take $A = \mathbb{G}_m$ to be the formal multiplicative group. Then it satisfies the properties of Theorem 5.2, and we obtain the Artin-Hasse reciprocity law:

$$\begin{bmatrix} v, -a_n \end{bmatrix} = Q^{n-1}$$

where

$$[v, -a_n] = \frac{1}{p^{n-1}} T_a\left(\frac{1}{p} \log(1 + x)\right)$$

with $x = \zeta - 1$ where $\zeta$ is a primitive $p^{n-1}$-th root of unity.
