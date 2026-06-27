---
role: proof
locale: en
of_concept: freyd-small-complete-preorder
source_book: gtm005
source_chapter: "V"
source_section: "1"
---

Suppose $C$ is not a preorder. Then there are objects $a, b \in C$ with arrows $f \neq g : a \to b$. For any small set $J$, form the product $\Pi_j b$ of factors $b_j$ all equal to $b$, which exists since $C$ is small-complete. Then an arrow $h : a \to \Pi_j b$ is determined by its components, each of which can be either $f$ or $g$. There are thus at least $2^{|J|}$ distinct arrows from $a$ to $\Pi_j b$. Choose $J$ with cardinality larger than the cardinality of the set of all arrows of $C$ (possible since $C$ is small but $J$ can be any small set). This yields a contradiction: there would be more arrows $a \to \Pi_j b$ than total arrows in $C$. Hence $C$ must be a preorder. In a preorder, a limit of a discrete diagram is exactly a greatest lower bound of the indexed objects, so the hypothesis of small-completeness translates to the existence of all small greatest lower bounds.
