---
role: proof
locale: en
of_concept: toral-subalgebra-is-abelian
source_book: gtm009
source_chapter: "8"
source_section: "8.1"
---

Let $T$ be a toral subalgebra of $L$. We need to show that $\operatorname{ad}_T x = 0$ for all $x \in T$. Since $\operatorname{ad} x$ is semisimple and $\mathbb{F}$ is algebraically closed, $x$ is diagonalizable. Thus it suffices to show that $\operatorname{ad}_T x$ has no nonzero eigenvalues.

Suppose, on the contrary, that $[x, y] = ay$ for some $a \neq 0$ and nonzero $y \in T$. Then:
$$\operatorname{ad}_T y(x) = [y, x] = -[x, y] = -ay.$$
So $-ay$ is an eigenvector of $\operatorname{ad}_T y$ with eigenvalue $0$.

On the other hand, since $y$ is also semisimple, $\operatorname{ad}_T y$ is diagonalizable, so we can write $x$ as a linear combination of eigenvectors of $\operatorname{ad}_T y$. Applying $\operatorname{ad}_T y$ to $x$, we get a linear combination of eigenvectors with nonzero eigenvalues (since $a \neq 0$). But $\operatorname{ad}_T y(x) = -ay$ belongs to the $0$-eigenspace. Since eigenvectors with distinct eigenvalues are linearly independent, this forces $a = 0$, a contradiction.

Therefore, $\operatorname{ad}_T x = 0$ for all $x \in T$, i.e., $T$ is abelian. $\square$
