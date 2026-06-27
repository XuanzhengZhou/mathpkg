---
role: proof
locale: en
of_concept: sigma-weakly-closed-ideal-central-projection
source_book: gtm003
source_chapter: "VI"
source_section: "8"
---

We may suppose $J \neq \{0\}$. Clearly, $J$ is a $W^*$-subalgebra of $W$ (being a $\sigma$-weakly closed $*$-subalgebra), hence $J$ is unital by the corollary of (6.2). Let $p$ denote the unit element of $J$; then $p$ is obviously a projection in $P(W)$.

Since $J$ is an ideal of $W$, we have $pW \subset J = pJ$ and also $J = Jp$, so $Wp \subset J$. Therefore $J = pW = Wp$.

To see that $p$ is central: for any $x \in W$, we have $xp \in J$ (since $J$ is a right ideal) and $px \in J$ (since $J$ is a left ideal). Since $p$ is the unit of $J$, we obtain $xp = p(xp) = (px)p = px$. This holds for all $x \in W$, hence $p \in Z(W)$.

Finally, $J = Wp = pW = pWp$ follows from the ideal property combined with $p$ being central.
