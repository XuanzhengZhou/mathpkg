---
role: proof
locale: en
of_concept: inclusion-exclusion-three-sets
source_book: gtm095
source_chapter: "1"
source_section: "14"
---

# Proof of Inclusion–Exclusion Principle for Three Sets

Let $\Omega$ be a finite set and $A, B, C \subseteq \Omega$. Denote by $N(D)$ the cardinality of a finite set $D$.

Extending the reasoning used for two sets, consider the sum $N(A) + N(B) + N(C)$. Elements belonging to exactly one of the three sets are counted once (correct). Elements belonging to exactly two sets are counted twice, and elements belonging to all three sets are counted three times.

To correct for double-counting of pairwise intersections, we subtract $N(AB) + N(AC) + N(BC)$. After this subtraction:
- Elements in exactly one set are still counted once.
- Elements in exactly two sets are now counted $2 - 1 = 1$ time (correct).
- Elements in all three sets were counted 3 times in the sum, then subtracted 3 times (once for each pair), resulting in a count of $0$.

Therefore, we must add back the triple intersection $N(ABC)$ to correctly count the elements in all three sets. This yields:

$$N(A \cup B \cup C) = \bigl[N(A) + N(B) + N(C)\bigr] - \bigl[N(AB) + N(AC) + N(BC)\bigr] + N(ABC).$$

The three groups of terms correspond respectively to **inclusion** (singletons), **exclusion** (pairs), and **inclusion** (triple).

Equivalently, using the notation $S_k = \sum_{1 \leq i_1 < \cdots < i_k \leq n} N(A_{i_1} \cap \cdots \cap A_{i_k})$ for $n = 3$:

$$N(A \cup B \cup C) = S_1 - S_2 + S_3.$$

The complementary formula for the set of elements belonging to none of $A, B, C$ is obtained via De Morgan's laws and the formula above:

$$N(\overline{A} \, \overline{B} \, \overline{C}) = N(\Omega) - \bigl[N(A) + N(B) + N(C)\bigr] + \bigl[N(AB) + N(AC) + N(BC)\bigr] - N(ABC).$$
