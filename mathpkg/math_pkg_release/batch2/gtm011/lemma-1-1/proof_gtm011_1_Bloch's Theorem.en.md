---
role: proof
locale: en
of_concept: lemma-1-1
source_book: gtm011
source_chapter: "The Range of an Analytic Function"
source_section: "1. Bloch's Theorem"
---

Proof. Let $0 < r < 1$ and $f(z) = z + a_2z^2 + \ldots$; according to Cauchy’s Estimate $|a_n| \leq M/r^n$ for $n \geq 1$. So $1 = |a_1| \leq M$. If $|z| = (4M)^{-1}$ then

$$|f(z)| \geq |z| - \sum_{n=2}^{\infty} |a_nz^n|$$

$$\geq (4M)^{-1} - \sum_{n=2}^{\infty} M(4M)^{-n}$$

$$= (4M)^{-1} - (16M - 4)^{-1}$$

$$\geq (6M)^{-1}$$

since $M \geq 1$.

Suppose $|w| < (6M)^{-1}$; it will be shown that $g(z) = f(z) - w$ has a zero. In fact, for $|z| = (4M)^{-1}$, $|f(z) - g(z)| = |w| < (6M)^{-1} \leq |f(z)|$. So, by Rouche’s Theorem, $f$ and $g$ have the same number of zeros in $B(0; 1/4M)$. Since $f(0) = 0$, $g(z_0) = 0$ for some $z_0$; hence $f(D) \supset B(0; 1/6M)$.
