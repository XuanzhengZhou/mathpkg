---
role: proof
locale: en
of_concept: recurrent-classes-are-closed-and-maximal
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** It is sufficient to prove that a recurrent class $S'$ is closed, since closed classes are clearly maximal.

Suppose the class can be left, say from a state $j \in S'$. Let $k$ be a state outside $S'$ for which $P_{jk} > 0$. Then it is not true that $R(k,j)$, because $j$ and $k$ do not communicate (they are in different equivalence classes). Thus,
$$\bar{H}_{jj} \leq 1 - P_{jk} < 1,$$
and $j$ is not recurrent, contradicting the hypothesis that $S'$ is a recurrent class. Therefore the class cannot be left, so it is closed.
