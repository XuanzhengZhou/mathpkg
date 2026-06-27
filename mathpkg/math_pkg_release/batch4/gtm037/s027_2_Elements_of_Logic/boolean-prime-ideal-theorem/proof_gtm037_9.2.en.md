---
role: proof
locale: en
of_concept: boolean-prime-ideal-theorem
source_book: gtm037
source_chapter: "9"
source_section: "2"
---

Let $\mathcal{A} = \{J : I \subseteq J,\; J \text{ is a proper ideal of } \mathfrak{A}\}$. Then $\mathcal{A} \neq \emptyset$, since $I \in \mathcal{A}$.

Let $\mathcal{B}$ be a nonempty subset of $\mathcal{A}$ simply ordered by inclusion. We show that $\bigcup \mathcal{B} \in \mathcal{A}$. Since $\mathcal{B}$ is a nonempty collection of ideals $\supseteq I$, clearly $\bigcup \mathcal{B} \neq \emptyset$, and $I \subseteq \bigcup \mathcal{B}$.

Let $x, y \in \bigcup \mathcal{B}$. Say $x \in J \in \mathcal{B}$ and $y \in K \in \mathcal{B}$. By symmetry we may assume $J \subseteq K$. Then $x, y \in K$, and since $K$ is an ideal it follows that $x + y \in K$ and hence $x + y \in \bigcup \mathcal{B}$. If $x \leq y \in \bigcup \mathcal{B}$, say $y \in J \in \mathcal{B}$, then $x \in J$ since $J$ is an ideal; thus $x \in \bigcup \mathcal{B}$. Hence $\bigcup \mathcal{B}$ is an ideal.

Moreover, $\bigcup \mathcal{B}$ is proper: if $1 \in \bigcup \mathcal{B}$, then $1 \in J$ for some $J \in \mathcal{B}$, contradicting that $J$ is proper. Thus $\bigcup \mathcal{B} \in \mathcal{A}$.

By Zorn's Lemma, $\mathcal{A}$ has a maximal element $J$. Since $J$ is maximal in $\mathcal{A}$, there is no proper ideal strictly extending $J$, so $J$ is a maximal ideal of $\mathfrak{A}$ with $I \subseteq J$.
