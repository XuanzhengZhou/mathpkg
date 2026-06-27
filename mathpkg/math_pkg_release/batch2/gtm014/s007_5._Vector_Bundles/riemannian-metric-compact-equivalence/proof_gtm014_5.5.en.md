---
role: proof
locale: en
of_concept: riemannian-metric-compact-equivalence
source_book: gtm014
source_chapter: "5"
source_section: "5. Vector Bundles"
---

*Proof.* The proof uses the fact that on a compact set $K$, the continuously varying coefficients $a_{ij}(x)$ of the Riemannian metric are bounded above and the matrix $(a_{ij}(x))$ is uniformly positive definite.

Since $K$ is compact and the functions $x \mapsto a_{ij}(x)$ are continuous, there exists a constant $M$ such that $|a_{ij}(x)| \leq M$ for all $x \in K$ and all $i, j$. For any curve $c: [0,1] \to \mathbf{R}^n$ lying in $K$, the Riemannian arc length is

$$\bar{\ell}(c) = \int_0^1 \sqrt{\sum_{i,j} a_{ij}(c(t)) \, \dot{c}_i(t) \, \dot{c}_j(t)} \, dt.$$

Bounding the quadratic form by the maximum eigenvalue yields $\bar{\ell}(c) \leq M' \cdot \ell(c)$ where $\ell(c)$ is the Euclidean length, establishing the upper bound $\bar{d}(p,q) \leq M \cdot d(p,q)$.

For the lower bound, since $(a_{ij}(x))$ is positive definite for each $x \in K$ and $K$ is compact, the smallest eigenvalue of $(a_{ij}(x))$ attains a positive minimum $L'$ on $K$. Hence for any tangent vector $v$ at $x \in K$,

$$\sum_{i,j} a_{ij}(x) v_i v_j \geq L' \sum_i v_i^2.$$

Integrating along curves gives $\bar{\ell}(c) \geq L \cdot \ell(c)$, and consequently $\bar{d}(p,q) \geq L \cdot d(p,q)$.

The statement extends from Riemannian metrics on $\mathbf{R}^n$ to metrics on a smooth manifold $X$ by using a coordinate chart $\phi: \overline{U}' \to \mathbf{R}^n$ and a bundle isomorphism $S^2(T^*X)|_{\overline{U}'} \cong \phi(\overline{U}') \times S^2(\mathbf{R}^n)$. On the compact closure $\overline{U}'$, the pulled-back metric is comparable to the Euclidean metric via $\phi$, which yields the desired local comparison on $X$. $\square$

*Note.* The text reproduces only the beginning of this proof; the lemma statement is given and the proof outline above reconstructs the standard argument from the context. The complete proof would appear later in the text (truncated in the OCR extraction).
