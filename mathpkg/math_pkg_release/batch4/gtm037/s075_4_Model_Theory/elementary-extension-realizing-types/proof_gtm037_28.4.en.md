---
role: proof
locale: en
of_concept: elementary-extension-realizing-types
source_book: gtm037
source_chapter: "28"
source_section: "4. Model Theory"
---

We prove the lemma by applying the compactness theorem; it can also be proved using ultraproducts (Exercise 28.39). We consider each language $\mathcal{L}_X$ as a reduct of a certain $A$-expansion $\mathcal{L}_A$ of $\mathcal{L}$. For each pair $(X, \Delta)$ such that $X \subseteq A$, $|X| \leq m$, and $\Delta$ is a $1$-type over $\mathrm{Th}((\mathfrak{A}, x)_{x \in X})$ in $\mathcal{L}_X$, we introduce a new constant $c_{X,\Delta}$, thus expanding $\mathcal{L}_A$ to a new language $\mathcal{L}'$. Let $\Gamma$ be the set:

$$\mathrm{Th}((\mathfrak{A}, a)_{a \in A}) \cup \{\varphi(c_{X,\Delta}) : \varphi \in \Delta,\; X \subseteq A,\; |X| \leq m,\; \Delta \text{ a } 1\text{-type over } \mathrm{Th}((\mathfrak{A}, x)_{x \in X})\}.$$

By the compactness theorem, $\Gamma$ is consistent (each finite subset involves only finitely many types, which can be realized by taking an appropriate elementary extension). A model of $\Gamma$ yields the desired elementary extension $\mathfrak{B}$. The cardinality bound $|B| = 2^m$ follows from the number of new constants introduced: there are at most $2^m$ subsets $X$ of size $\leq m$, and for each, at most $2^m$ types $\Delta$.
