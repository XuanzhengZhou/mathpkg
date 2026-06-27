---
role: proof
locale: en
of_concept: xp-d-operator-formula
source_book: gtm059
source_chapter: "2"
source_section: "2. Operations on Measure and Power Series"
---

Note that
$$x = \lim_{n \to \infty} \frac{(1 + X)^n - 1}{n} = \lim_{n \to \infty} \frac{\phi_p(x) - 1}{x}.$$

Hence for any step function $w$ we get
$$\int_{p_0}^{X} w \, dx = \lim_{n \to \infty} \frac{\phi_p(x) - 1}{x} = \lim_{n \to \infty} \int_{p_0}^{X} w \, dx$$
(by Lemma 1),

where
$$p_0(X) = \frac{(X + x) + X}{2} - \frac{X}{2} = (1 + X) f'(X) \pmod{x}$$
by Taylor's formula. The desired result follows by taking the limit as $x \to 0$ and using the nontrivial part of Theorem 4.1, namely
$$\begin{cases}
p_0(X) = p_0(1) + X - f'(X) \\
t = x^2, \quad X = t - 1, \quad T = 1 + X.
\end{cases}$$

**Remark.** We shall also show with three variables: let $T$ be the variable on the multiplicative group. We get
$$T = e^t, \quad X = T - 1, \quad T = 1 + X.$$
Then $Z$ is the corresponding variable on the additive group. For any power series $w(X)$ with coefficients in a field of characteristic $0$, there is a corresponding power series denoted by $f'(X)$ on $f(X)$ such that
$$f'(X) = f'(t) = f_p(X).$$
