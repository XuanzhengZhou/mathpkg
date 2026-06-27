---
role: proof
locale: en
of_concept: logarithmic-derivative-homomorphism-di1
source_book: gtm059
source_chapter: "12"
source_section: "2"
---

The proof follows from considering the basic Lubin-Tate generators $$w_n$$ satisfying

$$g(w_{n+1}) = w_n, \quad w_{n+1} + w_n = 0.$$

The relative different is obtained by taking the derivative and evaluating at $$w_n$$ and $$w_{n+1}$$. For $$x \in K_n$$ written as $$x = g(x_n)$$ with $$g(X) = X^p + \text{higher terms}$$ and $$c_n$$ a unit, we have

$$g'(X) = \frac{1}{2} X^p + \frac{1}{4} K(X).$$

Hence $$g'(x)$$ is integral if $$n = 0$$, and in any case lies in $$\mathfrak{p}_1^n$$.

If $$g(X) = X^p + K(X)$$ and $$h(X) = X^p - K(X)$$ are two power series whose values at $$x_n$$ equal $$x$$, and $$f(X)$$ is the irreducible polynomial of $$x_n$$ over $$K$$, then

$$g(X) \equiv X^p - K(X) X^p f(X) \equiv 0 \pmod{\varpi_1}$$

for some power series in $$\varpi_1$$. Hence

$$g'(X) \equiv \frac{1}{2} X^p + \frac{1}{4} f(X) \equiv 0 \pmod{\varpi_1}.$$

This shows that $$g'(x)$$ is well-defined modulo the different, and the homomorphism property follows from the Leibniz rule for the logarithmic derivative.
