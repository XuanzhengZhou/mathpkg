---
role: proof
locale: en
of_concept: criterion-for-distributive-law-via-zero-constant-sum
source_book: gtm008
source_chapter: "18"
source_section: "Model Theoretic Consequences of the Distributive Laws"
---

We show that this criterion implies the $(I, J)$-DL. Let $\{b_{ij} \mid i \in I \land j \in J\} \subseteq B$ be given.

Define:
$$
b = \prod_{i \in I} \sum_{j \in J} b_{ij} - \sum_{f \in J^I} \prod_{i \in I} b_{i, f(i)},
$$
and set:
$$
a_{ij} = b \cdot b_{ij} \quad \text{for } i \in I, \; j \in J.
$$

By Theorem 4.2, it suffices to prove that $b = 0$.

We compute:
$$
\sum_{j \in J} a_{ij} = b \cdot \sum_{j \in J} b_{ij}
= \sum_{j \in J} b_{ij} \cdot \left( \prod_{i' \in I} \sum_{j' \in J} b_{i'j'} - \sum_{f \in J^I} \prod_{i' \in I} b_{i', f(i')} \right) = b.
$$

Moreover, for any $f \in J^I$, we have:
$$
\prod_{i \in I} a_{i, f(i)} = 0.
$$

Thus the family $\{a_{ij}\}$ satisfies the hypotheses of the criterion: all products along selection functions vanish, and all row sums equal the constant $b$. By the criterion, $b = 0$, which verifies the $(I, J)$-DL.
