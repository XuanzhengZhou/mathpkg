---
role: proof
locale: en
of_concept: probability-measure-properties
source_book: gtm095
source_chapter: "1"
source_section: "5"
---

# Proof of Elementary Properties of Probability

Let $(\Omega, \mathcal{A}, \mathrm{P})$ be a discrete probability space with a finite set $\Omega = \{\omega_1, \ldots, \omega_N\}$ and $\mathcal{A}$ the algebra of all subsets of $\Omega$. The probability measure $\mathrm{P}$ is defined by assigning nonnegative numbers $p(\omega_i)$ to each outcome $\omega_i$ such that $\sum_{i=1}^N p(\omega_i) = 1$, with $\mathrm{P}(A) = \sum_{\omega_i \in A} p(\omega_i)$ for any $A \in \mathcal{A}$.

The following properties follow directly from this definition (axiom (4) in the text):

**1. $\mathrm{P}(\emptyset) = 0$.**

Since the empty set contains no sample points, the sum over an empty index set is zero:
$$\mathrm{P}(\emptyset) = \sum_{\omega_i \in \emptyset} p(\omega_i) = 0.$$

**2. $\mathrm{P}(\Omega) = 1$.**

By the normalization condition on the probabilities of sample points:
$$\mathrm{P}(\Omega) = \sum_{i=1}^N p(\omega_i) = 1.$$

**3. $\mathrm{P}(A \cup B) = \mathrm{P}(A) + \mathrm{P}(B) - \mathrm{P}(A \cap B)$.**

Write $A \cup B = A \cup (B \setminus A)$ and $B = (A \cap B) \cup (B \setminus A)$, where both unions are disjoint. By finite additivity:
$$\mathrm{P}(A \cup B) = \mathrm{P}(A) + \mathrm{P}(B \setminus A),$$
$$\mathrm{P}(B) = \mathrm{P}(A \cap B) + \mathrm{P}(B \setminus A).$$

Eliminating $\mathrm{P}(B \setminus A)$ yields:
$$\mathrm{P}(A \cup B) = \mathrm{P}(A) + \mathrm{P}(B) - \mathrm{P}(A \cap B).$$

**4. If $A \cap B = \emptyset$, then $\mathrm{P}(A + B) = \mathrm{P}(A) + \mathrm{P}(B)$.**

This is the special case of property 3 when $A \cap B = \emptyset$, giving $\mathrm{P}(A \cap B) = 0$. Here $A + B$ denotes the disjoint union $A \cup B$ with $A \cap B = \emptyset$. By finite additivity of the probability measure on disjoint events:
$$\mathrm{P}(A + B) = \sum_{\omega_i \in A \cup B} p(\omega_i) = \sum_{\omega_i \in A} p(\omega_i) + \sum_{\omega_i \in B} p(\omega_i) = \mathrm{P}(A) + \mathrm{P}(B).$$

**5. $\mathrm{P}(\overline{A}) = 1 - \mathrm{P}(A)$.**

Since $\Omega = A + \overline{A}$ is a disjoint union, applying property 4:
$$\mathrm{P}(\Omega) = \mathrm{P}(A) + \mathrm{P}(\overline{A}).$$
Using property 2, $\mathrm{P}(\Omega) = 1$, which gives:
$$\mathrm{P}(\overline{A}) = 1 - \mathrm{P}(A).$$
