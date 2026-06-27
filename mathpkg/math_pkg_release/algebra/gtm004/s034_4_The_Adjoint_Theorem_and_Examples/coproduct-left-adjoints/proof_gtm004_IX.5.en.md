---
role: proof
locale: en
of_concept: coproduct-left-adjoints
source_book: gtm004
source_chapter: "IX"
source_section: "5. Kan Extensions"
---

# Proof of Left Adjoint for Coproduct of Functors

**Lemma 5.5.** Let $F_i: \mathfrak{C}_i \rightarrow \mathfrak{D}$ be a left adjoint of $G_i: \mathfrak{D} \rightarrow \mathfrak{C}_i$ for each $i$, and suppose that $\mathfrak{D}$ has coproducts. Define $G: \mathfrak{D} \rightarrow \prod_i \mathfrak{C}_i$ by $GD = \{G_i D\}$. Then $F: \prod_i \mathfrak{C}_i \rightarrow \mathfrak{D}$, defined by $F\{C_i\} = \coprod_i F_i C_i$, is a left adjoint to $G$.

**Proof.** We establish the natural bijection:

$$\begin{aligned}
\mathfrak{D}\bigl(F\{C_i\}, D\bigr)
&= \mathfrak{D}\Bigl(\coprod_i F_i C_i, D\Bigr) \\
&= \prod_i \mathfrak{D}(F_i C_i, D) \quad\text{(universal property of coproduct)} \\
&\cong \prod_i \mathfrak{C}_i(C_i, G_i D) \quad\text{(adjunction } F_i \dashv G_i \text{)} \\
&= \Bigl(\prod_i \mathfrak{C}_i\Bigr)\bigl(\{C_i\}, \{G_i D\}\bigr) \\
&= \Bigl(\prod_i \mathfrak{C}_i\Bigr)\bigl(\{C_i\}, GD\bigr).
\end{aligned}$$

Each step is natural in both $\{C_i\}$ and $D$:
- The first equality is by definition of $F$.
- The second equality uses the universal property of the coproduct in $\mathfrak{D}$: a morphism out of a coproduct is uniquely determined by its components.
- The third isomorphism is the adjunction $F_i \dashv G_i$ applied componentwise.
- The fourth equality is the definition of the product category.
- The fifth equality is by definition of $G$.

Thus we have a natural isomorphism

$$\mathfrak{D}(F\{C_i\}, D) \cong \Bigl(\prod_i \mathfrak{C}_i\Bigr)(\{C_i\}, GD),$$

which establishes $F \dashv G$. $\square$
