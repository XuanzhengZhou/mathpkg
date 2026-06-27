---
role: proof
locale: en
of_concept: power-laws-in-a-group
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Power Laws in a Group

**Theorem.** For any element $A$ of a group $\mathfrak{G}$ and any integers $m, n$, the following computation rules for powers hold:

$$A^{m+n} = A^m \cdot A^n = A^n \cdot A^m, \qquad A^{-m} = (A^m)^{-1}, \qquad A^0 = E.$$

*Proof.* Let $E$ denote the unit element of $\mathfrak{G}$. We define powers inductively:

- For $m = 1$: $A^1 = A$.
- For positive $m > 1$: $A^m = A^{m-1} \cdot A$ (a product of $m$ copies of $A$).
- $A^0 = E$.
- For negative $m$: $A^m = (A^{-1})^{-m}$, where $A^{-1}$ is the inverse of $A$.

**Positive exponents.** Let $m, n > 0$. By the generalized associative law, the product of $m+n$ copies of $A$ can be partitioned into a block of $m$ copies followed by a block of $n$ copies:

$$A^{m+n} = \underbrace{A \cdot A \cdots A}_{m+n} = (\underbrace{A \cdots A}_{m}) \cdot (\underbrace{A \cdots A}_{n}) = A^m \cdot A^n.$$

Commuting the two blocks (which is valid since all factors are the same element $A$), we also obtain $A^{m+n} = A^n \cdot A^m$.

**Negative exponents.** For $m > 0$, the product $A^m \cdot (A^{-1})^m$ consists of $m$ factors of $A$ followed by $m$ factors of $A^{-1}$. Using the generalized associative law and the defining property $A \cdot A^{-1} = E$, successive cancellation yields:

$$\begin{aligned}
A^m \cdot (A^{-1})^m &= (A \cdot A \cdots A) \cdot (A^{-1} \cdot A^{-1} \cdots A^{-1}) \\
&= (A \cdot A \cdots A \cdot A^{-1}) \cdot (A^{-1} \cdots A^{-1}) \\
&= \cdots = A \cdot A^{-1} = E.
\end{aligned}$$

Thus $(A^{-1})^m$ is the inverse of $A^m$, i.e. $(A^{-1})^m = (A^m)^{-1}$. We denote this common element by $A^{-m}$:

$$A^{-m} := (A^{-1})^m = (A^m)^{-1}.$$

**Extension to all integers.** With the definitions $A^0 = E$ and $A^{-m} = (A^{-1})^m$ for $m > 0$, the rules $A^{m+n} = A^m \cdot A^n$ and $(A^m)^{-1} = A^{-m}$ hold for all integers $m, n$, which can be verified by checking the cases where one or both exponents are zero or negative. $\square$
