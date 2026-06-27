---
role: proof
locale: en
of_concept: regular-ultrafilter-existence
source_book: gtm037
source_chapter: "18"
source_section: "Model Theory"
---

Let $J = \{X \subseteq I : X \text{ is finite}\}$. It clearly suffices to prove the proposition for $J$ in place of $I$, since $|I| = |J|$ by 18.35.

For each $X \in J$ let $G_X = \{Y \in J : X \subseteq Y\}$. If $X_0, \ldots, X_{m-1} \in J$, then

$$G_{X_0} \cap \cdots \cap G_{X_{m-1}} = G_{X_0 \cup \cdots \cup X_{m-1}} \neq \varnothing,$$

so $E = \{G_X : X \in J\}$ has the finite intersection property and hence is included in an ultrafilter $F$ over $J$.

Note that $G_X \neq G_Y$ if $X, Y \in J$ and $X \neq Y$, so $|E| = |J|$. If $H \subseteq E$ and $H$ is infinite, clearly $\bigcap H = \varnothing$.

The above proof is of course similar to a part of our proof of the compactness theorem using ultraproducts; the ultrafilter constructed there is regular.
