---
role: proof
locale: en
of_concept: closed-subspace-locally-compact
source_book: gtm027
source_chapter: "5"
source_section: "Locally Compact Spaces"
---

# Proof that a Closed Subspace of a Locally Compact Space is Locally Compact

Let $X$ be a locally compact space and let $F \subset X$ be a closed subset. Let $x \in F$. Since $X$ is locally compact, $x$ has a compact neighborhood $C$ in $X$. Then $C \cap F$ is the intersection of the closed set $F$ with the compact set $C$. A closed subset of a compact set is compact, so $C \cap F$ is compact. Moreover, $C \cap F$ is a neighborhood of $x$ in the subspace $F$: since $C$ is a neighborhood of $x$ in $X$, there exists an open set $U$ in $X$ with $x \in U \subset C$. Then $U \cap F$ is open in $F$ (by definition of the subspace topology) and $x \in U \cap F \subset C \cap F$. Hence $C \cap F$ is a compact neighborhood of $x$ in $F$, proving that $F$ is locally compact. $\square$
