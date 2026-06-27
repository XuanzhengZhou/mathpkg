---
role: proof
locale: en
of_concept: null-sets-measurable
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** Let $T$ be any subset of $X$. Then $\mu(T \cap A) = 0$ since $T \cap A \subset A$. By monotonicity and subadditivity,
$$\mu(T) \leq \mu(T \cap A) + \mu(T \cap A') = \mu(T \cap A') \leq \mu(T).$$
Thus $\mu(T) = \mu(T \cap A) + \mu(T \cap A')$, proving $A$ is $\mu$-measurable. The equality $\mu(T) = \mu(T \cap A')$ also follows. $\square$
