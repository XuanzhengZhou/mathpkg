---
role: proof
locale: en
of_concept: general-form-of-differential-k-form-on-rn
source_book: gtm060
source_chapter: "7"
source_section: "34"
---
At each point $x \in \mathbb{R}^n$, the tangent space $T\mathbb{R}^n_x$ is an $n$-dimensional vector space. The coordinate functions $x_1, \ldots, x_n$ give rise to the $n$ 1-forms $dx_1, \ldots, dx_n$, which form a basis of the cotangent space $T^*\mathbb{R}^n_x$ (the space of 1-forms on $T\mathbb{R}^n_x$).

Consider the exterior products of these basic 1-forms:
$$dx_{i_1} \wedge \cdots \wedge dx_{i_k}, \quad i_1 < \cdots < i_k.$$
There are $\binom{n}{k}$ such products, and they form a basis of the space $\bigwedge^k T^*\mathbb{R}^n_x$ of exterior $k$-forms on $T\mathbb{R}^n_x$.

Therefore, for each fixed point $x$, every exterior $k$-form on $T\mathbb{R}^n_x$ can be written uniquely as a linear combination
$$\sum_{i_1 < \cdots < i_k} a_{i_1, \ldots, i_k}(x)\, dx_{i_1} \wedge \cdots \wedge dx_{i_k},$$
where the coefficients $a_{i_1,\ldots,i_k}(x)$ are real numbers depending on $x$.

For a differential $k$-form $\omega^k$ on $\mathbb{R}^n$, the coefficients $a_{i_1,\ldots,i_k}(x)$ vary with $x$. Since $\omega^k$ is differentiable (smooth) by definition, these coefficient functions are smooth functions on $\mathbb{R}^n$. Uniqueness follows from the fact that the basic wedge products are linearly independent at each point. This establishes the claimed representation.
