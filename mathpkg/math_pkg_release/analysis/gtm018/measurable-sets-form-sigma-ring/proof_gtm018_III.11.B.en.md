---
role: proof
locale: en
of_concept: measurable-sets-form-sigma-ring
source_book: gtm018
source_chapter: "III"
source_section: "11"
---

Replacing $E$ and $F$ in the definition of $\mu^*$-measurability for the case of a disjoint union, we see that

$$\mu^*(A \cap (E_1 \cup E_2)) = \mu^*(A \cap E_1) + \mu^*(A \cap E_2).$$

It follows by mathematical induction that

$$\mu^*(A \cap \bigcup_{i=1}^{n} E_i) = \sum_{i=1}^{n} \mu^*(A \cap E_i)$$

for every positive integer $n$. If we write

$$F_n = \bigcup_{i=1}^{n} E_i, \quad n = 1, 2, \cdots,$$

then it follows from Theorem A that

$$\mu^*(A) = \mu^*(A \cap F_n) + \mu^*(A \cap F_n') \geq$$

$$\geq \sum_{i=1}^{n} \mu^*(A \cap E_i) + \mu^*(A \cap E').$$

Since this is true for every $n$, we obtain

$$\mu^*(A) \geq \sum_{i=1}^{\infty} \mu^*(A \cap E_i) + \mu^*(A \cap E') \geq$$

$$\geq \mu^*(A \cap E) + \mu^*(A \cap E').$$

The reverse inequality, $\mu^*(A) \leq \mu^*(A \cap E) + \mu^*(A \cap E')$, is an automatic consequence of the subadditivity of $\mu^*$. Hence equality holds and $E \in \bar{\mathbf{S}}$, which proves that $\bar{\mathbf{S}}$ is a $\sigma$-ring.

Taking $A = E$ in the above inequality yields $\mu^*(E) = \sum_{n=1}^{\infty} \mu^*(E_n)$, proving the countable additivity formula.
