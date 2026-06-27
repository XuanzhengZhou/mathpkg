---
role: proof
locale: en
of_concept: finite-coproducts-and-filtered-colimits-give-coproducts
source_book: gtm005
source_chapter: "IX"
source_section: "1. Filtered Limits"
---

We wish to construct a colimit for a functor $F : J \rightarrow C$, where $J$ is a set (= a discrete category). Let $J^+$ be the preorder with objects all finite subsets $S \subset J$, ordered by inclusion; clearly, $J^+$ is filtered. Let $F^+$ assign to each finite subset $S$ the coproduct $\coprod Fs$, taken over all $s \in S$. If $S \subset T$ is an arrow $u : S \rightarrow T$ of $J^+$, take $F^+u$ to be the unique (dotted) arrow which makes the diagram

$$F^+ S = \coprod_{s \in S} Fs \rightarrow \coprod_{t \in T} Ft = F^+ T$$

commute for every $s \in S$, with the injections of the coproducts. This evidently makes $F^+$ a functor $J^+ \rightarrow C$ which agrees on $J$ with the given functor $F$, if $J$ is included in $J^+$ by identifying each $j$ with the one-point subset $\{j\}$.

Now consider any natural transformation $\theta : F^+ \rightarrow G$ to some other functor $G : J^+ \rightarrow C$. For each $s \in S$ the diagram

$$F^+ S = \coprod_{s \in S} Fs \xrightarrow{\theta_S} GS$$

together with the universal property of the coproduct determines $\theta_S$ uniquely in terms of its restrictions to the components $Fs$ for $s \in S$. In particular, a natural transformation from $F^+$ to a constant functor is uniquely determined by its values on the singleton subsets $\{j\}$. Hence any cone from $F$ to a constant functor extends uniquely to a cone from $F^+$, so the colimit of $F^+$ (which exists by hypothesis, since $J^+$ is a directed preorder) yields the coproduct of $F$. Thus $C$ has all small coproducts.
