---
role: proof
locale: en
of_concept: transfinite-induction-comparability
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Comparability of Transfinitely Defined Functions

Proof Since both domain $f$ and domain $h$ are ordinals it may be assumed that domain $f \subset \text{domain } h$ (either this or the reverse inclusion follows from 109) and it remains to be proved that $f(u) = h(u)$ for $u$ in domain $f$. Assuming the contrary, let $u$ be the $E$-first member of domain $f$ such that $f(u) \neq h(u)$. Then $f(v) = h(v)$ for each ordinal $v$ preceding $u$ and hence $f|u = h|u$. Then $f(u) = g(f|u)

ordinal such that $h(z) = g(h|z)$ for $z$ in domain $h$, then $h \subset f$, and if $z \in domain h$, then $f(z) = g(f|z)$.

Finally, suppose $x \in R \sim (domain f)$. Then $f(x) = u$ by theorem 69 and since domain $f$ is a set $f$ is a set (theorem 75). If $g(f|x) = g(f) = u$, then the equality $f(x) = g(f|x)$ follows. Otherwise $g(f)$ is a set (theorem 69 again). In this case if $y$ is the $E$-first member of $R \sim (domain f)$ and $h = f \cup \{(y,g(f))\}$, then the domain of $h$ is an ordinal and $h(z) = g(h|z)$ for $z$ in domain $h$. Hence $h \subset f$ and $y \in domain f$ which is a contradiction. Consequently, $g(f) = u$ and the theorem is proved.

The mechanics of this theorem deserves a little comment. If domain $f$ is not $R$, then $g(f) = u$ and $f(x) = u$ for each ordinal number $x$ such that domain $f \leq x$. If $g(0) = u$, then $f = 0$.

INTEGERS*

In this section the integers are defined and Peano’s postulates are derived as theorems. The real numbers may be constructed from the integers (see Landau [1]) by use of these postulates and the two facts: the class of integers is a set (theorem 138), and it is possible to define a function on the integers by induction (theorem 0.13; this fact may also be derived as a corollary to 128). Another axiom is needed.
