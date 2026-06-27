---
role: proof
locale: en
of_concept: lemma-c28-semimodular-lattice-chain
source_book: gtm054
source_chapter: "X"
source_section: "49"
---

**Proof.** (a) We proceed by induction on $|U|$. The result holds if $|U| \leq 2$. If it is not the case that $x = 0$ and $y = 1$, then since $L_{[x,y]}$ is semimodular, all maximal chains in $L_{[x,y]}$ have the same length. Now consider maximal chains $0 = x_0, \ldots, x_h = 1$ and $0 = y_0, \ldots, y_k = 1$ in $L$. If $x_1 \neq y_1$, let $z = x_1 \vee y_1$. Since both $x_1$ and $y_1$ are successors of $0$, $z$ must be a successor of both $x_1$ and $y_1$. By the induction hypothesis applied to $L_{[x_1,1]}$ and $L_{[y_1,1]}$, the maximal chains in each have the same length, and the result follows.

(b) If $x$ is an atom and $x \not\leq y$, then by semimodularity, since $0$ is covered by $x$ (as $x$ is an atom), the element $x \vee y$ covers $y$. Thus $x \vee y$ is a successor of $y$.
