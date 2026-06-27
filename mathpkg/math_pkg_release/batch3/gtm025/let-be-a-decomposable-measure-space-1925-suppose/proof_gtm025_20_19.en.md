---
role: proof
locale: en
of_concept: "let-be-a-decomposable-measure-space-1925-suppose"
source_book: gtm025
source_chapter: "Integration Theory Continued"
source_section: "20.19"
---

(I) Suppose that $\mu(X) < \infty$. For $E \in \mathcal{A}$, define

$$\nu(E) = L(\xi_E).$$

(1)

We claim that $\nu$ is a complex measure on $(X, \mathcal{A})$ such that $\nu \ll \mu$. Let $\{E_n\}_{n=1}^{\infty}$ be a pairwise disjoint family of sets in $\mathcal{A}$, let $E = \bigcup_{n=1}^{\infty} E_n$, and let $F_p = \bigcup_{n=p+1}^{\infty} E_n$ for each $p \in N$. We have $F_1 \supset F_2 \supset \cdots$ and $\bigcap_{p=1}^{\infty} F_p = \varnothing$; it follows from (10.15) and the hypothesis $\mu(X) < \infty$ that

$$\left| \nu(E) - \sum_{n=1}^{p} \nu(E_n) \right| = \left| L(\xi_E) - L\left(\sum_{n=1}^{p} \xi_E_n \right) \right| = \left|
Invoking (1), we obtain

$$\|L\| \mu(A) < \sum_{j=1}^{n} |v(A_j)| = \sum_{j=1}^{n} |L(\xi_{A_j})| \leq \sum_{j=1}^{n} \|L\| \cdot \|\xi_{A_j}\|_1$$

$$= \|L\| \cdot \sum_{j=1}^{n} \mu(A_j) = \|L\| \mu(A).$$

This contradiction shows that $|g| \leq \|L\| \mu$-a.e., and so we suppose with no harm done that $|g(x)| \leq \|L\|$ for all $x \in X$.

It obviously follows from (1) and (2) that

$$L(s) = \int_X s\bar{g} d\mu$$

for all complex-valued, $\mathcal{A}$-measurable, simple functions $s$ defined on $X$. Now let $f \in \mathfrak{L}_1(X, \mathcal{A}, \mu)$, and use (11.35) to select a sequence $(s_n)_{n=1}^{\infty}$ of $\mathcal{A}$-measurable simple functions such that $|s_1| \leq |s_2| \leq \cdots \leq |f|$ and $s_n(x) \rightarrow f(x)$ for all $x \in X$. Plainly $|s_n\bar{g}| \leq \|L\| \cdot |f| \in \mathfrak{L}_1$ and $|f - s_n| \leq 2|f| \in \mathfrak{L}_1$ for all $n \in N$; hence (12.30), (4), and the continuity of $L$ imply that

$$L(f) = \lim_{n \to \infty} L(s_n) = \lim_{n \to \infty} \int_X s_n\bar{g} d\mu = \int_X f\bar{g} d\mu.$$

This proves the theorem for the case that $\mu(X) < \infty$.

(II) We now consider the general

and (12.30) show that

$$L(f) = \lim_{p \to \infty} L\left( \sum_{n=1}^{p} f \xi_{F_n} \right) = \lim_{p \to \infty} \sum_{n=1}^{p} L\left( f \xi_{F_n} \right)$$

$$= \lim_{p \to \infty} \sum_{n=1}^{p} \int_{F_n} f \bar{g} \, d\mu = \lim_{p \to \infty} \int_{X} \sum_{n=1}^{p} f \xi_{F_n} \bar{g} \, d\mu$$

$$= \int_{X} f \bar{g} \, d\mu.$$
