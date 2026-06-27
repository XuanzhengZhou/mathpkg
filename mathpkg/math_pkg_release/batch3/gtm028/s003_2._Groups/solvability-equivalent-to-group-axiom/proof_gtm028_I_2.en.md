---
role: proof
locale: en
of_concept: solvability-equivalent-to-group-axiom
source_book: gtm028
source_chapter: "I"
source_section: "2. Groups"
---

Assume $G$ satisfies $G_1$ (non-empty) and $G_2$ (associativity), and that both equations $ax = b$ and $xa = b$ are solvable for all $a, b \in G$.

We fix an element $c \in G$ and denote by $e$ a solution of the equation $xc = c$ (so $ec = c$). Now let $a$ be any element of $G$. Let $b$ be a solution of the equation $cx = a$ (so $cb = a$). Then we compute:
$$ea = e(cb) = (ec)b = cb = a.$$
This establishes $G_3(1)$: $e$ is a left identity for all elements of $G$.

As to $G_3(2)$, it is an immediate consequence of the solvability of the equation $xa = e$: for each $a \in G$, there exists $a' \in G$ such that $a'a = e$, which is precisely the existence of inverses.

Conversely, if $G_3$ holds (i.e., $G$ is a group), then we have already shown that the equations $ax = b$ and $xa = b$ have unique solutions, namely $x = a^{-1}b$ and $x = ba^{-1}$ respectively.
