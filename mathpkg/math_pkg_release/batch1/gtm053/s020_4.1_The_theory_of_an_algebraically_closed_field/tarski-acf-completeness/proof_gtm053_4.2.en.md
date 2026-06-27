---
role: proof
locale: en
of_concept: tarski-acf-completeness
source_book: gtm053
source_chapter: "4"
source_section: "4.2"
---

In essence the theorem follows from the well-known Steinitz theorem: Given two algebraically closed fields $A$ and $B$ of the same characteristic $p$ and their common subfield $k$,

$$A \cong_k B \text{ if and only if } \operatorname{trd}(A/k) = \operatorname{trd}(B/k),$$

where $\operatorname{trd}$ is the transcendence degree of the field over the subfield, the cardinality of a maximal algebraically independent subset.

The theory is complete because any two models of $\text{ACF}_p$ of the same uncountable cardinality are isomorphic (by Steinitz), and the theory has no finite models, so by the Łoś–Vaught test it is complete.

For quantifier elimination, one considers a sufficiently saturated model. Given two algebraically closed fields $A$ and $B$ of characteristic $p$ with a common subfield $k$ and an isomorphism $\varphi: k \to k'$ between substructures, if $A$ and $B$ are sufficiently saturated, the Steinitz theorem guarantees that $\varphi$ extends to an automorphism of a larger model. When we consider $A = B$, the existence of the automorphism $\pi$ affirms elimination of quantifiers, by Theorem 3.18.
