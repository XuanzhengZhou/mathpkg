---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.2"
proof_technique: zorns-lemma
locale: en
content_hash: ""
written_against: ""
---
Let $X$ be any subset that spans $V$ (e.g., $V$ itself). Partially order the set $S$ of all linearly independent subsets of $X$ by inclusion. Zorn's Lemma implies the existence of a maximal linearly independent subset $Y$ of $X$. Every element of $X$ is a linear combination of elements of $Y$ (otherwise we could construct a larger linearly independent subset). Since $X$ spans $V$, so does $Y$. Hence $Y$ is a basis.
