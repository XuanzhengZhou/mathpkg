---
role: proof
locale: en
of_concept: injectivity-criterion-for-completion-map
source_book: gtm036
source_chapter: ""
source_section: ""
---

The proof follows from the definition of the completion map. Recall that $T^\wedge$ is defined on the completion of $E$ by extending $T$ to equivalence classes of Cauchy nets. The map $T^\wedge$ sends the equivalence class of a Cauchy net $\{x_\gamma\}$ to the limit of $\{T(x_\gamma)\}$.

If $T^\wedge$ is one-to-one, then whenever $T(x_\gamma) \rightarrow T(x_0)$, the Cauchy net $\{x_\gamma\}$ and the constant net $\{x_0\}$ belong to the same equivalence class in the completion, so $x_\gamma \rightarrow x_0$.

Conversely, suppose the condition holds. If $T^\wedge([\{x_\gamma\}])=T^\wedge([\{y_\delta\}])$, then the limits of $T(x_\gamma)$ and $T(y_\delta)$ coincide. By considering the combined net and applying the condition, we deduce that $\{x_\gamma\}$ and $\{y_\delta\}$ converge to the same limit, hence they represent the same element in the completion. Thus $T^\wedge$ is injective.
