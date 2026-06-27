---
role: proof
locale: en
of_concept: convergence-in-leopold-space
source_book: gtm059
source_chapter: ""
source_section: "5"
---

The proof is immediate from the estimate:

$$|a_n x^n|_p \le \|f\|_p \cdot |x|_p^n.$$

Since $\lim_{n \to \infty} |a_n|_p = 0$, the series converges whenever $|x|_p < |p|^{1/(p-1)}$, because for such $x$ we have $|x|_p^n \to 0$ as $n \to \infty$. The bound $|f(x)|_p \le \|f\|_p$ follows from the ultrametric inequality and the fact that each term satisfies $|a_n x^n|_p \le \|f\|_p \cdot |x|_p^n \le \|f\|_p$.
