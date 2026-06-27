---
role: proof
locale: en
of_concept: d5-matroid-perp-characterization
source_book: gtm054
source_chapter: "X"
source_section: "50"
---

Let $\mathcal{N} = \mathcal{M}(\mathcal{A})$. First, prove that $(V, \mathcal{A})$ satisfies condition B15. We prove the stronger result: if $(A_1, A_2, y)$ is an admissible triple for $(V, \mathcal{A})$, then there exists $A \in \mathcal{A}$ with $y \notin A \subseteq (A_1 \cup A_2) \setminus \{y\}$.

Let $(A_1, A_2, y)$ be admissible. Then there exist $M_1, M_2 \in \mathcal{M}$ such that $A_i \cap M_i = \{x_i\}$ for $i = 1, 2$, where $x_1 \neq x_2$ and $y \in M_1 \cap M_2 \setminus \{x_1, x_2\}$. Since $\mathcal{M}$ is the collection of cycles of a matroid, the strong cycle exchange property implies there exists $M \in \mathcal{M}$ with $x_1 \in M \subseteq (M_1 \cup M_2) \setminus \{y\}$. Set $A = (A_1 \cup A_2) \setminus (M \setminus \{x_1\})$. Then $y \notin A$ and one verifies $A \in \mathcal{A}$.

Thus $(V, \mathcal{A})$ satisfies B15, so $\mathcal{N} = \mathcal{M}(\mathcal{A})$ is a matroid. To show $\mathcal{N} = \mathcal{M}^\perp$, let $N \in \mathcal{M}^\perp$. Then for any $M \in \mathcal{M}$, $|N \cap M| \neq 1$ by definition of $\mathcal{M}^\perp$ as minimal sets meeting each basis, which implies they meet each cycle nontrivially. Hence $N \in \mathcal{A}$. If $N \notin \mathcal{N}$, then $N$ properly contains some $N' \in \mathcal{N} \subseteq \mathcal{A}$. But then $|N' \cap M| \neq 1$ for all $M \in \mathcal{M}$, and by a previous characterization $N'$ contains a set in $\mathcal{M}^\perp$, contradicting minimality of $N$. Thus $\mathcal{M}^\perp \subseteq \mathcal{N}$.

Conversely, suppose $N \in \mathcal{N}$ and $v \in N$. Let $B$ be a basis of $\Lambda^\perp$. If $V \setminus B \supseteq N$, then $N \cap M_v = \{v\}$ (where $M_v$ is the fundamental cycle of $v$ with respect to $B$), contrary to $N \in \mathcal{A}$. Hence $V \setminus B$ contains no cycle of the matroid $\Theta$ whose cycles are $\mathcal{N}$. Thus $V \setminus B \in \mathcal{I}(\Theta)$. One shows $V \setminus B$ is a maximal independent set, so $V \setminus B \in \mathcal{B}(\Theta)$ and $B \in \mathcal{B}(\Theta^\perp)$. Therefore $\mathcal{B}(\Theta^\perp) \subseteq \mathcal{B}(\Lambda^\perp)$, and by matroid duality $\mathcal{N} = \mathcal{M}(\Theta) = \mathcal{M}^\perp$.

For the second assertion, let $\mathcal{A}' = \{A \in \mathcal{P}(V): |A \cap N| \neq 1 \text{ for all } N \in \mathcal{N}\}$ and $\Phi = (V, \mathcal{N}')$ where $\mathcal{N}' = \mathcal{M}(\mathcal{A}')$. By the above argument, $\Phi$ is a matroid and every set in $\mathcal{A}'$ is a union of sets in $\mathcal{N}'$. Since $\mathcal{N} \subseteq \mathcal{A}$ by definition, applying the dual argument yields that each set in $\mathcal{A}$ is a union of sets in $\mathcal{N} = \mathcal{M}^\perp$.
