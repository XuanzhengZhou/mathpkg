---
role: proof
locale: en
of_concept: proposition-16-14-bipolar-theorem
source_book: gtm055
source_chapter: "16"
source_section: "16.4"
---

Let $A$ be absolutely convex. It is clear from the definitions that $A \subset \,^0(A^0)$ and that $^0(A^0)$ is weakly closed and absolutely convex. Hence the weak closure $\overline{A}^w$ of $A$ is contained in $^0(A^0)$.

Conversely, suppose $x_0 \notin \overline{A}^w$. Since $\overline{A}^w$ is absolutely convex and weakly closed, the Hahn–Banach separation theorem (in the form of Proposition 14.15, applied to the weak topology) yields a functional $g \in \mathcal{F}$ and a real number $c$ such that
$$|\langle x, g \rangle| \leq c, \quad x \in A, \quad \text{while} \quad |\langle x_0, g \rangle| > c.$$

Replacing $g$ by $f = \gamma g$ where $\gamma$ is a suitable complex number of modulus one, we obtain
$$|f(x)| \leq c, \; x \in A, \quad \text{while} \quad f(x_0) > c.$$

If $c > 0$, define $f_0 = f/c$; then $|f_0(x)| \leq 1$ for $x \in A$, so $f_0 \in A^0$, but $|f_0(x_0)| > 1$, hence $x_0 \notin \,^0(A^0)$. If $c = 0$, set $f_0 = 2f/f(x_0)$; then $|f_0(x)| = 0 \leq 1$ for $x \in A$, so $f_0 \in A^0$, but $f_0(x_0) = 2 > 1$, again yielding $x_0 \notin \,^0(A^0)$. In either case $x_0 \notin \,^0(A^0)$, establishing the reverse inclusion.
