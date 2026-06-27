---
role: proof
locale: en
of_concept: intersection-of-open-configurations-is-open
source_book: gtm006
source_chapter: "XI"
source_section: "1"
---

**Proof of Lemma 11.1.**

(i) Let $\{A_a\}$ be a collection of open sub-configurations of $C$, and let $A = \bigcap_a A_a$. Suppose, for contradiction, that $A$ is not open. Then $A$ contains a confined sub-configuration $B$. Since $B < A$, we have $B < A_a$ for every $a$. But each $A_a$ is open, meaning none of its sub-configurations is confined — contradicting that $B$ is confined. Hence $A$ must be open.

(ii) Let $\{A_a\}$ be a collection of confined sub-configurations of $C$, and let $A = \bigcup_a A_a$. Take any element $e$ (point or line) of $A$. Then $e$ belongs to some particular $A_{a_0}$. Since $A_{a_0}$ is confined, $e$ has at least three incidences within $A_{a_0}$, and therefore certainly has at least three incidences within $A = \bigcup_a A_a$. Thus every element of $A$ is incident with at least three elements, so $A$ is confined. $\square$
