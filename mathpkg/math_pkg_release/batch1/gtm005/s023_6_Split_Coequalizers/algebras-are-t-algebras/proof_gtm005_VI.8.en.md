---
role: proof
locale: en
of_concept: algebras-are-t-algebras
source_book: gtm005
source_chapter: "VI"
source_section: "8"
---

The proof uses Beck's theorem (Section 7). Consider the forgetful functor $G: \langle \Omega, E \rangle\text{-}\mathbf{Alg} \to \mathbf{Set}$ and the resulting monad $T$ in $\mathbf{Set}$. Let $f, g: A \to B$ be a parallel pair of algebra morphisms for which the underlying functions $Gf, Gg: GA \to GB$ have an absolute coequalizer $e$ in $\mathbf{Set}$:
$$GA \xrightarrow[Gg]{Gf} GB \xrightarrow{e} X.$$

To apply Beck's theorem we must lift $e$ to a unique algebra morphism and show the lift is a coequalizer in the category of algebras. For any $n$-ary operator $\omega \in \Omega$, consider the diagram
$$\begin{array}{ccc}
A^n & \xrightarrow{f^n} B^n & \xrightarrow{e^n} X^n \\
{\scriptstyle\omega_A}\downarrow & {\scriptstyle\omega_B}\downarrow & \\
A & \xrightarrow{f} B & \xrightarrow{e} X
\end{array}$$
where the left square commutes because $f$ is an algebra morphism. Since $e$ is an absolute coequalizer (hence a coequalizer in $\mathbf{Set}$) and $e^n$ is a coequalizer of $f^n, g^n$, the function $\omega_B$ induces a unique dotted arrow $\omega_X: X^n \to X$ making the right square commute. This defines the $\Omega$-algebra structure on $X$.

The identities in $E$ hold for $X$ because they hold for $B$ and $e$ is epic (being a coequalizer). Thus $X$ lifts uniquely to an $\langle \Omega, E \rangle$-algebra, and $e$ becomes an algebra morphism by construction.

To show $e$ is a coequalizer in the algebra category, let $h: B \to C$ be any algebra morphism with $hf = hg$. In $\mathbf{Set}$, since $e$ is a coequalizer, $h$ factors uniquely as $h = h' \circ e$ for some function $h': X \to C$. The fact that $h'$ is an algebra morphism follows because $e$ is epic and $h$ is an algebra morphism:
$$h' \circ \omega_X \circ e^n = h' \circ e \circ \omega_B = h \circ \omega_B = \omega_C \circ h^n = \omega_C \circ h'^n \circ e^n,$$
and since $e^n$ is epic, we get $h' \circ \omega_X = \omega_C \circ h'^n$.

Thus $G$ creates coequalizers for parallel pairs whose images have absolute coequalizers. By Beck's theorem (condition (ii)), the comparison functor $K: \langle \Omega, E \rangle\text{-}\mathbf{Alg} \to \mathbf{Set}^T$ is an isomorphism.
