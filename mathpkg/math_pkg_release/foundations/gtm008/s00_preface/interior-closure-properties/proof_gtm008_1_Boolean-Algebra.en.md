---
role: proof
locale: en
of_concept: interior-closure-properties
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.**

1. $x \in A^0 \rightarrow \exists N(x) \subseteq A \rightarrow x \in A$. Also $x \in A \rightarrow (\forall N(x))[N(x) \cap A \neq 0] \rightarrow x \in A^-$.

2. $x \in A^0 \rightarrow \exists N(x) \subseteq A \rightarrow (\exists N(x))[x \in (N(x) \cap A^0) \land (N(x) \cap A^0) \in T \land (N(x) \cap A^0) \subseteq A^0] \rightarrow x \in A^{00}$. Since by (1), $A^{00} \subseteq A^0$, we have $A^{00} = A^0$. The proof for $A^{--} = A^-$ is dual.

4. $x \in (X - A)^- \iff (\forall N(x))[N(x) \cap (X - A) \neq 0] \iff (\forall N(x))[N(x) \not\subseteq A] \iff x \notin A^0 \iff x \in X - A^0$. And $x \in (X - A)^0 \iff \exists N(x) \subseteq (X - A) \iff (\exists N(x))[N(x) \cap A = 0] \iff x \notin A^- \iff x \in X - A^-$.
