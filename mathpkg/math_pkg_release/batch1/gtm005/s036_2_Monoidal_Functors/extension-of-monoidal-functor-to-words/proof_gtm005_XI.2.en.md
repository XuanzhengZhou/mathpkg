---
role: proof
locale: en
of_concept: extension-of-monoidal-functor-to-words
source_book: gtm005
source_chapter: "XI"
source_section: "2. Monoidal Functors"
---

The extension is defined by induction on the structure of tensor words $v$ in $n$ letters, as defined in \S VII.2. For the base cases:
\begin{itemize}
\item $F_\square = F_2$, the given structure map for the binary tensor product.
\item $F_e = F_0$, the given structure map for the unit object.
\end{itemize}

For the inductive step, if $v$ and $v'$ are words, then $v \square v'$ is a word and we define

$$F_{v \square v'} = F_2 \circ (F_v \square F_{v'}).$$

With this definition, the naturality of each $F_v$ follows from the naturality of $F_2$ and the induction hypothesis. The coherence of all diagrams built from these $F_v$ follows from the three coherence conditions (3), (4), and (4') in the definition of a monoidal functor, together with the coherence theorem for monoidal categories (\S VII.2).
