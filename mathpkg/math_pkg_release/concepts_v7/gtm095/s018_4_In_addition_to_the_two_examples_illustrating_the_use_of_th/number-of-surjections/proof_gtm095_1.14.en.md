---
role: proof
locale: en
of_concept: number-of-surjections
source_book: gtm095
source_chapter: "1"
source_section: "14. Inclusion–Exclusion Principle"
---

# Proof of Number of Surjections Between Finite Sets

Let $A = A(n)$ and $B = B(m)$ be two finite sets with $|A| = n$ and $|B| = m$, where $n \geq m$. A *surjection* (or onto function) $\mathbb{S} : A \to B$ is a function such that every element of $B$ has at least one pre-image in $A$.

To count the number of surjections, we apply the inclusion–exclusion principle. The total number of functions from $A$ to $B$ is $m^n$.

For each $b_i \in B$ ($i = 1, \ldots, m$), let $C_i$ be the set of functions $f : A \to B$ such that $b_i$ is *not* in the image of $f$ (i.e., $f$ "misses" $b_i$). Then the set of surjections is precisely the complement of the union of the $C_i$:

$$N(\mathbb{S}) = N\!\left(\bigcap_{i=1}^{m} \overline{C}_i\right).$$

By inclusion–exclusion,

$$N(\mathbb{S}) = m^n - \sum_{i=1}^{m} N(C_i) + \sum_{1 \leq i < j \leq m} N(C_i \cap C_j) - \cdots + (-1)^m N(C_1 \cap \cdots \cap C_m).$$

For a given set of $i$ indices $\{j_1, \ldots, j_i\} \subseteq \{1, \ldots, m\}$, a function belonging to $C_{j_1} \cap \cdots \cap C_{j_i}$ cannot take any of the $i$ specified values. Its image is restricted to the remaining $m-i$ elements of $B$. Hence

$$N(C_{j_1} \cap \cdots \cap C_{j_i}) = (m-i)^n.$$

The number of $i$-element subsets of $B$ is $\binom{m}{i}$. Therefore, summing over all such subsets,

$$N(\mathbb{S}) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (m-i)^n.$$

This is the required formula. Note that when $n < m$, the sum evaluates to $0$, which is consistent since no surjection exists when the domain is smaller than the codomain.

$\square$
