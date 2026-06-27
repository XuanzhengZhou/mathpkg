---
role: proof
locale: en
of_concept: lorentz-light-cone-eigenvector
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

A light-vector $l$ is an eigenvector of $\varphi$ iff $(l, \varphi l) = 0$. Indeed, $\varphi l = \lambda l$ implies $(l, \varphi l) = \lambda(l, l) = 0$. Conversely, if $l$ is a light-vector with $(l, \varphi l) = 0$, then by property (3) of section 9.21, $l$ and $\varphi l$ are linearly dependent, so $l$ is an eigenvector.

Consider the selfadjoint mapping $\psi = \frac{1}{2}(\varphi + \tilde{\varphi}) = \frac{1}{2}(\varphi + \varphi^{-1})$. Then
$$(x, \psi x) = \frac{1}{2}(x, \varphi x) + \frac{1}{2}(x, \tilde{\varphi} x) = (x, \varphi x)$$
for all $x \in E$. Hence a light-vector $l$ is an eigenvector of $\varphi$ iff $(l, \psi l) = 0$.

Proceed by contradiction: assume $\varphi$ has no eigenvector on the light-cone. Then $(x, \psi x) = (x, \varphi x) \neq 0$ for all light-vectors $x$. By the theorem of section 9.24, $\psi$ has four eigenvectors $e_v$ forming an orthonormal basis. The eigenvalues of $\psi$ can be expressed as $\mu_v = \frac{1}{2}(\lambda_v + \lambda_v^{-1})$ where $\lambda_v$ are the corresponding quantities for $\varphi$ on the $e_v$-planes.

Each pair of eigenvectors with equal $|\lambda_v|$ spans a plane $F$ invariant under $\varphi$. This plane intersects the light-cone in two straight lines. Since $F$ and the light-cone are both $\varphi$-invariant, these lines are either interchanged or preserved by $\varphi$.

If they are preserved, we have two eigenvectors on the light-cone — contradiction. If interchanged, let $l_1, l_2$ be generating vectors with $(l_1, l_2) = 1$. Then $\varphi l_1 = \alpha l_2$, $\varphi l_2 = \beta l_1$, and inner product preservation forces $\alpha\beta = 1$. Consider $z = l_1 + \alpha l_2$:
$$\varphi z = \alpha l_2 + \alpha\beta l_1 = \alpha l_2 + l_1 = z.$$
Thus $z$ is an eigenvector with $\lambda = 1$. Moreover, $(z, z) = 2\alpha(l_1, l_2) = 2\alpha$. Let $t = l_1 - l_2$, which is time-like, and compute $(t, \varphi t) = \alpha + 1/\alpha$. Since $\varphi$ preserves the fore-cone and past-cone, $(t, \varphi t) < 0$, so $\alpha < 0$, showing $z$ is time-like.

Now use $z$ to construct an eigenvector on the light-cone. Let $E_1 = z^\perp$, a 3-dimensional Euclidean subspace invariant under $\varphi$. The restriction of $\varphi$ to $E_1$ is a proper Euclidean rotation, hence has an axis of rotation — a vector $a \in E_1$ with $\varphi a = a$. Then $l = z + a$ satisfies $(l, l) = (z, z) + (a, a) < 0 + (a, a)$. Adjusting the length of $a$ so that $(l, l) = 0$ yields a light-vector eigenvector — contradiction. Hence the assumption fails, and $\varphi$ has at least one eigenvector on the light-cone.
