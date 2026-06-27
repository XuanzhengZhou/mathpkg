---
role: proof
locale: en
of_concept: baire-first-class-continuity-theorem
source_book: gtm002
source_chapter: "7"
source_section: "7. Functions of First Class"
---

It suffices to show that, for each $\varepsilon > 0$, the set $F = \{x : \omega(x) \geq 5\varepsilon\}$ is nowhere dense. Let $f(x) = \lim f_n(x)$, $f_n$ continuous, and define

$$E_n = \bigcap_{i,j \geq n} \{x : |f_i(x) - f_j(x)| \leq \varepsilon\}.$$

Each $E_n$ is closed, being the intersection of closed sets. Since $\{f_n(x)\}$ converges for each $x$, we have $\bigcup_{n=1}^{\infty} E_n = \mathbb{R}$. For any interval $I$, since $I = \bigcup_{n=1}^{\infty} (I \cap E_n)$, the Baire category theorem implies that for some $n$, $I \cap E_n$ contains an interval $J$.

For $x \in J$ and $i \geq n$, $|f_i(x) - f_n(x)| \leq \varepsilon$ on $J$. Hence, for $x, y \in J$, $|f_n(x) - f_n(y)| \leq \varepsilon$ for all $i$, and therefore $|f(x) - f(y)| \leq \varepsilon$ for $x, y \in J$. This implies $\omega(J) \leq 2\varepsilon$. Consequently, $J \cap F = \emptyset$. Since $I$ was arbitrary, $F$ is nowhere dense.
