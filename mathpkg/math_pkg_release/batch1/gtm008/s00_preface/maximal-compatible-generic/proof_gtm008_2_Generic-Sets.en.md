---
role: proof
locale: en
of_concept: maximal-compatible-generic
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** If there exists $p \notin G$ such that $G \cup \{p\}$ is compatible, define $S = [p] \cup \{q \mid \neg \text{Comp}(p, q)\}$. Then $S$ is dense in $P$: for any $r \in P$, either $r$ is compatible with $p$ (in which case there exists $s \leq r, p$, and $s \in [p] \subseteq S$), or $r$ is incompatible with $p$ (in which case $r \in S$). Moreover $S \in M$. By genericity, $G \cap S \neq 0$. But $G \cap \{q \mid \neg \text{Comp}(p, q)\} = 0$ (since $p$ is compatible with everything in $G$), so $G \cap [p] \neq 0$, meaning some $q \in G$ satisfies $q \leq p$. Since $G$ is upward-closed, $p \in G$, contradiction. Thus $G$ is maximally compatible.
