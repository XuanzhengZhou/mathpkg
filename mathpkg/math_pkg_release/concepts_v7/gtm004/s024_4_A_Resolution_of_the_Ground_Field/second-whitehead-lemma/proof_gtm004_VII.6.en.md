---
role: proof
locale: en
of_concept: second-whitehead-lemma
source_book: gtm004
source_chapter: "VII"
source_section: "6"
---

# Proof of the Second Whitehead Lemma

**Proposition 6.3 (Second Whitehead Lemma).** Let $\mathfrak{g}$ be a semi-simple Lie algebra over a field of characteristic 0, and let $A$ be a finite-dimensional $\mathfrak{g}$-module. Then

$$H^2(\mathfrak{g}, A) = 0.$$

**Proof.** We proceed as in the proof of the First Whitehead Lemma. Suppose there exists a $\mathfrak{g}$-module $A$ with $H^2(\mathfrak{g}, A) \neq 0$, and choose such an $A$ of minimal $K$-dimension.

If $A$ is not simple, let $A' \subset A$ be a proper non-zero submodule. From the short exact sequence

$$0 \to A' \to A \to A/A' \to 0$$

we obtain the long exact cohomology sequence

$$\cdots \to H^2(\mathfrak{g}, A') \to H^2(\mathfrak{g}, A) \to H^2(\mathfrak{g}, A/A') \to \cdots.$$

By minimality of $\dim_K A$, we have $H^2(\mathfrak{g}, A') = H^2(\mathfrak{g}, A/A') = 0$, whence $H^2(\mathfrak{g}, A) = 0$, a contradiction. Thus $A$ must be simple.

By Proposition 5.6, a simple module over a semi-simple Lie algebra must be a trivial module. The only simple trivial $\mathfrak{g}$-module is $K$. Hence it suffices to prove $H^2(\mathfrak{g}, K) = 0$.

By Theorem 3.3, $H^2(\mathfrak{g}, K)$ classifies central extensions of $\mathfrak{g}$ by $K$. Thus we must show that every central extension

$$0 \to K \to \mathfrak{h} \xrightarrow{p} \mathfrak{g} \to 0 \tag{6.4}$$

of Lie algebras splits.

Let $s : \mathfrak{g} \to \mathfrak{h}$ be a $K$-linear section of (6.4) (so $p s = 1_{\mathfrak{g}}$). The Lie bracket in $\mathfrak{h}$ can be expressed in terms of $s$ and a 2-cocycle $h : \mathfrak{g} \times \mathfrak{g} \to K$:

$$[s x, s y]_{\mathfrak{h}} = s[x, y]_{\mathfrak{g}} + h(x, y), \quad x, y \in \mathfrak{g}.$$

The cocycle condition for $h$ is equivalent to the Jacobi identity in $\mathfrak{h}$.

Using the section $s$, we define a $\mathfrak{g}$-module structure on the underlying $K$-vector space of $\mathfrak{h}$ by

$$x \circ y = [s x, y]_{\mathfrak{h}}, \quad x \in \mathfrak{g}, \; y \in \mathfrak{h}.$$

One checks that this makes $\mathfrak{h}$ into a $\mathfrak{g}$-module and that $K \subset \mathfrak{h}$ is a $\mathfrak{g}$-submodule (isomorphic to the trivial module). By the First Whitehead Lemma, $H^1(\mathfrak{g}, \mathfrak{h}) = 0$, which implies that the extension splits as a sequence of $\mathfrak{g}$-modules. This splitting yields a Lie algebra section, showing the extension (6.4) splits as Lie algebras. Hence $H^2(\mathfrak{g}, K) = 0$.

This contradiction completes the proof that $H^2(\mathfrak{g}, A) = 0$ for all finite-dimensional $\mathfrak{g}$-modules $A$. $\square$
