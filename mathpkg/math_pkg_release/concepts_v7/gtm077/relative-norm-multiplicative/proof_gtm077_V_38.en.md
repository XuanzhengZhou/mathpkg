---
role: proof
locale: en
of_concept: relative-norm-multiplicative
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 107: Multiplicativity of the Relative Norm

**Theorem 107 (Multiplicativity).** We have $N_k(\mathfrak{A}\mathfrak{B}) = N_k(\mathfrak{A}) \cdot N_k(\mathfrak{B})$.

**Proof.** This follows directly from the definition of the relative norm of an ideal and the multiplicativity of the conjugation operation. Recall that for an ideal $\mathfrak{A}$ in $K$, the relative norm is defined as

$$N_k(\mathfrak{A}) = \mathfrak{A}^{(1)} \cdot \mathfrak{A}^{(2)} \cdots \mathfrak{A}^{(m)},$$

where $\mathfrak{A}^{(i)}$ denotes the $i$-th relative conjugate ideal (obtained by applying the $i$-th embedding of $K$ over $k$ to each element of $\mathfrak{A}$).

For two ideals $\mathfrak{A}$ and $\mathfrak{B}$ in $K$, the relative conjugate of their product satisfies

$$(\mathfrak{A} \cdot \mathfrak{B})^{(i)} = \mathfrak{A}^{(i)} \cdot \mathfrak{B}^{(i)}.$$

This is obvious because if $\mathfrak{A} = (A_1, \ldots, A_r)$ and $\mathfrak{B} = (B_1, \ldots, B_s)$, then $\mathfrak{A}\mathfrak{B} = (A_i B_j)$ and applying the $i$-th embedding distributes over the products $A_\mu B_\nu$.

Now compute:

$$N_k(\mathfrak{A}\mathfrak{B}) = \prod_{i=1}^{m} (\mathfrak{A}\mathfrak{B})^{(i)} = \prod_{i=1}^{m} \left(\mathfrak{A}^{(i)} \cdot \mathfrak{B}^{(i)}\right) = \left(\prod_{i=1}^{m} \mathfrak{A}^{(i)}\right) \cdot \left(\prod_{i=1}^{m} \mathfrak{B}^{(i)}\right) = N_k(\mathfrak{A}) \cdot N_k(\mathfrak{B}),$$

where we used commutativity of ideal multiplication to regroup the factors.
