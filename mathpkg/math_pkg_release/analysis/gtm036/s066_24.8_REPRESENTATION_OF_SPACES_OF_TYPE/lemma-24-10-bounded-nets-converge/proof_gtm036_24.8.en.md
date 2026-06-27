---
role: proof
locale: en
of_concept: lemma-24-10-bounded-nets-converge
source_book: gtm036
source_chapter: "24"
source_section: "24.8"
---

Observe that for $\alpha$ fixed, $\|x_\beta - x_\alpha\|$ is monotonic for $\beta \geq \alpha$, and bounded, and hence converges. Since the norm is linear on the positive cone, for $\gamma \geq \beta \geq \alpha$ it is true that $\|x_\gamma - x_\beta\| = \|x_\gamma - x_\alpha\| - \|x_\beta - x_\alpha\|$. From this it follows easily that the net is Cauchy and hence converges to a member $x$ of $E$. It is not hard to verify that $x$ is the supremum of the members $x_\alpha$, by making use of the fact that the set $\{z : z \geq y\}$ is always closed.

Finally, to prove the first statement of the lemma, if $B$ is a subset of $E$ (or of $E^*$) with an upper bound, then let $\mathcal{A}$ be the family of finite subsets of $B$ directed by $\supset$, and for $A$ in $\mathcal{A}$ let $x_A$ be the supremum of the set $A$. Then the net $\{x_A, A \in \mathcal{A}\}$ is monotonically increasing and bounded, and its limit is the supremum of $B$.
