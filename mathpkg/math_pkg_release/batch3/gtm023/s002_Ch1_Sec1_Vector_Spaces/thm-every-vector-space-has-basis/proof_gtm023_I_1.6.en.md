---
role: proof
locale: en
of_concept: thm-every-vector-space-has-basis
source_book: gtm023
source_chapter: "I"
source_section: "1.6"
---

Let $\mathcal{A}(R, S)$ be the set of all subsets $X$ of $E$ such that $R \subset X \subset S$ and the vectors of $X$ are linearly independent. $\mathcal{A}(R, S)$ is partially ordered by inclusion.

Let $\{X_\alpha\}$ be a chain in $\mathcal{A}(R, S)$ and set $A = \bigcup_\alpha X_\alpha$. We claim $A \in \mathcal{A}(R, S)$. Clearly $R \subset A \subset S$. To verify linear independence, consider a finite linear relation $\sum_{i=1}^n \lambda^i x_i = 0$ with $x_i \in A$. Since $\{X_\alpha\}$ is a chain, all $x_i$ belong to some $X_{\alpha_1}$. The vectors of $X_{\alpha_1}$ are independent, so $\lambda^i = 0$ for all $i$. Thus $A \in \mathcal{A}(R, S)$.

Zorn's Lemma gives a maximal element $T \in \mathcal{A}(R, S)$ with $R \subset T \subset S$ and $T$ linearly independent. To show $T$ generates $E$, take arbitrary $x \in E$. Then $T \cup \{x\}$ must be linearly dependent (otherwise $T \cup \{x\} \in \mathcal{A}(R, S)$, contradicting maximality). Hence there is a non-trivial relation
$$\lambda x + \sum_\nu \lambda^\nu x_\nu = 0, \quad x_\nu \in T.$$
Since $T$ is independent, $\lambda \neq 0$, so
$$x = -\sum_\nu \lambda^{-1} \lambda^\nu x_\nu.$$
Thus $T$ generates $E$ and is a basis.
