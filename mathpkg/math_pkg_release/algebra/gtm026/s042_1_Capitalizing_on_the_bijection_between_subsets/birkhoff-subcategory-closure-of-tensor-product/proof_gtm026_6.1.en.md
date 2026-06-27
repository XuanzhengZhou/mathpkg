---
role: proof
locale: en
of_concept: birkhoff-subcategory-closure-of-tensor-product
source_book: gtm026
source_chapter: "6"
source_section: "1"
---

The second statement follows directly from the first using results 1.19 and 1.18 (which characterize Beck functors in terms of closure properties). We prove the first statement: $\mathbf{Set}^S \otimes T$ is closed under products, subalgebras, and quotients.

All three closure properties are established simultaneously by interpreting the following generic commutative cube induced by a morphism $f: (X, \xi, \theta) \to (Y, \xi', \theta')$ in $\mathbf{Set}^S \times \mathbf{Set}^T$ and a $T$-operation $\alpha: (U^T)^n \to U^T$. The six faces of the cube correspond to the compositions

\[
\begin{array}{c}
(X^n, \xi^n) \xrightarrow{(X,\theta)\alpha} (X, \xi) \\
(Y^n, (\xi')^n) \xrightarrow{(Y,\theta')\alpha} (Y, \xi')
\end{array}
\]

and their factorizations through $f^n$ and $f$. Of the six faces, all commute except possibly the left and right sides (since $f$ is both an $S$-homomorphism and a $T$-homomorphism, but the algebra structures may not align).

\textbf{Closure under subalgebras.} If the right side commutes---that is, if $(Y, \xi', \theta')$ is an $S$-$T$ bialgebra---and $f$ is injective, then commutativity of the other faces forces the left side to commute when followed by the appropriate projections. Hence $(X, \xi, \theta)$ is also a bialgebra. This establishes closure under subalgebras.

\textbf{Closure under quotients.} If the left side commutes---that is, $(X, \xi, \theta)$ is a bialgebra---and $f$ is surjective, then the right side commutes when preceded by $f^n S$. By 1.4.29 with $H = ()^n S$, the map $f^n S$ is surjective. Consequently $(Y, \xi', \theta')$ is also a bialgebra. This establishes closure under quotients.

\textbf{Closure under products.} The product case follows from the fact that the bialgebra condition is equational (cf. 1.4.22), and equations are preserved under products. More directly, if each factor satisfies the commutativity condition for all $\alpha$, then the product inherits this condition componentwise.

Thus $\mathbf{Set}^S \otimes T$ is closed under products, subalgebras, and quotients, making it a Birkhoff subcategory.
