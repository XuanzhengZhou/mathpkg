---
role: proof
locale: en
of_concept: "let-denote-the-family-of-all-open-subsets"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.3"
---

Assertions (i) and (ii) follow at once from DE MORGAN's laws (1.9.iii) and (1.9.iv) applied to axioms (6.4.iii) and (6.4.ii) for open sets.

Since $A^{-}$ is the intersection of all closed supersets of $A$, assertion (ii) proves (iii). Assertion (iv) is all but obvious.

We next prove (v). Suppose first that $A$ is closed. Then $A'$ is a neighborhood of each point in $A'$ and $A' \cap A = \varnothing$, so that no point of $A'$ is a limit point of $A$, i.e., $A$ contains all of its limit points. Conversely, if no point of $A'$ is a limit point of $A$, then for each $x \in A'$, there is a neighborhood $U_x$ of $x$ such that $U_x \cap A = \varnothing$, and therefore $A' = \cup \{U_x : x \in A'\}$ is open, i.e., $A$ is closed.

To prove (vi), we compute as follows:

$$A'^{-} = \left[ \cap \{F : F \text{ is closed and } F \supset A'\} \right]'$$
$$= \cup \{F' : F \text{ is closed and } F \supset A'\}$$
$$= \cup \{F' : F' \text{ is open and } F' \subset A\}$$
$$= A^{\circ}$$

Assertion (vii) is immediate from (vi) and the
