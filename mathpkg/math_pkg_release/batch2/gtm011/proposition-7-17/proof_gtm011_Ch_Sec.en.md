---
role: proof
locale: en
of_concept: proposition-7-17
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Think of $f_n(z)$ as the integral of $\varphi(t, z) = e^{-t} t^{z-1}$ along the straight line segment $\left[ \frac{1}{n}, n \right]$ and apply Exercise IV. 2.2 to conclude that $f_n$ is analytic. Now if $K$ is a compact subset of $G$ there are positive real numbers $a$ and $A$ such that $K \subset \{z: a \leq \text{Re } z \leq A\}$. Since

$$f_m(z) - f_n(z) = \int_{1/m}^{1/n} e^{-t} t^{z-1} dt + \int_{n}^{m} e^{-t} t^{z-1} dt$$

for $m > n$, Lemma 7.16 and Lemma 1.7 imply that $\{f_n\}$ is a Cauchy sequence in $H(G)$. But $H(G)$ is complete (Corollary 2.3) so that $\{f_n\}$ must converge.

If $f$ is the limit of the functions $\{f_n\}$ from the above proposition then define the integral to be this function. That is,

7.18

$$f(z) = \int_{0}^{\infty} e^{-t

The gamma function

Theorem 7.15 is proved. This is indeed the case and it follows from the following lemma.
