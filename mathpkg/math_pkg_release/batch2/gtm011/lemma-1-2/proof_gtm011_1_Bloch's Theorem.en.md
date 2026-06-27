---
role: proof
locale: en
of_concept: lemma-1-2
source_book: gtm011
source_chapter: "The Range of an Analytic Function"
source_section: "1. Bloch's Theorem"
---

Proof. Let $K(r) = \max \{|f'(z)| : |z| = r\}$ and let $h(r) = (1-r)K(r)$. It is easy to see that $h : [0, 1] \to \mathbb{R}$ is continuous, $h(0) = 1, h(1) = 0$. Let $r_0 = \sup \{r : h(r) = 1\}$; then $h(r_0) = 1, r_0 < 1$, and $h(r) < 1$ if $r > r_0$ (Why?). Let $a$ be chosen with $|a| = r_0$ and $|f'(a)| = K(r_0)$; then

1.5 $|f'(a)| = (1-r_0)^{-1}$.

Now if $|z-a| < \frac{1}{2}(1-r_0) = \rho_0$, $|z| < \frac{1}{2}(1+r_0)$; since $r_0 < \frac{1}{2}(1+r_0)$, the definition of $r_0$ gives

1.6 $|f'(z)| \leq K\left(\frac{1}{2}(1+r_0)\right)$
$= h\left(\frac{1}{2}(1+r_0)\right)[1-\frac{1}{2}(1+r_0)]^{-1}$
$< [1-\frac{1}{2}(1+r_0)]^{-1}$
$= 1/\rho_0$

for $|z-a| < \rho_0$. Combining (1.5) and (1.6) gives
$|f'(z)-f'(a)| \leq |f'(z)| + |f'(a)|$
$< 3/2\rho_0$.

According to Schwarz’s Lemma, this implies that
$|f'(z)-f'(a)| < \frac{3|z-a|}{2\rho_0^2}$

for $z$ in $B(a; \rho_0)$. Hence if $z \in S = B(a; \frac{1}{3
