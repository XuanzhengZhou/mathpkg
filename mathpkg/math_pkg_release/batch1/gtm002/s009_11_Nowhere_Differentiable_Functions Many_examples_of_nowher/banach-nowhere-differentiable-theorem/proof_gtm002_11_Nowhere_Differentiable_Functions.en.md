---
role: proof
locale: en
of_concept: banach-nowhere-differentiable-theorem
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

**Step 1: Definition of $E_n$ and proof that $E_n$ is closed.**

Let $C$ be the space of continuous functions on $[0, 1]$ with the uniform metric. For each $n \in \mathbb{N}$, define

$$E_n = \{ f \in C : \exists\, x \in [0, 1 - 1/n] \text{ with } |f(x + h) - f(x)| \leq nh \text{ for all } 0 < h < 1 - x \}.$$

To see that $E_n$ is closed, let $f$ belong to the closure of $E_n$ and let $\{f_k\} \subset E_n$ converge uniformly to $f$. For each $k$, there exists $x_k \in [0, 1 - 1/n]$ such that $|f_k(x_k + h) - f_k(x_k)| \leq nh$ for all $0 < h < 1 - x_k$. Passing to a subsequence, assume $x_k \to x$ for some $x \in [0, 1 - 1/n]$. For any $h$ with $0 < h < 1 - x$, we have $0 < h < 1 - x_k$ for all sufficiently large $k$. Then

$$
\begin{aligned}
|f(x + h) - f(x)| &\leq |f(x + h) - f(x_k + h)|
+ |f(x_k + h) - f_k(x_k + h)| \\
&\quad + |f_k(x_k + h) - f_k(x_k)|
+ |f_k(x_k) - f(x_k)|
+ |f(x_k) - f(x)|.
\end{aligned}
$$

The first and fifth terms tend to $0$ by continuity of $f$; the second and fourth vanish by uniform convergence $f_k \to f$; the third is $\leq nh$ by definition of $x_k$. Hence $|f(x + h) - f(x)| \leq nh$, so $f \in E_n$. Thus $E_n$ is closed.

**Step 2: $E_n$ is nowhere dense.**

Any continuous function can be uniformly approximated by a piecewise-linear continuous function $g$. Let $M$ be the maximum absolute slope of the linear segments of $g$, and choose an integer $m$ such that $m\varepsilon > n + M$. Define the saw-tooth function

$$\phi(x) = \min(x - [x], [x] + 1 - x)$$

and set $h(x) = g(x) + \varepsilon \phi(mx)$. At each point of $[0, 1)$, the right derivative of $\varepsilon\phi(mx)$ is $\pm\varepsilon m$, while the right derivative of $g$ is at most $M$ in absolute value. Hence the right derivative of $h$ has absolute value at least $\varepsilon m - M > n$, so $h \notin E_n$. Since $\varrho(g, h) = \varepsilon/2 \leq \varepsilon$, it follows that $E_n$ is nowhere dense.

**Step 3: The set of functions with bounded right difference quotients is of first category.**

Since each $E_n$ is closed and nowhere dense, the set

$$E = \bigcup_{n=1}^{\infty} E_n$$

is of first category in $C$. The set $E$ is precisely the collection of all continuous functions on $[0, 1]$ that have a bounded right difference quotient at some point of $[0, 1)$.

**Step 4: Left difference quotients.**

The set of functions that have bounded left difference quotients at some point of $[0, 1]$ is also of first category. This follows by considering the isometry of $C$ induced by the substitution of $1 - x$ for $x$, which interchanges right and left difference quotients.

**Step 5: Conclusion.**

The union of these two first-category sets includes every continuous function that possesses a finite one-sided derivative at any point of $[0, 1]$. Since a finite union of first-category sets is of first category, the set of all such functions is of first category. By the Baire Category Theorem, its complement — the set of continuous functions that are nowhere differentiable — is a residual set in $C$. Thus, in the sense of Baire category, almost all continuous functions on $[0, 1]$ are nowhere differentiable.

By similar reasoning, one can show that a residual set of functions in $C$ have nowhere an infinite two-sided derivative.
