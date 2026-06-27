---
role: proof
locale: en
of_concept: b7-ramsey-recursive-bound
source_book: gtm054
source_chapter: "VIII"
source_section: "B"
---

Let $V$ be a set with $|V| = p_0 + 1$, and let $x \in V$ be fixed. Define $V_x = V \setminus \{x\}$, so $|V_x| = p_0$. Any coloring $h: \mathcal{P}_s(V) \to \{1, 2\}$ induces a coloring $g: \mathcal{P}_{s-1}(V_x) \to \{1, 2\}$ by
$$g(T) = h(T \cup \{x\})$$
for each $T \in \mathcal{P}_{s-1}(V_x)$.

Since $|V_x| = p_0 = n(p_1, p_2 : s-1)$, the definition of the Ramsey number implies there exists either a $p_1$-subset $U_1 \subseteq V_x$ with $\mathcal{P}_{s-1}(U_1) \subseteq g^{-1}[1]$, or a $p_2$-subset $U_2 \subseteq V_x$ with $\mathcal{P}_{s-1}(U_2) \subseteq g^{-1}[2]$.

Without loss of generality, assume the $p_1$-subset $U_1$ exists. By definition $p_1 = n(q_1 - 1, q_2 : s)$. Applying the Ramsey property to the restriction of $h$ to $\mathcal{P}_s(U_1)$, we obtain either a $(q_1-1)$-subset $T_1 \subseteq U_1$ with $\mathcal{P}_s(T_1) \subseteq h^{-1}[1]$, or a $q_2$-subset $T_2 \subseteq U_1$ with $\mathcal{P}_s(T_2) \subseteq h^{-1}[2]$.

If $T_1$ exists, then $T_1 \cup \{x\}$ is a $q_1$-subset of $V$ with $\mathcal{P}_s(T_1 \cup \{x\}) \subseteq h^{-1}[1]$, because any $s$-subset of $T_1 \cup \{x\}$ either lies in $T_1$ (colored 1 by the property of $T_1$) or contains $x$ and has its remaining $s-1$ elements in $T_1 \subseteq U_1$ (colored 1 by $g$, hence colored 1 by $h$).

Thus in either case we find a $q_1$-subset all of whose $s$-subsets are color 1, or a $q_2$-subset all of whose $s$-subsets are color 2. Therefore $n(q_1, q_2 : s) \leq p_0 + 1$. The finiteness follows by induction on $s$ with base case $s=1$ given by Lemma B4.
