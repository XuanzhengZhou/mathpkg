---
role: proof
locale: en
of_concept: gamma-integral-sequence-convergence
source_book: gtm011
source_chapter: "7"
source_section: "7.17"
---

Think of $f_n(z)$ as the integral of $\varphi(t, z) = e^{-t} t^{z-1}$ along the straight line segment $[1/n, n]$ and apply Exercise IV.2.2 to conclude that $f_n$ is analytic. Now if $K$ is a compact subset of $G$ there are positive real numbers $a$ and $A$ such that $K \subset \{z: a \leq \text{Re } z \leq A\}$. Since

$$f_m(z) - f_n(z) = \int_{1/m}^{1/n} e^{-t} t^{z-1} \, dt + \int_{n}^{m} e^{-t} t^{z-1} \, dt$$

for $m > n$, Lemma 7.16 and Lemma 1.7 imply that $\{f_n\}$ is a Cauchy sequence in $H(G)$. But $H(G)$ is complete (Corollary 2.3) so that $\{f_n\}$ must converge.
