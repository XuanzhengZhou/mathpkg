---
role: proof
locale: en
of_concept: "let-for-every-there-exists-a-depending-only"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.34"
---

For $n = 1, 2, \ldots$, let

$$\psi_n(x) = \begin{cases} |f(x)| & \text{if } |f(x)| \leq n, \\ n & \text{otherwise.} \end{cases}$$

Then $(\psi_n)$ is a nondecreasing sequence of $\mathcal{A}$-measurable functions and $\lim_{n \to \infty} \psi_n = |f|$. By (12.22), we have

$$\lim_{n \to \infty} \int_X \psi_n d\mu = \int_X \lim_{n \to \infty} \psi_n d\mu = \int_X |f| d\mu.$$

Select $n$ so that $\int_X (|f| - \psi_n) d\mu < \frac{1}{2} \varepsilon$. Setting $\delta = \frac{\varepsilon}{2n}$ and choosing any $E \in \mathcal{A}$ such that $\mu(E) < \delta$, we have

$$\int_E \psi_n d\mu \leq \int_E n d\mu = n \mu(E) < \frac{1}{2} \varepsilon.$$

It follows that

$$\left| \int_E f d\mu \right| \leq \int_E |

where $A_{n,k} = \left\{x \in X : \frac{k-1}{2^n} \leq f(x) < \frac{k}{2^n}\right\}$ and $B_n = \{x \in X : f(x) \geq n\}$. By (10.35) and (12.4), we have

$$\bar{I}(s_n) = \int_X s_n d\iota \quad \text{for all} \quad n \in N.$$

By (9.17), we have

$$\lim_{n \to \infty} \bar{I}(s_n) = \bar{I}(f).$$

By (12.11), we have

$$\lim_{n \to \infty} \int_X s_n d\iota = \int_X f d\iota.$$

Combining these equalities, we have (i). $\square$

Theorem (12.35) is a generalized form of one of the most famous and most important theorems of modern analysis; we now state it.

(12.36) F. Riesz's Representation Theorem. Let $X$ be a locally compact Hausdorff space and let $I$ be a nonnegative linear functional on $\mathfrak{C}_{00}(X)$. Then there is a measure space $(X, \mathfrak{M}_i, \iota)$, where $\mathfrak{M}_i$ contains all Borel sets, such that

(i) $$I(f) = \int_X f(x) d\iota(x)$$

for all $f \in \mathfrak{C}_{00}(X)$.

Proof. This is a special case of (12.35), since $\bar{I}(f) = I(f)$ for all nonnegative $f$ in $\mathfrak{C}_{00}(X)$, and $I$ and $\int_X \cdots d\iota$ are linear functionals. $\square$

(12.37) Remark. The importance of Riesz's representation theorem lies in the countable additivity of the integral, as described in (12.21) to (12.

It follows from (10.20), (9.27), (9.24), and (9.26) that every measure $\iota$ defined as in § 9 is a regular measure on $M$. [Cf. the different but related definition of regular outer measure in (10.40) supra.]
