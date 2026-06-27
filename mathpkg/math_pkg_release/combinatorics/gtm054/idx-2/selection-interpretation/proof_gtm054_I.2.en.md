---
role: proof
locale: en
of_concept: selection-interpretation
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

\textbf{(a)} This is the definition of the selection $s$ as the cardinality of the preimage: $s(S) = |f^{-1}[\{S\}]| = |\{e \in E : f(e) = S\}|$.

\textbf{(b)} From the definitions of $\bar{s}$ (E4) and $s$:
$$\bar{s}(S) = \sum_{V \supseteq T \supseteq S} s(T) = \sum_{V \supseteq T \supseteq S} |\{e \in E : f(e) = T\}| = |\{e \in E : f(e) \supseteq S\}|,$$
since the sets $\{e \in E : f(e) = T\}$ for $T \supseteq S$ partition $\{e \in E : f(e) \supseteq S\}$.

\textbf{(c)} By definition of the transpose,
\begin{align*}
s^*(A) &= |\{x \in V : f^*(x) = A\}| \\
&= |\{x \in V : \{e \in E : x \in f(e)\} = A\}| \\
&= |\{x \in V : x \in f(e) \iff e \in A\}|,
\end{align*}
which is precisely the set of vertices belonging to all blocks in $A$ and to no blocks outside $A$.

\textbf{(d)} By definition of $\overline{s^*}$ applied to $s^*$,
$$\bar{s}^*(A) = \sum_{B \supseteq A} s^*(B) = \sum_{B \supseteq A} |\{x \in V : f^*(x) = B\}| = |\{x \in V : f^*(x) \supseteq A\}| = |\{x \in V : x \in f(e) \text{ for all } e \in A\}| = \left|\bigcap_{e \in A} f(e)\right|.$$
