---
role: proof
locale: en
of_concept: left-ideal-quasi-regular-equivalence
source_book: gtm013
source_chapter: "9"
source_section: "15"
---
\textbf{(a) $\Rightarrow$ (b).} Assume (a) and let $x \in I$. Then $x$ is left quasi-regular, so there exists $x' \in R$ such that $x'(1 - x) = 1$. Since $x'x \in I$ is left quasi-regular and $x' = 1 + x'x = 1 - (-x'x)$, there exists $y \in R$ such that $yx' = 1$. But then $x'$ is invertible and $y = 1 - x$. Hence $(1 - x)x' = 1$, so $x$ is quasi-regular.

\textbf{(b) $\Rightarrow$ (c).} Assume (b) and let $K$ be a left ideal of $R$ with $R = I + K$. Then there exist $x \in I$ and $k \in K$ with $1 = x + k$. Thus $k = 1 - x$ is invertible, whence $1 \in K$ and $K = R$.

\textbf{(c) $\Rightarrow$ (a).} Assume (c) and let $x \in I$. Then $Rx \ll R$. But $R = Rx + R(1 - x)$, whence $R(1 - x) = R$, so $1 - x$ has a left inverse.
