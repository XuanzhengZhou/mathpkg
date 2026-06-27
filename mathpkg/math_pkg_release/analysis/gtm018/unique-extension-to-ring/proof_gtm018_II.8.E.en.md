---
role: proof
locale: en
of_concept: unique-extension-to-ring
source_book: gtm018
source_chapter: "II"
source_section: "8"
---

We know that every set $E$ in $\mathbf{R}$ may be represented as a finite, disjoint union of sets in $\mathbf{P}$. Suppose that

$$E = \bigcup_{i=1}^{n} E_i \quad \text{and} \quad E = \bigcup_{j=1}^{m} F_j$$

are two such representations of the same set $E$. Then, for each $i = 1, \dots, n$,

$$E_i = \bigcup_{j=1}^{m} (E_i \cap F_j)$$

is a representation of the set $E_i$ in $\mathbf{P}$ as a finite, disjoint union of sets in $\mathbf{P}$, and therefore, since $\mu$ is finitely additive,

$$\sum_{i=1}^{n} \mu(E_i) = \sum_{i=1}^{n} \sum_{j=1}^{m} \mu(E_i \cap F_j) = \sum_{j=1}^{m} \mu(F_j).$$

We define $\bar{\mu}(E) = \sum_{i=1}^{n} \mu(E_i)$ where $\{E_1, \cdots, E_n\}$ is a finite, disjoint class of sets in $\mathbf{P}$ whose union is $E$.

It is clear from its definition that the function $\bar{\mu}$ thus defined coincides with $\mu$ on $\mathbf{P}$ and is finitely additive. Since any function satisfying these conditions must in particular be finitely additive when the terms of the union to be formed are in $\mathbf{P}$, it is also clear that $\bar{\mu}$ is unique. The only non trivial thing left to prove is that $\bar{\mu}$ is countably additive.

Let $\{E_i\}$ be a disjoint sequence of sets in $\mathbf{R}$ whose union, $E$, is also in $\mathbf{R}$; then each $E_i$ is a finite, disjoint union of sets in $\mathbf{P}$,

$$E_i = \bigcup_j E_{ij} \text{ and } \bar{\mu}(E_i) = \sum_j \mu(E_{ij}).$$

If $E \in \mathbf{P}$, then, since the class of all $E_{ij}$ is countable and disjoint, it follows from the countable additivity of $\mu$ that

$$\bar{\mu}(E) = \mu(E) = \sum_i \sum_j \mu(E_{ij}) = \sum_i \bar{\mu}(E_i).$$

In the general case $E$ is a finite, disjoint union of sets in $\mathbf{P}$,

$$E = \bigcup_k F_k,$$

and, using the result just obtained, we have

$$\bar{\mu}(E) = \sum_k \bar{\mu}(F_k) = \sum_k \sum_i \bar{\mu}(E_i \cap F_k) = \sum_i \sum_k \bar{\mu}(E_i \cap F_k) = \sum_i \bar{\mu}(E_i).$$
