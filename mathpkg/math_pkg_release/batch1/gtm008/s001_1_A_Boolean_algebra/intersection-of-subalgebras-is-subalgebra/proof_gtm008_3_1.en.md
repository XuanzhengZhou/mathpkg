---
role: proof
locale: en
of_concept: intersection-of-subalgebras-is-subalgebra
source_book: gtm008
source_chapter: "3"
source_section: "1"
---

*Proof.* Left to the reader. The theorem follows directly from Definition 3.2 (subalgebra).

Since each $B_a$ is a subalgebra of $B$, we have $|B_a| \subseteq |B|$ for all $a \in I$, with the operations $+$, $\cdot$, $-$ in $B_a$ being restrictions of those in $B$, and $0,1$ being the same distinguished elements.

For the intersection $B' = \langle \bigcap_{a \in I} |B_a|, +, \cdot, -, 0, 1 \rangle$:

1. If $x, y \in \bigcap_{a \in I} |B_a|$, then $x, y \in |B_a|$ for every $a \in I$. Since each $B_a$ is a subalgebra, $x + y$, $x \cdot y$, and $-x$ belong to $|B_a|$ for every $a$, hence to the intersection. Thus $B'$ is closed under the operations.

2. Since $0, 1 \in |B_a|$ for every $a \in I$, we have $0, 1 \in \bigcap_{a \in I} |B_a|$.

Therefore $B'$ is a subalgebra of $B$.

For the $\sigma$-algebra part: if each $B_a$ is a $\sigma$-algebra, then for any countable $A \subseteq \bigcap_{a \in I} |B_a|$, we have $A \subseteq |B_a|$ for each $a$. By the $\sigma$-algebra property, $\sum_{a \in A} a \in |B_a|$ and $\prod_{a \in A} a \in |B_a|$ for each $a$, hence both belong to the intersection. Thus $B'$ is also a $\sigma$-algebra. $\square$
