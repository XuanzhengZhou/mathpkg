---
role: exercise
locale: en
chapter: "1"
section: "027"
exercise_number: 2
---

Exercise 1 raises the question whether a “familiar presentation” of a category $C$ in Struct(Set) can be recovered from the isomorphism class of $C$ in Struct(Set).

(a) Show that a standard presentation of “abelian group” can be recovered. [Hint: The object $Z$ of integers is distinguished by the facts that it admits infinitely many endomorphisms and is such that whenever $A$ admits a monomorphism into $Z$ then either $A$ is an initial object or $A$ admits an isomorphism to $Z$; define an element of $A$ to be a map from $Z$ to $A$; for any $A$ the canonical map $A + A \longrightarrow A \times A$ is an isomorphism and the map $A \times A = A + A \longrightarrow A$ which is the identity of $A$ preceded by each coproduct injection defines addition of elements.]

The hint in (a) achieved much more than was required since it used only the category and not the underlying set functor. Consider:

(b) Show that a standard presentation of “monoid” can be recovered. [Hint: Since $U: C \longrightarrow \text{Set}$ is given, the required $n$-ary operations will be natural transformations $U^n \longrightarrow U$; there are only two 2-ary operations which are not constant and are associative (because each such operation is a word on two symbols containing say $n$ occurrences of the first and $m$ of the second, and the equations imposed on $n$ and $m$ by associativity are very restrictive—it is perfectly valid to reason first in the “standard” category so long as all transits under isomorph
