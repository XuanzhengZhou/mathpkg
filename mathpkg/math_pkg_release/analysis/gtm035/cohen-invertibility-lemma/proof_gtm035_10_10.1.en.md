---
role: proof
locale: en
of_concept: cohen-invertibility-lemma
source_book: gtm035
source_chapter: "Chapter 10"
source_section: "10.1"
---
# Proof of Cohen Invertibility Lemma

**Lemma 10.1 (Paul Cohen).** Let $\mathfrak{A}$ be a uniform algebra on a compact space $X$ and let $a, b \in \mathfrak{A}$. Assume that

$$\|1 + a + \bar{b}\| < 1.$$

Then $a + b$ is invertible in $\mathfrak{A}$.

*Note.* When $b = 0$, this holds in an arbitrary Banach algebra.

**Proof.** Put $f = a + b$. We have

$$\|1 + a + \bar{b}\| < 1,$$

hence $\|1 + \bar{a} + b\| < 1$ (by taking complex conjugates, which does not change the sup-norm on $X$), whence

$$\|1 + a + b + 1 + \bar{a} + b\| < 2$$

or

$$k := \|1 + \operatorname{Re} f\| < 1.$$

For all $x \in X$, then

$$|1 + \operatorname{Re} f(x)| \leq k.$$

This means that $\operatorname{Re} f(x) \leq k - 1 < 0$ for all $x$; i.e., $f(x)$ lies in the open left-half plane for all $x$. This suggests that for sufficiently small $\varepsilon > 0$,

$$1 + \varepsilon f(x)$$

lies in the unit disk for all $x$. Indeed,

$$|1 + \varepsilon f(x)|^2 = (1 + \varepsilon \operatorname{Re} f(x))^2 + (\varepsilon \operatorname{Im} f(x))^2$$

$$= 1 + \varepsilon^2|f(x)|^2 + 2\varepsilon \operatorname{Re} f(x)$$

$$\leq 1 + c\varepsilon^2 + 2d\varepsilon,$$

where $c = \|f\|^2$ and $d = -1 + k < 0$. Since $d < 0$, for sufficiently small $\varepsilon > 0$ we have $c\varepsilon^2 + 2d\varepsilon < 0$, whence

$$|1 + \varepsilon f(x)| < 1 \quad \text{for all } x \in X,$$

or $\|1 + \varepsilon f\| < 1$. It follows that the Neumann series $\sum_{n=0}^\infty (-\varepsilon f)^n$ converges in the uniform norm, so $1 + \varepsilon f$ is invertible in $\mathfrak{A}$.

Since $1 + \varepsilon f$ is invertible and $\varepsilon \neq 0$, the element

$$f = \varepsilon^{-1}\big((1 + \varepsilon f) - 1\big)$$

is also invertible in $\mathfrak{A}$. Indeed, $(1 + \varepsilon f)^{-1}$ exists in $\mathfrak{A}$, and $f$ is a linear combination of the invertible element $1 + \varepsilon f$ and the identity, hence $f$ belongs to the group of units of $\mathfrak{A}$. ∎
