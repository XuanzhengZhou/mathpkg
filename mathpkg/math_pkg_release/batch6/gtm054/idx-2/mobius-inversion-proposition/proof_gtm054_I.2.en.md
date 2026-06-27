---
role: proof
locale: en
of_concept: mobius-inversion-proposition
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

Let $S \in \mathcal{P}(V)$. Starting from the right-hand side and using the definition of $\bar{s}$ (E4):

\begin{align*}
\sum_{T \in \mathcal{P}(V)} (-1)^{|S+T|}[S, T]\bar{s}(T)
&= \sum_{T \in \mathcal{P}(V)} (-1)^{|S+T|}[S, T] \sum_{W \in \mathcal{P}(V)} [T, W] s(W) \\
&= \sum_{W \in \mathcal{P}(V)} \left( \sum_{T \in \mathcal{P}(V)} (-1)^{|S+T|}[S, T][T, W] \right) s(W) \\
&= \sum_{W \in \mathcal{P}(V)} 0^{|S+W|} s(W) \quad \text{by Lemma E5} \\
&= 0^{|S+S|} s(S) \quad \text{(all terms with $W \neq S$ vanish)} \\
&= 1 \cdot s(S) = s(S).
\end{align*}

The interchange of summation is justified since all sums are finite ($\mathcal{P}(V)$ is finite). The application of Lemma E5 gives $0^{|S+W|}$ which equals $1$ only when $S = W$ and $0$ otherwise.
