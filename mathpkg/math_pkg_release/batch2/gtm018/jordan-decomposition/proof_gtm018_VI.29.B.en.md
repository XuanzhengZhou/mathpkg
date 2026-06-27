---
role: proof
locale: en
of_concept: jordan-decomposition
source_book: gtm018
source_chapter: "VI"
source_section: "29"
---

Let $X = A \cup B$ be a Hahn decomposition of $X$ with respect to $\mu$, with $A$ positive and $B$ negative. Define the upper variation $\mu^+$ and lower variation $\mu^-$ by

$$\mu^+(E) = \mu(E \cap A), \quad \mu^-(E) = -\mu(E \cap B),$$

and the total variation $|\mu|$ by $|\mu|(E) = \mu^+(E) + \mu^-(E)$ for every measurable set $E$.

The variations of $\mu$ are clearly non negative; if every measurable set is a countable union of measurable sets for which $\mu$ is finite, it follows from 28.A that the same is true for $\mu^+$ and $\mu^-$. The equation $\mu = \mu^+ - \mu^-$ follows from the definitions of $\mu^+$ and $\mu^-$; the fact that $\mu$ takes on at most one of the values $+\infty$ and $-\infty$ implies that at least one of the set functions $\mu^+$ and $\mu^-$ is always finite.

The countable additivity of $\mu^+$ follows from the countable additivity of $\mu$ restricted to the positive set $A$, and similarly for $\mu^-$. Hence $\mu^+$ and $\mu^-$ are measures.

If $\mu$ is [totally] finite or $\sigma$-finite, then so also are $\mu^+$ and $\mu^-$; at least one of the measures $\mu^+$ and $\mu^-$ is always finite. The representation $\mu = \mu^+ - \mu^-$ as the difference of its upper and lower variations is called the Jordan decomposition of $\mu$.
