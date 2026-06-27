---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma establishes that the class of Turing computable functions is closed under the scheme of primitive recursion without parameters. Given a Turing machine $M$ that computes a binary function $f$ and a base value $a$, one can construct a Turing machine that computes the function $g$ defined by $g(0) = a$ and $g(n+1) = f(n, g(n))$. This closure property is essential for showing that every primitive recursive (and hence every general recursive) function is Turing computable.
