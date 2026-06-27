---
role: proof
locale: en
of_concept: minimal-closed-subset-extreme-points
source_book: gtm003
source_chapter: "II"
source_section: "10"
---

This follows immediately from Theorem 10.5. Let $F \subset C$ be any closed subset such that $\overline{\operatorname{co}}(F) = C$. Since $C$ is compact and convex, its closed convex hull is $C$ itself, which is compact. The set $F$ is a closed subset of the compact set $C$, hence $F$ is compact. By Theorem 10.5 applied with $A = F$, every extreme point of $C = \overline{\operatorname{co}}(F)$ belongs to $F$. Thus $\mathcal{E} \subset F$. Taking $F = \overline{\mathcal{E}}$ (the closure of the set of extreme points), Theorem 10.5 implies $\mathcal{E} \subset \overline{\mathcal{E}}$, and the Krein-Milman theorem gives $\overline{\operatorname{co}}(\mathcal{E}) = C$, so $\overline{\mathcal{E}}$ has the required property and is minimal among all closed subsets whose convex closure equals $C$.
