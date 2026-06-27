---
role: proof
locale: en
of_concept: regularity-induction
source_book: gtm001
source_chapter: "5"
source_section: "5"
---

Assume that $(\forall x)[x \subseteq A \rightarrow x \in A]$. Let $B = V - A$. Suppose, for contradiction, that $B \neq 0$.

By the strong form of the Axiom of Regularity (Axiom 6'), there exists a set $a$ such that
$$a \in B \land a \cap B = 0.$$

The condition $a \cap B = 0$ means that no element of $a$ belongs to $B$. Equivalently,
$$(\forall y)[y \in a \rightarrow y \notin B].$$

Since $B = V - A$, we have $y \notin B \leftrightarrow y \in A$ (for any $y$). Thus
$$(\forall y)[y \in a \rightarrow y \in A],$$
which means $a \subseteq A$.

By our initial assumption, $a \subseteq A$ implies $a \in A$. But this contradicts $a \in B = V - A$, which requires $a \notin A$.

Therefore $B = 0$, i.e., $V - A = 0$, which by the properties of relative complement means $A = V$.
