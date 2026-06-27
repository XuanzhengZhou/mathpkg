---
role: proof
locale: en
of_concept: monad-in-preorder
source_book: gtm005
source_chapter: "VI"
source_section: "1. Monads in a Category"
---

In a preorder $P$ regarded as a category, an endofunctor $T: P \to P$ is a function preserving
the order: $x \leq y \implies Tx \leq Ty$. The identity functor $I_P$ sends each $x$ to itself.

A natural transformation $\eta: I_P \to T$ consists of components $\eta_x: x \to Tx$.
In the preorder category, such an arrow exists precisely when $x \leq Tx$.
Naturality is automatic: for any $f: x \to y$ (i.e., $x \leq y$), the square
\[
\begin{CD}
x @>{\eta_x}>> Tx \\
@V{f}VV @VV{Tf}V \\
y @>>{\eta_y}> Ty
\end{CD}
\]
commutes vacuously, since there is at most one arrow $x \to Ty$ (the composite both ways).

A natural transformation $\mu: T^2 \to T$ consists of components $\mu_x: T(Tx) \to Tx$,
which exist precisely when $T(Tx) \leq Tx$ for all $x$.

The monad axioms (associativity and unit laws) are expressed by commutative diagrams.
In a preorder category, any diagram commutes automatically because there is at most one arrow
between any two objects. Therefore the existence conditions $x \leq Tx$ and $T(Tx) \leq Tx$
are both necessary and sufficient for $\langle T, \eta, \mu \rangle$ to be a monad.

The condition $x \leq Tx$ is the \textbf{inflationary} property, and $T(Tx) \leq Tx$ is the
\textbf{idempotence} condition (together with $Tx \leq T(Tx)$ from applying the first condition
to $Tx$, we obtain $T(Tx) \cong Tx$). A monotone function satisfying these two properties
is precisely a closure operator on the preorder.
