---
role: proof
locale: en
of_concept: metric-from-pseudometric-function
source_book: gtm015
source_chapter: "6"
source_section: "Metrizable topological groups"
---

# Proof of Metric construction from a function satisfying triangle-like inequalities

Let $X$ be a set and suppose $f: X \times X \to \mathbb{R}$ satisfies:

(1) $f(x, y) \geq 0$ for all $x, y$;
(2) $f(x, x) = 0$ for all $x$;
(3) if $\varepsilon > 0$, the relations $f(w, x) \leq \varepsilon$, $f(x, y) \leq \varepsilon$, $f(y, z) \leq \varepsilon$ imply $f(w, z) \leq 2\varepsilon$.

For any finite system $\mathfrak{p} = \{x = x_0, x_1, \ldots, x_n = y\}$ define $|\mathfrak{p}| = \sum_{k=1}^n f(x_{k-1}, x_k)$, and set

$$d(x, y) = \inf |\mathfrak{p}|,$$

where the infimum is taken over all such finite systems. We prove:

(4) $\frac{1}{2} f(x, y) \leq d(x, y) \leq f(x, y)$;
(5) $d(x, z) \leq d(x, y) + d(y, z)$;
(6) if $f(x, y) = f(y, x)$ for all $x, y$, then $d(x, y) = d(y, x)$.

The upper bound in (4) is immediate from the definition: choosing $\mathfrak{p} = \{x, y\}$ gives $d(x, y) \leq f(x, y)$.

For the lower bound in (4), let $\mathfrak{p} = \{x = x_0, x_1, \ldots, x_n = y\}$ be any finite system. Define $r$ to be the largest integer such that $\sum_{k=1}^r f(x_{k-1}, x_k) \leq \frac{1}{2}|\mathfrak{p}|$. By maximality of $r$, $\sum_{k=1}^{r+1} f(x_{k-1}, x_k) > \frac{1}{2}|\mathfrak{p}|$, hence $\sum_{k=r+2}^n f(x_{k-1}, x_k) < \frac{1}{2}|\mathfrak{p}|$.

By induction on the chain length and condition (3), one obtains:

(i) $f(x_0, x_r) \leq |\mathfrak{p}|$,
(ii) $f(x_r, x_{r+1}) \leq |\mathfrak{p}|$,
(iii) $f(x_{r+1}, x_n) < |\mathfrak{p}|$.

Applying condition (3) to the triple $(x_0, x_r, x_{r+1}, x_n)$ yields $f(x_0, x_n) \leq 2|\mathfrak{p}|$, i.e., $\frac{1}{2}f(x, y) \leq |\mathfrak{p}|$. Taking the infimum over all $\mathfrak{p}$ gives $\frac{1}{2}f(x, y) \leq d(x, y)$.

For (5), fix $x, y, z \in X$. Given any systems $\mathfrak{p} = \{x = x_0, \ldots, x_n = y\}$ and $\mathfrak{q} = \{y = y_0, \ldots, y_m = z\}$, let $\mathfrak{s}$ be their concatenation. Then $d(x, z) \leq |\mathfrak{s}| = |\mathfrak{p}| + |\mathfrak{q}|$. Varying $\mathfrak{p}$ and $\mathfrak{q}$ independently, we obtain $d(x, z) \leq d(x, y) + d(y, z)$.

For (6), symmetry of $f$ implies that every system $\mathfrak{p}$ from $x$ to $y$ has a reverse of equal sum from $y$ to $x$, hence $d(x, y) = d(y, x)$.

If $f(x, y) = f(y, x)$ for all $x, y$, and $f(x, y) > 0$ whenever $x \neq y$, then (4) shows $d(x, y) > 0$ for $x \neq y$, so $d$ is a metric on $X$.
