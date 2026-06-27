---
role: proof
locale: en
of_concept: associativity-and-inverse-of-subset-multiplication-in-topological-group
source_book: gtm027
source_chapter: "3"
source_section: "S"
---

# Proof of Associativity and Inverse of Subset Multiplication in Topological Groups

**Statement.** If $X$, $Y$, and $Z$ are subsets of a group $G$, then

$$
(X \cdot Y) \cdot Z = X \cdot (Y \cdot Z)
$$

and

$$
(X \cdot Y)^{-1} = Y^{-1} \cdot X^{-1}.
$$

**Proof.** The subset product is defined by $A \cdot B = \{a \cdot b : a \in A,\; b \in B\}$, and $A^{-1} = \{a^{-1} : a \in A\}$.

**Associativity.** By definition,

$$
(X \cdot Y) \cdot Z = \{ (x \cdot y) \cdot z : x \in X,\; y \in Y,\; z \in Z \}.
$$

Since the group operation is associative, $(x \cdot y) \cdot z = x \cdot (y \cdot z)$ for all $x \in X$, $y \in Y$, $z \in Z$. Hence

$$
(X \cdot Y) \cdot Z = \{ x \cdot (y \cdot z) : x \in X,\; y \in Y,\; z \in Z \} = X \cdot (Y \cdot Z).
$$

**Inverse of product.** By definition,

$$
(X \cdot Y)^{-1} = \{ (x \cdot y)^{-1} : x \in X,\; y \in Y \}.
$$

In any group, $(x \cdot y)^{-1} = y^{-1} \cdot x^{-1}$. Therefore

$$
(X \cdot Y)^{-1} = \{ y^{-1} \cdot x^{-1} : x \in X,\; y \in Y \}.
$$

Now $Y^{-1} = \{ y^{-1} : y \in Y \}$ and $X^{-1} = \{ x^{-1} : x \in X \}$, so

$$
Y^{-1} \cdot X^{-1} = \{ y^{-1} \cdot x^{-1} : y \in Y,\; x \in X \} = (X \cdot Y)^{-1}.
$$

Both identities follow directly from the corresponding properties of the underlying group $G$. The topology of $G$ plays no role in these purely algebraic facts. ∎
