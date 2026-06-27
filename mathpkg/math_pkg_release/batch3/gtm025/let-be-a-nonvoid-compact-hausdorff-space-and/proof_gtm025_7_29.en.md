---
role: proof
locale: en
of_concept: "let-be-a-nonvoid-compact-hausdorff-space-and"
source_book: gtm025
source_chapter: "Spaces of Continuous Functions"
source_section: "7.29"
---

Consider $f_0 \in \mathfrak{C}'(X)$. If $f_0$ is constant, then the approximation is trivial. If not, we have

$$c = \inf\{f_0(x) : x \in X\} < d = \sup\{f_0(x) : x \in X\}.$$

Let $f = \frac{2}{d - c}(f_0 - d) + 1$, so that $f(X) \subset [-1, 1]$ and $\inf f = -1$, $\sup f = 1$. It obviously suffices to prove that $f$ lies in the closure of $\mathfrak{S}$.

Consider the nonvoid compact sets $E = \{x \in X : f(x) \leq -\frac{1}{3}\}$ and $F = \{x \in X : f(x) \geq \frac{1}{3}\}$. For every $x \in E$ and $y

Hence the function $\psi = \max \left\{\varphi_{y_1}, \varphi_{y_2}, \ldots, \varphi_{y_n}\right\}$ is in $\mathfrak{S}$ and satisfies the following inequalities: $\psi(x) < -\frac{1}{3}$ for all $x \in E$ and $\psi(x) > \frac{1}{3}$ for all $x \in F$. Now define $w_1$ by

$$w_1 = \min \left\{\max \left\{\psi, -\frac{1}{3}\right\}, \frac{1}{3}\right\}.$$

It is clear that $w_1 \in \mathfrak{S}$, $w_1(E) = \left\{-\frac{1}{3}\right\}$, $w_1(F) = \left\{\frac{1}{3}\right\}$, and $w_1(X) \subset \left[-\frac{1}{3}, \frac{1}{3}\right]$. The definitions of $E$ and $F$ show that

$$\|f - w_1\|_u = \frac{2}{3}.$$

The function $\frac{3}{2}(f - w_1)$ is in $\mathfrak{C}^r(X)$ and has minimum $-1$ and maximum 1. The method used to construct $w_1$ can again be used to approximate $\frac{3}{2}(f - w_1)$. Thus there exists $w_2 \in \mathfrak{S}$ such that

$$\left\|\frac{3}{2}(f - w_1) - w_2\right\|_u = \frac{2}{3}.$$

Multiplying by $\frac{2}{3}$, we have

$$\left\|f - w_1 - \frac{2}{3}w_2\right\|_u = \left(\frac{2}{3}\right)^2.$$

Our scheme is now clear. In the next step we approximate

$$\left(\frac{3}{2}\right)^2\left(f - w_1 - \frac{2}{3}w_2\right)$$

by a suitable function $w_3$ in

is a subalgebra of $\mathfrak{C}'(X)$. Suppose that $f$ and $g$ are in $\mathfrak{P}^{-}$, and that

$$\lim_{n \to \infty} \|f - f_n\|_u = 0, \quad \lim_{n \to \infty} \|g - g_n\|_u = 0,$$

where $f_n$ and $g_n$ are in $\mathfrak{P}$. Theorem (7.27) proves that $\max\{f_n, g_n\}$ is in $\mathfrak{P}^{-}$. It is easy to see from (5.36) that

$$\|\max\{f_n, g_n\} - \max\{f, g\}\|_u \leq \|f_n - f\|_u + \|g_n - g\|_u,$$

and so $\max\{f, g\}$ is in $(\mathfrak{P}^{-})^{-} = \mathfrak{P}^{-}$. Thus $\mathfrak{P}^{-}$ satisfies all the hypotheses imposed on $\mathfrak{S}$ in (7.29), and (7.29) therefore implies that $(\mathfrak{P}^{-})^{-} = \mathfrak{P}^{-}$ is $\mathfrak{C}'(X)$.
