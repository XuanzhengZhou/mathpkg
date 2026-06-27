---
role: proof
locale: en
of_concept: associativity-via-absolute-values
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

We are again to prove that $\pi(Af) = (\pi A)f$. Set $\pi = \pi^+ - \pi^-$, $A = A^+ - A^-$, and $f = f^+ - f^-$. Expand using distributivity (Proposition 1-2):

$$\pi(Af) = (\pi^+ - \pi^-)((A^+ - A^-)(f^+ - f^-)).$$

After expanding all products using distributivity, each term involves only non-negative matrices, row vectors, and column vectors. By Proposition 1-4, non-negative matrices associate, so all terms can be regrouped freely. The resulting expression equals $(\pi A)f$ after collecting terms. The finiteness condition on $|A|\,|B|\,|C|$ ensures that no indeterminate forms ($\infty - \infty$) arise.
