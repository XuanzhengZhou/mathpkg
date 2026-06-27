---
role: proof
locale: en
of_concept: minkowskis-inequality
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Minkowski's Inequality for Expectations

**Minkowski's Inequality.** If $E|\xi|^p < \infty$, $E|\eta|^p < \infty$, $1 \leq p < \infty$, then $E|\xi + \eta|^p < \infty$ and

$$(E|\xi + \eta|^p)^{1/p} \leq (E|\xi|^p)^{1/p} + (E|\eta|^p)^{1/p}. \tag{31}$$

*Proof.* We begin by establishing the following inequality: if $a, b > 0$ and $p \geq 1$, then

$$(a + b)^p \leq 2^{p-1}(a^p + b^p). \tag{32}$$

Consider the function $F(x) = (a + x)^p - 2^{p-1}(a^p + x^p)$. Then

$$F'(x) = p(a + x)^{p-1} - 2^{p-1} p x^{p-1},$$

and since $p \geq 1$, we have $F'(a) = 0$, $F'(x) > 0$ for $x < a$, and $F'(x) < 0$ for $x > a$. Therefore

$$F(b) \leq \max_x F(x) = F(a) = 0,$$

from which (32) follows.

According to this inequality,

$$|\xi + \eta|^p \leq (|\xi| + |\eta|)^p \leq 2^{p-1}(|\xi|^p + |\eta|^p), \tag{33}$$

and therefore if $E|\xi|^p < \infty$ and $E|\eta|^p < \infty$, it follows that $E|\xi + \eta|^p < \infty$.

If $p = 1$, inequality (31) follows directly from (33) (or from the triangle inequality $|\xi + \eta| \leq |\xi| + |\eta|$).

Now suppose that $p > 1$. Take $q > 1$ so that $1/p + 1/q = 1$. Then

$$|\xi + \eta|^p = |\xi + \eta| \cdot |\xi + \eta|^{p-1} \leq |\xi| \cdot |\xi + \eta|^{p-1} + |\eta| \cdot |\xi + \eta|^{p-1}.$$

Taking expectations and applying Hölder's inequality to each term on the right (with the conjugate exponents $p$ and $q$),

$$E|\xi + \eta|^p \leq E[|\xi| \cdot |\xi + \eta|^{p-1}] + E[|\eta| \cdot |\xi + \eta|^{p-1}]$$
$$\leq (E|\xi|^p)^{1/p} (E|\xi + \eta|^{(p-1)q})^{1/q} + (E|\eta|^p)^{1/p} (E|\xi + \eta|^{(p-1)q})^{1/q}.$$

Since $(p-1)q = p$ (because $1/p + 1/q = 1$), we have $E|\xi + \eta|^{(p-1)q} = E|\xi + \eta|^p$. Therefore

$$E|\xi + \eta|^p \leq \left[(E|\xi|^p)^{1/p} + (E|\eta|^p)^{1/p}\right] (E|\xi + \eta|^p)^{1/q}.$$

If $E|\xi + \eta|^p = 0$, the desired inequality (31) is evident. Now let $E|\xi + \eta|^p > 0$. Dividing both sides by $(E|\xi + \eta|^p)^{1/q}$, we obtain

$$(E|\xi + \eta|^p)^{1 - 1/q} \leq (E|\xi|^p)^{1/p} + (E|\eta|^p)^{1/p}.$$

Since $1 - 1/q = 1/p$, this is exactly (31). $\square$
