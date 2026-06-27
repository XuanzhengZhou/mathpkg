---
role: proof
locale: en
of_concept: bayes-formula
source_book: gtm095
source_chapter: "1"
source_section: "3"
---

# Proof of Bayes' Formula

Let $\{A_1, \ldots, A_n\}$ be a complete set of disjoint events (a partition of the sample space) with $P(A_i) > 0$ for all $i$, and let $B$ be an event with $P(B) > 0$.

By the definition of conditional probability,

$$P(A_i \mid B) = \frac{P(A_i B)}{P(B)}.$$

The numerator can be rewritten using the multiplication formula for probabilities:

$$P(A_i B) = P(B \mid A_i) \, P(A_i).$$

The denominator can be expanded using the formula for total probability over the partition $\{A_1, \ldots, A_n\}$:

$$P(B) = \sum_{j=1}^{n} P(B \mid A_j) \, P(A_j).$$

Substituting these two expressions back into the conditional probability yields **Bayes' formula**:

$$P(A_i \mid B) = \frac{P(A_i) \, P(B \mid A_i)}{\sum_{j=1}^{n} P(A_j) \, P(B \mid A_j)}.$$

The probabilities $P(A_i)$ are called the *prior* (or *a priori*) probabilities, and the conditional probabilities $P(A_i \mid B)$ are called the *posterior* (or *a posteriori*) probabilities after the occurrence of event $B$.
