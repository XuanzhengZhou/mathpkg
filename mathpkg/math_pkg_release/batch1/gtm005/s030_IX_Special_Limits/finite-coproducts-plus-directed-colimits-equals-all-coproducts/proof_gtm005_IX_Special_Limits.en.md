---
role: proof
locale: en
of_concept: finite-coproducts-plus-directed-colimits-equals-all-coproducts
source_book: gtm005
source_chapter: "IX"
source_section: "Special Limits"
---

Let $F : J \to C$ be a functor where $J$ is a set (a discrete category). We construct a colimit for $F$. Let $J^+$ be the preorder whose objects are all finite subsets $S \subset J$, ordered by inclusion; $J^+$ is directed (hence filtered). Define $F^+ : J^+ \to C$ by assigning to each finite subset $S$ the coproduct $\coprod_{s \in S} F(s)$. For an inclusion $S \subset T$, define $F^+(u)$ as the unique arrow making the diagram

$$
F^+(S) = \coprod_{s \in S} F(s) \longrightarrow \coprod_{t \in T} F(t) = F^+(T)
$$

commute with respect to the coproduct injections. This makes $F^+$ a functor. Identifying each $j \in J$ with the singleton $\{j\}$ embeds $J$ into $J^+$, and $F^+$ restricts to $F$ on $J$.

Now, any natural transformation $\theta : F^+ \Rightarrow \Delta_C$ to a constant functor corresponds uniquely to a cone from $F$ to $C$, because the values on singletons determine the values on all finite subsets via the universal property of coproducts. Thus a colimiting cone for $F^+$ (which exists by hypothesis, since $J^+$ is a directed preorder) restricts to a colimiting cone for $F$. Hence the colimit of $F$ exists and is given by $\varinjlim F^+$.
