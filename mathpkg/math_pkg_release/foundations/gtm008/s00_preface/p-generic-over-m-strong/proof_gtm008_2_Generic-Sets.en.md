---
role: proof
locale: en
of_concept: p-generic-over-m-strong
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** If $a, b \in G$ and $S = \{c \in P \mid [c \leq a \land c \leq b] \lor [\neg \text{Comp}(c, a) \land \neg \text{Comp}(c, b)]\}$, then $S \in M$ (by definability in $M$) and $S$ is dense in $P$. Indeed, for any $c \in P$, either $(\exists x \leq c)[\neg \text{Comp}(x, a) \lor \neg \text{Comp}(x, b)]$, in which case $[c] \cap S \neq 0$; or $(\forall x \leq c)[\text{Comp}(x, a) \land \text{Comp}(x, b)]$, in which case $c$ itself is compatible with both $a$ and $b$. Since $S \in M$ and $S$ is dense, $G \cap S \neq 0$ by genericity. Since $a, b \in G$ and $G$ is compatible, we cannot have the second disjunct, so there exists $c \in G$ with $c \leq a$ and $c \leq b$.
