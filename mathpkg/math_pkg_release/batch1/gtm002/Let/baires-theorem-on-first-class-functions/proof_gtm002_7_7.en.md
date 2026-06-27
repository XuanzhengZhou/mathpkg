---
role: proof
locale: en
of_concept: baires-theorem-on-first-class-functions
source_book: gtm002
source_chapter: "7"
source_section: "7"
---

It suffices to show that, for each $\varepsilon > 0$, the set $F = \{x : \omega(x) \geq 5\varepsilon\}$ is nowhere dense. Let $f(x) = \lim_{n \to \infty} f_n(x)$, with each $f_n$ continuous, and define

$$E_n = \bigcap_{i,j \geq n} \{x : |f_i(x) - f_j(x)| \leq \varepsilon\}.$$

Each $E_n$ is closed, being the intersection of closed sets (since $f_i - f_j$ is continuous). Moreover, $\bigcup_{n=1}^{\infty} E_n = \mathbb{R}$, because for any $x$, the sequence $\{f_n(x)\}$ is Cauchy. By the Baire category theorem, some $E_n$ contains an interval $I$. On $I$, we have $|f_i(x) - f_j(x)| \leq \varepsilon$ for all $i, j \geq n$. Letting $j \to \infty$, we obtain $|f_i(x) - f(x)| \leq \varepsilon$ for all $i \geq n$ and $x \in I$.

For any $x_0 \in I$, by continuity of $f_n$, there exists a neighborhood $J \subset I$ of $x_0$ such that $|f_n(x) - f_n(x_0)| \leq \varepsilon$ for all $x \in J$. Then for $x \in J$:

$$|f(x) - f(x_0)| \leq |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)| \leq 3\varepsilon.$$

Hence $\omega(x_0) \leq 6\varepsilon$ for all $x_0 \in I$, so $F \cap I = \varnothing$. This shows that $F$ does not contain any interval in its closure, i.e., $F$ is nowhere dense. Taking the union over a sequence of $\varepsilon \to 0$, the set of discontinuity points is a countable union of nowhere dense sets, hence of first category.
