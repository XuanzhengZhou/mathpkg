---
role: proof
locale: en
of_concept: proposition-14-6
source_book: gtm055
source_chapter: "13-14"
source_section: "Section 15_Section_15"
---

PROOF. If $\sigma$ is a pseudonorm on $\mathcal{E}$ then every ball $\{x \in \mathcal{E} : \sigma(x - x_0) < r\}$ is convex, and it follows at once that (i) implies (ii). Moreover, it is clear that (ii) implies (iii). To see that (iii) implies (iv), let $C$ be a convex neighborhood of 0 in $\mathcal{E}$, and let $V$ be a balanced neighborhood of 0 such that $V \subset C$ (Prob. 11M). Then

$$W = \bigcap_{|\gamma| = 1} \gamma C$$

contains $V$, and is therefore a neighborhood of 0. Since $W$ is an intersection of convex sets, $W$ is also convex, and it is obvious that $W$ is balanced. Thus $W$ is an absolutely convex neighborhood of 0 that is contained in $C$.

It remains to verify that (iv) implies (i). To this end, suppose $\{V_\gamma\}_{\gamma \in \Gamma}$ is a neighborhood base at 0 in $\mathcal{E}$ such that each $V_\gamma$ is absolutely convex. Since a neighborhood of 0 is absorbing, each $V_\gamma$ has a Minkowski function $\sigma_\gamma$ (Ex. F), and, as noted above, $\sigma_\gamma$ is a pseudonorm on $\mathcal{E}$ for each index $\gamma$. Since

$$\{x \in \mathcal{E} : \sigma_\gamma(x) < 1\} \subset V_\gamma \subset \{x \in \mathcal{E} : \sigma_\gamma(x) \leq 1\}, \quad \gamma \in \Gamma,$$

it is clear that the topology induced by the family of pseudonorms $\{\sigma_\gamma\}_{\gamma \in \Gamma}$ coincides with the given topology on $\mathcal{E}$ (see Proposition 11.26), and the proof is complete.

Note. For future purposes it is important to observe that the neighborhood bases referred to in conditions (iii) and (iv) of the foregoing proposition may be taken to consist exclusively either of open sets or of closed sets. To verify the
