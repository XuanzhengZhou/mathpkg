---
role: proof
locale: en
of_concept: egoroffs-theorem
source_book: gtm002
source_chapter: "8"
source_section: "8"
---

Assume without loss of generality that $f_n(x) \to f(x)$ for every $x \in E$ (discard the null set where convergence fails; the measure of $E$ is unchanged). For each pair of positive integers $n$ and $k$, define

$$
E_{n,k} = \bigcup_{i=n}^{\infty} \left\{ x \in E : |f_i(x) - f(x)| \geq \frac{1}{k} \right\}.
$$

Each $E_{n,k}$ is measurable (as a countable union of measurable sets, since $f_i$ and $f$ are measurable). For fixed $k$, the sequence $\{E_{n,k}\}_{n=1}^{\infty}$ is decreasing:

$$
E_{1,k} \supset E_{2,k} \supset E_{3,k} \supset \cdots
$$

Moreover, since $f_n(x) \to f(x)$ pointwise on $E$, for each $x \in E$ and each $k$ there exists $N$ such that $|f_i(x) - f(x)| < 1/k$ for all $i \geq N$. Hence $x \notin E_{N,k}$, and consequently

$$
\bigcap_{n=1}^{\infty} E_{n,k} = \emptyset \quad \text{for each } k.
$$

Since $E$ has finite measure, $m(E_{1,k}) \leq m(E) < \infty$. By continuity of measure from above for decreasing sequences of sets of finite measure,

$$
\lim_{n \to \infty} m(E_{n,k}) = m\!\left(\bigcap_{n=1}^{\infty} E_{n,k}\right) = 0.
$$

Now fix $\varepsilon > 0$. For each $k$, choose $n(k)$ sufficiently large so that

$$
m(E_{n(k),k}) < \frac{\varepsilon}{2^k}.
$$

Define

$$
F = \bigcup_{k=1}^{\infty} E_{n(k),k}.
$$

Then $F \subset E$ and

$$
m(F) \leq \sum_{k=1}^{\infty} m(E_{n(k),k}) < \sum_{k=1}^{\infty} \frac{\varepsilon}{2^k} = \varepsilon.
$$

Set $F' = E \setminus F$; then $m(E \setminus F') = m(F) < \varepsilon$. We claim that $f_n \to f$ uniformly on $F'$. Indeed, for any $k$ and any $x \in F' = E \setminus F$, we have $x \notin E_{n(k),k}$, which means that

$$
|f_i(x) - f(x)| < \frac{1}{k} \quad \text{for all } i \geq n(k).
$$

Thus, given $\delta > 0$, choose $k$ with $1/k < \delta$ and let $N = n(k)$. Then for all $i \geq N$ and all $x \in F'$,

$$
|f_i(x) - f(x)| < \frac{1}{k} < \delta,
$$

which proves uniform convergence on $F'$.
