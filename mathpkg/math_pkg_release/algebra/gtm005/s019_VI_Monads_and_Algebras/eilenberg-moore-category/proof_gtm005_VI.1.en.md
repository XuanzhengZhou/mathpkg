---
role: proof
locale: en
of_concept: eilenberg-moore-category
source_book: gtm005
source_chapter: "VI"
source_section: "1. Monads in a Category"
---

We construct the Eilenberg-Moore category $X^T$ and verify the adjunction.

\textbf{Step 1: $X^T$ is a category.}
Objects are $T$-algebras $\langle x, h \rangle$. Morphisms are $T$-algebra morphisms as defined.
The identity morphism on $\langle x, h \rangle$ is $1_x: x \to x$, which satisfies the compatibility
condition because $h \circ T(1_x) = h \circ 1_{Tx} = h = 1_x \circ h$.
Composition is composition in $X$; given morphisms
$f: \langle x, h \rangle \to \langle x', h' \rangle$ and $g: \langle x', h' \rangle \to \langle x'', h'' \rangle$,
we have $h'' \circ T(g \circ f) = h'' \circ Tg \circ Tf = g \circ h' \circ Tf = g \circ f \circ h$,
so $g \circ f$ is a $T$-algebra morphism. Associativity and unit laws inherit from $X$.

\textbf{Step 2: $F^T$ is a functor.}
For $x \in X$, define $F^T x = \langle Tx, \mu_x \rangle$. This is indeed a $T$-algebra because:
\begin{itemize}
\item Associativity: $\mu_x \circ T(\mu_x) = \mu_x \circ \mu_{Tx}$ by the monad associativity law.
\item Unit: $\mu_x \circ \eta_{Tx} = 1_{Tx}$ by the monad right unit law.
\end{itemize}
For $f: x \to x'$, define $F^T f = Tf$. This is a $T$-algebra morphism
$Tf: \langle Tx, \mu_x \rangle \to \langle Tx', \mu_{x'} \rangle$ because
$\mu_{x'} \circ T(Tf) = \mu_{x'} \circ T^2 f = Tf \circ \mu_x$ by the naturality of $\mu$.

\textbf{Step 3: $G^T$ is a functor.}
$G^T \langle x, h \rangle = x$ and $G^T f = f$. This is clearly functorial.

\textbf{Step 4: $\eta^T$ is natural.}
$\eta^T_x = \eta_x: x \to Tx = G^T F^T x$. Naturality follows from the naturality of $\eta$.

\textbf{Step 5: $\varepsilon^T$ is natural.}
For a $T$-algebra $\langle x, h \rangle$, define $\varepsilon^T_{\langle x, h \rangle} = h: F^T G^T \langle x, h \rangle \to \langle x, h \rangle$.
Here $F^T G^T \langle x, h \rangle = F^T x = \langle Tx, \mu_x \rangle$, so $h$ is a map
$\langle Tx, \mu_x \rangle \to \langle x, h \rangle$ precisely by the $T$-algebra associativity axiom.
Naturality of $\varepsilon^T$ follows directly from the definition of $T$-algebra morphism:
for $f: \langle x, h \rangle \to \langle x', h' \rangle$, the diagram
\[
\begin{CD}
F^T G^T \langle x, h \rangle @>{F^T G^T f}>> F^T G^T \langle x', h' \rangle \\
@V{\varepsilon^T_{\langle x, h\rangle}}VV @VV{\varepsilon^T_{\langle x', h'\rangle}}V \\
\langle x, h \rangle @>>{f}> \langle x', h' \rangle
\end{CD}
\]
commutes because this is exactly the defining condition $h' \circ Tf = f \circ h$ for $f$
to be a $T$-algebra morphism.

\textbf{Step 6: Triangular identities.}
\begin{itemize}
\item $G^T \varepsilon^T \circ \eta^T G^T$: For $x \in X$, this is
$\varepsilon^T_{F^T x} \circ F^T \eta^T_x = \mu_x \circ T\eta_x = 1_{Tx}$ by the monad right unit law.
\item $\varepsilon^T F^T \circ F^T \eta^T$: For a $T$-algebra $\langle x, h \rangle$, this is
$G^T \varepsilon^T_{\langle x, h\rangle} \circ \eta^T_{G^T \langle x, h\rangle} = h \circ \eta_x = 1_x$ by the $T$-algebra unit law.
\end{itemize}

\textbf{Step 7: The monad defined by this adjunction.}
The composite $G^T F^T = T$. The unit of the adjunction is $\eta$, matching the monad unit.
The multiplication derived from the adjunction is $G^T \varepsilon^T F^T$.
At object $x \in X$, this is $G^T(\varepsilon^T_{F^T x}) = G^T(\mu_x) = \mu_x$.
Thus the monad defined by the Eilenberg-Moore adjunction is exactly $\langle T, \eta, \mu \rangle$.
