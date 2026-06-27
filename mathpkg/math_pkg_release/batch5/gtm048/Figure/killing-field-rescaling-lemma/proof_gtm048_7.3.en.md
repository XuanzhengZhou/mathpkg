---
role: proof
locale: en
of_concept: killing-field-rescaling-lemma
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

Suppose $x \in M$. By the characterization of Killing fields in Section 3.6.1c, we have for all $X, Y \in M_x$:

$$g(D_X(\ell W), Y) + g(X, D_Y(\ell W)) = 0.$$

Expanding using the Leibniz rule for the covariant derivative:
$$D_X(\ell W) = (X\ell)W + \ell D_X W.$$

Since $W$ is Killing, $g(D_X W, Y) + g(X, D_Y W) = 0$. Substituting the expansion into the Killing equation for $\ell W$ yields:

$$(X\ell)g(W, Y) + (Y\ell)g(X, W) = 0 \quad \forall X, Y \in M_x.$$

Now consider two cases:

**Case 1:** Suppose $g(X, W) = 0$. Since $W_x \neq 0$, we can choose $Y$ such that $g(Y, W) \neq 0$. The equation then gives $(X\ell)g(W, Y) = 0$, so $X\ell = 0$.

**Case 2:** Suppose $g(X, W) \neq 0$. Choosing $Y = X$, the equation becomes:
$$(X\ell)g(W, X) + (X\ell)g(X, W) = 2(X\ell)g(X, W) = 0,$$
which again implies $X\ell = 0$.

Thus $X\ell = 0$ for all $X \in M_x$. Since $x \in M$ was arbitrary, all directional derivatives of $\ell$ vanish at every point. As $M$ is connected, $\ell$ must be constant on $M$.

The lemma also holds when $W$ is not identically zero (see Exercise 7.3.14), by applying the same argument on the open dense subset where $W \neq 0$ and using continuity.
