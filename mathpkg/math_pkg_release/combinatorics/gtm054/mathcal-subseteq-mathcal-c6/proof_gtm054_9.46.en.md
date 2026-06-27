---
role: proof
locale: en
of_concept: mathcal-subseteq-mathcal-c6
source_book: gtm054
source_chapter: "9"
source_section: "XC"
---

Assuming (a), we have C1 immediately. Let $U \in \mathcal{P}(V)$ and $x \in V + U$ be given. By definition, clearly $r(U) \leq r(U + \{x\})$. Now pick $J \subseteq U + \{x\}$ such that $|J| = r(U + \{x\})$. If $x \notin J$, then $r(U) = |J|$. If $x \in J$, then $J + \{x\} \in \mathcal{I}$ and $r(U) \geq |J + \{x\}|$. In either case, we have $r(U) \geq |J| - 1 = r(U + \{x\}) - 1$. Thus C2 holds.

To verify C3, let $J$ be a largest set in $\mathcal{I}$ such that $J

Since the bases are the largest sets $B$ such that $r(B) = |B|$, our definition is consistent with the definition of the rank of a matroid as defined in the previous section.

The next result enables us to relate the rank function of a matroid to the cycles of the matroid directly.
