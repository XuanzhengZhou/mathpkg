---
role: proof
locale: en
of_concept: characterization-of-orthogonal-matroids-via-1-sets
source_book: gtm054
source_chapter: "X"
source_section: "D"
---

Let $\mathcal{N} = \mathcal{M}(\mathcal{A})$. First we prove that $(V, \mathcal{A})$ satisfies condition B15. We will actually prove the stronger result: if $(A_1, A_2, y)$ is an admissible triple for $(V, \mathcal{A})$, then there exists $A \in \mathcal{A}$ such that $y \in A \subseteq (A_1 \cup A_2) \setminus \{y\}$.

Take $B \in \mathcal{B}(\Lambda^\perp)$ and define $\Theta = \Lambda_{V \setminus B}^\perp$. One shows that $B \in \mathcal{B}(\Theta^\perp)$. For each $x \in B$, there exists $N_x \in \mathcal{M}(\Theta)$ with $N_x \cap B = \{x\}$. We then verify $N_x \in \mathcal{A}$.

If $\varnothing \subset N' \subset N_x$, one easily verifies that $|N' \cap M_v| = 1$ for some $v \in N_x \setminus \{x\}$. Hence $N_x$ is a minimal set in $\mathcal{A}$; i.e., $N_x \in \mathcal{N}$.

Let $N \in \mathcal{N}$ and let $v \in N$. If $V \setminus B \supseteq N$, then $N \cap M_v = \{v\}$, contrary to the definition of $\mathcal{N}$. Hence $V \setminus B$ contains no cycle of $\Theta$. Thus $V \setminus B \in \mathcal{I}(\Theta)$. To prove that $V \setminus B$ is a maximal independent set of $\Theta$, we note that for any $x \in B$, we have $N_x \subseteq (V \setminus B) \cup \{x\}$, and we have just shown that $N_x$ is a cycle of $\Theta$. Hence $V \setminus B \in \mathcal{B}(\Theta)$, and so $B \in \mathcal{B}(\Theta^\perp)$.

Let
$$\mathcal{A}' = \{A \in \mathcal{P}(V): |A \cap N| \neq 1 \text{ for all } N \in \mathcal{N}\}$$
and consider the set system $\Phi = (V, \mathcal{N}')$ where $\mathcal{N}' = \mathcal{M}(\mathcal{A}')$. By the above argument, $\Phi$ is a matroid, and every set in $\mathcal{A}'$ is a union of sets in $\mathcal{N}'$. Since $\mathcal{M} \subseteq \mathcal{A}'$, we have $\mathcal{N}' \subseteq \mathcal{M}^\perp$. Moreover, each $M \in \mathcal{M}$ is a union of sets in $\mathcal{N}'$, which forces $\mathcal{N}' = \mathcal{M}^\perp$. Thus $\mathcal{M}^\perp = \mathcal{M}(\mathcal{A})$ as claimed.
