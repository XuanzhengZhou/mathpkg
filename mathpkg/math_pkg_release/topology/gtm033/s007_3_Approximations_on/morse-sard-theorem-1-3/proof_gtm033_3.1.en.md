---
role: proof
locale: en
of_concept: morse-sard-theorem-1-3
source_book: gtm033
source_chapter: "3"
source_section: "1. The Morse-Sard Theorem"
---

# Proof of the Morse-Sard Theorem (Theorem 1.3) for $C^\infty$ Maps

**Morse-Sard Theorem.** Let $M, N$ be manifolds of dimensions $m, n$ and $f: M \to N$ a $C^r$ map. If $r > \max\{0, m - n\}$, then the set of critical values $f(\Sigma_f)$ has measure zero in $N$.

*Proof for $C^\infty$ Maps.* It suffices to prove a local theorem; thus we deal with a $C^\infty$ map $f: W \to \mathbb{R}^n$ where $W \subset \mathbb{R}^m$ is open. If $m < n$ then $f(W)$ has measure zero by Proposition 1.2. We assume from now on that $m \geqslant n$.

**Step 1: Decomposition of the critical set.** Express the critical set $\Sigma_f$ as the union of three subsets. Write $f(x) = (f_1(x), \ldots, f_n(x))$.

- $\Sigma^1$ is the set of points $p \in \Sigma_f$ such that $\Delta f_i(p) = 0$ for all differential operators $\Delta$ of order $\leqslant m/n$ and all $i = 1, \ldots, n$.

- $\Sigma^2$ is the set of points $p \in \Sigma_f$ such that $\Delta f_i(p) \neq 0$ for some $i$ and some differential operator $\Delta$ of order $\geqslant 2$.

- $\Sigma^3$ is the set of points $p \in \Sigma_f$ such that $\frac{\partial f_i}{\partial x_j}(p) \neq 0$ for some $i, j$.

Clearly $\Sigma_f = \Sigma^1 \cup \Sigma^2 \cup \Sigma^3$.

**Step 2: $f(\Sigma^1)$ has measure zero.** Let $v$ be the smallest integer such that $v > m/n$. The Taylor expansion of $f$ of order $v$ about points of $\Sigma^1$ shows that every point of $\Sigma^1$ has a neighborhood $U$ in $W$ such that if $p \in \Sigma^1 \cap U$ and $q \in U$ then

$$|f(p) - f(q)| \leqslant B|x - y|^v, \quad B \geqslant 0.$$

We take $U$ to be a cube of edge $\lambda$. Divide $U$ into $s^m$ cubes of edge $\lambda/s$. Denote those that meet $\Sigma^1$ by $C_k$, $k = 1, \ldots, t$, where $t \leqslant s^m$.

Each $C_k$ is contained in a ball of radius $(\lambda/s)\sqrt{m}$ centered at a point of $U \cap \Sigma^1$. Therefore $f(C_k)$ is contained in a cube $C_k' \subset \mathbb{R}^n$ whose edge is not more than

$$2B\left(\frac{\lambda}{s}\sqrt{m}\right)^v = A s^{-v}.$$

The sum of the measures of all such $C_k'$ is at most

$$t \cdot (A s^{-v})^n \leqslant s^m \cdot A^n s^{-vn} = A^n s^{m-vn}.$$

Since $v > m/n$, we have $m - vn < 0$, so this sum tends to $0$ as $s \to \infty$. Thus $f(U \cap \Sigma^1)$ has measure zero.

**Step 3: $f(\Sigma^2)$ has measure zero.** This follows by induction on $m$, using the implicit function theorem and Fubini's theorem (the proof is similar to Step 4 below but with higher-order derivatives).

**Step 4: $f(\Sigma^3)$ has measure zero.** Every point $p \in \Sigma^3$ has an open neighborhood $U \subset W$ on which, for some $i, j$, $\partial f_i / \partial x_j \neq 0$. By the implicit function theorem we may choose $U$ so that there is an open set $A \times B \subset \mathbb{R}^{m-1} \times \mathbb{R}$ and a $C^\infty$ diffeomorphism $h: A \times B \to U$ such that $f_i(x_1, \ldots, x_{m-1}, t) \equiv t$ for $(x, t) \in A \times B$.

Reorder coordinates so that $f_i = f_n$. Identify $U$ with $A \times B$ via $h$; now $f|U$ has the form

$$\mathbb{R}^{m-1} \times \mathbb{R} \supset A \times B \xrightarrow{f} \mathbb{R}^{n-1} \times \mathbb{R},$$
$$f(x, t) = (u_t(x), t)$$

where for each $t \in B$, $u_t: A \to \mathbb{R}^{n-1}$ is a $C^\infty$ map. It is easy to see that $(x, t)$ is critical for $f$ if and only if $x$ is critical for $u_t$. Thus

$$\Sigma_f \cap (A \times B) = \bigcup_{t \in B} \Sigma_{u_t} \times \{t\}.$$

Since $\dim A = m - 1$, the inductive hypothesis (on dimension $m$) implies that

$$\mu_{n-1}(u_t(\Sigma_{u_t})) = 0$$

where $\mu_{n-1}$ denotes Lebesgue measure in $\mathbb{R}^{n-1}$. Fubini's theorem now implies that

$$\mu_n\!\left(\bigcup_{t \in B} u_t(\Sigma_{u_t}) \times \{t\}\right) = \int_B \mu_{n-1}(u_t(\Sigma_{u_t}))\,dt = 0.$$

Thus $f(\Sigma^3 \cap U)$ has measure zero. Since $\Sigma^3$ can be covered by countably many such neighborhoods $U$, $f(\Sigma^3)$ has measure zero.

Since $\Sigma_f = \Sigma^1 \cup \Sigma^2 \cup \Sigma^3$ and each of $f(\Sigma^1), f(\Sigma^2), f(\Sigma^3)$ has measure zero, the set of critical values $f(\Sigma_f)$ has measure zero.

QED
