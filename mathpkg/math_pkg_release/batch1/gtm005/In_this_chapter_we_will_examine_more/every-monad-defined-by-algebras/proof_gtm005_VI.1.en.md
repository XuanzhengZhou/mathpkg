---
role: proof
locale: en
of_concept: every-monad-defined-by-algebras
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "1. Monads in a Category"
---

We construct the Eilenberg-Moore category $X^T$ and the adjunction.

\textbf{Step 1: $X^T$ is a category.} Objects are $T$-algebras $\langle x, h \rangle$ with $h: Tx \to x$ satisfying the two commutative diagrams. Morphisms are as defined. Composition and identities are inherited from $X$; one must check that a composition of $T$-algebra morphisms is again a $T$-algebra morphism, which follows from the commutativity of the relevant diagrams.

\textbf{Step 2: $G^T$ is a functor.} Define $G^T: X^T \to X$ by $G^T(\langle x, h \rangle) = x$ on objects and $G^T(f) = f$ on morphisms. This clearly preserves composition and identities.

\textbf{Step 3: $F^T$ is a functor.} Define $F^T: X \to X^T$ by $F^T(x) = \langle Tx, \mu_x \rangle$ on objects. We must verify that $\langle Tx, \mu_x \rangle$ is indeed a $T$-algebra. The associative law for the algebra is precisely the associativity of the monad $\mu \circ T\mu = \mu \circ \mu T$ evaluated at $x$. The unit law is $\mu_x \circ \eta_{Tx} = \mathrm{id}_{Tx}$, which follows from the left unit law of the monad.

On morphisms, $F^T(f: x \to x') = Tf: \langle Tx, \mu_x \rangle \to \langle Tx', \mu_{x'} \rangle$. This is a $T$-algebra morphism because $\mu_{x'} \circ T(Tf) = Tf \circ \mu_x$ by naturality of $\mu$.

\textbf{Step 4: The adjunction.} Define $\eta^T_x = \eta_x: x \to Tx = G^T F^T x$, which is natural since $\eta$ is. Define $\varepsilon^T_{\langle x, h \rangle} = h: F^T G^T \langle x, h \rangle = \langle Tx, \mu_x \rangle \to \langle x, h \rangle$.

We must verify that $h$ is a $T$-algebra morphism from $\langle Tx, \mu_x \rangle$ to $\langle x, h \rangle$. The diagram
$$
\begin{array}{ccc}
T^2 x & \xrightarrow{Th} & Tx \\
{\scriptstyle \mu_x}\downarrow & & \downarrow{\scriptstyle h} \\
Tx & \xrightarrow{h} & x
\end{array}
$$
commutes by the associative law for the $T$-algebra $\langle x, h \rangle$. Thus $h$ is indeed a morphism.

Naturality of $\varepsilon^T$: for a $T$-algebra morphism $f: \langle x, h \rangle \to \langle x', h' \rangle$, the required square commutes by definition of a $T$-algebra morphism.

\textbf{Step 5: Triangular identities.} The first triangular identity: $\varepsilon^T_{F^T x} \circ F^T \eta^T_x = \mathrm{id}_{F^T x}$. Here $\varepsilon^T_{F^T x} = \mu_x$ and $F^T \eta^T_x = T\eta_x$, so we need $\mu_x \circ T\eta_x = \mathrm{id}_{Tx}$, which is the right unit law of the monad.

The second triangular identity: $G^T \varepsilon^T_{\langle x, h \rangle} \circ \eta^T_{G^T \langle x, h \rangle} = \mathrm{id}_{G^T \langle x, h \rangle}$. This is $h \circ \eta_x = \mathrm{id}_x$, which is the unit law of the $T$-algebra.

Thus $\langle F^T, G^T; \eta^T, \varepsilon^T \rangle$ is an adjunction.

\textbf{Step 6: The monad of this adjunction recovers $T$.} The monad defined by the adjunction has endofunctor $G^T F^T(x) = Tx$, unit $\eta^T = \eta$, and multiplication $G^T \varepsilon^T F^T(x) = \mu_x$. So the monad is exactly $\langle T, \eta, \mu \rangle$.
