---
role: proof
locale: en
of_concept: zero-one-law-for-baire-tail-sets
source_book: gtm002
source_chapter: "21"
source_section: "The Extended Principle of Duality"
---

Suppose that $E$ is a tail set with the property of Baire and that $E$ is not residual.

Since $E$ has the property of Baire, $X - E$ can be written as $X - E = G \triangle P$, where $G$ is open and $P$ is of first category. Because $E$ is not residual, $X - E$ is not of first category, so $G$ is non-empty.

The space $X$ is the product $\prod_{i=1}^{\infty} \{0,1\}$ with the product topology. Let $X^n = \prod_{i=1}^{n} \{0,1\}$ and $Y^n = \prod_{i=n+1}^{\infty} \{0,1\}$. Basic open sets in $X$ have the form $U = A_n \times Y^n$ where $A_n \subseteq X^n$.

Since $G$ is open, it is a countable union of such basic open sets. Because $G$ is non-empty, it contains a set $U = A_n \times Y^n$ with $A_n$ non-empty.

Since $E$ is a tail set, it can be written as $E = X^n \times B_n$ for some $B_n \subseteq Y^n$.

Now compute the intersection:
$$U \cap E = (A_n \times Y^n) \cap (X^n \times B_n) = A_n \times B_n.$$

On the other hand,
$$A_n \times B_n = U \cap E \subseteq G \cap E.$$

But $G \subseteq (X - E) \cup P$, so
$$G \cap E \subseteq [(X - E) \cup P] \cap E = P \cap E \subseteq P.$$

Therefore $A_n \times B_n \subseteq P$, so $A_n \times B_n$ is of first category.

Now $A_n$ is a non-empty subset of the finite discrete space $X^n$. A finite discrete space is of second category (it is a Baire space with the discrete topology). By Theorem 15.3 (the Kuratowski-Ulam theorem), if $A_n \times B_n$ is of first category in $X^n \times Y^n$ and $A_n$ is of second category in $X^n$, then $B_n$ must be of first category in $Y^n$.

Thus $B_n$ is of first category in $Y^n$, and consequently
$$E = X^n \times B_n$$
is of first category in $X$.

This completes the proof: any tail set $E$ with the property of Baire is either residual or of first category. $\square$
