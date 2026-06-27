---
role: proof
locale: en
of_concept: grothendieck-vanishing-theorem
source_book: gtm052
source_chapter: "III"
source_section: "§2 Cohomology of Sheaves"
---

We prove the theorem by induction on $n = \dim X$, in several steps.

**Notation.** If $Y$ is a closed subset of $X$, then for any sheaf $\mathcal{F}$ on $X$ we let $\mathcal{F}_Y = j_*(\mathcal{F}|_Y)$, where $j: Y \to X$ is the inclusion. If $U$ is an open subset of $X$, we let $\mathcal{F}_U = i_*(\mathcal{F}|_U)$, where $i: U \to X$ is the inclusion. In particular, if $U = X \setminus Y$, we have an exact sequence (II, Ex. 1.19)

$$0 \to \mathcal{F}_U \to \mathcal{F} \to \mathcal{F}_Y \to 0.$$

**Step 1: Reduction to the case $X$ irreducible.** If $X$ is reducible, let $Y$ be one of its irreducible components, and let $U = X \setminus Y$. Then for any $\mathcal{F}$ we have an exact sequence

$$0 \to \mathcal{F}_U \to \mathcal{F} \to \mathcal{F}_Y \to 0.$$

From the long exact sequence of cohomology, it suffices to prove that $H^i(X, \mathcal{F}_Y) = 0$ and $H^i(X, \mathcal{F}_U) = 0$ for $i > n$. But $Y$ is closed and irreducible, and $\mathcal{F}_U$ can be regarded as a sheaf on the closed subset $\overline{U}$, which has one fewer irreducible component than $X$. Thus by induction on the number of irreducible components, we reduce to the case $X$ irreducible.

**Step 2: Reduction to sheaves of the form $\mathcal{R} \subseteq \mathbf{Z}_U$.** Using the long exact sequence of cohomology, it suffices to prove vanishing for subsheaves $\mathcal{R} \subseteq \mathbf{Z}_U$ and for $\mathbf{Z}_U$ itself.

**Step 3.** Let $U$ be an open subset of $X$ and let $\mathcal{R} \subseteq \mathbf{Z}_U$ be a subsheaf. For each $x \in U$, the stalk $\mathcal{R}_x$ is a subgroup of $\mathbf{Z}$. If $\mathcal{R} = 0$, skip to the next step. If not, let $d$ be the least positive integer occurring in any $\mathcal{R}_x$. Then there exists a nonempty open $V \subseteq U$ such that $\mathcal{R}|_V \cong d \cdot \mathbf{Z}|_V$ as a subsheaf of $\mathbf{Z}|_V$. Thus $\mathcal{R}_V \cong \mathbf{Z}_V$ and we have

$$0 \to \mathbf{Z}_V \to \mathcal{R} \to \mathcal{R}/\mathbf{Z}_V \to 0.$$

The sheaf $\mathcal{R}/\mathbf{Z}_V$ is supported on the closed subset $(U \setminus V)^-$, which has dimension $< n$. By (2.10) and induction, $H^i(X, \mathcal{R}/\mathbf{Z}_V) = 0$ for $i \geq n$. By the long exact sequence, it suffices to prove vanishing for $\mathbf{Z}_V$.

**Step 4.** To complete the proof, we need only show that for any open $U \subseteq X$, $H^i(X, \mathbf{Z}_U) = 0$ for $i > n$. Let $Y = X \setminus U$. Then

$$0 \to \mathbf{Z}_U \to \mathbf{Z} \to \mathbf{Z}_Y \to 0.$$

Now $\dim Y < \dim X$ since $X$ is irreducible, so by induction $H^i(X, \mathbf{Z}_Y) = 0$ for $i \geq n$. On the other hand, $\mathbf{Z}$ is flasque (it is a constant sheaf on an irreducible space), hence acyclic. From the long exact sequence, we obtain $H^i(X, \mathbf{Z}_U) = 0$ for $i > n$, completing the proof.
