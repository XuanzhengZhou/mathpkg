---
role: proof
locale: en
of_concept: independence-v-neq-l-boolean-models
source_book: gtm008
source_chapter: "19"
source_section: "19"
---

Let $M$ be a countable transitive model of $ZF$ such that $\langle M, \in, B^M \rangle$ is elementarily equivalent to $\langle V, \in, B \rangle$, and let $G$ be $P$-generic over $M$ (where $P$ is the partial order structure in $M$ associated with $B^M$). By Theorem 18.2, since $B$ does not satisfy the $(\omega, 2)$-DL,

$$P(\omega)^M \subsetneq P(\omega)^{M[G]}.$$

If $M[G]$ satisfied $V = L$, then by the absoluteness of $L$ and the minimality of $L$, we would have $M[G] = M$, contradicting the proper inclusion above. Therefore $M[G] \models V \neq L$. By the correspondence between generic extensions and Boolean-valued models (Theorem 14.22 and Corollary 14.23), this implies $\llbracket V \neq L \rrbracket = 1$ in $V^{(B)}$.
