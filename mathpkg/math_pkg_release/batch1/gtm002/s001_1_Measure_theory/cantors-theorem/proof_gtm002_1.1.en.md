---
role: proof
locale: en
of_concept: cantors-theorem
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
Let $I_1$ be a closed subinterval of $I$ such that $a_1 \notin I_1$. Let $I_2$ be a closed subinterval of $I_1$ such that $a_2 \notin I_2$. Proceeding inductively, let $I_n$ be a closed subinterval of $I_{n-1}$ such that $a_n \notin I_n$. The nested sequence of closed intervals $I_n$ has a non-empty intersection. If $p \in \bigcap I_n$, then $p \in I$ and $p \neq a_n$ for every $n$.

To make the choices definite, one may use the following rule: divide $I_{n-1}$ into three subintervals of equal length and take for $I_n$ the first one of these that does not contain $a_n$. If $I_0$ is taken to be the closed interval, this rule determines a definite sequence of closed intervals $I_n$ with non-empty intersection.
