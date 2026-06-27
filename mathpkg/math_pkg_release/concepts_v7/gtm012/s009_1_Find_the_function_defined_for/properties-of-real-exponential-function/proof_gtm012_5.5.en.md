---
role: proof
locale: en
of_concept: properties-of-real-exponential-function
source_book: gtm012
source_chapter: "5"
source_section: "5"
---

# Proof of Properties of the Real Exponential Function

**Theorem 5.4.** The exponential function $E: \mathbb{R} \to \mathbb{R}$ defined by

$$E(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!}$$

has the following properties:

(a) $E(0) = 1$, and $E'(x) = E(x)$ for all $x \in \mathbb{R}$.

(b) $E$ is a strictly increasing bijection from $\mathbb{R}$ onto $(0, \infty)$.

(c) $E(x + y) = E(x) E(y)$ for all $x, y \in \mathbb{R}$.

(d) For each rational number $r$, $E(r) = e^r$, where $e = E(1)$.

**Proof.** (a) Substituting $x = 0$ into the power series gives $E(0) = 1$. By Theorem 4.4 (termwise differentiation),

$$E'(x) = \sum_{n=1}^{\infty} \frac{n x^{n-1}}{n!} = \sum_{n=1}^{\infty} \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^{\infty} \frac{x^m}{m!} = E(x).$$

(b) For $y > 0$, all terms in the series are positive, so $E(y) > 1 + y > y$. Also, $E(-y) = 1/E(y)$ (as will be shown in part (c)), so $E(-y^{-1}) = 1/E(y^{-1})$. Since $E(y^{-1}) > y^{-1}$, we obtain $E(-y^{-1}) < y$.

Thus for any $y > 0$, we have $E(-y^{-1}) < y < E(y)$. By the Intermediate Value Theorem, there exists $x \in (-y^{-1}, y)$ such that $E(x) = y$. Since $E'(x) = E(x) > 0$ for all $x$, $E$ is strictly increasing, and this $x$ is unique. Hence $E$ maps $\mathbb{R}$ bijectively onto $(0, \infty)$.

(c) Fix $y \in \mathbb{R}$ and consider the function

$$\varphi(x) = E(x + y) E(-x) E(-y), \quad x \in \mathbb{R}.$$

When $x = 0$, $\varphi(0) = E(y) E(0) E(-y) = E(y) \cdot 1 \cdot E(-y)$. To see this equals $1$, differentiate $\varphi$:

$$\varphi'(x) = E'(x + y) E(-x) E(-y) + E(x + y) (-E'(-x)) E(-y)$$
$$= E(x + y) E(-x) E(-y) - E(x + y) E(-x) E(-y) = 0,$$

where we used $E' = E$. Thus $\varphi$ is constant: $\varphi(x) = \varphi(0)$ for all $x$. In particular, $\varphi(y) = \varphi(0)$, i.e.,

$$E(2y) E(-y) E(-y) = E(y) E(-y).$$

Repeated application of this argument (or evaluating at $x = -y$) shows $E(x) E(-x) = 1$ for all $x$, hence $E(-x) = 1/E(x)$. Then $\varphi(x) \equiv 1$, giving

$$E(x + y) E(-x) E(-y) = 1 \implies E(x + y) = \frac{1}{E(-x) E(-y)} = E(x) E(y).$$

(d) From (c), by induction on $n \in \mathbb{N}$,

$$E(n x) = E(x)^n, \quad n = 1, 2, 3, \ldots$$

Since $E(-x) = 1/E(x)$, this also holds for negative integers. Therefore

$$e = E(1) = E(n \cdot 1/n) = E(1/n)^n \implies e^{1/n} = E(1/n), \quad n = 1, 2, \ldots$$

For any rational $r = m/n$ with $n > 0$,

$$E(r) = E(m/n) = E(1/n)^m = (e^{1/n})^m = e^{m/n} = e^r.$$

Thus $E(r) = e^r$ for all rational $r$. $\square$
