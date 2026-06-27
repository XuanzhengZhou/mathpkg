---
role: proof
locale: en
of_concept: injective-duality-mapping
source_book: gtm015
source_chapter: "3"
source_section: "38"
---

# Proof of Injectivity of the canonical duality embeddings

Let $E, F$ be vector spaces over $\mathbb{K}$ with a duality $B$. Define $B_x(y) = B(x, y)$ for $x \in E, y \in F$ and $B^y(x) = B(x, y)$ for $y \in F, x \in E$.

Then the correspondence $x \mapsto B_x$ is an injective linear mapping of $E$ into the vector space $\mathcal{V}(F, \mathbb{K})$ of all linear forms on $F$. Similarly, the correspondence $y \mapsto B^y$ is an injective linear mapping of $F$ into $\mathcal{V}(E, \mathbb{K})$.

*Proof.* The linearity of $x \mapsto B_x$ follows from the bilinearity of $B$: for all $y \in F$,
$$B_{x_1 + x_2}(y) = B(x_1 + x_2, y) = B(x_1, y) + B(x_2, y) = (B_{x_1} + B_{x_2})(y),$$
$$B_{\lambda x}(y) = B(\lambda x, y) = \lambda B(x, y) = (\lambda B_x)(y).$$

Injectivity results from the nondegeneracy of $B$: if $B_x = 0$ (the zero linear form on $F$), then $B(x, y) = 0$ for all $y \in F$, so by nondegeneracy, $x = \theta$. The proof for $y \mapsto B^y$ is symmetrical.
