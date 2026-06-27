---
role: proof
locale: en
of_concept: toral-subalgebra-is-abelian
source_book: gtm009
source_chapter: "8"
source_section: "8.1 Maximal toral subalgebras and roots"
---

Let $T$ be a toral subalgebra of $L$. We must show that $\mathrm{ad}_T x = 0$ for all $x \in T$.

Since $x$ is semisimple and $\mathbb{F}$ is algebraically closed, $\mathrm{ad} x$ is diagonalizable. Thus it suffices to show that $\mathrm{ad}_T x$ has no nonzero eigenvalues. Suppose, on the contrary, that $[x y] = a y$ with $a \neq 0$ for some nonzero $y \in T$.

Then $\mathrm{ad}_T y(x) = -a y$ is an eigenvector of $\mathrm{ad}_T y$ with eigenvalue $0$. On the other hand, since $y$ is also semisimple, we can write $x$ as a linear combination of eigenvectors of $\mathrm{ad}_T y$. After applying $\mathrm{ad}_T y$ to this expression, we find that $\mathrm{ad}_T y(x)$ is a linear combination of eigenvectors of $\mathrm{ad}_T y$ belonging to nonzero eigenvalues. But $\mathrm{ad}_T y(x) = -a y$ is an eigenvector with eigenvalue $0$, forcing $y = 0$, a contradiction.

Therefore, $\mathrm{ad}_T x$ has no nonzero eigenvalues, so $\mathrm{ad}_T x = 0$ for all $x \in T$, and $T$ is abelian.
