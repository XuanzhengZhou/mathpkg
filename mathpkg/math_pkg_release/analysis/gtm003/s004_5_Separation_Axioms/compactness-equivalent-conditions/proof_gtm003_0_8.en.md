---
role: proof
locale: en
of_concept: compactness-equivalent-conditions
source_book: gtm003
source_chapter: "0"
source_section: "8"
---

The text states the equivalences without proof. Standard proof sketch: (compact $\Rightarrow$ a): The complement of the intersection being empty implies a finite subcollection has non-empty intersection by de Morgan's laws. (a $\Rightarrow$ b): Given a filter $\mathfrak{F}$, the family $\{\overline{F} : F \in \mathfrak{F}\}$ has the finite intersection property, so $\bigcap \overline{F} \neq \varnothing$; any point in this intersection is a cluster point. (b $\Rightarrow$ c): An ultrafilter's cluster points are exactly its limit points. (c $\Rightarrow$ compact): Given an open cover with no finite subcover, the complements of finite unions form a filter subbase generating a filter; extend to an ultrafilter. This ultrafilter cannot converge (as any limit would lie in some open set of the cover, whose complement is in the ultrafilter), contradicting (c).
