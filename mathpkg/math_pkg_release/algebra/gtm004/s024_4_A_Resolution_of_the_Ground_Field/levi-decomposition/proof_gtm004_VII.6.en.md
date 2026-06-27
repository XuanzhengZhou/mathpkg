---
role: proof
locale: en
of_concept: levi-decomposition
source_book: gtm004
source_chapter: "VII"
source_section: "6"
---

# Proof of the Levi Decomposition

**Theorem 6.7 (Levi Decomposition).** Every finite-dimensional Lie algebra $\mathfrak{g}$ over a field of characteristic 0 is the split extension of a semi-simple Lie algebra by its radical $\mathfrak{r}$. That is, there exists a semi-simple subalgebra $\mathfrak{s} \subset \mathfrak{g}$ (called a *Levi factor*) such that

$$\mathfrak{g} = \mathfrak{r} \rtimes \mathfrak{s}$$

as Lie algebras (semi-direct product).

**Proof.** The proof proceeds by induction on the derived length of the radical $\mathfrak{r}$.

**Step 1: Reduction to the case $[\mathfrak{r}, \mathfrak{r}] = 0$.** If $\mathfrak{r}$ is not abelian, consider $[\mathfrak{r}, \mathfrak{r}]$, which is a solvable ideal of $\mathfrak{g}$ (being a characteristic ideal of $\mathfrak{r}$). The quotient $\mathfrak{g}/[\mathfrak{r}, \mathfrak{r}]$ has radical $\mathfrak{r}/[\mathfrak{r}, \mathfrak{r}]$, which has smaller derived length. If the theorem holds for $\mathfrak{g}/[\mathfrak{r}, \mathfrak{r}]$, then lifting a Levi factor back to $\mathfrak{g}$ (using the Second Whitehead Lemma to handle the extension) yields a Levi factor for $\mathfrak{g}$.

**Step 2: The abelian radical case.** Assume $\mathfrak{r}$ is abelian, so $[\mathfrak{r}, \mathfrak{r}] = 0$. Then $\mathfrak{r}$ is a $\mathfrak{g}/\mathfrak{r}$-module via the adjoint action. Since $\mathfrak{g}/\mathfrak{r}$ is semi-simple (Proposition 6.6), we can apply the cohomology theory.

The exact sequence

$$0 \to \mathfrak{r} \to \mathfrak{g} \to \mathfrak{g}/\mathfrak{r} \to 0$$

is an extension of the semi-simple Lie algebra $\mathfrak{g}/\mathfrak{r}$ by the abelian ideal $\mathfrak{r}$. Such extensions are classified by $H^2(\mathfrak{g}/\mathfrak{r}, \mathfrak{r})$, where $\mathfrak{r}$ is regarded as a $\mathfrak{g}/\mathfrak{r}$-module.

By the Second Whitehead Lemma (Proposition 6.3), $H^2(\mathfrak{g}/\mathfrak{r}, \mathfrak{r}) = 0$. Hence the extension splits, meaning there exists a Lie algebra homomorphism $s : \mathfrak{g}/\mathfrak{r} \to \mathfrak{g}$ splitting the quotient map. The image $\mathfrak{s} = s(\mathfrak{g}/\mathfrak{r})$ is the desired Levi factor.

**Step 3: Induction step.** For non-abelian $\mathfrak{r}$, let $\mathfrak{r}_1 = [\mathfrak{r}, \mathfrak{r}]$ (which is a proper ideal of $\mathfrak{r}$ since $\mathfrak{r}$ is solvable). Consider the extension

$$0 \to \mathfrak{r}/\mathfrak{r}_1 \to \mathfrak{g}/\mathfrak{r}_1 \to \mathfrak{g}/\mathfrak{r} \to 0.$$

Since $\mathfrak{r}/\mathfrak{r}_1$ is an abelian ideal of $\mathfrak{g}/\mathfrak{r}_1$, the abelian radical case (Step 2) gives a splitting, yielding a Levi factor for $\mathfrak{g}/\mathfrak{r}_1$. By induction on the derived length, we then lift this to $\mathfrak{g}$.

The detailed step establishing that $[\mathfrak{r}, \mathfrak{r}]$ is the radical of $[\mathfrak{g}, \mathfrak{g}]$ (Exercise 6.5) is used to ensure the induction hypothesis applies correctly. $\square$

**References:** For a complete proof, see N. Jacobson, *Lie Algebras*, Interscience, 1962, pp. 91–95; or J.-P. Serre, *Lie Algebras and Lie Groups*, W. A. Benjamin, 1965.
