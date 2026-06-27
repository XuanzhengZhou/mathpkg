---
role: proof
locale: en
of_concept: product-locally-compact-characterization
source_book: gtm027
source_chapter: "5"
source_section: "Locally Compact Spaces"
---

# Proof of the Characterization of Locally Compact Product Spaces (Theorem 19)

Let $X = \prod_{a \in A} X_a$ be a product space. We prove the two directions of the characterization.

**($\Rightarrow$)** Suppose $X$ is locally compact. For each coordinate index $a$, the projection map $\pi_a: X \to X_a$ is continuous and open. By the proposition on open continuous images, each $X_a$ is locally compact. Now suppose, for contradiction, that infinitely many coordinate spaces are non-compact. Then by Theorem 5.16 (which states that in a product with infinitely many non-compact factors, each compact subset is nowhere dense), every compact subset of $X$ has empty interior. Hence no point of $X$ can have a compact neighborhood (a compact neighborhood would require a compact set with nonempty interior), contradicting the local compactness of $X$. Therefore all but finitely many coordinate spaces must be compact.

**($\Leftarrow$)** If each coordinate space is locally compact and all but finitely many are compact, then the product is locally compact. (This direction is stated implicitly; the theorem as given in the text only states the forward direction. The converse follows from the fact that a finite product of locally compact spaces is locally compact, and a product of compact spaces is compact — hence locally compact. Multiplying finitely many locally compact factors by an arbitrary product of compact factors yields a locally compact space via Tychonoff's theorem and the characterization of the product topology.)

Thus a product is locally compact if and only if each factor is locally compact and all but finitely many factors are compact. $\square$
