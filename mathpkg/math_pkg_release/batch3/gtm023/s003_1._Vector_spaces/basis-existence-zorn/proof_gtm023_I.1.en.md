---
role: proof
locale: en
of_concept: basis-existence-zorn
source_book: gtm023
source_chapter: "I"
source_section: "§1. Vector spaces"
---

Consider the set $\mathcal{A}(R, S)$ consisting of all subsets $X$ of $E$ such that $R \subset X \subset S$ and the vectors of $X$ are linearly independent. The set $\mathcal{A}(R, S)$ is partially ordered by inclusion.

Let $\{X_{\alpha}\}$ be a chain in $\mathcal{A}(R, S)$. Set $A = \bigcup_{\alpha} X_{\alpha}$. We verify that $A \in \mathcal{A}(R, S)$. Clearly $R \subset A \subset S$. To check linear independence, suppose
$$\sum_{v=1}^{n} \lambda^{v} x_{v} = 0, \quad x_{v} \in A.$$
For each $i$, $x_i \in X_{\alpha}$ for some $\alpha$. Since $\{X_{\alpha}\}$ is a chain, we may assume all
$$x_i \in X_{\alpha_1} \quad (i = 1, \ldots, n).$$
Since the vectors of $X_{\alpha_1}$ are linearly independent, it follows that $\lambda^{v} = 0$ ($v = 1, \ldots, n$), whence $A \in \mathcal{A}(R, S)$.

Now Zorn's lemma implies there is a maximal element $T$ in $\mathcal{A}(R, S)$. Then $R \subset T \subset S$ and the vectors of $T$ are linearly independent. To show that $T$ is a system of generators, let $x \in E$ be arbitrary. Then the vectors $T \cup \{x\}$ are linearly dependent — otherwise $T \cup \{x\} \in \mathcal{A}(R, S)$, contradicting the maximality of $T$. Hence there is a non-trivial relation
$$\lambda x + \sum_{v} \lambda^{v} x_{v} = 0, \quad \lambda, \lambda^{v} \in \Gamma, \; x_{v} \in T.$$

Since the vectors of $T$ are linearly independent, $\lambda \neq 0$, whence
$$x = -\sum_{v} \lambda^{-1} \lambda^{v} x_{v} = \sum_{v} \alpha^{v} x_{v}.$$

This shows that $T$ generates $E$, so $T$ is a basis of $E$.
