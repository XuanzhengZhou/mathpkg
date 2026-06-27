---
role: proof
locale: en
of_concept: theorem-order-completeness
source_book: gtm027
source_chapter: "0"
source_section: "Orderings"
---

# Proof of Theorem 9: Equivalence of Upper and Lower Bound Completeness

Suppose that $X$ is order-complete (relative to the ordering $<$) and that $A$ is a non-void subset which has a lower bound. Let $B$ be the set of all lower bounds for $A$. Then $B$ is non-void and surely every member of the non-void set $A$ is an upper bound for $B$. Hence $B$ has a least upper bound, say, $b$. Then $b$ is less than or equal to each upper bound of $B$, and in particular $b$ is less than or equal to each member of $A$, and hence $b$ is a lower bound of $A$. On the other hand, $b$ is itself an upper bound of $B$; that is, $b$ is greater than or equal to each lower bound of $A$. Hence $b$ is a greatest lower bound (infimum) of $A$.

The converse proposition may be proved by the same sort of argument, or, directly, one may apply the result just proved to the relation inverse to $<$. Explicitly: if every non-void subset with a lower bound has an infimum, then given a non-void subset $A$ with an upper bound, consider the set $B$ of all upper bounds of $A$. Reversing the order (i.e., working with the inverse relation), $B$ is precisely the set of lower bounds of $A$ under the inverse order, and the argument above yields a supremum for $A$. Thus order-completeness with respect to upper bounds is entirely equivalent to order-completeness with respect to lower bounds.
