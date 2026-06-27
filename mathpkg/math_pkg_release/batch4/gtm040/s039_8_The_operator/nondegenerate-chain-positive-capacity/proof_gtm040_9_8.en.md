---
role: proof
locale: en
of_concept: nondegenerate-chain-positive-capacity
source_book: gtm040
source_chapter: "9"
source_section: "8"
---
Choose an arbitrary point as the reference state $0$. Then, by Lemma 9-100, there is either a one-point set or a set in $\mathcal{L}_0$ which has non-zero capacity.

If $k(\{1\}) > 0$ for some state, then we may choose $0$ and $1$ as indicated, since $k(E) \geq k(\{1\}) > 0$ if $1 \in E$. If $k(\{1\}) < 0$ for some state, then use $1$ as a new reference point, and $k'(\{0\}) = -k(\{1\}) > 0$. Hence we simply interchange the roles of $0$ and $1$.

Otherwise $k(E) \neq 0$ for some $E \in \mathcal{L}_0$. Then $k(E) > 0$. Let $E$ be a set in $\mathcal{L}_0$ with positive capacity and containing as few states as possible; let $1$ be any state in $E$ other than $0$. Then for any set containing both $0$ and $1$, monotonicity guarantees positive capacity.
