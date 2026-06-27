---
role: proof
locale: en
of_concept: bounded-primitive-recursion
source_book: gtm037
source_chapter: "2"
source_section: "Elementary Recursive and Primitive Recursive Functions"
---

**(i)** For any $x_0, \ldots, x_m, z \in \omega$ let

$$s(x_0, \ldots, x_m) = (x_m + 1) \cdot \sum_{z < x_m} k(x_0, \ldots, x_{m-1}, z).$$

Let $R$ consist of all $(m + 2)$-tuples $\langle x_0, \ldots, x_m, y \rangle$ such that there is a $q \leq p_{x_m}^{s(x_0, \ldots, x_m)}$ so that

(1) $(q)_0 = f(x_0, \ldots, x_{m-1})$

and, for all $z < x_m$,

(2) $(q)_{z+1} = h(x_0, \ldots, x_{m-1}, z, (q)_z)$

and, finally, $y = (q)_{x_m}$.

Here $(q)_z$ denotes the exponent of $p_z$ in the prime factorization of $q$, and $p_z$ is the $z$-th prime. The set $R$ is elementary because all the functions involved ($f$, $h$, exponent extraction, bounded quantifiers) are elementary. Now (i) follows from

(3) $g(x_0, \ldots, x_m) = \mu y \leq k(x_0, \ldots, x_m)[\langle x_0, \ldots, x_m, y \rangle \in R]$.

Since $k$ is elementary and $R$ is an elementary relation, the bounded $\mu$-operator applied to an elementary relation yields an elementary function. Hence $g$ is elementary.

The idea is that $q$ codes the entire computation history $g(x_0, \ldots, x_{m-1}, 0), g(x_0, \ldots, x_{m-1}, 1), \ldots, g(x_0, \ldots, x_{m-1}, x_m)$ using prime power coding. The bound $p_{x_m}^{s(x_0, \ldots, x_m)}$ ensures that the search for $q$ is bounded by an elementary function, keeping the definition within the elementary class.

**(ii)** The proof for the 0-ary base case is analogous, with $g(0) = a$ and the same coding argument for the recursion step.
