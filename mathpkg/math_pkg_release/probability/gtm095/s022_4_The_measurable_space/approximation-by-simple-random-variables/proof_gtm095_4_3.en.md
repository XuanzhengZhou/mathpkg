---
role: proof
locale: en
of_concept: approximation-by-simple-random-variables
source_book: gtm095
source_chapter: "4"
source_section: "3"
---

# Proof of Approximation of Random Variables by Simple Functions

We begin by proving the second statement. For $n = 1, 2, \ldots$, put

$$\xi_n(\omega) = \sum_{k=1}^{n2^n} \frac{k-1}{2^n} I_{k,n}(\omega) + n I_{\{\xi(\omega) \geq n\}}(\omega),$$

where $I_{k,n}$ is the indicator of the set $\{(k-1)/2^n \leq \xi(\omega) < k/2^n\}$. It is easy to verify that the sequence $\xi_n(\omega)$ so constructed is such that $\xi_n(\omega) \uparrow \xi(\omega)$ for all $\omega \in \Omega$.

The first statement follows from this if we merely observe that $\xi$ can be represented in the form $\xi = \xi^+ - \xi^-$. This completes the proof of the theorem.
