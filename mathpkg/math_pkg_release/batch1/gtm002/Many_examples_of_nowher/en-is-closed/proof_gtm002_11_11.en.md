---
role: proof
locale: en
of_concept: en-is-closed
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

Consider any $f$ in the closure of $E_n$, and let $\{f_k\}$ be a sequence in $E_n$ that converges uniformly to $f$. There is a corresponding sequence of numbers $x_k$ such that, for each $k$,

(1) $0 \leq x_k \leq 1 - 1/n$ and

(2) $|f_k(x_k + h) - f_k(x_k)| \leq n h$ for all $0 < h < 1 - x_k$.

We may assume also that

(3) $x_k \to x$, for some $0 \leq x \leq 1 - 1/n$,

since this condition will be satisfied if we replace $\{f_k\}$ by a suitably chosen subsequence. If $0 < h < 1 - x$, the inequality $0 < h < 1 - x_k$ holds for all sufficiently large $k$, and then

$$
\begin{aligned}
|f(x + h) - f(x)| &\leq |f(x + h) - f(x_k + h)| + |f(x_k + h) - f_k(x_k + h)| \\
&\quad + |f_k(x_k + h) - f_k(x_k)| + |f_k(x_k) - f(x_k)| + |f(x_k) - f(x)|.
\end{aligned}
$$

The first term tends to $0$ as $k \to \infty$ by continuity of $f$ at $x + h$ and the convergence $x_k \to x$. The second term tends to $0$ by uniform convergence $f_k \to f$. The third term is $\leq n h$ by condition (2). The fourth term tends to $0$ by uniform convergence. The fifth term tends to $0$ by continuity of $f$ at $x$ and $x_k \to x$. Hence $|f(x+h) - f(x)| \leq n h$, so $f \in E_n$. Therefore $E_n$ is closed.
