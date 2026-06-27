---
role: proof
locale: en
of_concept: bolzano-weierstrass-nonstandard
source_book: gtm037
source_chapter: "Part 4"
source_section: "Model Theory"
---

Let $x \in {}^\omega\mathbb{R}$ be bounded. Thus there is an $M \in \mathbb{R}$ such that $|x_n| \leq M$ for all $n \in \omega$. Hence $^*|t[x]| \leq M$ also, since $\omega = \{n : |x_n| \leq M\} \in F$. Let $y = \operatorname{st} t[x]$; we claim that $y$ is a limit point of $x$. Given $\varepsilon > 0$ and any positive integer $m$, we must find $n \geq m$ such that $|x_n - y| \leq \varepsilon$. Now $|t[x] - y| \leq \varepsilon$ since $t[x] - y$ is infinitesimal, so $\{n : |x_n - y| \leq \varepsilon\} \in F$. In particular, there are infinitely many $n$ so that $|x_n - y| \leq \varepsilon$, as desired.
