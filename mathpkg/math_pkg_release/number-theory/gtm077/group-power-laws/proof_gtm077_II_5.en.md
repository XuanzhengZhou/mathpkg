---
role: proof
locale: en
of_concept: group-power-laws
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Laws of Exponents in Groups (Theorem 18)

**Theorem 18.** For any element $A$ of a group $\mathfrak{G}$ and any integers $m, n$, the following power laws hold:

1. $A^{m+n} = A^m \cdot A^n = A^n \cdot A^m$,
2. $(A^m)^{-1} = (A^{-1})^m =: A^{-m}$,
3. $A^0 = E$.

*Proof.* We first define the powers of $A$ for positive exponents. For a positive integer $m$, $A^m$ is defined as the product of $m$ factors, each equal to $A$:

$$A^m = \underbrace{A \cdot A \cdots A}_{m \text{ factors}}.$$

This definition is made precise by the recursive rule for group products given earlier in the section.

**1. Addition of exponents.** Let $m, n$ be positive integers. Using the generalized associative law (the Lemma proved in this section), the product of $m+n$ copies of $A$ can be regrouped as the product of $m$ copies followed by $n$ copies:

$$A^{m+n} = \underbrace{A \cdots A}_{m+n} = (\underbrace{A \cdots A}_{m}) \cdot (\underbrace{A \cdots A}_{n}) = A^m \cdot A^n.$$

Since the same regrouping can be done in the opposite order, we also have $A^{m+n} = A^n \cdot A^m$. Hence for positive $m, n$,

$$A^{m+n} = A^m \cdot A^n = A^n \cdot A^m.$$

**2. Negative exponents and the inverse.** Consider $A^m$ and $(A^{-1})^m$ for a positive integer $m$. Forming their product and using the generalized associative law together with $A \cdot A^{-1} = A^{-1} \cdot A = E$ repeatedly, we obtain

$$A^m \cdot (A^{-1})^m = \underbrace{(A \cdots A)}_{m} \cdot \underbrace{(A^{-1} \cdots A^{-1})}_{m} = E.$$

Indeed, one can successively cancel adjacent pairs $A \cdot A^{-1} = E$ from the inside outward. Therefore $(A^{-1})^m$ is the inverse of $A^m$, i.e.,

$$(A^{-1})^m = (A^m)^{-1}.$$

We denote this common element by $A^{-m}$:

$$A^{-m} := (A^{-1})^m = (A^m)^{-1}.$$

**3. Zero exponent.** For completeness, we define

$$A^0 := E,$$

the unit element of the group.

With these definitions, the power laws extend to all integers $m, n$ (not just positive ones). The relations $A^{m+n} = A^m \cdot A^n$, $(A^m)^n = A^{mn}$, and $A^{-m} = (A^m)^{-1}$ hold for all integers $m, n$, as can be verified by case analysis on the signs of the exponents. $\square$
