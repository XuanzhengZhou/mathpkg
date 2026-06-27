---
role: proof
locale: en
of_concept: characterizations-of-reflexive-spaces
source_book: gtm036
source_chapter: "20"
source_section: "20.5"
---

A linear topological space $E$ is reflexive if and only if the evaluation map of $E$ into $E^{**}$ is a topological isomorphism onto. The evaluation map is continuous and carries $E$ onto $E^{**}$ exactly when $E$ is semi-reflexive (Proposition 20.4). The evaluation map is a homeomorphism when, in addition, $E$ is evaluable: strongly bounded subsets of $E^*$ are equicontinuous (Proposition 20.1). Moreover, the evaluation map of a locally convex space $E$ is one-to-one if and only if $E$ is Hausdorff.

Combining these facts from Propositions 20.1, 20.4, and 20.5 yields the first characterization: a locally convex Hausdorff space is reflexive if and only if it is both semi-reflexive and evaluable.

For the equivalent characterization, recall that $E$ evaluable implies $E$ is a Mackey space (since the Mackey topology is the topology of uniform convergence on convex circled weak$^*$ compact subsets of $E^*$, and evaluability ensures strongly bounded sets -- hence their convex circled weak$^*$ closed hulls -- are equicontinuous). Conversely, if $E$ is a Mackey space and both $E$ and $E^*$ are semi-reflexive, then Corollary 20.5 implies $E$ is evaluable; together with semi-reflexivity of $E$ this yields reflexivity by the first characterization.
