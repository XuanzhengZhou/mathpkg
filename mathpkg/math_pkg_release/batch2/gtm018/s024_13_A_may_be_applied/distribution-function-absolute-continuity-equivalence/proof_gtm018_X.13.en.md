---
role: proof
locale: en
of_concept: distribution-function-absolute-continuity-equivalence
source_book: gtm018
source_chapter: "X"
source_section: "13"
---

If $\nu \ll \mu$, then to every positive number $\epsilon$ there corresponds a positive number $\delta$ such that $\nu(E) < \epsilon$ for every Borel set $E$ for which $\mu(E) < \delta$. Hence if $\{(a_i, b_i): i = 1, \dots, n\}$ is a finite, disjoint class of bounded open intervals for which

$$\mu\left(\bigcup_{i=1}^{n}[a_i, b_i)\right) = \sum_{i=1}^{n}(b_i - a_i) < \delta,$$

then

$$\sum_{i=1}^{n}|f_{\nu}(b_i) - f_{\nu}(a_i)| = \sum_{i=1}^{n}\nu([a_i, b_i)) = \nu\left(\bigcup_{i=1}^{n}[a_i, b_i)\right) < \epsilon.$$

Thus $f_\nu$ is absolutely continuous.

Suppose, conversely, that $f_{\nu}$ is absolutely continuous. Let $\epsilon$ be any positive number and let $\delta$ be a positive number such that $\sum_{i=1}^{n}(b_i - a_i) < \delta$ implies $\sum_{i=1}^{n}|f_{\nu}(b_i) - f_{\nu}(a_i)| < \epsilon$. If $E$ is a Borel set of Lebesgue measure zero, then there exists a disjoint sequence $\{[a_i, b_i)\}$ of semiclosed intervals such that $E \subset \bigcup_{i=1}^{\infty}[a_i, b_i)$ and $\sum_{i=1}^{\infty}(b_i - a_i) < \delta$. By the absolute continuity of $f_\nu$, for each $n$ we have

$$\sum_{i=1}^{n}|f_{\nu}(b_i) - f_{\nu}(a_i)| = \sum_{i=1}^{n}\nu([a_i, b_i)) < \epsilon.$$

Letting $n \to \infty$ yields $\nu(E) \leq \sum_{i=1}^{\infty}\nu([a_i, b_i)) \leq \epsilon$. Since $\epsilon$ is arbitrary, $\nu(E) = 0$. This shows $\nu \ll \mu$.
