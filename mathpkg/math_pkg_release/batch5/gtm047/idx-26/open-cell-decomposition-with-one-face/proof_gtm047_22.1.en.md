---
role: proof
locale: en
of_concept: open-cell-decomposition-with-one-face
source_book: gtm047
source_chapter: "22"
source_section: "1"
---

Let $K$ be a finite triangulation of the compact connected $2$-manifold $M$. Consider finite sequences $\sigma_1, \sigma_2, \ldots, \sigma_n$ of $2$-faces of $K$ such that:
\begin{enumerate}
  \item[(a)] the $2$-faces $\sigma_i$ are all distinct, and
  \item[(b)] $\sigma_{i+1}$ has an edge $e_i$ in common with $\bigcup_{j \leqslant i} \sigma_j$.
\end{enumerate}

Since $K$ is finite, there exists a finite sequence satisfying (a) and (b) that is maximal with respect to these properties. By maximality:
\begin{enumerate}
  \item[(c)] if $\sigma$ is a $2$-face of $K$ with $\sigma \neq \sigma_i$ for all $i$, then $\sigma$ has no edge in common with $\bigcup_{i \leqslant n} \sigma_i$.
\end{enumerate}

It follows that $\bigcup_{i \leqslant n} \sigma_i$ contains either all or none of each set $\operatorname{Int}|\operatorname{St} v|$ for vertices $v \in K^0$. Since $|K| = M$ is connected, we must have $\bigcup_{i \leqslant n} \sigma_i = M$.

Define
$$C^2 = \bigcup_{i=1}^{n} \operatorname{Int} \sigma_i \cup \bigcup_{i=1}^{n-1} \operatorname{Int} e_i.$$

Rewriting,
$$C^2 = \operatorname{Int} \sigma_1 \cup \operatorname{Int} e_1 \cup \operatorname{Int} \sigma_2 \cup \cdots \cup \operatorname{Int} e_{n-1} \cup \operatorname{Int} \sigma_n.$$

Then $C^2$ is homeomorphic to $\operatorname{Int} \sigma_1$, i.e., an open $2$-cell. Let the edges and vertices of $\mathcal{C}$ be the edges and vertices of $K$ that lie in the boundary of $C^2$. Then $\mathcal{C}$ is the desired open cell-decomposition with exactly one $2$-face $C^2$, and every edge of $\mathcal{C}$ is an edge of $K$.
