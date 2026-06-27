---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Prenex Normal Form Theorem asserts that every first-order formula $\varphi$ is provably equivalent to a formula $\psi$ in prenex normal form (all quantifiers at the front, followed by a quantifier-free matrix), with the additional property that the set of free variables is preserved. The proof proceeds by induction on the structure of $\varphi$, with the critical step being the handling of disjunctions and conjunctions of formulas already in prenex form. This requires renaming bound variables to avoid clashes and then applying quantifier distribution lemmas (such as 10.76) to pull the quantifiers outward. The theorem is fundamental for normal-form reasoning in predicate logic.
