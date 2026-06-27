---
role: proof
locale: en
of_concept: three-independent-periods-implies-arbitrarily-small-periods
source_book: gtm041
source_chapter: "7"
source_section: "7.7"
---

Suppose first that $\omega_2/\omega_1$ is real. If $\omega_2/\omega_1$ is rational, then $\omega_1$ and $\omega_2$ are linearly dependent over the integers, hence $\omega_1, \omega_2, \omega_3$ are also dependent, contradicting the hypothesis. If $\omega_2/\omega_1$ is irrational, then $f$ has arbitrarily small nonzero periods by Theorem 7.12.

Now suppose $\omega_2/\omega_1$ is not real. Geometrically, this means that $\omega_1$ and $\omega_2$ are not collinear with the origin. Hence $\omega_3$ can be expressed as a linear combination of $\omega_1$ and $\omega_2$ with real coefficients, say
$$\omega_3 = \alpha\omega_1 + \beta\omega_2, \quad \text{where } \alpha \text{ and } \beta \text{ are real.}$$

Now we consider three cases:
(a) Both $\alpha$ and $\beta$ rational.
(b) One of $\alpha, \beta$ rational, the other irrational.
(c) Both $\alpha$ and $\beta$ irrational.

**Case (a)** implies $\omega_1, \omega_2, \omega_3$ are dependent over the integers, contradicting the hypothesis.

**Case (b):** Without loss of generality, assume $\alpha$ is rational, say $\alpha = a/b$, and $\beta$ is irrational. Then we have
$$\omega_3 = \frac{a}{b}\omega_1 + \beta\omega_2.$$
Multiplying by $b$, we obtain $b\omega_3 - a\omega_1 = b\beta\omega_2$, which is a period of $f$. Since $\beta$ is irrational and $\omega_2$ is a period, the ratio $(b\beta\omega_2)/\omega_2 = b\beta$ is irrational. Hence by Theorem 7.12, $f$ has arbitrarily small nonzero periods.

**Case (c):** Both $\alpha$ and $\beta$ are irrational. By Kronecker's theorem (one-dimensional version for two numbers), given any $\varepsilon > 0$, there exist an integer $k > 0$ and integers $h_1, h_2$ such that
$$|k\alpha - h_1| < \frac{\varepsilon}{1 + |\omega_1| + |\omega_2|}, \quad |k\beta - h_2| < \frac{\varepsilon}{1 + |\omega_1| + |\omega_2|}.$$

Multiplying these inequalities by $|\omega_1|$ and $|\omega_2|$ respectively:
$$|k\alpha\omega_1 - h_1\omega_1| < \frac{\varepsilon|\omega_1|}{1 + |\omega_1| + |\omega_2|}, \quad |k\beta\omega_2 - h_2\omega_2| < \frac{\varepsilon|\omega_2|}{1 + |\omega_1| + |\omega_2|}.$$

Since $k\omega_3 = k\alpha\omega_1 + k\beta\omega_2$, by the triangle inequality:
$$|k\omega_3 - h_1\omega_1 - h_2\omega_2| < \frac{\varepsilon(|\omega_1| + |\omega_2|)}{1 + |\omega_1| + |\omega_2|} < \varepsilon.$$

Thus $k\omega_3 - h_1\omega_1 - h_2\omega_2$ is a nonzero period (nonzero because of the independence hypothesis) with modulus $< \varepsilon$. Hence $f$ has arbitrarily small nonzero periods.
