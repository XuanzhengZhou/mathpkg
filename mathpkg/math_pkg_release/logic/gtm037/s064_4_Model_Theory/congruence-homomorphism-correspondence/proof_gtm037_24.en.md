---
role: proof
locale: en
of_concept: congruence-homomorphism-correspondence
source_book: gtm037
source_chapter: "24"
source_section: ""
---
(i) If $R$ is a congruence relation on $\mathfrak{A}$, then the map $[\,\cdot\,]_R : \mathfrak{A} \to \mathfrak{A}/R$ sending each $a \in A$ to its $R$-equivalence class satisfies the homomorphism condition by definition of the operations on $\mathfrak{A}/R$.

(ii) If $f: \mathfrak{A} \to \mathfrak{B}$ is a homomorphism, then $\ker f$ is an equivalence relation. The congruence condition follows from the fact that $f$ preserves operations: if $a_i R a_i'$ for all $i < m$, then $f a_i = f a_i'$, so $f(\mathbf{O}^{\mathfrak{A}}(a_0,\ldots,a_{m-1})) = \mathbf{O}^{\mathfrak{B}}(f a_0,\ldots,f a_{m-1}) = \mathbf{O}^{\mathfrak{B}}(f a_0',\ldots,f a_{m-1}') = f(\mathbf{O}^{\mathfrak{A}}(a_0',\ldots,a_{m-1}'))$, hence the images are equal and the relation is preserved under operations.

(iii) Define $g: \mathfrak{B} \to \mathfrak{A}/\ker f$ by $g(f a) = [a]_{\ker f}$. This is well-defined because if $f a = f a'$, then $a \ker f\, a'$, so $[a] = [a']$. It is injective for the same reason reversed, surjective because $f$ is onto, and a homomorphism because $f$ and $[\,\cdot\,]$ are homomorphisms.
