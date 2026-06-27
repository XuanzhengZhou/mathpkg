---
role: proof
locale: en
of_concept: sl2-irreducible-classification
source_book: gtm009
source_chapter: "3"
source_section: "7"
---

Let $V$ be an irreducible $L$-module. Since $\dim V < \infty$, there exists a maximal vector $v_0 \in V_\lambda$ with $x.v_0 = 0$. Define $v_i = \frac{1}{i!} y^i.v_0$ for $i \geq 0$ and $v_{-1} = 0$.

By Lemma 7.2, the nonzero $v_i$ are eigenvectors of $h$ with distinct eigenvalues $\lambda - 2i$, hence linearly independent. Since $V$ is finite dimensional, there exists a largest $m$ such that $v_m \neq 0$. Then $v_{m+1} = 0$, so by Lemma 7.2(b), $y.v_m = (m+1)v_{m+1} = 0$. Also, by Lemma 7.2(c):
$$0 = y.v_{m+1} = \frac{1}{m+1}y^2.v_m$$
and
$$x.v_{m+1} = (\lambda - (m+1) + 1)v_m = (\lambda - m)v_m.$$

Since $v_{m+1} = 0$, we must have $x.v_{m+1} = 0$, so $(\lambda - m)v_m = 0$, hence $\lambda = m$.

The span of $\{v_0, v_1, \ldots, v_m\}$ is a nonzero submodule of $V$ (closed under $x, y, h$ by Lemma 7.2). Since $V$ is irreducible, this span equals $V$. Thus $\dim V = m+1$ and the weights are $m, m-2, \ldots, -m$, each occurring with multiplicity one.

The uniqueness of the maximal vector follows because any maximal vector in $V$ must be a weight vector of weight $m$ (the highest weight), and $V_m$ is one-dimensional.

For part (c), the action is given by Lemma 7.2 with $\lambda = m$, establishing uniqueness of the irreducible module for each dimension.
