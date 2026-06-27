---
role: proof
locale: en
of_concept: "fubini-let-be-a-sequence-of-nondecreasing-or"
source_book: gtm025
source_chapter: "Haar Measure"
source_section: "17.18"
---

There is no harm in supposing [and we do] that all $f_n$ are nondecreasing. Also, by considering the functions $f_n - f_n(a)$, we may suppose that $f_n \geq 0$. Thus $s = \sum_{n=1}^{\infty} f_n$ is nonnegative and nondecreasing. The derivative $s'(x)$ exists and is finite for almost all $x \in ]a, b[$, as (17.12) shows.

Consider then the partial sums $s_n = f_1 + f_2 + \cdots + f_n$, and the remainders $r_n = s - s_n$. Each $f_j$ has a finite derivative a.e.; hence there is a set

for $x \in A$ and $n = 1, 2, \dots$. Hence

$$\lim_{n \to \infty} s'_n(x) = \sum_{j=1}^{\infty} f'_j(x)$$

exists a.e., and it remains to show that $\lim_{n \to \infty} s'_n(x) = s'(x)$ a.e. Since the sequence $(s'_n(x))_{n=1}^{\infty}$ is nondecreasing for each $x \in A$, it suffices to show that $(s'_n)$ admits a subsequence converging a.e. to $s'$. To this end, let $n_1, n_2, \dots, n_k, \dots$ be an increasing sequence of integers such that

$$\sum_{k=1}^{\infty} [s(b) - s_{n_k}(b)] < \infty.$$

For each $n_k$ and for every $x \in ]a, b[$, we have

$$0 \leq s(x) - s_{n_k}(x) \leq s(b) - s_{n_k}(b).$$

The terms on the left side of this inequality are bounded by the terms of a convergent series of nonnegative terms. Hence $\sum_{k=1}^{\infty} [s(x) - s_{n_k}(x)]$ converges. The terms of this series are monotone functions that have finite derivatives a.e. Therefore the argument used above to prove that $\sum_{j=1}^{\infty} f'_j(x)$ converges a.e. also proves that $\sum_{k=1}^{\infty} [s'(x) - s'_{n_k}(x)]$ converges a.e.; and of course it follows that $\lim_{k \to \infty} s'_{n_k}(x) = s'(x)$ a.e. $\square$

We close this section with a long collection of exercises. A number are merely illustrative examples; several are minor theorems with sketched proofs [(17.24), (17.25), (17.26), (17.27), (17.31), (17.36), (17.37

that $\sum_{n=1}^{\infty} |u_n| < \infty$ and $\sum_{n=1}^{\infty} |v_n| < \infty$. Define

$$f_n(x) = \begin{cases} 0 & \text{if } x < a_n, \\ u_n & \text{if } x = a_n, \\ v_n & \text{if } x > a_n. \end{cases}$$

Prove that $s(x) = \sum_{n=1}^{\infty} f_n(x)$ has a finite derivative a.e., and that $s'(x) = 0$ a.e. [Hint. The function $s$ has finite variation; find each $V_a^x$ by using the numbers $|u_n|$ and $|v_n|$. Then apply (17.18).]

(17.22) Exercise. Find a real-valued strictly increasing function $f$ on $R$ such that $f'(x) = 0$ a.e.

(17.23) Exercise. Let $f \in \mathfrak{C}^r([a, b])$. Suppose that there exist real constants $\alpha < \beta$ such that

$$\alpha \leq D^+ f(x) \leq \beta$$

for all $x \in [a, b]$. Prove that

$$h \alpha \leq f(x + h) - f(x) \leq h \beta$$

if $a \leq x < x + h \leq b$. [Hint. Assuming that

$$f(x_0 + h_0) - f(x_0) < \gamma h_0 < \alpha h_0$$

and writing $h_1 = \sup \{h : 0 < h < h_0, f(x_0 + h) - f(x_0) \geq \gamma h\}$, show that $D^+ f(x_0 + h_1) < \alpha.$]

(17.24) Exercise. Let $f$ be a function in $\mathfrak{C}^r([a, b])$ and let $c$ be a number in $]a, b[$. Suppose that $D^+ f(c)$ is finite and that $D^+ f$ is continuous at $c$.

(17.28) Exercise. Let $E$ be a subset of $R$ that is the union of a family of quite arbitrary intervals, each being open, closed, or half open and half closed. Prove that $E$ is Lebesgue measurable. [Use VITALI's theorem.]

(17.29) Exercise. Let $\alpha$ and $\beta$ be positive real numbers. Define $f$ on $[0, 1]$ by $f(x) = x^\alpha \sin(x^{-\beta}) (0 < x \leq 1)$, $f(0) = 0$. Prove that $f$ is of finite variation on $[0, 1]$ if and only if $\alpha > \beta$.

(17.30) Exercise. Prove or disprove the following statement. If $f$ is a function in $\mathfrak{C}^r([0, 1])$, then there exist $a, b \in R$ such that $0 \leq a < b \leq 1$ and $f$ is of finite variation on $[a, b]$.

(17.31) Exercise. A function $f$ defined on an interval $I$ of $R$ is said to satisfy a Lipschitz condition of order $\alpha > 0$ if there exists a constant $M \geq 0$ such that

$$|f(x) - f(y)| \leq M |x - y|^\alpha$$

for all $x, y \in I$. We write $f \in \mathfrak{Lip}_\alpha(I)$. Prove the following.

(a) If $\alpha > 1$ and $f \in \mathfrak{Lip}_\alpha(I)$, then $f$ is a constant.

(b) If $0 < \alpha < 1$, then there exists a function $f \in \mathfrak{Lip}_\alpha([0, 1])$ such that $f$ has infinite variation over $[0, 1]$.

(c) There exists a continuous function of finite variation on $[0, 1]$ which satisfies no Lipschitz condition.

(d) If $f \in \mathfrak{C}^r([a, b])$, then $f \in \mathfrak{

each $n$, define

$$v_n = \sum_{k=1}^{m_n} \xi_{B_{n,k}}.$$

where $B_{n,k} = f([x_{k-1}^{(n)}, x_k^{(n)}])$. Prove that $v_n(y) \rightarrow v(y)$ for almost all $y \in R$ and apply B. Levi's monotone convergence theorem.] The function $v$ is known as the Banach indicatrix of $f$.

(17.35) Exercise. For an interval $[a, b] \subset R$, let $\mathfrak{V}([a, b])$ denote the set of all complex-valued functions $f$ on $[a, b]$ such that $V_a^b f < \infty$ and $f(a) = 0$. For $f \in \mathfrak{V}([a, b])$, define $\|f\| = V_a^b f$. Prove (a)–(c) and answer (d) and (e).

(a) With pointwise operations $\mathfrak{V}([a, b])$ is a complex linear algebra.

(b) For $f \in \mathfrak{V}([a, b])$, the inequality $\|f\|_u \leq \|f\|$ holds.

(c) With the above norm, $\mathfrak{V}([a, b])$ is a Banach space.

(d) Is it true that $\|fg\| \leq \|f\| \cdot \|g\|$ for all $f, g \in \mathfrak{V}([a, b])$?

(e) Find the least cardinal number of a dense subset of $\mathfrak{V}([a, b])$ in the topology defined by the variation norm.

(17.36) Exercise. Let $x$ be a real number and let $f$ be a real-valued function defined in a neighborhood of $x$. The upper [lower] first and second symmetric derivatives of $f$ at $x$ are defined to be the limits superior [inferior] of the expressions

$$\frac{f(x + h) - f(x - h)}{2h}$$

and

$$

$$y = \frac{z - y}{z - x} x + \frac{y - x}{z - x} z$$ and so $f(y) \leq \frac{z - y}{z - x} f(x) + \frac{y - x}{z - x} f(z)$. Hence

$$\frac{f(y) - f(x)}{y - x} \leq \frac{f(z) - f(x)}{z - x} \leq \frac{f(z) - f(y)}{z - y}. \tag{1}$$

From (1) our assertions follow easily.]

(b) Prove that $f$ is in $\mathfrak{Lip}_1([a, b])$ for all closed bounded subintervals $[a, b]$ of $I$. For $a < x < y < b$, (1) implies that

$$\frac{f(x) - f(a)}{x - a} \leq \frac{f(y) - f(x)}{y - x} \leq \frac{f(b) - f(y)}{b - y},$$

and from this and (a) it is easy to see that

$$\left| \frac{f(y) - f(x)}{y - x} \right| \leq \max \{ |f'_+ (a)|, |f'_- (b)| \}. \tag{c}$$

(c) Let $g$ be a real-valued function on an open interval $I$ in $R$. Prove that $g$ is convex if and only if $g$ is continuous and $\bar{D}_2 g \geq 0$ on $I$ [see (17.36)]. First suppose that $\bar{D}_2 g > 0$ on $I$, assume that $g$ is not convex on $I$, and find a point $x$ such that $\bar{D}_2 g(x) \leq 0$. Next consider the functions $g_n(x) = g(x) + \frac{1}{n} x^2$, $n = 1, 2, \ldots$.

§ 18. Absolutely continuous functions

In this section, we identify the class of functions $F$ of the form $F(x) = \int_a

Proof. For $x' > x$, the equality $|F(x') - F(x)| = \left| \int_x^x f(t) dt \right|$ holds; therefore it is clear from (12.34) that $F$ is uniformly continuous. If $a = x_0 < x_1 < \cdots < x_n = b$, then we have

$$\sum_{k=1}^{n} |F(x_k) - F(x_{k-1})| = \sum_{k=1}^{n} \left| \int_{x_{k-1}}^{x_k} f(t) dt \right| \leq \sum_{k=1}^{n} \int_{x_{k-1}}^{x_k} |f(t)| dt = \int_a^b |f(t)| dt.$$

Hence the inequality $V_a^b F \leq \int_a^b |f(t)| dt$ holds, and so $F$ has finite variation.

To prove the reversed inequality, first recall that step functions

$$\sigma = \sum_{k=1}^{n} \alpha_k \xi_{[x_{k-1}, x_k]} \quad (a = x_0 < x_1 < \cdots < x_n = b)$$

are dense in $\mathfrak{L}_1([a, b])$ (13.23). Consider the function $\text{sgn}\bar{f}$; for every positive integer $m$, select a step function $\sigma_m$ of the form (1) such that

$$\|\sigma_m - \text{sgn}\bar{f}\|_1 < \frac{1}{m}.$$

Since $|\text{sgn}\bar{f}(x)| = 1$ or 0 for every $x$, it is easy to see that the inequality (2) is only improved by replacing every $\alpha_k$ such that $|\alpha_k| > 1$ by the number $\alpha_k |\alpha_k|^{-1}$. There is thus no harm in supposing that $|\sigma_m(x)| \leq 1$ for all $x \in [a, b]$ and $m \in N$. Clearly $\sigma_m \rightarrow \text{sgn}\bar{f}$ in measure, and so by

The foregoing theorem shows that indefinite integrals are continuous and have finite variation. We wish now to show that the derivative of an indefinite integral is the integrated function [a.e.!]. To prove this, we need a preliminary, which is of some interest in its own right.
