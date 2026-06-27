---
role: proof
locale: en
of_concept: becks-theorem
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "7. Beck's Theorem"
---

**Proof of (iii) $\Rightarrow$ (i).** Assume $G$ creates coequalizers for parallel pairs whose images have split coequalizers in $X$. First we show that the functor $G^T : X^T \to X$ also satisfies this condition. Given a parallel pair $d_0, d_1 : \langle x, h \rangle \to \langle y, k \rangle$ of $T$-algebra morphisms whose underlying maps have a split coequalizer $e : y \to z$ in $X$, we have the split fork in $X$:
$$x \xrightarrow[d_1]{d_0} y \xrightarrow{e} z, \qquad x \xleftarrow{t} y \xleftarrow{s} z$$
with $e d_0 = e d_1$, $e s = 1_z$, $d_0 t = 1_x$, $d_1 t = s e$.

We construct a $T$-algebra structure $m : T z \to z$ on $z$. Consider the diagram
\[
\xymatrix{
T x \ar[r]^{T d_0}_{T d_1} \ar[d]_{h} & T y \ar[r]^{T e} \ar[d]^{k} & T z \ar@{.>}[d]^{m} \\
x \ar[r]_{d_0}^{d_1} & y \ar[r]_{e} & z
}
\]
The left square commutes because $d_0, d_1$ are $T$-algebra maps. The right square would define $m$. Since $e$ is an absolute coequalizer (as any split coequalizer is), $T e$ is a coequalizer of $T d_0$ and $T d_1$. We have
$$e \circ k \circ T d_0 = e \circ d_0 \circ h = e \circ d_1 \circ h = e \circ k \circ T d_1$$
using that $d_0, d_1$ are algebra maps and $e d_0 = e d_1$. Thus $e \circ k$ coequalizes $T d_0, T d_1$, so by the universal property of $T e$, there exists a unique $m : T z \to z$ with $m \circ T e = e \circ k$, giving the algebra structure on $z$.

The associative law for $m$ is proved via the diagram comparing $m \circ T m$ with $m \circ \mu_z$. Both sides composed with $T^2 e$ give the same result (using naturality of $\mu$, the algebra laws for $k$, and the definition of $m$). Since $T^2 e$ is a coequalizer (hence epi), we cancel it to obtain $m \circ T m = m \circ \mu_z$. The unit law $m \circ \eta_z = 1_z$ is proved similarly. Thus $\langle z, m \rangle$ is a $T$-algebra, $e$ is a morphism of $T$-algebras by construction, and one verifies it is a coequalizer in $X^T$.

Now consider any adjunction $\langle F', G', \eta', \varepsilon' \rangle : X \rightleftharpoons A'$ defining the same monad $T$ in $X$. By the Lemma (see uniqueness-of-comparison-functor), there exists a unique comparison functor $M : A' \to A$ with $M F' = F$ and $G M = G'$. Applying this to both $X^T$ and $A$, we construct the comparison $K : A \to X^T$ and a functor $M : X^T \to A$. The composites $M K$ and $K M$ are comparison functors of adjunctions to themselves, hence identities by uniqueness. Thus $K$ is an isomorphism.

**(i) $\Rightarrow$ (ii).** If $K$ is an isomorphism, then $A \cong X^T$ and the claim reduces to verifying that $G^T$ creates coequalizers for absolute coequalizers in $X$, which follows from the construction above.

**(ii) $\Rightarrow$ (iii).** Every split coequalizer is an absolute coequalizer, so condition (ii) applies in particular to pairs with split coequalizers.
