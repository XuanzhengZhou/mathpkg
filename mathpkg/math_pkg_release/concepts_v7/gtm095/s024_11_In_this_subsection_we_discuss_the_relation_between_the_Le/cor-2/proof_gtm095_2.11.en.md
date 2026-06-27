---
role: proof
locale: en
of_concept: cor-2
source_book: gtm095
source_chapter: "2"
source_section: "11"
---

# Proof of Corollary 2 (Moment Formula via Tail Probability)

Let $\xi$ be a random variable with distribution function $F(x)$ and $E|\xi|^n < \infty$. Then

$$\int_0^\infty x^n\, dF(x) = n \int_0^\infty x^{n-1}[1 - F(x)]\, dx, \tag{69}$$

$$\int_{-\infty}^0 |x|^n\, dF(x) = -\int_0^\infty x^n\, dF(-x) = n \int_0^\infty x^{n-1}F(-x)\, dx, \tag{70}$$

and

$$E|\xi|^n = \int_{-\infty}^{\infty}|x|^n\, dF(x) = n \int_0^\infty x^{n-1}[1 - F(x) + F(-x)]\, dx. \tag{71}$$

**Proof.** To prove (69) we apply integration by parts (Theorem 11). Let $G(x) = 1 - F(x)$ and observe that

$$\int_0^b x^n\, dF(x) = -\int_0^b x^n\, d(1 - F(x)).$$

Applying the integration by parts formula (62) with $G(s) = 1 - F(s)$ and noting that $dF(s) = -dG(s)$, we obtain

$$\int_0^b x^n\, dF(x) = -b^n(1 - F(b)) + n \int_0^b x^{n-1}(1 - F(x))\, dx. \tag{72}$$

Now we show that, since $E|\xi|^n < \infty$, the boundary term vanishes as $b \to \infty$:

$$b^n(1 - F(b) + F(-b)) \leq b^n P(|\xi| \geq b) \to 0, \quad b \to \infty. \tag{73}$$

Indeed,

$$E|\xi|^n = \sum_{k=1}^{\infty} \int_{k-1}^k |x|^n\, dF(x) < \infty$$

and therefore the tail sum

$$\sum_{k \geq b+1} \int_{k-1}^k |x|^n\, dF(x) \to 0, \quad b \to \infty.$$

But

$$\sum_{k \geq b+1} \int_{k-1}^k |x|^n\, dF(x) \geq b^n P(|\xi| \geq b),$$

which establishes (73); hence the boundary term $b^n(1 - F(b)) \to 0$ as $b \to \infty$.

Taking the limit as $b \to \infty$ in (72), we obtain (69).

Formula (70) is proved similarly. To see this, note that

$$\int_{-\infty}^0 |x|^n\, dF(x) = -\int_0^\infty x^n\, dF(-x),$$

where the change of variables $x \mapsto -x$ is applied. Applying integration by parts to $\int_0^\infty x^n\, dF(-x)$ as above, with the relevant boundary behavior, yields

$$\int_{-\infty}^0 |x|^n\, dF(x) = n \int_0^\infty x^{n-1} F(-x)\, dx.$$

Finally, formula (71) follows directly from (69) and (70):

$$E|\xi|^n = \int_{-\infty}^{\infty} |x|^n\, dF(x) = \int_0^\infty x^n\, dF(x) + \int_{-\infty}^0 |x|^n\, dF(x)$$

$$= n \int_0^\infty x^{n-1}[1 - F(x)]\, dx + n \int_0^\infty x^{n-1}F(-x)\, dx$$

$$= n \int_0^\infty x^{n-1}[1 - F(x) + F(-x)]\, dx.$$

This completes the proof. $\square$
