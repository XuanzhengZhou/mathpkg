---
role: proof
locale: en
of_concept: almost-open-subgroup-dichotomy
source_book: gtm027
source_chapter: "6"
source_section: "P"
---

# Proof of the Almost Open Subgroup Dichotomy

Let $H$ be an almost open subgroup of a non-meager topological group $X$.

By the Banach-Kuratowski-Pettis theorem (part (b)), if $H$ is non-meager, then $HH^{-1} = H$ (since $H$ is a subgroup) is a neighborhood of the identity. Thus $H$ contains an open neighborhood of $e$, and since $H$ is a subgroup, $H = \bigcup_{h \in H} hU$ is open.

Since $H$ is an open subgroup, its complement $X \setminus H = \bigcup_{g \notin H} gH$ is a union of open cosets, hence open. Therefore $H$ is also closed.

The alternative is that $H$ is meager. Thus an almost open subgroup of a non-meager topological group is either meager in $X$, or open and closed in $X$.

(For a counterexample showing that "almost open" cannot be omitted, consider the group $X = \mathbb{R}$ and a subgroup $Y$ such that $X/Y$ is countably infinite. For each $z \in X/Y$, there is a homeomorphism of $X$ onto itself carrying $Y$ onto $z + Y$, so $Y$ is non-meager and not open.)
