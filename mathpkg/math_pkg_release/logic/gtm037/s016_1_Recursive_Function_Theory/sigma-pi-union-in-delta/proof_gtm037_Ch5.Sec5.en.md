---
role: proof
locale: en
of_concept: sigma-pi-union-in-delta
source_book: gtm037
source_chapter: "Part 1: Recursive Function Theory"
source_section: "5. Arithmetic Hierarchy"
---

Let $R \in \Sigma_m$, say $R$ is $n$-ary. Let $S = \{(x_0, \ldots, x_n) : (x_0, \ldots, x_{n-1}) \in R\}$. Then $S \in \Sigma_m$ by 5.26 and 5.27. Clearly

$$R = \{(x_0, \ldots, x_{n-1}) : \forall y \in \omega[(x_0, \ldots, x_{n-1}, y) \in S]\},$$

so $R \in \Pi_{m+1}$ by Proposition 5.25. Thus $\Sigma_m \subseteq \Pi_{m+1}$, and similarly $\Pi_m \subseteq \Sigma_{m+1}$. An easy inductive argument then shows that $\Sigma_m \subseteq \Sigma_{m+1}$ and $\Pi_m \subseteq \Pi_{m+1}$.
