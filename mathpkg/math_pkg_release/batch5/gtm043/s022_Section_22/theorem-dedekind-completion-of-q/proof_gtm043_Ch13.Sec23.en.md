---
role: proof
locale: en
of_concept: theorem-dedekind-completion-of-q
source_book: gtm043
source_chapter: "13"
source_section: "23"
---

Obviously, $R \supset Q$. To show $R$ is Dedekind-complete, consider any bounded subset $A$, and let $s = \sup A$ in $s$. Then either $s \in R$, or $s^+$ is the supremum of $A$ in $R$. Next, since $R$ contains no lower elements, Lemma 13.19(a) implies that between any two elements of $R$ there lies an element of $Q$. Clearly, no proper subset of $R$ containing $Q$ is Dedekind-complete. Therefore $R$ is the Dedekind completion of $Q$.

For cardinality: $|s| = 2^{\aleph_1}$. The set $s - R - \{0, 1\}$ of all lower elements is in one-one correspondence with $Q$, so $|s - R| = |Q| \leq |R|$. From $s = (s - R) \cup R$, we obtain $|s| \leq |R| + |R| = |R|$. Therefore $|R| = |s| = 2^{\aleph_1}$.
