---
role: proof
locale: en
of_concept: nonsingularity-iff-regular-local-ring
source_book: gtm052
source_chapter: "I"
source_section: "5"
---

Let $P$ be the point $(a_1, \ldots, a_n)$ in $\mathbf{A}^n$, and let $\mathfrak{a}_P = (x_1 - a_1, \ldots, x_n - a_n)$ be the corresponding maximal ideal in $A = k[x_1, \ldots, x_n]$. Define a linear map $\theta: A \to k^n$ by

$$\theta(f) = \left\langle \frac{\partial f}{\partial x_1}(P), \ldots, \frac{\partial f}{\partial x_n}(P) \right\rangle$$

for any $f \in A$. It is clear that $\theta(x_i - a_i)$ for $i = 1, \ldots, n$ form a basis of $k^n$, and that $\theta(\mathfrak{a}_P^2) = 0$. Thus $\theta$ induces an isomorphism $\theta': \mathfrak{a}_P/\mathfrak{a}_P^2 \to k^n$.

Now let $\mathfrak{b}$ be the ideal of $Y$ in $A$, and let $f_1, \ldots, f_t$ be a set of generators of $\mathfrak{b}$. Then the rank of the Jacobian matrix $J = \|(\partial f_i/\partial x_j)(P)\|$ is just the dimension of the subspace $\theta(\mathfrak{b})$ of $k^n$. Using the isomorphism $\theta'$, this is the same as the dimension of the subspace $(\mathfrak{b} + \mathfrak{a}_P^2)/\mathfrak{a}_P^2$ of $\mathfrak{a}_P/\mathfrak{a}_P^2$.

Now the local ring $\mathcal{O}_{P,Y}$ is the localization of $A/\mathfrak{b}$ at the maximal ideal corresponding to $P$. Its maximal ideal $\mathfrak{m}$ is $\mathfrak{a}_P/(\mathfrak{b} + \mathfrak{a}_P^2)$ (modulo further localization). More precisely, $\mathfrak{m}/\mathfrak{m}^2 \cong \mathfrak{a}_P/(\mathfrak{b} + \mathfrak{a}_P^2)$. Counting dimensions, we have

$$\dim_k \mathfrak{m}/\mathfrak{m}^2 = n - \operatorname{rank} J.$$

On the other hand, $\dim \mathcal{O}_{P,Y} = \dim Y = r$. And $Y$ is nonsingular at $P$ (by the Jacobian criterion) if and only if $\operatorname{rank} J = n - r$. Therefore $Y$ is nonsingular at $P$ if and only if $\dim_k \mathfrak{m}/\mathfrak{m}^2 = r = \dim \mathcal{O}_{P,Y}$, i.e., if and only if $\mathcal{O}_{P,Y}$ is a regular local ring.
