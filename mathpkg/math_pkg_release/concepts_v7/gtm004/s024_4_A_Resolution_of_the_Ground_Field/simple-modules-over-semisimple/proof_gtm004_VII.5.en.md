---
role: proof
locale: en
of_concept: simple-modules-over-semisimple
source_book: gtm004
source_chapter: "VII"
source_section: "5"
---

# Proof of Proposition 5.6: Simple Modules over Semi-simple Lie Algebras

**Proposition 5.6.** Let $\mathfrak{g}$ be a semi-simple Lie algebra over a field of characteristic 0. If $A$ is a simple $\mathfrak{g}$-module that is not the trivial module $K$, then the structure map $\varrho : \mathfrak{g} \to \operatorname{End}_K(A)$ is non-trivial, and in fact the associated trace form is non-degenerate.

More precisely: every non-trivial simple $\mathfrak{g}$-module is a faithful module over a non-zero semi-simple quotient of $\mathfrak{g}$. In particular, if $A$ is a non-trivial simple $\mathfrak{g}$-module, then the representation $\varrho$ is injective on the unique simple ideal of $\mathfrak{g}$ complementary to the kernel of $\varrho$.

**Proof.** Let $\mathfrak{h} = \ker \varrho$ be the kernel of the structure map. Then $\mathfrak{h}$ is an ideal of $\mathfrak{g}$, and by Corollary 5.4, $\mathfrak{h}$ admits a complementary ideal $\mathfrak{h}'$ such that $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{h}'$. Since $A$ is non-trivial, $\mathfrak{h} \neq \mathfrak{g}$, so $\mathfrak{h}' \neq 0$. Moreover, $\mathfrak{h}'$ is semi-simple by Corollary 5.5 (semi-simplicity is hereditary for ideals).

The restriction $\varrho|_{\mathfrak{h}'} : \mathfrak{h}' \to \operatorname{End}_K(A)$ is injective, and $A$ is a faithful $\mathfrak{h}'$-module. By Theorem 5.2, the bilinear form $\beta$ on $\mathfrak{h}'$ associated with this representation is non-degenerate.

Choosing $K$-bases $\{e_i\}$ and $\{e_j'\}$ of $\mathfrak{h}'$ such that $\beta(e_i, e_j') = \delta_{ij}$ (possible since $\beta$ is non-degenerate), we obtain the element

$$c = \sum_i e_i e_i' \in U\mathfrak{g}$$

in the universal enveloping algebra. A computation using the invariance of $\beta$ shows that $c$ lies in the center of $U\mathfrak{g}$. Consequently, for any $\mathfrak{g}$-module $B$, the map

$$t_B : B \to B, \quad t_B(b) = \sum_i e_i \circ (e_i' \circ b)$$

is a $\mathfrak{g}$-module endomorphism.

Applying this to $B = A$, the element $c$ acts as a scalar (by Schur's Lemma, since $A$ is simple). A trace computation shows this scalar is non-zero, hence $t_A$ is an isomorphism. This fact is then used in the proof of the Whitehead Lemmas to construct a contracting homotopy for the Chevalley–Eilenberg complex.

In the context of the Whitehead Lemma proofs, the crucial consequence is that a simple non-trivial $\mathfrak{g}$-module cannot exist when $\mathfrak{g}$ is semi-simple; the only simple $\mathfrak{g}$-module is the trivial module $K$ (in the proof, this leads to a contradiction via $H^1(\mathfrak{g}, A) \cong \operatorname{Hom}_K(\mathfrak{g}_{ab}, A) = 0$). $\square$
