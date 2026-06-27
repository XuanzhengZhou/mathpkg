---
role: proof
locale: en
of_concept: carlemans-test
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Carleman's test for uniqueness of the moment problem

**Carleman's Test.** Let $\{m_n\}_{n \geq 1}$ be the moments of a probability distribution.

(a) If

$$\sum_{n=0}^{\infty} \frac{1}{(m_{2n})^{1/2n}} = \infty,$$

then the moments determine the probability distribution uniquely.

(b) If $\{m_n\}_{n \geq 1}$ are the moments of a distribution concentrated on $[0, \infty)$, then the solution is unique if

$$\sum_{n=0}^{\infty} \frac{1}{(m_n)^{1/2n}} = \infty.$$

*The proof is not included in the source text. The reader is referred to [31], VII.3.*

**Remarks:**

Carleman's test provides a sufficient condition for the determinacy of the moment problem that is often easier to verify than the growth condition $\limsup \mu_n^{1/n}/n < \infty$ of Theorem 7. The test is based on the rate of growth of the moments: if the moments do not grow too fast (in the sense that the above series diverges), then the distribution is uniquely determined by its moments.

For example, the log-normal distribution has moments $m_n = e^{n^2/2}$, for which $\sum 1/(m_{2n})^{1/2n} = \sum e^{-n/2} < \infty$, so Carleman's condition fails -- and indeed the log-normal distribution is not uniquely determined by its moments.
