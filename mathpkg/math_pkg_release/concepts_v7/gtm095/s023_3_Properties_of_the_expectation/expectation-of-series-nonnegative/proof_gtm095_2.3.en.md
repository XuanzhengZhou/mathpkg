---
role: proof
locale: en
of_concept: expectation-of-series-nonnegative
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Expectation of Series of Nonnegative Random Variables

**Corollary (to the Monotone Convergence Theorem).** Let $\{\eta_n\}_{n \geq 1}$ be a sequence of nonnegative random variables. Then

$$E \sum_{n=1}^{\infty} \eta_n = \sum_{n=1}^{\infty} E \eta_n.$$

*Proof.* Set $S_N = \sum_{n=1}^{N} \eta_n$. Then $S_N \geq 0$ and $S_N \uparrow \sum_{n=1}^{\infty} \eta_n$ as $N \to \infty$. By Property E (additivity of expectation for nonnegative random variables, applied inductively),

$$E S_N = E \sum_{n=1}^{N} \eta_n = \sum_{n=1}^{N} E \eta_n.$$

By the Monotone Convergence Theorem (Theorem 1), since $S_N \uparrow S$ and $S_N \geq 0$,

$$E \sum_{n=1}^{\infty} \eta_n = E\left[\lim_{N \to \infty} S_N\right] = \lim_{N \to \infty} E S_N = \lim_{N \to \infty} \sum_{n=1}^{N} E \eta_n = \sum_{n=1}^{\infty} E \eta_n.$$

$\square$
