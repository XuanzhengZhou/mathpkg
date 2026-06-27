---
role: proof
locale: en
of_concept: t-algebras-have-products
source_book: gtm026
source_chapter: "2"
source_section: "1"
---

Let $p_i: A \longrightarrow A_i$ be a product of the underlying objects in $\mathcal{K}$. The reasoning establishing that $(A, \xi)$ is a $\mathbf{T}$-algebra (for a suitable structure map $\xi$) is perfectly general, analogous to the Set case in 1.4.27.

To establish the universal property: Suppose we have $\mathbf{T}$-homomorphisms $f_i: (B, \theta) \longrightarrow (A_i, \xi_i)$. Since $p_i: A \longrightarrow A_i$ is a product in $\mathcal{K}$ of the underlying objects, there exists a unique $\mathcal{K}$-morphism $f: B \longrightarrow A$ such that $f.p_i = f_i$ for all $i$.

It remains to verify that $f$ is a $\mathbf{T}$-homomorphism, i.e., that the leftmost square in the relevant diagram commutes given that all the outer rectangles commute (since each $f_i$ is a $\mathbf{T}$-homomorphism). This follows immediately from the universal property of the product in $\mathcal{K}$: the leftmost square commutes when followed by each projection $p_i$, and uniqueness forces equality.
