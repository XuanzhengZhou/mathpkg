---
role: proof
locale: en
of_concept: "let-be-an-inner-product-space-not-that"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.23"
---

Suppose, as we may, that $0 \notin D$, and enumerate $D$ as $(x_n)_{n=1}^{\infty}$. Define $y_1 = x_{n_1}$ where $n_1 = 1$. Suppose that $y_1 = x_{n_1}, \ldots, y_k = x_{n_k}$ have been defined and are linearly independent, and that $n_1 < n_2 < \cdots < n_k$. If there is no $j > n_k$ such that $\{y_1, \ldots, y_k, x_j\}$ is linearly independent, stop the process. Otherwise let $n_{k+1}$ be the smallest such $j$ and define $y_{k+1} = x_{n_{k+1}}$. We have thus defined a finite or countably infinite linearly independent set $\{y_1, y_2, \ldots\} \subset D$. Let $S$ be the smallest linear

preserves all inner product space structure, i.e., it is one-to-one, onto, linear, and preserves inner products [hence norms as well]. The converse is trivial. $\square$

(16.25) Example. By way of illustration, we work out a certain classical orthonormal set. For each integer $n \geq 0$, define $f_n$ on $R$ by

$$f_n(x) = x^n \exp \left[ -\frac{x^2}{2} \right].$$

Since $\sum_{k=1}^{\infty} \frac{k^2 n}{\exp(k^2)} < \infty$ for all $n \geq 0$, each $f_n$ is evidently in the Hilbert space $\mathfrak{L}_2(R, \mathcal{M}_\lambda, \lambda)$. Since each polynomial has only finitely many roots, the set $\{f_n\}_{n=0}^{\infty}$ is linearly independent over $K$. For each integer $n \geq 0$, define

$$H_n(x) = (-1)^n \exp[x^2] \exp^{(n)}[-x^2],$$

where the superscript $^{(n)}$ denotes the $n^{th}$ derivative of the function $x \rightarrow \exp[-x^2]$. The functions $(H_n)_{n=0}^{\infty}$ are clearly all polynomials. They are called the Hermite polynomials. The first three Hermite polynomials are

$$H_0(x) = 1,$$
$$H_1(x) = 2x,$$
$$H_2(x) = 4x^2 - 2.$$

One can go on computing them as long as patience will permit. Next let

$$\varphi_n(x) = \exp \left[ -\frac{x^2}{2} \right] H_n(x);$$

these functions are called the Hermite functions. They are all in $\mathfrak{L}_2(R, \mathcal{M}_\lambda, \lambda)$, and, as we will now show, they are an orthogonal set. First we have

$$\varphi''_n(x) = (-1)^n \left\{(x^2 + 1

Substituting this expression in (1), we obtain

$$\varphi_n''(x) = (-1)^n \exp \left[ \frac{x^2}{2} \right] \left\{ (x^2 + 1) \exp^{(n)}[-x^2] + 2x \exp^{(n+1)}[-x^2] \right.$$

$$+ (-2x \exp^{(n+1)}[-x^2] - 2(n+1) \exp^{(n)}[-x^2]) \right\}$$

$$= (-1)^n \exp \left[ \frac{x^2}{2} \right] \exp^{(n)}[-x^2] (x^2 - 2n - 1) = (x^2 - 2n - 1) \varphi_n(x).$$

Thus every $\varphi_n$ satisfies the differential equation

$$\varphi_n''(x) = (x^2 - 2n - 1) \varphi_n(x).$$

Hence for every pair of nonnegative integers $m$ and $n$, we have

$$\varphi_n''\varphi_m - \varphi_n\varphi_m' = (x^2 - 2n - 1) \varphi_n\varphi_m - (x^2 - 2m - 1) \varphi_n\varphi_m = 2(m - n) \varphi_n\varphi_m.$$

If $m \neq n$, we have

$$\int_{-\infty}^{\infty} \varphi_n\varphi_m \, dx = \frac{1}{2(m - n)} \int_{-\infty}^{\infty} \left[ \varphi_n''\varphi_m - \varphi_n\varphi_m' \right] \, dx$$

$$= \frac{1}{2(m - n)} \lim_{A \to \infty} \left\{ \varphi_m\varphi_n' \left| A - A \int_{-A}^{A} \varphi_n'\varphi_m' \, dx - \varphi_m'\varphi_n \right| A + \int_{-A}^{A} \varphi_n'\varphi_m' \, dx \right\} = 0.$$

[This computation requires Lebesgue's theorem on dominated convergence.] Thus the set $\{\varphi_n\}_{

as is well known. [See (21.60) infra.] Next, we have

$$\int_{-\infty}^{\infty} \varphi_n^2(x) \, dx = \int_{-\infty}^{\infty} \exp[-(x^2)] H_n^2(x) \, dx$$

$$= \int_{-\infty}^{\infty} \exp[-(x^2)] H_n(x) \exp[x^2] (-1)^n \exp^{(n)}(-x^2) \, dx$$

$$= (-1)^n \int_{-\infty}^{\infty} H_n(x) \exp^{(n)}(-x^2) \, dx$$

$$= \lim_{A \to \infty} \left\{ (-1)^n H_n(x) \exp^{(n-1)}(-x^2) \right|_{-A} + (-1)^n \int_{-A}^{\infty} H_n'(x) \exp^{(n-1)}(-x^2) \, dx \right\}$$

$$= 2n \int_{-\infty}^{\infty} (-1)^n -1 H_{n-1}(x) \exp^{(n-1)}(-x^2) \, dx$$

$$= 2n \int_{-\infty}^{\infty} \varphi_n^2(x) \, dx.$$

This establishes the recursive formula

$$\int_{-\infty}^{\infty} \varphi_n^2(x) \, dx = 2n \int_{-\infty}^{\infty} \varphi_n^2_{n-1}(x) \, dx,$$

and it follows that

$$\int_{-\infty}^{\infty} \varphi_n^2(x) \, dx = \pi^{\frac{1}{2}} 2^n n!$$

for $n = 0, 1, 2, \ldots$. Hence the functions $\{\psi_n\}_{n=0}^{\infty}$ given by $\psi_n(x) = \left( \pi^{\frac{1}{2}} 2^n n! \right)^{-\frac{1}{2}} \varphi_n(x) = \left( \pi^{\frac{1}{2}} 2^n n! \right)^{-\frac{1}{2}} (-1)^n \exp \left[ \

(iv) For all $x, y \in H$, we have $\langle x, y \rangle = \sum_{z \in E} \langle x, z \rangle \overline{\langle y, z \rangle}$ [Parseval's identity].

(v) The smallest subspace of $H$ containing $E$ is dense in $H$.

Proof. Suppose that (i) holds and let $x \in H$. According to Bessel's inequality (16.17), there are only countably many $z \in E$ such that $\langle x, z \rangle \neq 0$; enumerate these as $(z_n)$. By (16.18), the vector $y = \sum_{n} \langle x, z_n \rangle z_n = \sum_{z \in E} \langle x, z \rangle z$ exists and $x - y$ is orthogonal to $E$. Since $E$ is complete, it follows that $x - y = 0$; and so (ii) holds.

To show that (ii) implies (iv), let $x, y \in H$ be given and let $(z_k)$ be an enumeration of all $z \in E$ such that $\langle x, z \rangle \neq 0$ or $\langle y, z \rangle \neq 0$. Let

$$x_n = \sum_{k=1}^{n} \langle x, z_k \rangle z_k$$

and

$$y_n = \sum_{k=1}^{n} \langle y, z_k \rangle z_k.$$

Then we have

$$\left| \langle x, y \rangle - \sum_{k=1}^{n} \langle x, z_k \rangle \overline{\langle y, z_k \rangle} \right| = \left| \langle x, y \rangle - \langle x_n, y_n \rangle \right|$$

$$\leq \left| \langle x, y \rangle - \langle x_n, y_n \rangle \right| + \left| \langle x_n, y \rangle - \langle x_n, y_n \rangle

$a \in A$. For any $b \in B$ we have $1 = \|b\|^2 = \sum_{a \in A} |\langle b, a \rangle|^2$ (16.26.iii), and so there is some $a \in A$ such that $\langle a, b \rangle \neq 0$, i.e., $b \in B_a$. Thus $B = \bigcup_{a \in A} B_a$. It follows that $\bar{B} \leq \kappa_0 \bar{A} = \bar{A}$. Interchanging the roles of $A$ and $B$ in this argument, we see also that $\bar{A} \leq \bar{B}$. It follows from the Schröder-Bernstein theorem that $\bar{A} = \bar{B}$.
