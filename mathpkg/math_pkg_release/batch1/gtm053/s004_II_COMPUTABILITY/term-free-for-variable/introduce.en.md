---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This definition provides the hygiene condition for substituting a term for a variable in a formula. Without this condition, a substitution could inadvertently "capture" a free variable from the term inside the scope of a quantifier, changing the intended meaning. The condition ensures that substitution respects the logical structure of the formula. This is analogous to avoiding variable capture when renaming bound variables in analysis, e.g. renaming $\int_1^x f(y)dy$ to $\int_1^x f(z)dz$ rather than $\int_1^x f(x)dx$.
