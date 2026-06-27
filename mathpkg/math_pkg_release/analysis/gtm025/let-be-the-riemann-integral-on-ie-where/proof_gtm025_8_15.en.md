---
role: proof
locale: en
of_concept: "let-be-the-riemann-integral-on-ie-where"
source_book: gtm025
source_chapter: "Riemann-Stieltjes Integral"
source_section: "8.15"
---

Conclusions (i) and (ii) are contained in (8.13). To prove (iii), let $f \in \mathfrak{C}_{00}^{+}(R)$ where $f$ is not the zero function. Then there exists $u \in R$ such that $f(u) > 0$. Since $f$ is continuous at $u$, there is some neighborhood $]u - \delta, u + \delta[$ of $u$ such that $f(x) > \frac{1}{2} f(u)$ whenever $u - \delta < x < u + \delta$. Suppose that $f$ vanishes off of $[a, b]$, where $a

such that $|f(x) - f(y)| < \frac{\varepsilon}{\alpha(b) - \alpha(a) + 1}$ whenever $|x - y| < \delta$. Because $D$ is dense in $R$, there exists a subdivision $\Delta = \{a = t_0 < \cdots < t_n = b\} \subset D$ such that $t_j - t_{j-1} < \delta$ for $j = 1, 2, \ldots, n$. Then, as in the proof of (8.7), it follows that

$$U(f, \alpha, \Delta) - L(f, \alpha, \Delta) < \varepsilon.$$

Since $\Delta \subset D$, we have $U(f, \beta, \Delta) = U(f, \alpha, \Delta)$ and $L(f, \beta, \Delta) = L(f, \alpha, \Delta)$. Therefore $|S_\beta(f) - S_\alpha(f)| < \varepsilon$ [see (8.6)]. Since $\varepsilon$ is arbitrary, the theorem is proved. $\square$

We next examine a few interesting properties of nondecreasing functions. First, a definition is in order.
