---
role: proof
locale: en
of_concept: inclusion-exclusion-probability-form
source_book: gtm095
source_chapter: "1"
source_section: "14"
---

# Proof of Inclusion–Exclusion Principle for Probabilities

Assume $\Omega$ is a finite sample space with $N(\Omega) < \infty$, and equiprobable outcomes. Under the **classical definition of probability**, the probability of an event $A \subseteq \Omega$ is:

$$P(A) = \frac{N(A)}{N(\Omega)}.$$

The general inclusion–exclusion formula for cardinalities of $n$ sets $A_1, \dots, A_n \subseteq \Omega$ states:

$$N\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} N(A_i) - \sum_{1 \leq i < j \leq n} N(A_i \cap A_j) + \cdots + (-1)^{n+1} N(A_1 \cap \cdots \cap A_n).$$

Divide both sides of this equality by $N(\Omega)$:

$$\frac{N\!\left(\bigcup_{i=1}^{n} A_i\right)}{N(\Omega)} = \sum_{i=1}^{n} \frac{N(A_i)}{N(\Omega)} - \sum_{1 \leq i < j \leq n} \frac{N(A_i \cap A_j)}{N(\Omega)} + \cdots + (-1)^{n+1} \frac{N(A_1 \cap \cdots \cap A_n)}{N(\Omega)}.$$

By the classical definition, each ratio $N(\cdot)/N(\Omega)$ is exactly the probability of the corresponding event. Hence:

$$P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i) - \sum_{1 \leq i < j \leq n} P(A_i \cap A_j) + \cdots + (-1)^{n+1} P(A_1 \cap \cdots \cap A_n).$$

In compact notation, with $T = \{1, 2, \dots, n\}$:

$$P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{\varnothing \neq S \subseteq T} (-1)^{|S|+1} \, P\!\left(\bigcap_{i \in S} A_i\right).$$

The same division-by-$N(\Omega)$ argument applies to all four forms of the inclusion–exclusion theorem (union, intersection of complements, etc.), showing that every cardinality formula has an exact probability counterpart under the classical model.
