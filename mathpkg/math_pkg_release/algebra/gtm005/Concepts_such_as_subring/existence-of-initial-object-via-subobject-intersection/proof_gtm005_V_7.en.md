---
role: proof
locale: en
of_concept: existence-of-initial-object-via-subobject-intersection
source_book: gtm005
source_chapter: "V"
source_section: "7. Subobjects and Generators"
---

Form the product $q_0 = \prod_{q \in Q} q$ of all the objects in the small cogenerating set $Q$ and take the intersection $r$ of all subobjects of $q_0$. For any object $d \in \mathcal{D}$, there is at most one arrow $r \to d$, for if there were two different arrows, their equalizer would be a proper monic to $r$, hence a subobject of $q_0$ smaller than the intersection $r$.

To show $r$ is initial in $\mathcal{D}$, we thus need only construct an arrow $r \to d$ for each $d$. So consider the set $H$ of all arrows $h : d \to q$ (for $q \in Q$) and the (small) product $\prod_{h \in H} q$. Take the arrow $j : d \to \prod_{h \in H} q$ with components $h$ (i.e., with $p_h \circ j = h$ for each projection $p_h$). Since the set $Q$ cogenerates, $j$ is monic. Form the pullback
\[
\begin{array}{ccc}
c & \xrightarrow{j'} & d \\
{\scriptstyle}\Big\downarrow & & \Big\downarrow{\scriptstyle j} \\
\prod_{q \in Q} q = q_0 & \xrightarrow{k} & \prod_{h \in H} q,
\end{array}
\]
where $k$ is the arrow with components $p_h \circ k = p_q$ for each $h : d \to q$. Then $j'$, as pullback of a monic $j$, is monic (by the lemma that pullbacks of monics are monic), so $c$ is a subobject of $q_0$. But $r$ was the intersection of all subobjects of $q_0$, so there is an arrow $r \to c$. The composite $r \to c \xrightarrow{j'} d$ is the desired arrow.
