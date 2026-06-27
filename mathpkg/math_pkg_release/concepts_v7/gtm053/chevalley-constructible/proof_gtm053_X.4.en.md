---
role: proof
locale: en
of_concept: chevalley-constructible
source_book: gtm053
source_chapter: "X"
source_section: "4"
---

# Proof of Chevalley's Theorem (Constructible Sets)

**Theorem 4.3 (Chevalley's Theorem).** Let $F$ be an algebraically closed field. The family of $L_1\mathrm{Ar}$-definable (using parameters) subsets of $F^n$, for all $n$, coincides with the family of constructible subsets. Here, a set is *constructible* if it is a Boolean combination of zero-sets of polynomials (i.e., algebraic sets).

*Proof.* This is a direct translation of the quantifier elimination statement for $\mathrm{ACF}$ (Theorem 4.2).

By quantifier elimination, every $L_1\mathrm{Ar}$-formula $\varphi(\bar{x}, \bar{a})$ with parameters $\bar{a} \in F$ is equivalent modulo $\mathrm{ACF}$ to a quantifier-free formula $\psi(\bar{x}, \bar{a})$. Atomic formulas in the language of fields are of the form $p(\bar{x}, \bar{a}) = 0$, where $p$ is a polynomial with integer coefficients. A quantifier-free formula is therefore a Boolean combination of such atomic formulas, i.e., a Boolean combination of conditions of the form $p(\bar{x}) = 0$ or $p(\bar{x}) \neq 0$.

The set defined by $p(\bar{x}) = 0$ is exactly the zero-set (algebraic set) of the polynomial $p$. The set defined by $p(\bar{x}) \neq 0$ is the complement of a zero-set. Therefore, any quantifier-free definable set is a Boolean combination (union, intersection, complement) of zero-sets — which is precisely the definition of a constructible set.

Conversely, any constructible set is by definition a Boolean combination of zero-sets, and each zero-set $\{\bar{x} : p(\bar{x}) = 0\}$ is defined by an atomic $L_1\mathrm{Ar}$-formula. Hence constructible sets are definable.

The equivalence extends to all $n$: the projection $F^{n+1} \to F^n$ (corresponding to existential quantification) preserves the family of constructible sets, which is exactly what quantifier elimination guarantees. The family of $L_1\mathrm{Ar}$-definable sets is the closure of zero-sets under Boolean operations and projections; since quantifier elimination eliminates the need for projections, the families coincide. $\square$
