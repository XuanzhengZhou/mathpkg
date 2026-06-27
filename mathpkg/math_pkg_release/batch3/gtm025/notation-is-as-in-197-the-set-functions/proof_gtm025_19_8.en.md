---
role: proof
locale: en
of_concept: "notation-is-as-in-197-the-set-functions"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.8"
---

Let $E$ be any fixed set in $\mathcal{A}$, and let $\beta$ denote the right side of (i). Then we have

$$\sum_{k=1}^{n} |v(E_k)| = \sum_{k=1}^{n} |v^+ (E_k) - v^- (E_k)|$$

$$\leq \sum_{k=1}^{n} (v^+ (E_k) + v^- (E_k))$$

$$= \sum_{k=1}^{n} |v| (E_k) = |v| (E)$$

for every measurable dissection $\{E_1, \ldots, E_n\}$ of $E$; hence $\beta \leq |v| (E)$. Consider the dissection $\{E \cap P, E \cap P'\}$ where $(P, P')$ is a Hahn decomposition of $X$ for $v$. We get

$$\beta \geq |v| (E \cap P)| + |v| (E \cap P')| = v^+ (E) + v^- (E) = |v| (E).$$

In view of (19.10), we make the following definition with no risk of inconsistency.
