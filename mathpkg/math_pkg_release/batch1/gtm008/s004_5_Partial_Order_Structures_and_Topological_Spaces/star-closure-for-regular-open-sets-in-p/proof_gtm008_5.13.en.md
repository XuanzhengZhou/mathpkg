---
role: proof
locale: en
of_concept: star-closure-for-regular-open-sets-in-p
source_book: gtm008
source_chapter: "5"
source_section: "5"
---
By Theorem 5.10, we have $G \subseteq G^{*\Delta}$. For the reverse inclusion, suppose $a \in G^{*\Delta}$. For each $c \leq a$, there is an ultrafilter $F'$ for $P$ such that $c \in F'$. Since $c \leq a$ and $c \in F'$, we have $a \in F'$. Consequently if $a \in G^{*\Delta}$, then $\exists b \in F' \cap G$. Since $F'$ is an ultrafilter for $P$ and both $c$ and $b$ are in $F'$:
$$(\exists b' \in F')[b' \leq c \wedge b' \leq b].$$
But $b \in G$ and $b' \leq b$. Therefore $b' \in G$, i.e.,
\begin{align*}
a \in G^{*\Delta} &\rightarrow (\forall c \leq a)(\exists b \leq c)[b \in G] \\
&\rightarrow (\forall c \leq a)[[c] \cap G \neq 0] \\
&\rightarrow (\forall c \leq a)[c \in G^{-}] \\
&\rightarrow [a] \subseteq G^{-} \\
&\rightarrow a \in G^{-0} \\
&\rightarrow a \in G \quad \text{(since $G$ is regular open)}.
\end{align*}
Thus $G^{*\Delta} \subseteq G$, and by Theorem 5.10, $G^{*\Delta} = G$.
