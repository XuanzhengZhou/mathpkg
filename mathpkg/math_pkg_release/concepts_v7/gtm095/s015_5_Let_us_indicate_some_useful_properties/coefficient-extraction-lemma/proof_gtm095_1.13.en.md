---
role: proof
locale: en
of_concept: coefficient-extraction-lemma
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of the Coefficient Extraction Lemma

## Statement

Let $N(r; n)$ be the number of nonnegative integer-valued solutions $(X_1, \ldots, X_n)$ of

$$X_1 + \cdots + X_n = r$$

subject to the constraints $X_j \in \{k_j^{(1)}, k_j^{(2)}, \ldots\}$ for $j = 1, \ldots, n$, where $0 \leq k_j^{(1)} < k_j^{(2)} < \cdots \leq r$.

Define the generating functions encoding the allowed values of each variable:

$$A_j(x) = x^{k_j^{(1)}} + x^{k_j^{(2)}} + \cdots, \qquad j = 1, \ldots, n.$$

Then $N(r; n)$ equals the coefficient of $x^r$ in the expansion of the product

$$A(x) = A_1(x) \cdots A_n(x).$$

## Proof

Consider the product

$$A(x) = \left(x^{k_1^{(1)}} + x^{k_1^{(2)}} + \cdots\right) \cdots \left(x^{k_n^{(1)}} + x^{k_n^{(2)}} + \cdots\right).$$

When we multiply out the expressions in parentheses, each term in the expansion is formed by choosing one monomial $x^{k_j^{(i_j)}}$ from each factor $A_j(x)$. The resulting term is

$$x^{k_1^{(i_1)} + k_2^{(i_2)} + \cdots + k_n^{(i_n)}}.$$

The exponent of $x$ in this term equals $r$ precisely when

$$k_1^{(i_1)} + k_2^{(i_2)} + \cdots + k_n^{(i_n)} = r.$$

Each such choice $(k_1^{(i_1)}, \ldots, k_n^{(i_n)})$ corresponds bijectively to a solution $(X_1, \ldots, X_n)$ of the equation $X_1 + \cdots + X_n = r$ with $X_j \in \{k_j^{(1)}, k_j^{(2)}, \ldots\}$.

Therefore the coefficient of $x^r$ in $A(x)$ counts exactly the number of valid solutions, i.e., $N(r; n)$.

## Special case: no constraints

When each $X_j$ can take any nonnegative integer value (i.e., $\{k_j^{(1)}, k_j^{(2)}, \ldots\} = \{0, 1, 2, \ldots\}$), we have

$$A_j(x) = 1 + x + x^2 + \cdots = \frac{1}{1 - x}, \qquad j = 1, \ldots, n.$$

Hence

$$A(x) = \left(\frac{1}{1 - x}\right)^n = (1 - x)^{-n}.$$

The binomial expansion for negative integer exponent gives

$$(1 - x)^{-n} = \sum_{r \geq 0} \binom{n+r-1}{r} x^r.$$

Thus

$$\boxed{N(r; n) = \binom{n+r-1}{r}},$$

which recovers the classical stars-and-bars formula from elementary combinatorics. $\square$
