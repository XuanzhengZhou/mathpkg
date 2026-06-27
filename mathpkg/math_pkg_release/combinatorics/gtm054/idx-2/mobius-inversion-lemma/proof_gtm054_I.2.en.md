---
role: proof
locale: en
of_concept: mobius-inversion-lemma
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

\begin{align*}
\sum_{T \in \mathcal{P}(V)} (-1)^{|S+T|}[S, T][T, W]
&= \sum_{T \in \mathcal{P}(V)} (-1)^{|S+T|}[S + T, S + W][S, W] \quad \text{by E3} \\
&= \sum_{R \in \mathcal{P}(V)} (-1)^{|R|}[R, S + W][S, W] \quad \text{(let $R = S + T$; as $T$ ranges over all supersets of $S$, $R$ ranges over all subsets)} \\
&= \left[ \sum_{R \in \mathcal{P}(S+W)} (-1)^{|R|} \right][S, W] \quad \text{(since $[R, S+W] = 0$ unless $R \subseteq S+W$)} \\
&= 0^{|S+W|}[S, W] \quad \text{by C22: $\sum_{R \subseteq X} (-1)^{|R|} = 0^{|X|}$} \\
&= 0^{|S+W|}.
\end{align*}

The last equality holds because $[S, W] \in \{0, 1\}$ and $0^{|S+W|}$ is either $0$ or $1$; when $S = W$, $0^{|S+W|} = 0^0 = 1$ and $[S, W] = 1$; when $S \neq W$, $|S+W| > 0$ so $0^{|S+W|} = 0$.
