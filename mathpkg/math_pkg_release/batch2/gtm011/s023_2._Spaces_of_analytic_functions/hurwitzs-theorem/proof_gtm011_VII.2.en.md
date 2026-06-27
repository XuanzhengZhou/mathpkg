---
role: proof
locale: en
of_concept: hurwitzs-theorem
source_book: gtm011
source_chapter: "VII"
source_section: "2"
---

Since $f(z) \neq 0$ on the compact circle $|z-a| = R$, there exists $\delta > 0$ such that $|f(z)| \geq \delta$ for all $|z-a| = R$. Because $f_n \to f$ uniformly on $\overline{B}(a; R)$ (a compact set), there exists $N$ such that for all $n \geq N$,

$$|f_n(z) - f(z)| < \delta \leq |f(z)|$$

for all $|z-a| = R$. By Rouch\'{e}'s Theorem, for each $n \geq N$, the functions $f$ and $f_n = f + (f_n - f)$ have the same number of zeros in $B(a; R)$, counting multiplicities.
