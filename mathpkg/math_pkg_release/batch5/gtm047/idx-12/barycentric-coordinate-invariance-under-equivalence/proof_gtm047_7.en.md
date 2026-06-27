---
role: proof
locale: en
of_concept: barycentric-coordinate-invariance-under-equivalence
source_book: gtm047
source_chapter: "7"
source_section: "Abstract complexes and PL complexes"
---

Given $g \sim h$, let $\sigma_g = v_0v_1 \ldots v_k$ and set

$$w_i = g(v_i), \quad x_i = h^{-1}(w_i).$$

Since $h^{-1} \circ g$ is a simplicial isomorphism (by the definition of $\sim$), it maps the ordered simplex $\sigma_g = v_0v_1\ldots v_k$ to the ordered simplex $\sigma_h = x_0x_1\ldots x_k$.

Now let $w = g(\sum \alpha_i v_i)$ be any point of $|g|$. Then

$$h^{-1}(w) = h^{-1}\!\left(g\!\left(\sum \alpha_i v_i\right)\right) = \sum \alpha_i \, h^{-1}\!(g(v_i)) = \sum \alpha_i x_i,$$

where the second equality uses the linearity of $h^{-1} \circ g$. Therefore

$$w = h\!\left(\sum \alpha_i x_i\right).$$

In both representations, the barycentric coordinate corresponding to $w_i = g(v_i) = h(x_i)$ is $\alpha_i$. Thus the barycentric coordinate system induced on $|g| = |h|$ is the same for $g$ and $h$.
