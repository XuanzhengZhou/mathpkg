---
role: proof
locale: en
of_concept: weierstrass-division-theorem
source_book: gtm059
source_chapter: "12"
source_section: "1"
---

Let $\pi: A[[X]] \to A[[X]]$ be the projections on the beginning and tail end of the series, defined by

$$\pi\left(\sum b_i X^i\right) = \sum_{i=0}^{n-1} b_i X^i, \qquad \tau\left(\sum b_i X^i\right) = \sum_{i=n}^{\infty} b_i X^i.$$

Note that $\tau(g) = X^n h$ for some $h \in A[[X]]$.

The existence of $q$ and $r$ is equivalent to the existence of a $q$ such that

$$\tau(g) = \tau(q f).$$

We can rewrite $f = \pi(f) + X^n u$ where $u$ is a unit in $A[[X]]$ (since $a_n$ is a unit). Therefore the problem is equivalent to solving

$$\tau(g) = \tau(q \cdot \pi(f)) + X^n q u = \tau(q \cdot \pi(f)) + q \cdot X^n u.$$

Note that $\tau(f) = X^n u$ is invertible in the appropriate sense. Setting $Z = q \cdot X^n u$, the equation becomes

$$\tau(g) = Z \cdot \frac{\pi(f)}{X^n u} + Z = Z \cdot \left(1 + \frac{\pi(f)}{X^n u}\right).$$

Since $\pi(f) \in \mathfrak{m} A[X]$, the factor $\left(1 + \frac{\pi(f)}{X^n u}\right)$ is invertible. Thus

$$Z = \tau(g) \cdot \left(1 + \frac{\pi(f)}{X^n u}\right)^{-1}$$

which proves both existence and uniqueness. Convergence follows from the completeness of $A$ in the $\mathfrak{m}$-adic topology.
