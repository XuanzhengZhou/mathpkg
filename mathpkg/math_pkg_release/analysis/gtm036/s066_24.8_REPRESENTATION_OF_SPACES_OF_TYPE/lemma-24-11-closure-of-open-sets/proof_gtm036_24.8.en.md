---
role: proof
locale: en
of_concept: lemma-24-11-closure-of-open-sets
source_book: gtm036
source_chapter: "24"
source_section: "24.8"
---

Let $U$ be an open set in $X$, let $B$ be the family of all non-negative continuous real functions which are $0$ on $X \sim U$ and are bounded by $1$, and let $f$ be the supremum of the set $B$. Then $f$ is a continuous function which is $1$ on $U$, because for each $s$ in $U$ there is a member of $B$ which assumes the value $1$ at $s$. On the other hand, if $s \notin U^-$, then there is a member of $B$ vanishing on a neighborhood of $s$, so that $f$ is $0$ on $X \sim U^-$. Hence the characteristic function of $U^-$ coincides with $f$ except on the boundary of $U$, which is nowhere dense. Consequently $U^-$ is both open and closed (as $f$ is continuous and takes values $0$ and $1$ on the appropriate sets), and each $m_x$ assigns measure zero to the boundary of any open set. Since the Borel sets of the first category are precisely those contained in a countable union of boundaries of open sets, each $m_x$ vanishes on first-category Borel sets.
