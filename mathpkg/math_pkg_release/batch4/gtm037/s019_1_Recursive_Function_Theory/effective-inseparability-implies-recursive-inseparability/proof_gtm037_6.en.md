---
role: proof
locale: en
of_concept: effective-inseparability-implies-recursive-inseparability
source_book: gtm037
source_chapter: "6"
source_section: "Recursive Function Theory"
---

Suppose $A$ and $B$ are effectively inseparable, witnessed by the recursive function $f$ as in Definition 6.21(iii). If $A$ and $B$ were recursively separable, there would exist a recursive set $C$ such that $A \subseteq C$ and $B \subseteq \omega \sim C$. Since $C$ is recursive, both $C$ and $\omega \sim C$ are r.e., so there exist $e, r \in \omega$ such that $C = \mathrm{Dmn}\,arphi_e^1$ and $\omega \sim C = \mathrm{Dmn}\,arphi_r^1$. Then $A \subseteq \mathrm{Dmn}\,arphi_e^1$, $B \subseteq \mathrm{Dmn}\,arphi_r^1$, and $\mathrm{Dmn}\,arphi_e^1 \cap \mathrm{Dmn}\,arphi_r^1 = C \cap (\omega \sim C) = \emptyset$. By effective inseparability, $f(e, r) \in \omega \sim (\mathrm{Dmn}\,arphi_e^1 \cup \mathrm{Dmn}\,arphi_r^1) = \omega \sim (C \cup (\omega \sim C)) = \emptyset$, a contradiction. Thus $A$ and $B$ are recursively inseparable.
