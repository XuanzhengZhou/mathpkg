---
role: proof
locale: en
of_concept: difference-quotient-set-is-closed
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

Consider any $f$ in the closure of $E_n$, and let $\{f_k\}$ be a sequence in $E_n$ that converges uniformly to $f$. For each $k$, there exists a number $x_k$ such that

$$0 \leq x_k \leq 1 - 1/n$$

and

$$|f_k(x_k + h) - f_k(x_k)| \leq nh \quad \text{for all } 0 < h < 1 - x_k.$$

By passing to a suitably chosen subsequence, we may assume that

$$x_k \to x \quad \text{for some } 0 \leq x \leq 1 - 1/n.$$

Now take any $h$ with $0 < h < 1 - x$. For all sufficiently large $k$, the inequality $0 < h < 1 - x_k$ holds. Applying the triangle inequality, we estimate

$$
\begin{aligned}
|f(x + h) - f(x)| &\leq |f(x + h) - f(x_k + h)| \\
&\quad + |f(x_k + h) - f_k(x_k + h)| \\
&\quad + |f_k(x_k + h) - f_k(x_k)| \\
&\quad + |f_k(x_k) - f(x_k)| \\
&\quad + |f(x_k) - f(x)|.
\end{aligned}
$$

The first and fifth terms tend to $0$ because $f$ is continuous and $x_k \to x$. The second and fourth terms tend to $0$ because $f_k \to f$ uniformly. The third term is bounded by $nh$ by the defining property of $x_k$. Therefore

$$|f(x + h) - f(x)| \leq nh \quad \text{for all } 0 < h < 1 - x,$$

which shows that $f \in E_n$. Hence $E_n$ is closed.
