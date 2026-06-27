---
role: proof
locale: en
of_concept: "if-is-a-real-valued-nondecreasing-function-on-then"
source_book: gtm025
source_chapter: "Differentiation"
source_section: "18.14"
---

For $x > b$, let $f(x) = f(b)$. Let

$$f_n(x) = -\frac{f\left(x + \frac{1}{n}\right) - f(x)}{\frac{1}{n}}$$

for $n = 1, 2, 3, \ldots$ and $a \leq x \leq b$. Then $(f_n)$ is a sequence of nonnegative measurable functions and

$$\lim_{n \to \infty} f_n(x) = f'(x)$$

for almost all $x \in ]a, b[$ [see (17.12)]; thus $f'$ is measurable. By FATOU's lemma (12.23) and (12.44) we have

$$\int_{a}^{b} f'(x) \, dx = \int_{a}^{b} \lim_{n \to \infty} f_n(x) \, dx \leq \lim_{n \to \infty} \int_{a}^{b} f_n(x) \, dx$$

$$= \lim_{n \to \infty} n \int_{a}^{b} \left[ f\left(x + \frac{1}{n}\right) - f(x) \right] \, dx$$

$$= \lim_{n \to \infty} \left[ n \int_{b}^{b + \frac{1}{n}} f(x) \, dx - n \int_{a}^{a + \frac{1}{n}} f(x) \, dx \right]$$

$$\leq \lim_{n \to \infty} \left[ n \int_{b}^{b + \frac{1}{n}} f(b) \, dx - n \int_{a

$E = \{x \in ]a, c[ : f'(x) = 0\}$. Clearly $\lambda(E) = c - a$. For each $x \in E$ there exist arbitrarily small $h > 0$ such that $[x, x + h] \subset ]a, c[$ and

$$|f(x + h) - f(x)| < \frac{\varepsilon h}{c - a}. \tag{1}$$

The family of all such intervals $[x, x + h]$ is a Vitali cover of $E$, and so by Vitali's theorem (17.11) there exists a finite pairwise disjoint family $\{[x_k, x_k + h_k]\}_{k=1}^n$ of these intervals such that

$$\lambda\left(E \cap \bigcup_{k=1}^{n}[x_k, x_k + h_k]\right)' < \delta.$$

Then

$$\lambda([a, c]) = \lambda(E) < \delta + \sum_{k=1}^{n} h_k. \tag{2}$$

We may [and do] suppose that $x_1 < x_2 < \cdots < x_n$. It follows from (2) that the sum of the lengths of the open intervals

$$]a, x_1[, ]x_1 + h_1, x_2[, \ldots, ]x_n + h_n, c[$$

complementary to $\bigcup_{k=1}^{n}[x_k, x_k + h_k]$ is less than $\delta$, and so, in view of our choice of $\delta$, we have

$$|f(a) - f(x_1)| + \sum_{k=1}^{n-1}|f(x_k + h_k) - f(x_{k+1})| + |f(x_n + h_n) - f(c)| < \varepsilon. \tag{3}$$

The inequalities (1) and (3) combine to yield

$$|f(a) - f(c)| \leq |f(a) - f(x_1)| + \sum_{k=1}^{n-1}|f(x_k + h_k) - f(x_{k+1})|$$

$$+ |f(x_n + h_n)

Therefore

$$f(x) = h(x) + g(x) = h(a) + \int_{a}^{x} f'(t) dt = f(a) + \int_{a}^{x} f'(t) dt$$

for all $x \in [a, b]$.
