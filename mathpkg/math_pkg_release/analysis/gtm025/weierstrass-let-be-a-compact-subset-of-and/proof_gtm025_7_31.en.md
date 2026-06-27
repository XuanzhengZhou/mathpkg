---
role: proof
locale: en
of_concept: "weierstrass-let-be-a-compact-subset-of-and"
source_book: gtm025
source_chapter: "Spaces of Continuous Functions"
source_section: "7.31"
---

The corollary is simply (7.30) with $\mathfrak{S} = \{\iota, 1\}$ where $\iota(x) = x$ for all $x \in X$.

(7.32) Remarks. The hypothesis in (7.29) and (7.30) that $\mathfrak{S}$ be a separating family of functions is obviously necessary. Let $X$ be a compact Hausdorff space containing at least two points

if $x_1 < x_2$. Hence the one-element family $\{exp\}$ is a separating family on $R$, and the family of polynomials in exp and 1 is dense in $\mathfrak{C}^r(X)$ for every compact subset $X$ of $R$. These polynomials are precisely all functions $P$ of the form $P(x) = \sum_{k=0}^{n} \alpha_k \exp(n_k x)$, where the $\alpha_k$'s are real numbers, the $n_k$'s are nonnegative integers, and $n = 1, 2, 3, \ldots$.

(c) Polynomials in the cosine function and 1 are dense in $\mathfrak{C}^r([0, \pi])$. For every $n \in N$, $\cos^n(x)$ can be written as a linear combination of terms of the form $\cos(kx)$ and 1 [this fact can be proved by induction on $n$]. Hence the family of all linear combinations of the functions 1, $\cos(x)$, $\cos(2x)$, $\ldots$ is dense in $\mathfrak{C}^r([0, \pi])$.

(d) Consider $\mathfrak{C}^r([0, 1])$ and the smallest subset $\mathfrak{S}$ of $\mathfrak{C}^r([0, 1])$ containing 1, the function $\iota [\iota(x) = x]$, and satisfying (7.29.iii)–(7.29.v). It is not hard to see that $\mathfrak{S}$ is exactly the linear lattice consisting of all piecewise linear, continuous, real-valued functions $f$ on $[0, 1]$. That is, there are a finite number of subintervals $[0, x_1], [x_1, x_2], \ldots, [x_{n-1}, 1]$ such that $0 < x_1 < \cdots < x_{n-1} < 1$ and such that $f$ is linear on each $[x_{k-1}, x_k]$. Theorem (7.29) shows that $\mathfrak{S}$ is dense in $\

(7.35) Examples. (a) Let $X = \{z \in K : |z| \leq 1\}$, and let $\mathfrak{S} = \{\iota\}$ where $\iota(z) = z$. Uniform limits of polynomials in $\iota$ and 1 are analytic on the open unit disk $\{z \in K : |z| < 1\}$ and continuous on the closed unit disk $\{z \in K : |z| \leq 1\}$. There are certainly nonanalytic continuous functions on the unit disk, and so polynomials in functions from $\mathfrak{S}$ are not dense in $\mathfrak{C}(X)$. Thus some additional hypothesis is necessary in the complex Stone-Weierstrass theorem. Conditions on $X$ under which the theorem holds for $\mathfrak{C}(X)$ with no additional hypothesis have been found by W. Rudin [Proc. Amer. Math. Soc. 8, 39–42 (1957)].

(b) Let $T = \{z \in K : |z| = 1\}$, and consider the function $\iota$ on $T$ given by $\iota(z) = z$. For any $z \in T$, we have $z = \exp(ix) = \cos(x) + i \sin(x)$, for exactly one $x \in [0, 2\pi]$. Hence $\iota(\exp(ix)) = \exp(ix)$, and we see that $\{\iota\}$ is a separating family for $T$. We have $\bar{\iota}(z) = \overline{\iota(\exp(ix))} = \cos(x) - i \sin(x) = \cos(-x) + i \sin(-x) = \exp(-ix)$. Recall that $\exp(ix)^n = \exp(inx)$, $n = 1, 2, \ldots$. The family $\{\iota, \bar{\iota}, 1\}$ satisfies the conditions of (7.34). Now let $f \in \mathfrak{C}(T)$ and let $\varepsilon > 0$. By the above remarks there is a function

$$\exp(ix) \rightarrow \

for a fixed point $x_0 \in X$. A separating subalgebra $\mathfrak{A}$ of $\mathfrak{C}_0^r(X)$ vanishing identically at no point of $X$ is dense in $\mathfrak{C}_0^r(X)$.

(c) State and prove complex versions of (a) and (b).

(7.38) Exercise. Theorems (7.29) and (7.30) are incomparable, in the sense that subalgebras of $\mathfrak{C}^r(X)$ need not be sublattices and sublattices need not be subalgebras.

(a) Let $P$ and $Q$ be real polynomials on $[0, 1]$. Prove that $\max\{P, Q\}$ is a polynomial if and only if $P \geq Q$ or $Q \geq P$. Prove, however, that if $P_1, Q_1, P_2$, and $Q_2$ are polynomials such that $P_1 \leq P_2, P_1 \leq Q_2, Q_1 \leq P_2$, and $Q_1 \leq Q_2$, then there is a polynomial $\Phi$ such that $\max\{P_1, Q_1\} \leq \Phi \leq \min\{P_2, Q_2\}$.

(b) The sublattice $\mathfrak{S}$ of $\mathfrak{C}^r([0, 1])$ defined in (7.33.d) is not a subalgebra of $\mathfrak{C}^r([0, 1])$. Prove that if $f$ and $f^2$ are both in $\mathfrak{S}$, then $f$ is a constant. Find conditions on $f$ and $g$ in $\mathfrak{S}$ necessary and sufficient for $fg$ to be in $\mathfrak{S}$.

(7.39) Exercise. Let $X$ be a nonvoid compact subset of $R^n$, where $n \in N$. For $x = (x_1, \ldots, x_n) \in X$ and $(k_1, \

$f^{\dagger}(X \cap U') \subset \{0\}$. Let $\alpha^{\dagger} = \max\{\alpha, 0\}$ and $\beta^{\dagger} = \min\{\beta, 0\}$. Then define the function $\varphi$ on $X$ as

$$\varphi = \min\{\max\{f^{\dagger}, \beta^{\dagger}\}, \alpha^{\dagger}\}.$$

It is clear that $\varphi$ is in $\mathfrak{C}^r(X)$, and it is easy to see that: $\varphi(x) = f(x)$ for $x \in Y$; $\alpha^{\dagger} = \max\{\varphi(x) : x \in X\}$; $\beta^{\dagger} = \min\{\varphi(x) : x \in X\}$; $\varphi(x) = 0$ for $x \in X \cap U'$. Thus $\varphi$ is an extension of $f$ of the sort we want for which $\|\varphi\|_u = \|f\|_u$. That is, if $f \in \mathfrak{S}$, then $f$ admits an extension $f^{\dagger}$ such that $\|f^{\dagger}\|_u = \|f\|_u$.

Now let $g$ be a function in $\mathfrak{C}^r(Y)$ that is the uniform limit on $Y$ of a sequence $(f_n)_{n=1}^{\infty}$ of functions in $\mathfrak{S}$. Choose a subsequence $(f_{n_k})_{k=1}^{\infty}$ such that $\|f_{n_k} - f_{n_{k+1}}\|_u < 2^{-k}$ and write $g_k = f_{n_k} - f_{n_{k+1}}$ ($k = 1, 2, 3, \ldots$). Then we have

$$g - f_{n_1} = \sum_{k=1}^{\infty} g_k,$$

where the infinite series converges uniformly on $Y$, and $\|g_k\|_u < 2^{-k}$. Now let $g_k^{\dagger}$ be a continuous extension of $g_k$ over $X$ such that $

$$|\varphi(x) - f(x)| < \varepsilon$$ and $$|\varphi(y) - f(y)| < \varepsilon.$$ Prove that for each $\varepsilon > 0$ there exists a function $h \in \mathfrak{L}$ such that $$\|\varphi - h\|_u < \varepsilon.$$

(7.44) Exercise [ROBERT I. JEWETT]. Let $I$ denote the interval $[0, 1]$. A family $\mathfrak{F}$ of functions is said to have property $V$ if

(i) $\mathfrak{F} \subset I^X$ for some set $X$,

(ii) $f \in \mathfrak{F}$ implies $(1 - f) \in \mathfrak{F}$, and

(iii) $f, g \in \mathfrak{F}$ implies $fg \in \mathfrak{F}$.

Supply $I^X$ with the topology of uniform convergence [the topology induced by the uniform metric]. Prove assertions (a)–(k). [This exercise is rather difficult.]

(a) If $X$ is a set and $\mathfrak{A} \subset I^X$, then $\mathfrak{A}$ is contained in a smallest subfamily [closed subfamily] of $I^X$ having property $V$. [Intersect a collection of families.]

Suppose that $X$ is a topological space, and let $\mathfrak{D}(X) = I^X \cap \mathfrak{C}(X)$. For $n \in N$, let $\mathfrak{P}_n$ be the smallest subfamily of $\mathfrak{D}(I^n)$ that has property $V$ and contains the $n$ projections

$$(x_1, \ldots, x_n) \rightarrow x_k \quad (k = 1, \ldots, n).$$

(b) If $\mathfrak{F}$ has property $V$, if $\{f_1, \ldots, f_n\} \subset \mathfrak{F}$, and if $p \in \mathfrak{P}_n$, then the function $f$ defined on $X$ by

[Take $p(x, y) = (1 - p_1(x))p_2(x)(1 - p_3(y))p_4(y)$, where the $p_j$'s are obtained by using (d).]

(g) Let $A$ and $B$ be disjoint compact subsets of $I^2$, and consider arbitrary $\varepsilon > 0$ and $p \in \mathfrak{P}_2$. Then there exists $q \in \mathfrak{P}_2$ such that

$$q \geq p \quad \text{on} \quad I^2,$$

$$q > 1 - \varepsilon \quad \text{on} \quad A,$$

and

$$q < p + \varepsilon \quad \text{on} \quad B.$$

[Let $4\delta = \text{dist}(A, B)$. Use compactness and (f) to piece together a $q_0 \in \mathfrak{P}_2$ such that $q_0$ is near 1 on $B$ and near 0 on $A$. Then let $q = 1 - (1 - p)q_0.$]

(h) Define $\varphi$ and $\psi$ on $I^2$ by $\varphi(x, y) = \max\{x, y\}$ and $\psi(x, y) = \min\{x, y\}$. For each $\varepsilon > 0$ there exist functions $r, q \in \mathfrak{P}_2$ such that

$$\|\varphi - r\|_u < \varepsilon$$

and

$$\|\psi - q\|_u < \varepsilon.$$

[Let $8\delta = \varepsilon < 1$. Let $C = \{(x, y) \in I^2 : \delta \leq \psi(x, y) \leq 1 - \delta\}$ and choose $m \in N$ such that $(xy)^m < \delta$ on $C$. Let $p(x, y) = 1 - (xy)^m$. Then $p \in \mathfrak{P}_2$ and $1 - \delta < p < 1$ on $C$. For $k \geq 0$ let $A

as $\{1, i, j, k\}$, with the following multiplication table:

| | 1 | $i$ | $j$ | $k$ |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | $i$ | $j$ | $k$ |
| $i$ | $i$ | $-1$ | $k$ | $-j$ |
| $j$ | $j$ | $-k$ | $-1$ | $i$ |
| $k$ | $k$ | $j$ | $-i$ | $-1$ |

Products $(a1 + bi + cj + dk)(a'1 + b'i + c'j + d'k)$ [real coefficients!] are defined by supposing that $H$ is an associative algebra over $R$. Prove the following.

(a) For every $a1 + bi + cj + dk \in H$,

$$(a1 + bi + cj + dk)(a1 - bi - cj - dk) = (a^2 + b^2 + c^2 + d^2)1.$$

(b) The set $H \cap \{01 + 0i + 0j + 0k\}'$ is a non-Abelian group under multiplication.

(c) For $x = a1 + bi + cj + dk \in H$, we have $x - ixi - jxj - kxk = 4a1.$

(d) For $x = a1 + bi + cj + dk \in H$, let $\|x\| = (a^2 + b^2 + c^2 + d^2)^{\frac{1}{2}}$. Prove that $\| \|$ is a norm on $H$ (7.5) and that $\|xy\| = \|x\| \|y\|$ for all $x, y \in H.$

(e) Let $X$ be a topological space and $\mathfrak{C}(X, H)$ the set of all continuous mappings $f$ of $X$ into $H$ [make $H$ into a metric and hence topological space via the norm] for which $\|f\|_

CHAPTER THREE

The Lebesgue Integral

Integration from one point of view is an averaging process for functions, and it is in this spirit that we will introduce and discuss integration. In applying an averaging process to a class $f$ of real- or complex-valued functions, a number $I(f)$ is assigned to each $f \in f$. If $I(f)$ is to be an average, then it should certainly satisfy the conditions

$$I(f + g) = I(f) + I(g),$$
$$I(\alpha f) = \alpha I(f)$$

for $f, g \in f$ and $\alpha \in R$. A less essential but often desirable property for $I$ is that $I(f) \geq 0$ if $f \geq 0$. In some cases these three properties suffice to identify the averaging process completely.

Let us mention a few such averaging processes. Suppose for example that $f$ is all real-valued functions on the finite set $\{1, 2, 3, \ldots, n\}$, i.e., $f = R^n$, and define

$$e_j(k) = \begin{cases} 1 & \text{if } j = k, \\ 0 & \text{if } j \neq k; \end{cases}$$

that is, $e_j(k) = \delta_{jk}$. For each $f \in f$, we have

$$f = \sum_{j=1}^{n} f(j) e_j.$$

For any "integral" $I$ we must have

$$I(f) = \sum_{j=1}^{n} f(j) I(e_j).$$

In fact if we choose the numbers $I(e_1), I(e_2), \ldots, I(e_n)$ arbitrarily, then an integral $I$ satisfying the first two conditions is determined by the above sum for all $f \in f$. Hence in this case the integral is merely a finite sum in which certain weights have been assigned to the points in the domain of the function. To satisfy the third property, we need only require that $I(e_j) \geq 0$.

If $f = \mathfrak{C}([0, 1])$ and $I(f) = \int_

Let $(x_n)_{n=1}^{\infty}$ be an enumeration of a countably infinite set $C$, let $(\alpha_n)$ be a sequence of complex numbers such that $\sum_{n=1}^{\infty} |\alpha_n| < \infty$, and let $\mathfrak{F}$ be the set of all bounded complex-valued functions defined on $C$. Then $I$ defined on $\mathfrak{F}$ by $I(f) = \sum_{n=1}^{\infty} \alpha_n f(x_n)$ is an average. It satisfies the third property if and only if $\alpha_n \geq 0$ for all $n$.

As a final example, let $\mathfrak{F}$ be all complex-valued functions $f$ on the set $C$ of our last example such that $\sum_{n=1}^{\infty} |f(x_n)|^2 < \infty$. For fixed $g \in \mathfrak{F}$ let $I_g(f) = \sum_{n=1}^{\infty} f(x_n) \overline{g(x_n)}$. This series converges absolutely by Cauchy's inequality (13.13), i.e.,

$$|I_g(f)| \leq \left( \sum_{n=1}^{\infty} |f(x_n)|^2 \right)^{\frac{1}{2}} \left( \sum_{n=1}^{\infty} |g(x_n)|^2 \right)^{\frac{1}{2}}.$$

In this chapter we will first discuss averages of continuous functions and then extend the process to wider classes of functions. In particular, we will extend the Riemann integral qua averaging process to obtain the Lebesgue integral.

We begin with a rapid review of the Riemann-Stieltjes integral, which is a classical device for averaging continuous functions on intervals $[a, b]$.

§ 8. The Riemann-Stieltjes integral
