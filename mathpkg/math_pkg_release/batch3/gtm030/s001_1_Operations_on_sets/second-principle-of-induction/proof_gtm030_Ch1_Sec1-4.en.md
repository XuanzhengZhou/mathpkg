---
role: proof
locale: en
of_concept: second-principle-of-induction
source_book: gtm030
source_chapter: "Chapter I: Basic Concepts"
source_section: "1-4"
---

Let $F$ be the set of elements $r$ such that $E(r)$ is not true. If $F$ is not vacuous, then by the well-ordering property (O4), $F$ contains a least element $\ell$. For all $s < \ell$, $s \notin F$, so $E(s)$ is true. By hypothesis, $E(\ell)$ must then be true, contradicting $\ell \in F$. Hence $F$ is vacuous and $E(n)$ is true for all $n$.
