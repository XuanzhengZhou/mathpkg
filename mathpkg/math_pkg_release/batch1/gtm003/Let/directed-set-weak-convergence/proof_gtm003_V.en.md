---
role: proof
locale: en
of_concept: directed-set-weak-convergence
source_book: gtm003
source_chapter: "V"
source_section: "4.2"
---

Without loss, suppose $S$ is directed for $\geq$ and $\lim \mathfrak{J}(S) = 0$ weakly. Then $S \subset C$. If the assertion fails, there exists a 0-neighborhood $U$ containing no section of $S$. Since $C$ is normal, $U$ can be taken convex and $C$-saturated. Then $S \cap U = \varnothing$ and $(S+C) \cap U = \varnothing$. Since $S+C$ is convex (union of a directed family of convex sets), by (II, 9.2) $U$ and $S$ can be separated by a closed real hyperplane, contradicting weak convergence.
