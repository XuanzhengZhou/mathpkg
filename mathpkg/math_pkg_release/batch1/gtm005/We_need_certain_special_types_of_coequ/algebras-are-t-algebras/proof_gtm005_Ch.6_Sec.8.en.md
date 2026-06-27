---
role: proof
locale: en
of_concept: algebras-are-t-algebras
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "8. Algebras Are T-Algebras"
---

By Beck's Theorem, it suffices to show that the forgetful functor $G : \langle \Omega, E \rangle\text{-}\mathbf{Alg} \to \mathbf{Set}$ satisfies condition (ii): it creates coequalizers for parallel pairs whose images have absolute coequalizers.

Consider any parallel pair $f, g : A \rightrightarrows B$ of $\langle \Omega, E \rangle$-algebra morphisms whose underlying functions have an absolute coequalizer $e : G B \to X$ in $\mathbf{Set}$:
$$G A \xrightarrow[G g]{G f} G B \xrightarrow{e} X.$$

For any $n$-ary operator $\omega \in \Omega$, consider the diagram
\[
\xymatrix{
A^n \ar[r]^{f^n}_{g^n} \ar[d]_{\omega_A} & B^n \ar[r]^{e^n} \ar[d]_{\omega_B} & X^n \ar@{.>}[d]^{\omega_X} \\
A \ar[r]_{f}^{g} & B \ar[r]_{e} & X
}
\]
The left square commutes because $f, g$ are $\Omega$-algebra morphisms. We need to define $\omega_X : X^n \to X$ making the right square commute.

Since $e$ is an absolute coequalizer, $e^n$ is a coequalizer of $f^n$ and $g^n$. We compute:
$$e \circ \omega_B \circ f^n = e \circ f \circ \omega_A = e \circ g \circ \omega_A = e \circ \omega_B \circ g^n.$$
Thus $e \circ \omega_B : B^n \to X$ coequalizes $f^n, g^n$. By the universal property of $e^n$, there exists a unique map $\omega_X : X^n \to X$ with $\omega_X \circ e^n = e \circ \omega_B$.

This defines an $\Omega$-algebra structure on $X$. One verifies that $X$ satisfies the identities $E$ using the fact that $e$ is surjective (as an absolute coequalizer in $\mathbf{Set}$ is a surjection): for any identity, both sides composed with the appropriate power of $e$ agree because $B$ satisfies $E$, and since $e$ is epi, they agree on $X$.

The map $e : B \to X$ is then a morphism of $\langle \Omega, E \rangle$-algebras by construction. It is a coequalizer in the algebra category: given any algebra morphism $h : B \to C$ with $h f = h g$, the underlying function factors uniquely as $h' \circ e$ in $\mathbf{Set}$, and $h'$ is easily seen to be an algebra morphism using the surjectivity of $e$. Thus $G$ creates coequalizers, and Beck's Theorem yields the isomorphism.
