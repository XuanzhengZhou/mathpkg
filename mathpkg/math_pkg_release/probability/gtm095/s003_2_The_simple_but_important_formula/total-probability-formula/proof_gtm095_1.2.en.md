---
role: proof
locale: en
of_concept: total-probability-formula
source_book: gtm095
source_chapter: "1"
source_section: "2"
---

# Proof of the Total Probability Formula

Consider a decomposition $\mathcal{D} = \{A_1, \ldots, A_n\}$ with $P(A_i) > 0$, $i = 1, \ldots, n$ (such a decomposition is often called a complete set of disjoint events). Since the $A_i$ form a partition of the sample space $\Omega$, we have

$$B = B \cap A_1 + B \cap A_2 + \cdots + B \cap A_n,$$

where the sum denotes a union of disjoint events. By the additivity of probability,

$$P(B) = \sum_{i=1}^{n} P(B A_i).$$

Now, by the definition of conditional probability (since $P(A_i) > 0$),

$$P(B A_i) = P(B \mid A_i) \, P(A_i).$$

Substituting this into the sum yields the **formula for total probability**:

$$P(B) = \sum_{i=1}^{n} P(B \mid A_i) \, P(A_i).$$

This formula expresses the probability of an event $B$ as a weighted average of the conditional probabilities $P(B \mid A_i)$, where the weights are the probabilities $P(A_i)$ of the elements of the partition.
