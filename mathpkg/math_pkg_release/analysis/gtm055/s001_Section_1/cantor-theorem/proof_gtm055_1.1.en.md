---
role: proof
locale: en
of_concept: cantor-theorem
source_book: gtm055
source_chapter: "1"
source_section: "1"
---

Suppose, for contradiction, that there exists a surjective mapping $\varphi: X \to \mathcal{P}(X)$. Define the set
$$
A = \{x \in X : x \notin \varphi(x)\}.
$$
Since $A \subset X$, we have $A \in \mathcal{P}(X)$. Because $\varphi$ is surjective, there exists $x_0 \in X$ such that $\varphi(x_0) = A$. Now consider whether $x_0 \in A$:
- If $x_0 \in A$, then by definition of $A$, $x_0 \notin \varphi(x_0) = A$, contradiction.
- If $x_0 \notin A$, then $x_0 \notin \varphi(x_0) = A$, so by definition of $A$, $x_0 \in A$, contradiction.
Thus no such surjection exists, and $\operatorname{card} \mathcal{P}(X) > \operatorname{card} X$.
