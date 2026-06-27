---
role: proof
locale: en
of_concept: first-countable-nonopen-set
source_book: gtm027
source_chapter: "2"
source_section: "Sequences and Subsequences"
---

# Proof of Characterization of Non-Open Sets via Sequences

**Theorem 8(b).** Let $X$ be a topological space satisfying the first axiom of countability. Then a subset $A$ of $X$ is open if and only if no sequence in $X \sim A$ converges to a point of $A$.

*Proof.* If $A$ is a subset of $X$ which is not open, then there is a sequence in $X \sim A$ which converges to a point of $A$. To see this, let $s \in A$ be a point such that no neighborhood of $s$ is contained in $A$ (such a point exists because $A$ is not open). Then $s$ is an accumulation point of $X \sim A$. By part (a) of the theorem, there exists a sequence in $(X \sim A) \sim \{s\} \subset X \sim A$ converging to $s$. Such a sequence surely fails to be eventually in $A$.

Conversely, if there is a sequence in $X \sim A$ converging to a point $s \in A$, then $s$ is in the closure of $X \sim A$ but not in the interior of $A$, so $A$ cannot be open. $\square$
