---
role: proof
locale: en
of_concept: oscillation-riemann-integrability-lemma
source_book: gtm002
source_chapter: "7"
source_section: "7. Functions of First Class"
---

Suppose the contrary. Then $F(I) \geq \varepsilon|I|$, and so $F(I_1) \geq \varepsilon|I|/2$ for at least one of the intervals $I_1$ obtained by bisecting $I$. Similarly, $F(I_2) \geq \varepsilon|I|/2^2$ for at least one of the intervals $I_2$ obtained by bisecting $I_1$. By repeated bisection we obtain a nested sequence of closed intervals $I_n$ such that $F(I_n) \geq \varepsilon|I|/2^n$ ($n=1, 2, \ldots$). These intersect in a point $x$ of $I$. By hypothesis, $\omega(x) < \varepsilon$ and therefore $\omega(J) < \varepsilon$ for some open interval $J$ containing $x$. Choose $n$ so that $I_n \subset J$. Then

$$F(I_n) \leq \omega(I_n) |I_n| \leq \omega(J) |I|/2^n < \varepsilon|I|/2^n,$$

contradicting $F(I_n) \geq \varepsilon|I|/2^n$. Hence $F(I) < \varepsilon|I|$.
