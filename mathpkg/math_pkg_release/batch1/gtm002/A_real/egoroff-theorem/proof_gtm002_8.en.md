---
role: proof
locale: en
of_concept: egoroff-theorem
source_book: gtm002
source_chapter: "8"
source_section: "The Theorems of Lusin and Egoroff"
---

For each pair of positive integers $n$ and $k$, define
$$E_{n,k} = \bigcup_{i=n}^{\infty} \left\{ x \in E : |f_i(x) - f(x)| \geq \frac{1}{k} \right\}.$$

Then $E_{n,k} \supset E_{n+1,k}$ for each $k$, and since $f_n(x) \to f(x)$ for every $x \in E$, we have
$$\bigcap_{n=1}^{\infty} E_{n,k} = \emptyset$$
for each $k$.

Given $\varepsilon > 0$, for each $k$ there exists an integer $n(k)$ such that
$$m\bigl( E_{n(k),k} \bigr) < \frac{\varepsilon}{2^k}.$$
(This uses the fact that $m(E) < \infty$ and continuity of measure from above.)

Put
$$F = \bigcup_{k=1}^{\infty} E_{n(k),k}.$$
Then
$$m(F) \leq \sum_{k=1}^{\infty} m\bigl( E_{n(k),k} \bigr) < \sum_{k=1}^{\infty} \frac{\varepsilon}{2^k} = \varepsilon.$$

For each $k$, we have $E - F \subset E - E_{n(k),k}$. Therefore, for all $i \geq n(k)$ and all $x \in E - F$,
$$|f_i(x) - f(x)| < \frac{1}{k}.$$

This means precisely that $f_n$ converges to $f$ uniformly on $E - F$.
