---
role: proof
locale: en
of_concept: reconstruction-of-complex-linear-form
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Reconstruction of a Complex Linear Form from Its Real Part

Let $E$ be a vector space over $\mathbb{C}$, also regarded as a vector space over $\mathbb{R}$ by restricting scalar multiplication.

**Theorem 21.13.** If $g: E \to \mathbb{R}$ is an $\mathbb{R}$-linear form (i.e., $g$ is additive and $\mathbb{R}$-homogeneous), then the formula

$$f(x) = g(x) - ig(ix) \quad (x \in E)$$

defines a $\mathbb{C}$-linear form $f$ on $E$ such that $\operatorname{Re} f = g$.

*Proof.*

Clearly $f$ is additive, since $g$ is additive:

$$f(x + y) = g(x + y) - ig(i(x + y)) = g(x) + g(y) - i(g(ix) + g(iy)) = f(x) + f(y).$$

Moreover, $\operatorname{Re} f(x) = g(x)$ by definition, so $f$ recovers $g$ as its real part.

It remains to show that $f$ is complex-homogeneous. By additivity and real-homogeneity (which follows from the $\mathbb{R}$-linearity of $g$), it suffices to verify that $f(ix) = if(x)$ for all $x \in E$:

$$f(ix) = g(ix) - ig(i^2 x) = g(ix) - ig(-x)$$
$$= g(ix) + ig(x) \quad (\text{since } g(-x) = -g(x))$$
$$= i\bigl[-ig(ix) - g(-x)\bigr]$$
$$= i\bigl[-ig(ix) + g(x)\bigr]$$
$$= i\bigl[g(x) - ig(ix)\bigr] = if(x).$$

Thus $f$ is $\mathbb{C}$-homogeneous, hence a $\mathbb{C}$-linear form.

**Mutual inverses.** The correspondences described in Theorems 21.11 and 21.13 are mutually inverse: starting from a $\mathbb{C}$-form $f$, taking its real part $g = \operatorname{Re} f$ and applying the formula $g(x) - ig(ix)$ recovers $f$ (by 21.11(iii)); conversely, starting from an $\mathbb{R}$-form $g$, defining $f(x) = g(x) - ig(ix)$ and then taking the real part recovers $g$ (by definition). This establishes a bijection between the set of all $\mathbb{C}$-linear forms on $E$ and the set of all $\mathbb{R}$-linear forms on $E$.
