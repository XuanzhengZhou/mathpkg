---
role: proof
locale: en
of_concept: lemma-generating-function-counting-solutions
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of the Lemma on Counting Solutions via Generating Functions

## Statement

Let $N(r; n)$ be the number of nonnegative integer-valued solutions $(X_1, \ldots, X_n)$ of

$$X_1 + \cdots + X_n = r$$

subject to constraints $X_j \in \{k_j^{(1)}, k_j^{(2)}, \ldots\}$, $j = 1, \ldots, n$, where $0 \leq k_j^{(1)} < k_j^{(2)} < \cdots \leq r$. Define the generating functions

$$A_j(x) = x^{k_j^{(1)}} + x^{k_j^{(2)}} + \cdots, \qquad j = 1, \ldots, n.$$

Then $N(r; n)$ equals the coefficient of $x^r$ in the expansion of $A(x) = A_1(x) \cdots A_n(x)$.

## Proof

Consider the product

$$A(x) = A_1(x) A_2(x) \cdots A_n(x).$$

When expanding this product, each term arises by selecting one summand $x^{k_j^{(i_j)}}$ from each factor $A_j(x)$. The product of these selected monomials is

$$x^{k_1^{(i_1)}} \cdot x^{k_2^{(i_2)}} \cdots x^{k_n^{(i_n)}} = x^{k_1^{(i_1)} + k_2^{(i_2)} + \cdots + k_n^{(i_n)}}.$$

The exponent equals $r$ exactly when

$$k_1^{(i_1)} + k_2^{(i_2)} + \cdots + k_n^{(i_n)} = r.$$

Each tuple $(k_1^{(i_1)}, \ldots, k_n^{(i_n)})$ satisfying this equation corresponds to exactly one solution $(X_1, \ldots, X_n)$ of the original Diophantine equation, and conversely every solution corresponds to a unique choice of terms in the product expansion. Thus, the number of terms $x^r$ appearing in the expansion of $A(x)$ is precisely $N(r; n)$. In other words, $N(r; n)$ is the coefficient of $x^r$ in $A(x)$.

## The unrestricted case

In the important special case where there are no constraints on the $X_j$ (i.e., each $X_j$ can be any nonnegative integer), we have

$$A_j(x) = 1 + x + x^2 + \cdots = \sum_{k=0}^{\infty} x^k = \frac{1}{1-x}, \qquad j = 1, \ldots, n.$$

Therefore

$$A(x) = \left(\frac{1}{1-x}\right)^n = \frac{1}{(1-x)^n}.$$

Using the binomial series expansion

$$\frac{1}{(1-x)^n} = \sum_{r=0}^{\infty} \binom{n+r-1}{r} x^r,$$

we extract the coefficient of $x^r$ to obtain the well-known formula

$$\boxed{N(r; n) = \binom{n+r-1}{r}}.$$

This is the number of ways to distribute $r$ indistinguishable objects into $n$ distinguishable bins, also known as the stars-and-bars formula. $\square$
