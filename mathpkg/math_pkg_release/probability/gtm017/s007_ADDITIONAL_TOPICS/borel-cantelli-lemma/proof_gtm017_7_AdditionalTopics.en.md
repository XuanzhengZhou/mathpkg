---
role: proof
locale: en
of_concept: borel-cantelli-lemma
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

From the definition $A_i \text{ i.o.} = \bigcap_{n=1}^{\infty} \bigcup_{i=n}^{\infty} A_i$, it follows that for any $n$,
$$A_i \text{ i.o.} \subset \bigcup_{i=n}^{\infty} A_i.$$
By monotonicity and countable subadditivity of the probability measure,
$$P(A_i \text{ i.o.}) \leq P\left(\bigcup_{i=n}^{\infty} A_i\right) \leq \sum_{i=n}^{\infty} P(A_i).$$
If $\sum_{i=1}^{\infty} P(A_i) < \infty$, then the tail sum $\sum_{i=n}^{\infty} P(A_i) \to 0$ as $n \to \infty$. Hence $P(A_i \text{ i.o.}) = 0$.
