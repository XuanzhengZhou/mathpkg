---
role: proof
locale: en
of_concept: "for-every-we-have"
source_book: gtm025
source_chapter: "Extending Functionals"
source_section: "9.24"
---

If $\iota(A) = \infty$, then the result is trivial since $A \subset X$, $X$ is open, and $\infty = \iota(A) \leq \iota(X) = \infty$. Thus suppose that $\iota(A) < \infty$ and let $\varepsilon > 0$ be arbitrary. Choose a real number $\delta$ such that $0 < \delta < \frac{\varepsilon}{1 + \varepsilon + \iota(A)} < 1$. Next select $g \in \mathfrak{M}^+$ such that $g \geq \xi_{A}$ and $\bar{I}(g) - \delta < \bar{I}(\xi_{A}) = \iota

Proof. Take any real number $\beta$ such that $\beta < \iota(U)$. Since $U$ is open, we have $\iota(U) = \bar{I}(\xi_U) = \sup\{I(f) : f \in \mathfrak{C}_{00}^+, f \leq \xi_U\}$. Thus we can choose $f \in \mathfrak{C}_{00}^+$ such that $\beta < I(f) \leq \iota(U)$. For $n = 1, 2, 3, \ldots$, define $F_n = \{x \in X : f(x) \geq \frac{1}{n}\}$, and $W_n = \{x \in X : f(x) > \frac{1}{n}\}$; $F_n$ is compact, $W_n$ is open, and $W_n^-$ is compact. Let $W = \{x \in X : f(x) > 0\}$. It is clear that $\lim_{n \to \infty} \xi_{F_n}(x) = \lim_{n \to \infty} \xi_{W_n}(x) = \xi_W(x)$ for each $x \in X$, and it is clear too that the sequences are nondecreasing. Applying (9.17), we have

$$\beta < I(f) \leq \bar{I}(\xi_W) = \lim_{n \to \infty} \bar{I}(\xi_{F_n}) = \lim_{n \to \infty} \bar{I}(\xi_{W_n}) = \lim_{n \to \infty} \iota(F_n) = \lim_{n \to \infty} \iota(W_n).$$

The theorem follows from these inequalities. $\square$
