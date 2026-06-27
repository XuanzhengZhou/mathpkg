---
role: proof
locale: en
of_concept: unique-readability-formulas
source_book: gtm037
source_chapter: "2"
source_section: "2.2"
---

The proposition follows by an argument entirely similar to the unique readability theorem for terms (Proposition 10.9). The key is that the set of formulas is defined inductively, and the operations used to build formulas have the property that they produce expressions with distinct initial symbols: an equality formula begins with a term (which begins with a variable or operation symbol), a relational formula begins with $\langle R \rangle$, a negation begins with $\neg$, a disjunction is parenthesized and begins with $($, a conjunction is parenthesized, and a universal quantification begins with $\forall$. These syntactic differences make the parsing unambiguous.

The recursiveness of $g^{+*} \operatorname{Fmla}$ follows because one can effectively parse an expression by examining its initial segment: check which of the six forms it matches, then recursively verify that the constituent subexpressions are formulas. The uniqueness guarantees that only one parse is possible, and the recursion terminates since proper subexpressions are strictly shorter.
