---
role: proof
locale: en
of_concept: monotone-convergence-theorem
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Expectation of Series of Nonnegative Random Variables

**Corollary (to the Monotone Convergence Theorem).** Let $\{\eta_n\}_{n \geq 1}$ be a sequence of nonnegative random variables. Then

$$E \sum_{n=1}^{\infty} \eta_n = \sum_{n=1}^{\infty} E \eta_n.$$

*Proof.* The proof follows from Property E (additivity of expectation for nonnegative random variables), the Monotone Convergence Theorem (Theorem 1), and the remark that

$$\sum_{n=1}^{N} \eta_n \uparrow \sum_{n=1}^{\infty} \eta_n.$$

By Property E, $E\sum_{n=1}^{N} \eta_n = \sum_{n=1}^{N} E\eta_n$ for each finite $N$. By the Monotone Convergence Theorem, since the partial sums form a non-decreasing sequence of nonnegative random variables converging to the infinite sum,

$$E \sum_{n=1}^{\infty} \eta_n = \lim_{N\to\infty} E \sum_{n=1}^{N} \eta_n = \lim_{N\to\infty} \sum_{n=1}^{N} E\eta_n = \sum_{n=1}^{\infty} E\eta_n.$$

$\square$
