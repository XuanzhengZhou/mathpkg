---
role: proof
locale: en
of_concept: e-term-factorization
source_book: gtm004
source_chapter: "VIII. Spectral Sequences"
source_section: "2. Filtered Differential Objects"
---

# Proof of Factorization of the E-term Functor via Associated Graded Object

**Statement.** Let $\mathfrak{A}$ be an abelian category and let $(\mathfrak{A}, d, f)$ be the category of filtered differential objects in $\mathfrak{A}$. For any $C \in (\mathfrak{A}, d, f)$ with filtration

$$\cdots \subseteq C^{(p-1)} \subseteq C^{(p)} \subseteq \cdots \subseteq C, \qquad -\infty < p < \infty,$$

the $E$-term functor

$$E : (\mathfrak{A}, d, f) \rightarrow \mathfrak{A}^\mathbb{Z}, \qquad E(C)^p = H(C^{(p)}/C^{(p-1)})$$

admits the factorization

$$E = H \circ Gr,$$

where $Gr : (\mathfrak{A}, d, f) \rightarrow (\mathfrak{A}^\mathbb{Z}, d)$ is the associated graded object functor and $H : (\mathfrak{A}^\mathbb{Z}, d) \rightarrow \mathfrak{A}^\mathbb{Z}$ is the homology functor.

**Proof.** Given any abelian category $\mathfrak{B}$, we form the category $(\mathfrak{B}, f)$ of filtered objects of $\mathfrak{B}$:

$$\cdots \subseteq B^{(p-1)} \subseteq B^{(p)} \subseteq \cdots \subseteq B, \qquad -\infty < p < \infty. \tag{2.5}$$

A morphism $\varphi : B \rightarrow B'$ of filtered objects sends $B^{(p)}$ to $B'^{(p)}$ for all $p$. From (2.5) we construct the graded object whose $p$-th component is $B^{(p)}/B^{(p-1)}$. This defines the associated graded functor

$$Gr : (\mathfrak{B}, f) \rightarrow \mathfrak{B}^\mathbb{Z}, \qquad Gr(B)^p = B^{(p)}/B^{(p-1)}.$$

Now specialize to $\mathfrak{B} = (\mathfrak{A}, d)$, the category of differential objects in $\mathfrak{A}$. For $X \in (\mathfrak{A}, d, f)$, the filtration subobjects $X^{(p)}$ are closed under the differential $d$, i.e., $dX^{(p)} \subseteq X^{(p)}$. Hence the differential $d$ induces a well-defined differential on each quotient $X^{(p)}/X^{(p-1)}$, making $Gr(X)$ a graded differential object:

$$Gr(X) \in (\mathfrak{A}, d)^\mathbb{Z} = (\mathfrak{A}^\mathbb{Z}, d).$$

Applying the homology functor $H$ to $Gr(X)$ yields, in degree $p$,

$$(H \circ Gr)(X)^p = H(Gr(X)^p) = H(X^{(p)}/X^{(p-1)}) = E(X)^p.$$

Thus $E = H \circ Gr$ as functors $(\mathfrak{A}, d, f) \rightarrow \mathfrak{A}^\mathbb{Z}$.

**Remark.** This factorization is fundamental to the construction of spectral sequences from filtered differential objects: the $E$-term is obtained by first passing to the associated graded (thereby discarding extension data) and then taking homology.
