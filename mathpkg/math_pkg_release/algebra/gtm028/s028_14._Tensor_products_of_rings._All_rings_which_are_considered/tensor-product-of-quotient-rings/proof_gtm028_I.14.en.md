---
role: proof
locale: en
of_concept: tensor-product-of-quotient-rings
source_book: gtm028
source_chapter: "I"
source_section: "14. Tensor products of rings"
---

Let $\alpha: A \to A/\mathfrak{A}$ and $\beta: B \to B/\mathfrak{B}$ be the canonical homomorphisms. Let $(A \otimes B, g, h)$ be the canonical tensor product of $A$ and $B$ over $k$ (with $g(a) = a \otimes 1$, $h(b) = 1 \otimes b$). Compose $\alpha$ and $\beta$ with the embedding maps to obtain homomorphisms $\alpha': A \to (A \otimes B)/(\mathfrak{A}, \mathfrak{B})$ and $\beta': B \to (A \otimes B)/(\mathfrak{A}, \mathfrak{B})$ factoring through the quotient. By the universal property of the tensor product (Theorem 34), there exists a homomorphism $f: (A/\mathfrak{A}) \otimes (B/\mathfrak{B}) \to (A \otimes B)/(\mathfrak{A}, \mathfrak{B})$.

Conversely, the natural map $\pi: A \otimes B \to (A/\mathfrak{A}) \otimes (B/\mathfrak{B})$ given by $a \otimes b \mapsto \alpha(a) \otimes \beta(b)$ has kernel containing $(\mathfrak{A}, \mathfrak{B})$, so it induces a homomorphism $\bar{\pi}: (A \otimes B)/(\mathfrak{A}, \mathfrak{B}) \to (A/\mathfrak{A}) \otimes (B/\mathfrak{B})$.

These two maps are mutually inverse. Moreover, $f = \varphi^{-1}$ on $(A/\mathfrak{A})\varphi$ and $f = \psi^{-1}$ on $(B/\mathfrak{B})\psi$, where $\varphi, \psi$ are the canonical embeddings. By Corollary 2 of Theorem 34, this completes the proof that the natural map is an isomorphism:

$$(A/\mathfrak{A}) \otimes_k (B/\mathfrak{B}) \cong (A \otimes_k B) / (\mathfrak{A}, \mathfrak{B}).$$
