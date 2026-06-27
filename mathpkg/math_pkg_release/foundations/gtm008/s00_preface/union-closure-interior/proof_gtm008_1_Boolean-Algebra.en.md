---
role: proof
locale: en
of_concept: union-closure-interior
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.**

1. Since $A \subseteq A \cup B$ and $B \subseteq A \cup B$, we have $A^- \subseteq (A \cup B)^-$ and $B^- \subseteq (A \cup B)^-$. Therefore $(A^- \cup B^-) \subseteq (A \cup B)^-$.

For the reverse inclusion, let $x \in (A \cup B)^-$ and $x \notin A^-$. Then $(\forall N(x))[N(x) \cap (A \cup B) \neq 0]$ and $(\exists N'(x))[N'(x) \cap A = 0]$. Then $(\forall N(x))(\exists N'(x))[N(x) \cap N'(x) \cap A = 0 \land (N(x) \cap N'(x)) \cap (A \cup B) \neq 0]$. Hence $(\forall N(x))[N(x) \cap B \neq 0]$, so $x \in B^-$. Thus $(A \cup B)^- \subseteq (A^- \cup B^-)$, and equality follows.

2. $x \in (A^0 \cap B^0) \leftrightarrow [\exists N(x) \subseteq A] \land [\exists N'(x) \subseteq B] \leftrightarrow \exists N(x) \subseteq A \cap B \leftrightarrow x \in (A \cap B)^0$.
