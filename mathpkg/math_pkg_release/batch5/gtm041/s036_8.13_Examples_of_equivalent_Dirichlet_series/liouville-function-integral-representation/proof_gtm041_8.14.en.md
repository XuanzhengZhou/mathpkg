---
role: proof
locale: en
of_concept: liouville-function-integral-representation
source_book: gtm041
source_chapter: "8"
source_section: "8.14"
---

By Abel's identity (Theorem 4.2 in [4]) we have
$$
\sum_{n \leq x} \frac{\lambda(n)}{n} \cdot \frac{1}{n^s} = \frac{C(x)}{x^s} + s \int_1^x \frac{C(t)}{t^{s+1}} \, dt.
$$

Keep $\sigma > 0$ and let $x \to \infty$. Then
$$
\frac{C(x)}{x^s} = O\!\left(\frac{1}{x^\sigma} \sum_{n \leq x} \frac{1}{n}\right) = O\!\left(\frac{\log x}{x^\sigma}\right) = o(1) \quad \text{as } x \to \infty.
$$

Thus, letting $x \to \infty$,
$$
\sum_{n=1}^\infty \frac{\lambda(n)}{n^{s+1}} = s \int_1^\infty \frac{C(t)}{t^{s+1}} \, dt, \quad \sigma > 0.
$$

Now recall the identity
$$
\sum_{n=1}^\infty \frac{\lambda(n)}{n^s} = \frac{\zeta(2s)}{\zeta(s)} \quad (\sigma > 1).
$$

Replacing $s$ by $s-1$ yields
$$
\sum_{n=1}^\infty \frac{\lambda(n)}{n^s} = \frac{\zeta(2s-2)}{\zeta(s-1)},
$$
and by the Abel summation formula,
$$
\frac{\zeta(2s)}{(s-1)\zeta(s)} = \int_1^\infty \frac{C(x)}{x^s} \, dx
$$
for $\sigma > 1$.
