---
role: proof
locale: en
of_concept: cantor-set
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
\textbf{Closed:} $C = \bigcap F_n$ is an intersection of closed sets (each $F_n$ is a finite union of closed intervals), hence $C$ is closed.

\textbf{Nowhere dense:} Each $F_n$ consists of $2^n$ intervals of length $1/3^n$. For any $n$, $F_n$ contains no interval longer than $1/3^n$. Since $C \subset F_n$, $C$ also contains no interval longer than $1/3^n$ for any $n$, so $C$ contains no interval at all. Hence $C$ is nowhere dense.

\textbf{Nullset:} The sum of the lengths of the intervals composing $F_n$ is $(2/3)^n$. For any $\varepsilon > 0$, choose $n$ large enough so that $(2/3)^n < \varepsilon$. Then $C \subset F_n$ and the total length of the intervals in $F_n$ is less than $\varepsilon$. Hence $C$ is a nullset.

\textbf{Uncountable:} Each $x \in (0, 1]$ has a unique non-terminating binary development $x = 0.x_1 x_2 x_3 \dots$. Define $y_i = 2x_i$; then $0.y_1 y_2 y_3 \dots$ is the ternary development (with $y_i \in \{0, 2\}$, so $y_i \neq 1$) of some point $y \in C$. This correspondence, extended by mapping $0 \mapsto 0$, defines a one-to-one map from $[0, 1]$ onto a proper subset of $C$. Therefore $\operatorname{card}(C) \geq \mathfrak{c}$. Since $C \subset [0, 1]$, we have $\operatorname{card}(C) = \mathfrak{c}$.
