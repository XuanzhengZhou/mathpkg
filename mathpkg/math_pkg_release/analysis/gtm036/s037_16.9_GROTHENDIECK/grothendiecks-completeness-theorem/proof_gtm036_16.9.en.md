---
role: proof
locale: en
of_concept: grothendiecks-completeness-theorem
source_book: gtm036
source_chapter: "16"
source_section: "16.9"
---

The completeness theorem is a direct consequence of the foregoing results. 

For part (i): From the preceding approximation theorem, if $f$ is a linear functional on $F$ which is $w(F, E)$-continuous on each member of $\mathcal{A}$, then for every $A \in \mathcal{A}$ and every $\varepsilon > 0$ there exists a member of $E$ (via the canonical image $T[E]$) that approximates $f$ within $\varepsilon$ on $A$. This means $T[E]$ is $\mathcal{T}_{\mathcal{A}}$-dense in the space of all such functionals.

For part (ii): Suppose the linear extension of $\bigcup \mathcal{A}$ equals $F$. If $E$ is $\mathcal{T}_{\mathcal{A}}$-complete, then $T[E]$ is $\mathcal{T}_{\mathcal{A}}$-closed in the space of $\mathcal{A}$-continuous functionals. Combined with the density established in (i), this forces the space of $\mathcal{A}$-continuous functionals to coincide with $T[E]$, meaning every such functional comes from an element of $E$ and is thus $w(F, E)$-continuous on all of $F$. Conversely, if every $\mathcal{A}$-continuous functional is $w(F, E)$-continuous (hence represented by an element of $E$), then the space of $\mathcal{A}$-continuous functionals is exactly $T[E]$, which is therefore $\mathcal{T}_{\mathcal{A}}$-complete. The hyperplane equivalence follows from the fact that a linear functional is continuous if and only if its kernel (a hyperplane) is closed.
