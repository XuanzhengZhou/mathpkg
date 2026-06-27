---
role: proof
locale: en
of_concept: baires-theorem-on-functions-of-first-class
source_book: gtm002
source_chapter: "7"
source_section: "Functions of First Class"
---

It suffices to show that, for each $\varepsilon > 0$, the set $F = \{x : \omega(x) \geq 5\varepsilon\}$ is nowhere dense. Let $f(x) = \lim f_n(x)$, where each $f_n$ is continuous, and define
$$E_n = \bigcap_{i,j \geq n} \{x : |f_i(x) - f_j(x)| \leq \varepsilon\}.$$
Each $E_n$ is closed (as an intersection of closed sets, since $f_i - f_j$ is continuous). Since $f_n(x)$ converges for every $x$, we have $\bigcup_{n=1}^{\infty} E_n = \mathbb{R}$.

Now, for any closed interval $I$, consider $F \cap I$. If $F \cap I$ contained an interior point relative to $I$, then by the Baire category theorem applied to the complete metric space $I$, there would exist an $n$ such that $E_n \cap I$ has nonempty interior. Thus there exists an open interval $J \subset E_n \cap I$.

For any $x \in J$ and any $i \geq n$, we have $|f_i(x) - f_n(x)| \leq \varepsilon$. Letting $i \to \infty$, we obtain $|f(x) - f_n(x)| \leq \varepsilon$ for all $x \in J$. Since $f_n$ is continuous, there exists a subinterval $J' \subset J$ such that $\omega_{f_n}(J') < \varepsilon$. Consequently, for any $x, y \in J'$,
$$|f(x) - f(y)| \leq |f(x) - f_n(x)| + |f_n(x) - f_n(y)| + |f_n(y) - f(y)| < 3\varepsilon.$$
Hence $\omega_f(x) \leq 3\varepsilon < 5\varepsilon$ for each $x \in J'$, contradicting $x \in F$. Therefore $F$ is nowhere dense. Taking the union over $\varepsilon = 1/n$ shows that the set of discontinuities is of first category.
