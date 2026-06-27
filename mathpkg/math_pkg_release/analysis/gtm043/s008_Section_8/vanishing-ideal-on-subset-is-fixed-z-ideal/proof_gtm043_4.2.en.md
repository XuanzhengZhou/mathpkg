---
role: proof
locale: en
of_concept: vanishing-ideal-on-subset-is-fixed-z-ideal
source_book: gtm043
source_chapter: "4"
source_section: "4.2"
---

Let $I_S = \{f \in C(X) : f[S] = \{0\}\}$. First, $I_S$ is clearly an ideal: if $f, g \in I_S$, then $(f-g)[S] = f[S] - g[S] = \{0\}$, and for any $h \in C(X)$, $(fh)[S] = f[S] \cdot h[S] = \{0\}$.

To see that $I_S$ is a $z$-ideal: if $f \in I_S$ and $g \in C(X)$ satisfies $Z(f) \subseteq Z(g)$, then $g$ vanishes wherever $f$ vanishes. Since $f$ vanishes on $S$, we have $S \subseteq Z(f) \subseteq Z(g)$, so $g[S] = \{0\}$ and $g \in I_S$. Hence $I_S$ is a $z$-ideal.

The ideal is fixed because every $f \in I_S$ vanishes on $S$, so $S \subseteq \bigcap Z[I_S]$, and since $S \neq \emptyset$, the intersection is nonempty. Moreover, $\overline{S} \subseteq \bigcap Z[I_S]$ because zero-sets are closed and each $f \in I_S$ vanishes on the closed set $\overline{S}$.

If $S$ is not dense in $X$, then there exists a nonzero continuous function vanishing on $\overline{S}$ (by complete regularity of $X$), so $I_S \neq \{0\}$. If $S$ is dense, then $I_S$ may be the zero ideal.

Finally, $I_S \cap C^*(X)$ is the corresponding fixed ideal in $C^*(X)$.
