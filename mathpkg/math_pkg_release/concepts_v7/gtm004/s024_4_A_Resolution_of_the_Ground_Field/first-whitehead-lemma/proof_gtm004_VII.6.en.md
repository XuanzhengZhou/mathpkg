---
role: proof
locale: en
of_concept: first-whitehead-lemma
source_book: gtm004
source_chapter: "VII"
source_section: "6"
---

# Proof of the First Whitehead Lemma

**Proposition 6.1 (First Whitehead Lemma).** Let $\mathfrak{g}$ be a semi-simple Lie algebra over a field of characteristic 0, and let $A$ be a finite-dimensional $\mathfrak{g}$-module. Then

$$H^1(\mathfrak{g}, A) = 0.$$

**Proof.** Suppose to the contrary that there exists a $\mathfrak{g}$-module $A$ with $H^1(\mathfrak{g}, A) \neq 0$. Choose such an $A$ of minimal $K$-dimension.

If $A$ is not simple, then there exists a proper non-zero submodule $A' \subset A$. Consider the short exact sequence

$$0 \to A' \to A \to A/A' \to 0$$

and the associated long exact cohomology sequence

$$\cdots \to H^1(\mathfrak{g}, A') \to H^1(\mathfrak{g}, A) \to H^1(\mathfrak{g}, A/A') \to \cdots.$$

Since $\dim_K A' < \dim_K A$ and $\dim_K A/A' < \dim_K A$, the minimality of $A$ forces

$$H^1(\mathfrak{g}, A') = H^1(\mathfrak{g}, A/A') = 0.$$

By exactness, this implies $H^1(\mathfrak{g}, A) = 0$, contradicting our assumption. Hence $A$ must be simple.

But a simple module over a semi-simple Lie algebra must be a trivial $\mathfrak{g}$-module by Proposition 5.6 (indeed it must be isomorphic to $K$). For a trivial module $A$, we have

$$H^1(\mathfrak{g}, A) \cong \operatorname{Hom}_K(\mathfrak{g}_{ab}, A)$$

by Proposition 2.2. Now consider the exact sequence

$$[\mathfrak{g}, \mathfrak{g}] \to \mathfrak{g} \to \mathfrak{g}_{ab}.$$

By Corollary 5.4, the ideal $[\mathfrak{g}, \mathfrak{g}]$ has a complement in $\mathfrak{g}$, which must be isomorphic to $\mathfrak{g}_{ab}$ and therefore abelian. Since $\mathfrak{g}$ is semi-simple (the only abelian ideal is $\{0\}$), we conclude $\mathfrak{g}_{ab} = 0$. Hence

$$H^1(\mathfrak{g}, A) \cong \operatorname{Hom}_K(\mathfrak{g}_{ab}, A) = \operatorname{Hom}_K(0, A) = 0.$$

This contradiction shows that our initial assumption was false; therefore $H^1(\mathfrak{g}, A) = 0$ for all finite-dimensional $\mathfrak{g}$-modules $A$. $\square$
