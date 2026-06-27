---
role: proof
locale: en
of_concept: idempotent-transition-independent-trials
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

For an independent trials process, $P_{ij} = p_j$ for all $i$. Compute the two-step transition probability:

$$P_{ij}^{(2)} = \sum_k P_{ik} P_{kj} = \sum_k p_k p_j = p_j \sum_k p_k = p_j \cdot 1 = p_j = P_{ij}.$$

Thus $P^2 = P$. By induction, assume $P^{(n-1)} = P$. Then

$$P_{ij}^{(n)} = \sum_k P_{ik}^{(n-1)} P_{kj} = \sum_k P_{ik} P_{kj} = \sum_k p_k p_j = p_j = P_{ij}.$$

Hence $P^n = P$ for all $n \geq 1$.
