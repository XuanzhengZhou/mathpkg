---
role: proof
locale: en
of_concept: coherence-of-extension-with-monoidal-natural-transformations
source_book: gtm005
source_chapter: "XI"
source_section: "2. Monoidal Functors"
---

The proof proceeds by induction on the structure of the word $v$. For the base cases $v = \square$ (binary tensor) and $v = e$ (unit), the commutative diagrams are exactly conditions (5) and (6) in the definition of a monoidal natural transformation.

For the inductive step, suppose the diagram commutes for words $v$ and $v'$. Then for the concatenated word $v \square v'$, consider the following diagram:

\begin{center}
\begin{tikzcd}
(v \square v')(F a_1, \ldots) \arrow[r, "F_{v \square v'}"] \arrow[d] & F((v \square v')(a_1, \ldots)) \arrow[d] \\
(v \square v')(G a_1, \ldots) \arrow[r, "G_{v \square v'}"] & G((v \square v')(a_1, \ldots))
\end{tikzcd}
\end{center}

By definition, $F_{v \square v'} = F_2 \circ (F_v \square F_{v'})$ and $G_{v \square v'} = G_2 \circ (G_v \square G_{v'})$. The diagram factors through the tensor products, and the required commutativity follows from condition (5) applied to the outer $F_2$, $G_2$ layer together with the induction hypothesis applied to $F_v$, $G_v$ and $F_{v'}$, $G_{v'}$.
