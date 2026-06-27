---
role: proof
locale: en
of_concept: coequalizers-in-set
source_book: gtm026
source_chapter: "1"
source_section: "1. The Base Category"
---

Let $R_0 = \{(af, ag) : a \in A\} \subseteq B \times B$ and let $R$ be the intersection of all equivalence relations on $B$ containing $R_0$. Set $Q = B/R$, the set of $R$-equivalence classes, and let $q: B \to Q$ be the canonical projection $q(b) = bR$.

First, $f \circ q = g \circ q$: for any $a \in A$, $(af)R_0(ag)$, so $(af, ag) \in R$, hence $(af)R = (ag)R$, i.e., $q(f(a)) = q(g(a))$.

Now suppose $q': B \to Q'$ satisfies $f \circ q' = g \circ q'$. Define $S = \{(b_1, b_2) \in B \times B : b_1 q' = b_2 q'\}$. $S$ is an equivalence relation on $B$:
\begin{itemize}
\item Reflexive: $b q' = b q'$;
\item Symmetric: if $b_1 q' = b_2 q'$ then $b_2 q' = b_1 q'$;
\item Transitive: if $b_1 q' = b_2 q'$ and $b_2 q' = b_3 q'$ then $b_1 q' = b_3 q'$.
\end{itemize}
For any $a \in A$, $f(a) q' = g(a) q'$ (since $f \circ q' = g \circ q'$), so $(af, ag) \in S$. Thus $S$ contains $R_0$, and since $S$ is an equivalence relation, $S$ contains $R$ (as $R$ is the intersection of all equivalence relations containing $R_0$). Hence $R \subseteq S$.

Define $h: Q \to Q'$ by $(bR)h = bq'$. This is well-defined: if $b_1 R = b_2 R$, then $(b_1, b_2) \in R \subseteq S$, so $b_1 q' = b_2 q'$. For any $b \in B$, $(q \circ h)(b) = (bR)h = bq' = q'(b)$, so $q \circ h = q'$.

For uniqueness, if $k: Q \to Q'$ satisfies $q \circ k = q'$, then for any $bR \in Q$, $(bR)k = q(b) \circ k = q'(b) = (bR)h$, so $k = h$.
