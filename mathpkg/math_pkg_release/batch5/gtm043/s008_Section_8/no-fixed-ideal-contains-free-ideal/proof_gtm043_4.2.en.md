---
role: proof
locale: en
of_concept: no-fixed-ideal-contains-free-ideal
source_book: gtm043
source_chapter: "4"
source_section: "4.2"
---

Suppose, for contradiction, that $I$ is a fixed ideal and $J$ is a free ideal with $J \subseteq I$. Since $I$ is fixed, $\bigcap Z[I] \neq \emptyset$; pick $p \in \bigcap Z[I]$. Then every $f \in I$ satisfies $f(p) = 0$. Since $J \subseteq I$, every $g \in J$ also satisfies $g(p) = 0$. But $J$ is free, so by the equivalent characterization of free ideals, there exists some $g \in J$ with $g(p) \neq 0$, a contradiction. Therefore no fixed ideal can contain a free ideal.
