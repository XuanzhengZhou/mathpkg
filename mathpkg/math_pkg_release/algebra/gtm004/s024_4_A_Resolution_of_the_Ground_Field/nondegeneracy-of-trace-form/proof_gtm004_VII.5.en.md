---
role: proof
locale: en
of_concept: nondegeneracy-of-trace-form
source_book: gtm004
source_chapter: "VII"
source_section: "5"
---

# Proof of Non-degeneracy of the Trace Form

**Theorem 5.2.** Let $\mathfrak{g}$ be a semi-simple Lie algebra over a field of characteristic 0, and let $A$ be a $\mathfrak{g}$-module. If the structure map $\varrho : \mathfrak{g} \to \operatorname{End}_K(A)$ is injective (i.e., $A$ is a faithful representation), then the bilinear form

$$\beta(x, y) = \operatorname{Tr}(\varrho x \circ \varrho y), \quad x, y \in \mathfrak{g},$$

is non-degenerate.

**Proof.** The proof of this theorem is a deep result closely related to Cartan's criterion for solvability of Lie algebras. The original text states: "We do not attempt to give a proof of this rather deep result, which is closely related to Cartan's criterion for solvability of Lie algebras. Elementary proofs are easily accessible in the literature."

For completeness, we sketch the standard approach:

First, one proves Cartan's criterion: A Lie subalgebra $\mathfrak{h} \subset \mathfrak{gl}(V)$ (with $V$ finite-dimensional over a field of characteristic 0) is solvable if and only if $\operatorname{Tr}(x \circ y) = 0$ for all $x \in [\mathfrak{h}, \mathfrak{h}]$ and $y \in \mathfrak{h}$.

Now let $\mathfrak{g}$ be semi-simple and $\varrho : \mathfrak{g} \to \operatorname{End}_K(A)$ be a faithful representation. Let $\mathfrak{r}$ be the radical of the bilinear form $\beta$:

$$\mathfrak{r} = \{ x \in \mathfrak{g} \mid \beta(x, y) = 0 \text{ for all } y \in \mathfrak{g} \}.$$

Using the invariance property $\beta([x, y], z) = \beta(x, [y, z])$ (which holds because $\operatorname{Tr}(\varrho x \varrho y \varrho z) = \operatorname{Tr}(\varrho y \varrho z \varrho x)$, etc.), one shows that $\mathfrak{r}$ is an ideal of $\mathfrak{g}$.

Applying Cartan's criterion to $\varrho(\mathfrak{r}) \subset \operatorname{End}_K(A)$, one deduces that $\varrho(\mathfrak{r})$ is solvable. Since $\varrho$ is injective, $\mathfrak{r}$ is solvable. But $\mathfrak{g}$ is semi-simple, so its only solvable ideal is $\{0\}$. Hence $\mathfrak{r} = \{0\}$, meaning $\beta$ is non-degenerate. $\square$

**References:**
- G. Hochschild, *The Structure of Lie Groups*, Holden-Day, 1965, pp. 117–122.
- J.-P. Serre, *Lie Algebras and Lie Groups*, W. A. Benjamin, 1965, LA. 5.14–LA. 5.20.
