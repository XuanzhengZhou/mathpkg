---
role: proof
locale: en
of_concept: complete-ideal-is-principal
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** If $I$ is a complete ideal, then since $I \subseteq I$, we have $\sum_{a \in I} a \in I$ by completeness. Let $b = \sum_{a \in I} a$. Then $(\forall a \in I)[a \leq b]$, so $I \subseteq [b]$. Conversely, since $b \in I$, every $x \leq b$ satisfies $x = xb \in I$ (by ideal property 3). Thus $[b] \subseteq I$, and $I = [b]$ is principal.
