---
role: proof
locale: en
of_concept: finite-limits-commute-with-filtered-colimits-in-set
source_book: gtm005
source_chapter: "IX"
source_section: "2. Interchange of Limits"
---

By the construction of colimits in terms of coproducts and coequalizers (dual of Theorem V.2.2 with $J$ filtered),

$$\operatorname{Colim}_j F(p,j) = \coprod_j F(p,j)/E,$$

where $\coprod_j$ is the disjoint union and $E$ is the equivalence relation defined for elements $x \in F(p,j)$ and $x' \in F(p,j')$ in that union by $xEx'$ if and only if there are arrows $u:j \rightarrow k$, $u':j' \rightarrow k$ with $F(p,u)x = F(p,u')x'$. Write $(x,j)$ for the $E$-equivalence class of an element $x \in F(p,j)$.

Now $J$ is filtered; condition (a) in the definition of "filtered" implies that any finite list $(x_1,j_1), \ldots, (x_m,j_m)$ of such elements can be written as a list $(y_1,k), \ldots, (y_m,k)$ with one second index $k$. Condition (b) in the definition implies that every equality between elements of this list takes place after application of a suitable one arrow $w:k \rightarrow k'$.

For any functor $G:P \rightarrow \mathbf{Set}$, $\operatorname{Lim}_p Gp = \operatorname{Cone}(*,G)$, the set of cones $\tau$ over $G$ with vertex a point $*$. If $Gp = \operatorname{Colim}_j F(p,j)$ and $P$ is finite, each such cone consists of a finite number of elements of $\operatorname{Colim}_j F(p,j)$ and the conditions that $\tau$ be a cone involve a finite number of equations between these elements. Since $J$ is directed, the observations above now mean that each cone $\tau$ can consist of elements $\tau_p = (y_p,k')$ for some one index $k'$, where the $y_p \in F(p,k')$ already constitute a cone $y:* \rightarrow F(-,k')$. This cone $y$ is an element of $\operatorname{Lim}_p F(p,k')$, and its image under the canonical map $\operatorname{Lim}_p F(p,k') \rightarrow \operatorname{Colim}_j \operatorname{Lim}_p F(p,j)$ gives an element mapping to $\tau$ under $\kappa$. This shows $\kappa$ is surjective.

For injectivity, if two elements of $\operatorname{Colim}_j \operatorname{Lim}_p F(p,j)$ map to the same cone under $\kappa$, the filteredness argument allows us to represent both by cones in $F(-,k)$ for a common index $k$, and condition (b) ensures the equality persists in some $F(-,k')$. Hence $\kappa$ is injective and therefore an isomorphism.
