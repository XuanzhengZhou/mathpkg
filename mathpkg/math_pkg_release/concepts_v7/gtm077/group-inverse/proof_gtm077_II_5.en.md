---
role: proof
locale: en
of_concept: group-inverse
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Existence and Uniqueness of Inverses (Theorem 17)

**Theorem 17.** For every element $A$ of a group $\mathfrak{G}$, there exists a uniquely determined element $X$, called the *inverse* of $A$ and denoted by $A^{-1}$, such that

$$A \cdot A^{-1} = A^{-1} \cdot A = E,$$

where $E$ is the unit element of $\mathfrak{G}$.

*Proof.* By axiom (iv), applied with $B = E$ (the unit element, whose existence is guaranteed by Theorem 16), there exist elements $X$ and $Y$ in $\mathfrak{G}$ such that

$$AX = E \qquad \text{and} \qquad YA = E.$$

We shall show that $X = Y$, so that $X$ is simultaneously a right inverse and a left inverse of $A$.

Consider the product $YAX$. By the associative law (ii), it may be parenthesized in two ways:

$$YAX = Y(AX) = Y \cdot E = Y,$$
$$YAX = (YA)X = E \cdot X = X.$$

Both expressions represent the same group element, hence $X = Y$.

Thus the element $X$ satisfies both $AX = E$ and $XA = E$. It is therefore a *two-sided inverse* of $A$.

**Uniqueness.** Suppose $X'$ is another element with $AX' = E$. Then

$$X' = E \cdot X' = (YA)X' = Y(AX') = Y \cdot E = Y = X.$$

The same reasoning applied on the other side shows that any left inverse must also equal $Y = X$. Hence the inverse is uniquely determined by $A$.

We denote this unique element by $A^{-1}$. By construction it satisfies

$$A \cdot A^{-1} = A^{-1} \cdot A = E. \quad \square$$
