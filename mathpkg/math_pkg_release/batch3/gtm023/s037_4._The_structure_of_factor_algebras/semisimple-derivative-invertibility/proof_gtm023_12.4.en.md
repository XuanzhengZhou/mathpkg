---
role: proof
locale: en
of_concept: semisimple-derivative-invertibility
source_book: gtm023
source_chapter: "12"
source_section: "4. The structure of factor algebras"
---

If $a$ is semisimple, then the minimum polynomial $f$ of $a$ is the product of relatively prime irreducible polynomials. By Proposition V (sec. 12.9), $f$ and $f'$ are relatively prime. Thus, by Corollary I to Proposition II (sec. 12.8), there exist polynomials $p$ and $q$ such that

$$p f + q f' = 1.$$

Since $f(a) = 0$, it follows that $q(a) f'(a) = e$, so $f'(a)$ is invertible in $\Gamma(a)$.

Conversely, assume that $f'(a)$ is invertible in $\Gamma(a)$. Then there exists a polynomial $g$ such that $f'(a) g(a) = e$. Set $h = f' g - 1$. Then $h(a) = 0$, so $f$ divides $h$. Thus $h = f \cdot r$ for some polynomial $r$, giving $f' g - f r = 1$. This Bezout relation shows that $f$ and $f'$ are relatively prime. Hence $f$ cannot have repeated irreducible factors, so $a$ is semisimple.
