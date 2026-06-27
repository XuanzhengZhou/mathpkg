---
role: proof
locale: en
of_concept: exponential-generating-function-derangements
source_book: gtm095
source_chapter: "1"
source_section: "14. Inclusion–Exclusion Principle"
---

# Proof of Exponential Generating Function for Derangements

An alternative derivation of the derangement formula uses the method of exponential generating functions.

Set $D_0 = 1$ and note that $D_1 = 0$. For any $n \geq 2$, the derangement numbers satisfy the recurrence relation

$$D_n = (n-1)\bigl[D_{n-1} + D_{n-2}\bigr],$$

whose proof is left to the reader.

Define the exponential generating function

$$E(x) = \sum_{n=0}^{\infty} D_n \frac{x^n}{n!}.$$

Using the recurrence, we write

$$E(x) = 1 + \sum_{n \geq 2} D_n \frac{x^n}{n!}
= 1 + \sum_{n \geq 2} \bigl\{ nD_{n-1} + (-1)^n \bigr\} \frac{x^n}{n!}.$$

Re-indexing the sum and simplifying yields

$$E(x) = 1 + \sum_{n \geq 0} \frac{D_n}{n!} x^n + \bigl[e^{-x} - (1-x)\bigr]
= xE(x) + \bigl[e^{-x} - (1-x)\bigr].$$

Solving for $E(x)$:

$$E(x)(1-x) = e^{-x} - (1-x),$$

hence

$$E(x) = \frac{e^{-x}}{1-x}.$$

Expanding the right-hand side as the product of two power series:

$$E(x) = \left(1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots\right)(1 + x + x^2 + \cdots).$$

Multiplying out and comparing the coefficient of $x^n/n!$ with the definition $E(x) = \sum_{n \geq 0} D_n \frac{x^n}{n!}$, one recovers

$$D_n = n! \sum_{m=0}^{n} \frac{(-1)^m}{m!},$$

which is precisely the formula obtained by the inclusion–exclusion method. The inclusion–exclusion proof is simpler than the generating function approach in this case.

$\square$
