---
role: proof
locale: en
of_concept: proposition-6-6-quotient-by-radical
source_book: gtm004
source_chapter: "VII"
source_section: "6"
---

# Proof that the Quotient by the Radical is Semi-simple

**Proposition 6.6.** Let $\mathfrak{g}$ be a finite-dimensional Lie algebra and let $\mathfrak{r}$ be its radical. Then $\mathfrak{g}/\mathfrak{r}$ is semi-simple.

**Proof.** Let $\mathfrak{a}$ be an abelian ideal of $\mathfrak{g}/\mathfrak{r}$. Let $\tilde{\mathfrak{a}}$ be its preimage in $\mathfrak{g}$ under the quotient map $\pi : \mathfrak{g} \to \mathfrak{g}/\mathfrak{r}$.

We have the exact sequence

$$0 \to \mathfrak{r} \to \tilde{\mathfrak{a}} \to \mathfrak{a} \to 0.$$

Since $\mathfrak{a}$ is abelian, it is solvable. Since $\mathfrak{r}$ is solvable (being the radical), and $\mathfrak{a}$ is solvable, Lemma 6.4 implies that $\tilde{\mathfrak{a}}$ is solvable.

But $\tilde{\mathfrak{a}}$ is an ideal of $\mathfrak{g}$ containing $\mathfrak{r}$. Since $\mathfrak{r}$ is the unique maximal solvable ideal, we must have $\tilde{\mathfrak{a}} = \mathfrak{r}$, which forces $\mathfrak{a} = 0$.

Thus $\{0\}$ is the only abelian ideal of $\mathfrak{g}/\mathfrak{r}$, which means $\mathfrak{g}/\mathfrak{r}$ is semi-simple. $\square$
