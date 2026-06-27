---
role: proof
locale: en
of_concept: differentiation-under-integral-sign
source_book: gtm012
source_chapter: "1"
source_section: "7. Functions of two variables"
---

# Proof: Differentiation Under the Integral Sign (Fixed Limits)

**Lemma.** If $f$ is a complex-valued function of class $C^1$ defined on a rectangle

$$\{(x, y) \mid |x - a| < r_1,\; |y - b| < r_2\},$$

then the derivative with respect to $y$ of

$$\int_a^x f(s, y) \, ds$$

is

$$\int_a^x D_2 f(s, y) \, ds.$$

Similarly, the derivative with respect to $x$ of

$$\int_b^y f(x, t) \, dt$$

is

$$\int_b^y D_1 f(x, t) \, dt.$$

**Proof.** This result was established in the course of proving Theorem 7.1 (Equality of Mixed Partial Derivatives). The argument proceeds as follows.

We differentiate the identity

$$f(x, y) = \int_a^x D_1 f(s, y) \, ds + f(a, y)$$

with respect to $y$. Because $D_2 D_1 f$ exists and is continuous (as a consequence of $f$ being of class $C^1$ — more precisely, for the application in Theorem 7.1, $f$ is $C^2$), the differentiation operator may be passed inside the integral:

$$D_2 f(x, y) = \int_a^x D_2 D_1 f(s, y) \, ds + D_2 f(a, y).$$

The interchange of differentiation and integration is justified by the continuity of the partial derivative $D_2 D_1 f$ on the compact rectangle. One may estimate the difference quotient

$$\frac{1}{h} \left[ \int_a^x f(s, y+h) \, ds - \int_a^x f(s, y) \, ds \right] = \int_a^x \frac{f(s, y+h) - f(s, y)}{h} \, ds$$

and pass to the limit $h \to 0$. By the mean value theorem and the uniform continuity of $D_2 f$ on compact subsets, the convergence is uniform, and the limit can be taken inside the integral.

The second statement, concerning differentiation with respect to $x$ of $\int_b^y f(x, t) \, dt$, follows by symmetry. $\square$
