---
role: proof
locale: en
of_concept: product-category-with-interval
source_book: gtm005
source_chapter: "II"
source_section: "4"
---

Let $\mathbf{2}$ be the category with two objects $0, 1$ and one non-identity arrow $\alpha: 0 \to 1$. The product $C \times \mathbf{2}$ has objects $(c, 0)$ and $(c, 1)$ for $c \in C$. 

Embedding functors $i_0, i_1: C \to C \times \mathbf{2}$ are defined by $i_j(c) = (c, j)$. There is a natural transformation $\iota: i_0 \Rightarrow i_1$ with components $\iota_c = (1_c, \alpha): (c, 0) \to (c, 1)$. Naturality: for $f: c \to c'$, the square
$$\begin{CD} (c, 0) @>{(1_c, \alpha)}>> (c, 1) \\ @V{(f, 1_0)}VV @VV{(f, 1_1)}V \\ (c', 0) @>>{(1_{c'}, \alpha)}> (c', 1) \end{CD}$$
commutes since $(1_{c'}, \alpha) \circ (f, 1_0) = (f, \alpha) = (f, 1_1) \circ (1_c, \alpha)$.

The functor category $C^{\mathbf{2}}$ (whose objects are arrows of $C$ and morphisms are commutative squares) admits a universal natural transformation: a functor $H: D \to C^{\mathbf{2}}$ corresponds exactly to a pair of functors $F, G: D \to C$ and a natural transformation $\tau: F \Rightarrow G$, where $H(d) = \tau_d: F(d) \to G(d)$.
