---
role: proof
locale: en
of_concept: weierstrass-factorization-theorem
source_book: gtm011
source_chapter: "5"
source_section: "5.14"
---

According to the Weierstrass Product Theorem (Theorem 5.12), integers $\{p_n\}$ can be chosen such that

$$h(z) = z^m \prod_{n=1}^{\infty} E_{p_n}\left(\frac{z}{a_n}\right)$$

has the same zeros as $f$ with the same multiplicities. Consider the quotient $f(z)/h(z)$. Both $f$ and $h$ are entire functions (the product converges in $H(\mathbb{C})$ by Theorem 5.12), and they have exactly the same zeros with the same multiplicities. Therefore $f/h$ is an entire function with no zeros.

Since $\mathbb{C}$ is simply connected, any nowhere-vanishing entire function can be written as $e^{g(z)}$ for some entire function $g$. Thus $f(z)/h(z) = e^{g(z)}$, which gives

$$f(z) = z^m e^{g(z)} \prod_{n=1}^{\infty} E_{p_n}\left(\frac{z}{a_n}\right).$$
