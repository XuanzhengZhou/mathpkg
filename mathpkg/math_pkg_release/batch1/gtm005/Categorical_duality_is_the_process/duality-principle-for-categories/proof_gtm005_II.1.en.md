---
role: proof
locale: en
of_concept: duality-principle-for-categories
source_book: gtm005
source_chapter: "II"
source_section: "1. Duality"
---

Observe that each of the axioms for a category (as given in §I.1) is self-dual: replacing each atomic constituent by its dual transforms an axiom into another axiom. Concretely:

\begin{itemize}
\item The axiom ``for all $f$ there exist $a$ and $b$ with $f : a \rightarrow b$'' dualizes to ``for all $f$ there exist $a$ and $b$ with $f : b \rightarrow a$'', which is simply the same axiom with the variables renamed. Both state that every arrow has a domain and a codomain.
\item The associativity axiom $h \circ (g \circ f) = (h \circ g) \circ f$ dualizes to $(f \circ g) \circ h = f \circ (g \circ h)$, which is again the associativity law under renaming of variables.
\item The identity axioms $f \circ 1_a = f$ and $1_b \circ f = f$ dualize to $1_a \circ f = f$ and $f \circ 1_b = f$, which are the same two axioms swapped.
\end{itemize}

Now let $\Sigma$ be any statement that is a consequence of the category axioms. Then there exists a formal proof $\Pi$ of $\Sigma$ from the axioms. Define $\Pi^{*}$ to be the sequence of statements obtained by replacing each statement in $\Pi$ by its dual. Since each axiom dualizes to an axiom, each assumption in $\Pi^{*}$ is an axiom. Moreover, each inference rule of first-order logic (modus ponens, generalization, etc.) is invariant under dualization, because dualization merely permutes atomic formulas and reverses the order of composition without affecting the logical structure. Therefore $\Pi^{*}$ is a valid proof of $\Sigma^{*}$ from the axioms. Hence $\Sigma^{*}$ is also a consequence of the axioms.

For the extension to functors: The atomic statements for a functor $T : C \to B$ include $T(g \circ f) = Tg \circ Tf$ and $T(1_a) = 1_{Ta}$. Under dualization in both $C$ and $B$, the first becomes $T(f \circ g) = Tf \circ Tg$, which is the same functoriality condition (just with the order of arguments swapped). The second becomes $T(1_a) = 1_{Ta}$, which is literally identical. Thus the statement ``$T$ is a functor'' is self-dual, and the same proof-dualization argument applies.

As an immediate application: from the theorem that a terminal object is unique up to isomorphism (if it exists), the duality principle yields that an initial object is unique up to isomorphism (if it exists), without any additional proof.
