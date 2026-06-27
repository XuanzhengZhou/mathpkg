---
role: proof
locale: en
of_concept: constructible-function-piecewise-rational
source_book: gtm053
source_chapter: "4"
source_section: "4.4"
---

An easy analysis of constructible sets and constructible functions (those with constructible graphs) yields the result.

By Chevalley's theorem, the graph $\Gamma(f) = \{(\bar{x}, y) \in V \times F : y = f(\bar{x})\}$ is a Boolean combination of zero-sets of polynomials. Consider the projection of $\Gamma(f)$ onto the coordinate axes and the algebraic relations that define it. Since constructible sets are quantifier-free definable, the condition $y = f(\bar{x})$ is described by a Boolean combination of polynomial equations.

By decomposing the domain $V$ according to which combinations of equations and inequations hold, one obtains a finite constructible partition. On each piece $V_i$, the function value $f(\bar{x})$ is characterized as one of finitely many algebraic functions. Over characteristic zero, the primitive element theorem and elimination theory imply that on each piece the function is given by a rational expression.

The explicit form is: there exist polynomials $P_i, Q_i$ such that for $\bar{x} \in V_i$, $Q_i(\bar{x}) \neq 0$ and $f(\bar{x}) = P_i(\bar{x}) / Q_i(\bar{x})$.
