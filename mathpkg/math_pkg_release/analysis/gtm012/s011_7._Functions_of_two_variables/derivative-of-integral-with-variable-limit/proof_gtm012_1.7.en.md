---
role: proof
locale: en
of_concept: derivative-of-integral-with-variable-limit
source_book: gtm012
source_chapter: "1"
source_section: "7. Functions of two variables"
---

# Proof: Derivative of an Integral with Variable Upper Limit

**Lemma (Formula 7.3).** Let $f$ be a complex-valued function of class $C^1$ defined on a rectangle

$$\{(s, y) \mid |s - a| < r_1,\; |y - a| < r_1\}.$$

Define

$$F(y) = \int_a^y f(s, y) \, ds$$

for $|y - a| < r_1$. Then $F$ is differentiable and

$$F'(y) = \int_a^y D_2 f(s, y) \, ds + f(y, y). \tag{7.3}$$

**Proof.** Consider the difference quotient:

$$F(y + \varepsilon) - F(y) = \int_a^{y+\varepsilon} f(s, y+\varepsilon) \, ds - \int_a^y f(s, y) \, ds.$$

Rewrite the first integral by splitting the interval of integration:

$$\int_a^{y+\varepsilon} f(s, y+\varepsilon) \, ds = \int_a^y f(s, y+\varepsilon) \, ds + \int_y^{y+\varepsilon} f(s, y+\varepsilon) \, ds.$$

Therefore

$$F(y + \varepsilon) - F(y) = \int_a^y [f(s, y+\varepsilon) - f(s, y)] \, ds + \int_y^{y+\varepsilon} f(s, y+\varepsilon) \, ds.$$

Divide by $\varepsilon$ and let $\varepsilon \to 0$.

For the first term:

$$\frac{1}{\varepsilon} \int_a^y [f(s, y+\varepsilon) - f(s, y)] \, ds = \int_a^y \frac{f(s, y+\varepsilon) - f(s, y)}{\varepsilon} \, ds.$$

Since $f$ is of class $C^1$, the partial derivative $D_2 f$ exists and is continuous. By the differentiation under the integral sign lemma, we may pass the limit inside the integral, obtaining

$$\lim_{\varepsilon \to 0} \int_a^y \frac{f(s, y+\varepsilon) - f(s, y)}{\varepsilon} \, ds = \int_a^y D_2 f(s, y) \, ds.$$

For the second term, we are integrating $f(s, y+\varepsilon)$ over an interval of length $|\varepsilon|$. As $\varepsilon \to 0$, the integrand approaches $f(y, y)$ uniformly on the shrinking interval (by continuity of $f$). Hence

$$\lim_{\varepsilon \to 0} \frac{1}{\varepsilon} \int_y^{y+\varepsilon} f(s, y+\varepsilon) \, ds = f(y, y).$$

Combining both limits yields formula (7.3). $\square$
