---
role: proof
locale: en
of_concept: epsilon-relation-is-not-a-set
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Epsilon-Relation is Not a Set

PROOF If $E \in u$, then $\{E\} \in u$ and $(E, \{E\}) \in E$. Recall that $(x,y) = \{\{x\}\{xy\}\}$ and, if $(x,y)$ is a set, $z \in (x,y)$ iff $z = \{x\}$ or $z = \{xy\}$. Consequently $E \in \{E\} \in \{\{E\}\{E\}\}\in E$. But if $a \in b \in c \in a$, then, upon application of the axiom of regularity to $\{x: x = a \text{ or } x = b \text{ or } x = c\}$, a contradiction results.

An informal discussion of the structure of the first few ordinals may be conceptually enlightening.* The first ordinal will be 0, the next $1 = 0 \cup \{0\}$, the next $2 = 1 \cup \{1\}$, and the next $3 = 2 \cup \{2\}$. Observe 0 is the only member of 1, that 0 and 1 are the only members of 2, and 0, 1, and 2 are the only members of 3. Each ordinal preceding 3 is not only a member but also a subset of 3. Ordinals are defined so that this very special sort of structure results.
