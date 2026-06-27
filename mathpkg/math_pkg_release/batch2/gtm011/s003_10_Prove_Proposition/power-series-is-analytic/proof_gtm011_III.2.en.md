---
role: proof
locale: en
of_concept: power-series-is-analytic
source_book: gtm011
source_chapter: "III"
source_section: "2"
---

We may assume $a = 0$ and $R > 0$. For part (a), wish to show that $R^{-1} = \limsup |n a_n|^{1/(n-1)}$. It follows from l'Hopital's rule that $\lim_{n \to \infty} \frac{\log n}{n-1} = 0$, so that $\lim_{n \to \infty} n^{1/(n-1)} = 1$. The result follows if it can be shown that $\limsup |a_n|^{1/(n-1)} = R^{-1}$.

Let $(R')^{-1} = \limsup |a_n|^{1/(n-1)}$; then $R'$ is the radius of convergence of $\sum_{n=1}^{\infty} a_n z^{n-1} = \sum_{n=0}^{\infty} a_{n+1} z^n$. Notice that $z \sum a_{n+1} z^n + a_0 = \sum a_n z^n$; hence if $|z| < R'$ then $\sum |a_n z^n| = |a_0| + |z| \sum |a_{n+1} z^n| < \infty$. This gives $R' \leq R$. If $|z| < R$ and $z \neq 0$ then $\sum |a_n z^n| < \infty$ and $\sum |a_{n+1} z^n| = \frac{1}{|z|} \cdot \sum_{n \geq 1} |a_n z^n| + \frac{1}{|z|} |a_0| < \infty$, so that $R \leq R'$. This gives that $R = R'$ and completes the proof of part (a).

For part (b), define $g(z) = \sum_{n=1}^{\infty} n a_n z^{n-1}$ which has radius $R$ by part (a). Fix $w \in B(0; R)$ and $r$ with $|w| < r < R$. For $z$ near $w$, one shows that $[f(z) - f(w)]/(z-w) \to g(w)$ using power series manipulation and uniform convergence on $\{z: |z| \leq r\}$.

Part (c) follows by induction from (b).
