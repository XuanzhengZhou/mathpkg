---
role: proof
locale: en
of_concept: ae-limit-measurable
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** Let $A = (\operatorname{dom} f) \cap (\bigcap \operatorname{dom} f_n) \cap \{x : f_n(x) \to f(x)\}$. Then $A \in \mathcal{A}$ and $\mu(A') = 0$. Define $g_n = f_n$ on $A$ and $0$ on $A'$; $g = f$ on $A$ and $0$ on $A'$. Each $g_n$ is measurable (by completeness and (11.23)), and $g_n \to g$ everywhere. By (11.14), $g$ is measurable. By completeness and (11.23), $f$ is measurable. $\square$
