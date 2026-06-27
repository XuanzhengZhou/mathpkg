---
role: proof
locale: en
of_concept: projective-injective-descent-for-lie-subalgebras
source_book: gtm004
source_chapter: "VII"
source_section: "1. Lie Algebras and their Universal Enveloping Algebra"
---

# Proof of Projective and Injective Module Descent for Lie Subalgebras

**Corollary 1.5.** Let $\mathfrak{h}$ be a Lie subalgebra of $\mathfrak{g}$. Then every $\mathfrak{g}$-projective (resp. $\mathfrak{g}$-injective) module is $\mathfrak{h}$-projective (resp. $\mathfrak{h}$-injective).

**Proof.** This is a consequence of Corollary 1.4 together with Theorem IV.12.5.

By Corollary 1.4, $U\mathfrak{g}$ is a free $U\mathfrak{h}$-module (with basis given by the PBW monomials corresponding to increasing sequences in a completion of an ordered basis of $\mathfrak{h}$ to an ordered basis of $\mathfrak{g}$).

Now let $P$ be a $\mathfrak{g}$-projective module. Then $P$ is a direct summand of a free $U\mathfrak{g}$-module, i.e., there exists a $U\mathfrak{g}$-module $Q$ such that

$$P \oplus Q \cong \bigoplus_{I} U\mathfrak{g}$$

as $U\mathfrak{g}$-modules. Restricting the module structures via the inclusion $U\mathfrak{h} \hookrightarrow U\mathfrak{g}$, we obtain an isomorphism of $U\mathfrak{h}$-modules. Since $U\mathfrak{g}$ is a free $U\mathfrak{h}$-module, the right-hand side $\bigoplus_I U\mathfrak{g}$ is a free $U\mathfrak{h}$-module. Hence $P$ is a direct summand of a free $U\mathfrak{h}$-module and therefore is $\mathfrak{h}$-projective.

For the injective case, let $I$ be a $\mathfrak{g}$-injective module. By Theorem IV.12.5, since $U\mathfrak{g}$ is a free (hence flat) $U\mathfrak{h}$-module, the restriction functor from $U\mathfrak{g}$-modules to $U\mathfrak{h}$-modules has an exact left adjoint (the induction functor $U\mathfrak{g} \otimes_{U\mathfrak{h}} -$). The restriction of an injective module along a ring homomorphism that makes the larger ring a free module over the smaller one preserves injectivity. More explicitly, one can verify that $\operatorname{Hom}_{U\mathfrak{h}}(-, I) \cong \operatorname{Hom}_{U\mathfrak{g}}(U\mathfrak{g} \otimes_{U\mathfrak{h}} -, I)$, and since $U\mathfrak{g} \otimes_{U\mathfrak{h}} -$ is exact (by freeness) and $I$ is $U\mathfrak{g}$-injective, the functor $\operatorname{Hom}_{U\mathfrak{h}}(-, I)$ is exact, so $I$ is $U\mathfrak{h}$-injective. $\square$
