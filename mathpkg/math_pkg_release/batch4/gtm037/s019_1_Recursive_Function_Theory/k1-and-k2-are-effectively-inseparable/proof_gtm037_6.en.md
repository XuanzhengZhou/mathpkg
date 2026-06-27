---
role: proof
locale: en
of_concept: k1-and-k2-are-effectively-inseparable
source_book: gtm037
source_chapter: "6"
source_section: "Recursive Function Theory"
---

Clearly $K_1$ and $K_2$ are r.e. and $K_1 \cap K_2 = \emptyset$. For any $e, r \in \omega$ let $f(e, r) = 2^r \cdot 3^e$. To verify Definition 6.21(iii), assume that $K_1 \subseteq \mathrm{Dmn}\,arphi_e^1$ and $K_2 \subseteq \mathrm{Dmn}\,arphi_r^1$ with $\mathrm{Dmn}\,arphi_e^1 \cap \mathrm{Dmn}\,arphi_r^1 = \emptyset$.

Suppose $f(e, r) \in \mathrm{Dmn}\,arphi_e^1 \cup \mathrm{Dmn}\,arphi_r^1$. By symmetry, say $f(e, r) \in \mathrm{Dmn}\,arphi_e^1$. Thus $\exists y\,((e, 2^r \cdot 3^e, y) \in T_1)$, and since $\mathrm{Dmn}\,arphi_e^1 \cap \mathrm{Dmn}\,arphi_r^1 = \emptyset$, obviously $orall z\,((r, 2^r \cdot 3^e, z) 
otin T_1)$. Thus $2^r \cdot 3^e \in K_2$, so $2^r \cdot 3^e \in \mathrm{Dmn}\,arphi_r^1$, contradiction.

Therefore $f(e, r) 
otin \mathrm{Dmn}\,arphi_e^1 \cup \mathrm{Dmn}\,arphi_r^1$, i.e. $f(e, r) \in \omega \sim (\mathrm{Dmn}\,arphi_e^1 \cup \mathrm{Dmn}\,arphi_r^1)$, establishing effective inseparability.
