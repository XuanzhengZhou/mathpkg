---
role: proof
locale: en
of_concept: "consider-any-for-every-and-every-there-exists"
source_book: gtm025
source_chapter: "Spaces of Integrable Functions"
source_section: "13.20"
---

Note first that $\mathfrak{S} \cap \mathfrak{L}_p \subset \mathfrak{L}_p$. Suppose next that $f \geq 0$, $f \in \mathfrak{L}_p$. According to (11.35) there exists a nondecreasing sequence $(s_n)$ of nonnegative simple functions such that $s_n(x) \rightarrow f(x)$ $\mu$-a.e. For each $n \in N$ we have

$$|f - s_n|^p \leq f^p \in \mathfrak{L}_1.$$

It follows from Lebesgue's theorem on dominated convergence (12.24) that

$$\lim_{n \to \

If $\sigma = 0$, then $\sigma \in \mathfrak{C}_{00}(X)$ and the proof is complete. Thus suppose that $\|\sigma\|_u = M > 0$.

Let $E = \{x \in X : \sigma(x) \neq 0\}$. Since $\sigma \in \mathfrak{S} \cap \mathfrak{L}_p$, we have $\iota(E) < \infty$. We apply Luzin's theorem (11.36) to obtain a function $\varphi \in \mathfrak{C}_{00}$ such that $\|\varphi\|_u \leq M$ and if $A = \{x \in X : \varphi(x) \neq \sigma(x)\}$, then $\iota(A) < \left(\frac{\varepsilon}{4M}\right)^p$. We therefore have

$$\|f - \varphi\|_p \leq \|f - \sigma\|_p + \|\sigma - \varphi\|_p < \frac{\varepsilon}{2} + \left(\int_X |\sigma - \varphi|^p d\iota\right)^{\frac{1}{p}}$$

$$= \frac{\varepsilon}{2} + \left(\int_A |\sigma - \varphi|^p d\iota\right)^{\frac{1}{p}} \leq \frac{\varepsilon}{2} + \left(\int_A (2M)^p d\iota\right)^{\frac{1}{p}}$$

$$= \frac{\varepsilon}{2} + 2M \cdot \iota(A)^{\frac{1}{p}} < \varepsilon.$$
