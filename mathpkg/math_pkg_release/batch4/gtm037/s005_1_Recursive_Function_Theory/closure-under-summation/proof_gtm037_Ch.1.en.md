---
role: proof
locale: en
of_concept: closure-under-summation
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

Suppose $f \in A$ is $m$-ary and $A$ is closed under primitive recursive operations. Define $g = \sum f$ by

$$g(x_0, \ldots, x_{m-2}, z) = \sum_{y < z} f(x_0, \ldots, x_{m-2}, y).$$

We show $g \in A$. Observe that $g$ satisfies the primitive recursion:

$$g(x_0, \ldots, x_{m-2}, 0) = 0,$$
$$g(x_0, \ldots, x_{m-2}, \delta z) = \sum_{y < \delta z} f(x_0, \ldots, x_{m-2}, y)$$
$$= g(x_0, \ldots, x_{m-2}, z) + f(x_0, \ldots, x_{m-2}, z).$$

The base function is the constant-zero function $C_0^{m-1} \in A$. The step function is

$$h(x_0, \ldots, x_{m-2}, z, w) = w + f(x_0, \ldots, x_{m-2}, z),$$

which is a composition of $+$ (primitive recursive) and $f \in A$, hence in $A$. Since $A$ is closed under primitive recursion, $g \in A$. Thus $A$ is closed under summation.
