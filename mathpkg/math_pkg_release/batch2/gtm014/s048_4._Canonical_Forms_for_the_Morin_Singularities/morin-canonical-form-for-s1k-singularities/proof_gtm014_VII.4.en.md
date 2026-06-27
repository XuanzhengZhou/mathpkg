---
role: proof
locale: en
of_concept: morin-canonical-form-for-s1k-singularities
source_book: gtm014
source_chapter: "VII"
source_section: "4"
---

Choose coordinates $x_1, \ldots, x_n$ centered at $x_0$ and $y_1, \ldots, y_n$ centered at $f(x_0)$ so that $f(x_1, \ldots, x_n) = (h(x), x_2, \ldots, x_n)$. Since $x_0$ is an $S_{1_k}$ singularity, the local ring $\mathcal{R}_f(x_0)$ is generated as a vector space over $\mathbf{R}$ by $1, x_1, \ldots, x_1^k$.

By the Malgrange preparation theorem, every germ of a function at $x_0$ can be written as a linear combination of $1, x_1, \ldots, x_1^k$ with smooth functions of the $y$'s as coefficients. In particular, we can write

$$
x_1^{k+1} = f^* a_1 + (f^* a_2) x_1 + \cdots + (f^* a_{k+1}) x_1^k
$$

or equivalently

$$
f^* a_1 = -(f^* a_2) x_1 - \cdots - (f^* a_{k+1}) x_1^k + x_1^{k+1}
$$

where the $a_i$ are smooth functions of $y$. Furthermore, we can assume $a_{k+1} = 0$ by replacing $x_1$ with $x_1 + \frac{1}{k} f^* a_{k+1}$ and leaving $x_2, \ldots, x_n$ fixed.

Comparing the two sides of the equation, we see that $a_1(0) = a_2(0) = \cdots = a_k(0) = 0$.

Now set $x_2 = \cdots = x_n = y_2 = \cdots = y_n = 0$ in the equation and expand both sides in powers of $x_1$. By assumption,

$$
f^* y_1 = h(x_1, 0, \ldots, 0) = c x_1^{k+1} + \cdots
$$

with $c \neq 0$ a nonzero constant and the dots indicating terms of degree $> k+1$ in $x_1$. Therefore, for the $x_1^{k+1}$ terms to be equal, we must have

$$
a_1(y_1, 0, \ldots, 0) = \frac{1}{c} y_1 + \cdots
$$

In particular, $\frac{\partial a_1}{\partial y_1} \neq 0$. This means the map

$$
(y_1, \ldots, y_n) \mapsto (a_1(y), y_2, \ldots, y_n)
$$

is a legitimate coordinate change. With respect to these new coordinates, $f$ has the canonical form.
