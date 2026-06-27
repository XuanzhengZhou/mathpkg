---
role: proof
locale: en
of_concept: well-ordering-property
source_book: gtm030
source_chapter: "Chapter I: Basic Concepts"
source_section: "1-4"
---

Let $S$ be the given set and $M$ the set of natural numbers $m$ that satisfy $m \leq s$ for every $s \in S$. Clearly $1 \in M$. If $s$ is a particular element in $S$, then $s^+ > s$, hence $s^+ \notin M$. Thus $M \neq P$. By the principle of induction (Peano's axiom 4), there exists a natural number $\ell$ such that $\ell \in M$ but $\ell^+ \notin M$. We claim $\ell$ is the least element of $S$. Indeed, $\ell \leq s$ for every $s \in S$ by definition of $M$. Moreover, $\ell \in S$, for otherwise $\ell < s$ for every $s \in S$, which would imply $\ell^+ \leq s$ for every $s \in S$, contradicting $\ell^+ \notin M$. Hence $\ell$ is the required least element.
