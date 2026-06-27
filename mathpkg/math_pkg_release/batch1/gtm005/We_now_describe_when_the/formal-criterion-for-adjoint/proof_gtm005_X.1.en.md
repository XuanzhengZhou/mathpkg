---
role: proof
locale: en
of_concept: formal-criterion-for-adjoint
source_book: gtm005
source_chapter: "X"
source_section: "1. Adjoints and Limits"
---

A functor $G: A \to X$ has a left adjoint precisely when for each $x \in X$ the comma category $(x \downarrow G)$ has an initial object. By the preceding discussion, an initial object is the limit of the identity functor, and more specifically the limit of the projection $Q: (x \downarrow G) \to A$. The existence of such a limit for each $x$ is condition (ii). Condition (i) is necessary because right adjoints (and $G$ would be a right adjoint) preserve all existing limits. The sufficiency follows from Lemma 1 applied to the comma category: if the limit of $Q$ exists, it provides a cone that restricts to a limiting cone for the identity, hence gives an initial object. Thus the left adjoint $F$ is defined by $Fx = \lim Q$ for each $x \in X$.
