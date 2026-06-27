---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A right Kan extension generalizes the notion of extending a functor along another functor. Given $K: M \to C$ and $T: M \to A$, the right Kan extension $\mathrm{Ran}_K T$ is a functor $C \to A$ equipped with a universal natural transformation $\varepsilon: (\mathrm{Ran}_K T)K \to T$. The universal property states that any natural transformation from $SK$ to $T$ factors uniquely through $\varepsilon$. When $M$ is a subcategory of $C$ and $K$ is the inclusion, this gives a canonical way to extend functors.
