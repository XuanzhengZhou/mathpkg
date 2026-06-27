---
role: proof
locale: en
of_concept: hahn-banach-classical
source_book: gtm015
source_chapter: "3"
source_section: "28"
---

# Proof of Classical Hahn-Banach theorem

Let $E$ be a vector space over $\mathbb{R}$ and suppose $p$ is a real-valued function on $E$ such that (i) $p(x + y) \le p(x) + p(y)$ for all $x, y \in E$, and (ii) $p(\alpha x) = \alpha p(x)$ for all $x \in E$ and $\alpha > 0$. If $g$ is a linear form defined on a linear subspace $M$ of $E$, such that $g(y) \le p(y)$ for all $y \in M$, then $g$ may be extended to a linear form $f$ on $E$ such that $f(x) \le p(x)$ for all $x \in E$.

The proof uses Zorn's lemma. Consider the set of all pairs $(N, h)$ where $N$ is a linear subspace of $E$ containing $M$ and $h$ is a linear form on $N$ extending $g$ such that $h(y) \le p(y)$ for all $y \in N$. Order by: $(N_1, h_1) \le (N_2, h_2)$ if $N_1 \subset N_2$ and $h_2|_{N_1} = h_1$. By Zorn's lemma, there exists a maximal element $(T, f)$. If $T \ne E$, choose $a \in E \setminus T$ and extend $f$ to $T + \mathbb{R}a$ as follows.

For $y, z \in M$, by the properties of $p$ and $g$:
$$g(y) - g(z) = g(y - z) \le p(y - z) = p[(y + a) + (-z - a)] \le p(y + a) + p(-z - a).$$
Rearranging: $-g(z) - p(-z - a) \le -g(y) + p(y + a)$ for all $y, z \in M$.

Thus there exists $\beta \in \mathbb{R}$ (e.g., $\beta = \inf\{-g(y) + p(y + a) : y \in M\}$) satisfying
$$-g(z) - p(-z - a) \le \beta \le -g(y) + p(y + a) \quad \forall y, z \in M.$$

Define $f(y + \alpha a) = g(y) + \alpha \beta$ for $y \in M$, $\alpha \in \mathbb{R}$. One verifies that $f(x) \le p(x)$ for all $x \in T + \mathbb{R}a$, contradicting maximality of $T$. Hence $T = E$ and $f$ is the desired extension.
