---
role: proof
locale: en
of_concept: semigroup-with-insoluble-word-problem
source_book: gtm022
source_chapter: "X"
source_section: "2"
---

The semigroup presentation is constructed from the Turing machine $M$: generators include the symbols $s_j$, state symbols $q_i$, an end marker $e$, and possibly extra symbols. Relations encode the machine transitions. By Lemma 2.8, special words $w, w'$ with $w'$ terminal are equivalent iff there is a forward computation path. Thus the word problem for this presentation solves the halting problem for $M$ on inputs coding natural numbers. Since $E$ is non-recursive, the word problem is insoluble.
