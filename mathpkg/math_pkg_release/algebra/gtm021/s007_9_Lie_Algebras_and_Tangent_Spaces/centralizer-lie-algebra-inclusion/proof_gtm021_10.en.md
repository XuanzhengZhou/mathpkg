---
role: proof
locale: en
of_concept: centralizer-lie-algebra-inclusion
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
Since $C_G(x) = \gamma_x^{-1}(e)$, the tangent space $\mathcal{L}(C_G(x))$ is contained in $\operatorname{Ker}(d\gamma_x)_e = \operatorname{Ker}(1 - \operatorname{Ad} x)$. Thus $\mathcal{L}(C_G(x)) \subset \mathfrak{c}_{\mathfrak{g}}(x) = \{X \in \mathfrak{g} \mid \operatorname{Ad} x(X) = X\}$.

For $G = \mathrm{GL}(n, K)$, Lemma B gives $\operatorname{Ad} x(X) = x X x^{-1}$. The condition $\operatorname{Ad} x(X) = X$ means $X$ commutes with $x$. The set of all such matrices is the linear subspace $\mathfrak{c}_{\mathfrak{gl}(n)}(x)$. The centralizer $C_G(x)$ consists of the invertible matrices in this subspace, which is a principal open subset. Therefore $\dim C_G(x) = \dim \mathfrak{c}_{\mathfrak{g}}(x)$. Combined with the inclusion $\mathcal{L}(C_G(x)) \subset \mathfrak{c}_{\mathfrak{g}}(x)$, we get equality of dimensions and hence equality of the Lie algebras.
