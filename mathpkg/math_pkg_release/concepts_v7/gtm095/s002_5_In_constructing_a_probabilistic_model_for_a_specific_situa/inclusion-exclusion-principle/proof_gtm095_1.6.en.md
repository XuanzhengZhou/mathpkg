---
role: proof
locale: en
of_concept: inclusion-exclusion-principle
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of the Inclusion-Exclusion Principle

**Problem 5 (Section 6).** For events $A_1, \ldots, A_n$ in a discrete probability space, let
$$S_r = \sum_{1 \leq i_1 < \cdots < i_r \leq n} \mathrm{P}(A_{i_1} \cap \cdots \cap A_{i_r}), \quad r = 1, \ldots, n.$$
Also let
$$B_m = \{\omega : \omega \text{ belongs to exactly } m \text{ of the events } A_1, \ldots, A_n\}.$$
Show that:
$$\mathrm{P}(B_m) = \sum_{r=m}^{n} (-1)^{r-m} \binom{r}{m} S_r, \quad m = 1, \ldots, n.$$

In particular, the probability that at least one of the events occurs is
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) = \mathrm{P}(B_1) + \cdots + \mathrm{P}(B_n) = S_1 - S_2 + \cdots + (-1)^{n-1} S_n. \tag{*}$$

Formula (*) is the **inclusion-exclusion principle** (also called the Poincaré formula).

**Proof.** The proof proceeds by induction on $n$.

**Base case $n = 2$.** For two events $A$ and $B$, we have the disjoint decomposition
$$A \cup B = A \cup (B \setminus A), \quad B = (A \cap B) \cup (B \setminus A).$$
By finite additivity:
$$\mathrm{P}(A \cup B) = \mathrm{P}(A) + \mathrm{P}(B \setminus A),$$
$$\mathrm{P}(B) = \mathrm{P}(A \cap B) + \mathrm{P}(B \setminus A).$$
Eliminating $\mathrm{P}(B \setminus A)$ yields
$$\mathrm{P}(A \cup B) = \mathrm{P}(A) + \mathrm{P}(B) - \mathrm{P}(A \cap B) = S_1 - S_2.$$

**Inductive step.** Assume the formula holds for $n-1$ events. Write
$$\bigcup_{i=1}^{n} A_i = \left(\bigcup_{i=1}^{n-1} A_i\right) \cup A_n.$$
Applying the base case with $A = \bigcup_{i=1}^{n-1} A_i$ and $B = A_n$:
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) = \mathrm{P}\left(\bigcup_{i=1}^{n-1} A_i\right) + \mathrm{P}(A_n) - \mathrm{P}\left(\left(\bigcup_{i=1}^{n-1} A_i\right) \cap A_n\right).$$

By the distributive law, $\left(\bigcup_{i=1}^{n-1} A_i\right) \cap A_n = \bigcup_{i=1}^{n-1} (A_i \cap A_n)$. Applying the induction hypothesis to the $n-1$ events $A_i \cap A_n$:
$$\mathrm{P}\left(\bigcup_{i=1}^{n-1} (A_i \cap A_n)\right) = \sum_{i=1}^{n-1} \mathrm{P}(A_i \cap A_n) - \sum_{i<j}^{n-1} \mathrm{P}(A_i \cap A_j \cap A_n) + \cdots$$

Substituting and using the induction hypothesis for $\mathrm{P}\left(\bigcup_{i=1}^{n-1} A_i\right)$:
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) = \left[\sum_{i=1}^{n-1} \mathrm{P}(A_i) - \sum_{i<j}^{n-1} \mathrm{P}(A_i \cap A_j) + \cdots\right] + \mathrm{P}(A_n) - \left[\sum_{i=1}^{n-1} \mathrm{P}(A_i \cap A_n) - \sum_{i<j}^{n-1} \mathrm{P}(A_i \cap A_j \cap A_n) + \cdots\right].$$

Collecting terms of equal order gives
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} \mathrm{P}(A_i) - \sum_{1 \leq i < j \leq n} \mathrm{P}(A_i \cap A_j) + \cdots + (-1)^{n-1} \mathrm{P}(A_1 \cap \cdots \cap A_n).$$

This completes the induction.

**Formula for $\mathrm{P}(B_m)$.** The probability that an outcome belongs to exactly $m$ events can be derived by indicator method. Let $I_i(\omega) = 1$ if $\omega \in A_i$ and $0$ otherwise. Then $\mathbf{1}_{B_m}(\omega)$ is the indicator that $\sum I_i = m$. Using generating functions:
$$\mathbf{1}_{B_m} = \sum_{r=m}^{n} (-1)^{r-m} \binom{r}{m} \sum_{i_1 < \cdots < i_r} \mathbf{1}_{A_{i_1} \cap \cdots \cap A_{i_r}}.$$
Taking expectations yields the claimed formula for $\mathrm{P}(B_m)$.
