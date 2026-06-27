---
role: proof
locale: en
of_concept: finite-nonstandard-reals-subring
source_book: gtm037
source_chapter: "Part 4"
source_section: "Model Theory"
---

If $a, b \in {}^*\mathbb{R}$ are finite, there exist $M, N \in \omega$ such that $|a| \leq M$ and $|b| \leq N$. Then $|a - b| \leq |a| + |b| \leq M + N$, so $a - b$ is finite. Also $|ab| = |a||b| \leq MN$, so $ab$ is finite. Hence the finite nonstandard reals are closed under subtraction and multiplication and contain $0$ and $1$, forming a subring ${}^t\mathbb{R}$ of $^*\mathbb{R}$.

If $\varepsilon, \delta$ are infinitesimal, then for any standard $r > 0$, $|\varepsilon| < r/2$ and $|\delta| < r/2$, so $|\varepsilon \pm \delta| \leq |\varepsilon| + |\delta| < r$. Hence $\varepsilon \pm \delta$ is infinitesimal. If $a$ is finite with $|a| \leq M$ for some standard $M$, then for any standard $r > 0$, $|\varepsilon| < r/M$, so $|\varepsilon a| < r$. Hence $\varepsilon a$ is infinitesimal.
