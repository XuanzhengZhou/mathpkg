---
role: proof
locale: en
of_concept: finite-products-from-terminal-and-binary
source_book: gtm005
source_chapter: "III"
source_section: "3"
---

A category has all finite products iff it has a terminal object and binary products.

($\Rightarrow$) Terminal object is the empty product (product over the empty diagram). Binary products are products over a two-object discrete category. Both are finite products.

($\Leftarrow$) By induction: the product of $n$ objects ($n \geq 0$) is constructed iteratively. For $n = 0$, the terminal object $1$ is the empty product. For $n = 1$, the object itself (with identity projection) is the product. For $n \geq 2$, given a terminal object and binary products, define
$$A_1 \times A_2 \times \cdots \times A_n = (\cdots((A_1 \times A_2) \times A_3) \times \cdots) \times A_n$$
with projections defined by composing the binary projections. The universal property follows by induction: any cone over $\{A_1, \ldots, A_n\}$ factors uniquely through this iterated product.

More elegantly, one can use the associativity isomorphism: $(A \times B) \times C \cong A \times (B \times C)$ (derived from the universal property of products). By coherence for products, any two iterated binary products are canonically isomorphic, so finite products exist.
