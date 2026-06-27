---
role: proof
locale: en
of_concept: nonmeasurable-cardinals-form-closed-class
source_book: gtm043
source_chapter: "12"
source_section: "12.5"
---
Let $\mathfrak{m}$ be nonmeasurable and $X$ a set of cardinal $\mathfrak{m}$. Let $\mathfrak{X}$ be the family of all subsets of $X$, so $|\mathfrak{X}| = 2^{\mathfrak{m}}$. Let $\mu$ be any nonzero $\{0,1\}$-valued measure on $\mathfrak{X}$.

By 12.3(a), since $\mathfrak{m}$ is nonmeasurable, $\mu$ is $\mathfrak{m}$-additive.

For each $x \in X$, define
$$\mathfrak{S}_x = \{A \subset X : x \in A\}, \quad -\mathfrak{S}_x = \{B \subset X : x \notin B\}.$$
Set $S = \{x \in X : \mu(\mathfrak{S}_x) = 1\}$. Then
$$\mathfrak{S} = \bigcap_{x \in S} \mathfrak{S}_x \cap \bigcap_{x \notin S} (-\mathfrak{S}_x)$$
is the intersection of $\mathfrak{m}$ families of measure $1$, hence $\mu(\mathfrak{S}) = 1$ by $\mathfrak{m}$-additivity.

But $\mathfrak{S} = \{A \in \mathfrak{X} : A \supset S\} \cap \{B \in \mathfrak{X} : B \subset S\} = \{S\}$, a singleton. Thus $\mu(\{S\}) = 1$, so $\mu$ is not free. Hence $2^{\mathfrak{m}}$ is nonmeasurable.

The general closure follows from Lemma 12.4.