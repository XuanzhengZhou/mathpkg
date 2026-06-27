---
role: proof
locale: en
of_concept: cone-homotopy-identity
source_book: gtm060
source_chapter: "7"
source_section: "Differential forms"
---
For chains: The cone $pc$ of a $k$-chain $c$ is the $(k+1)$-chain formed by joining each point of $c$ to the origin by straight line segments. Computing the boundary of $pc$ geometrically gives: the boundary consists of the original chain $c$, the cone over the boundary $\partial c$ (with appropriate orientation), and possibly the vertex point (which is a degenerate chain taken to be zero in the normalized chain group). This yields the identity $\partial(pc) = c - p(\partial c)$, or equivalently $\partial \circ p + p \circ \partial = \text{id}$.

For differential forms: Define the co-cone operator by duality:
$$\int_{c_{k-1}} p\omega^k = \int_{p c_{k-1}} \omega^k.$$
Using Stokes' theorem and the chain homotopy identity:
$$\int_{c_k} d(p\omega^k) = \int_{\partial c_k} p\omega^k = \int_{p(\partial c_k)} \omega^k = \int_{p(\partial c_k)} \omega^k.$$
While
$$\int_{c_k} p(d\omega^k) = \int_{p c_k} d\omega^k = \int_{\partial(p c_k)} \omega^k = \int_{c_k - p(\partial c_k)} \omega^k.$$
Adding these yields $\int_{c_k} (dp + pd)\omega^k = \int_{c_k} \omega^k$ for all $c_k$, hence $dp + pd = \text{id}$ on forms. The explicit integral formula follows from the definition of the cone over a chain.
