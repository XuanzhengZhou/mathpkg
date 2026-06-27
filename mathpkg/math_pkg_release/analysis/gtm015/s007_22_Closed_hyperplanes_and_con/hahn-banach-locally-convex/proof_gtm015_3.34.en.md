---
role: proof
locale: en
of_concept: hahn-banach-locally-convex
source_book: gtm015
source_chapter: "3"
source_section: "34"
---

# Proof of Hahn-Banach theorem for locally convex spaces

If $E$ is a locally convex TVS over $\mathbb{K}$ and $M$ is a linear subspace of $E$, then every continuous linear form $g$ on $M$ may be extended to a continuous linear form $f$ on $E$.

Consider first the case $\mathbb{K} = \mathbb{R}$. Let $g$ be a continuous linear form on $M$. Since $g$ is continuous, the set $U = \{x \in M : |g(x)| < 1\}$ is a neighborhood of $\theta$ in $M$. By definition of the relative topology, there exists a convex, balanced neighborhood $V$ of $\theta$ in $E$ such that $V \cap M \subset U$. Let $p$ be the Minkowski functional (gauge) of $V$:

$$p(x) = \inf\{\lambda > 0 : x \in \lambda V\}.$$

Then $p$ is a seminorm on $E$, and $|g(y)| \le p(y)$ for all $y \in M$ (since $V \cap M \subset U$). By the Hahn-Banach-Bohnenblust-Sobczyk theorem (28.8), $g$ extends to a linear form $f$ on $E$ with $|f(x)| \le p(x)$. The inequality $|f(x)| \le p(x)$ implies $f$ is continuous at $\theta$, hence continuous everywhere.

For $\mathbb{K} = \mathbb{C}$, let $g_0 = \operatorname{Re} g$ be the real part. This is an $\mathbb{R}$-linear continuous form on $M$. Extend it to a continuous $\mathbb{R}$-linear form $f_0$ on $E$ by the real case just proved. Let $f$ be the $\mathbb{C}$-linear form with $\operatorname{Re} f = f_0$ (22.6). Then $f$ is continuous and $f|_M = g$ (since $\operatorname{Re}(f|_M) = g_0 = \operatorname{Re} g$, and two $\mathbb{C}$-forms with equal real part are equal by (21.11)).
