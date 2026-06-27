---
role: proof
locale: en
of_concept: scaling-of-nowhere-zero-killing-vector-field
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

Suppose $x \in M$. By Section 3.6.1c, the Killing equation for $\ell W$ is

$$g(D_X(\ell W), Y) + g(X, D_Y(\ell W)) = 0 \quad \forall X, Y \in M_x.$$

Expanding using the Leibniz rule $D_X(\ell W) = (X\ell)W + \ell D_X W$ and the fact that $W$ is Killing (so $g(D_X W, Y) + g(X, D_Y W) = 0$), we obtain

$$(X\ell)g(W, Y) + (Y\ell)g(X, W) = 0 \quad \forall X, Y \in M_x.$$

Now fix $x$ and consider two cases:
1. If $g(X, W) = 0$: Since $W_x \neq 0$, we can choose $Y$ such that $g(Y, W) \neq 0$ (by nondegeneracy of $g$) and conclude $X\ell = 0$.
2. If $g(X, W) \neq 0$: Choose $Y = X$, giving $2(X\ell)g(X, W) = 0$, hence $X\ell = 0$.

Thus $X\ell = 0$ for all $X \in M_x$. Since $x$ was arbitrary, $d\ell = 0$ everywhere. As $M$ is connected, $\ell$ is constant.

This lemma remains valid so long as $W$ is not identically zero (see Exercise 7.3.14).
