---
role: proof
locale: en
of_concept: initial-object-from-cogenerating-set
source_book: gtm005
source_chapter: "V. Limits"
source_section: "7. Subobjects and Generators"
---

Form the product $q_0 = \prod_{q \in Q} q$ of all the objects in the small cogenerating set $Q$ and take the intersection $r$ of all subobjects of $q_0$.

**Uniqueness.** For any object $d \in D$, there is at most one arrow $r \to d$: if there were two different arrows, their equalizer would be a proper monic to $r$, hence a subobject of $q_0$ smaller than the intersection $r$, contradicting that $r$ is the intersection of all subobjects of $q_0$.

**Existence.** To show $r$ is initial in $D$, we need only construct an arrow $r \to d$ for each $d$. Consider the set $H$ of all arrows $h: d \to q$ with $q \in Q$ and the (small) product $\prod_{h \in H} q$. Take the arrow $j: d \to \prod_{h \in H} q$ with components $h$ (i.e., with $p_h \circ j = h$ for each projection $p_h$). Since the set $Q$ cogenerates, $j$ is monic.

Form the pullback
$$
\begin{array}{ccc}
c & \xrightarrow{j'} & d \\
{\scriptstyle}\downarrow && {\scriptstyle j}\downarrow \\
\prod_{q \in Q} q = q_0 & \xrightarrow{k} & \prod_{h \in H} q
\end{array}
$$
where $k$ is the arrow with components $p_h \circ k = p_q$ for each $h: d \to q$. Then $j'$, as pullback of a monic $j$, is monic (by the lemma that pullbacks of monics are monic), so $c$ is a subobject of $q_0$. But $r$ was the intersection of all subobjects of $q_0$, so there is an arrow $r \to c$. The composite $r \to c \xrightarrow{j'} d$ is the desired arrow.

Thus $r$ is an initial object of $D$.
