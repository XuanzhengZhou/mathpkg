---
role: proof
locale: en
of_concept: l1-linfinity-duality
source_book: gtm036
source_chapter: "4"
source_section: "Problem section (L^p duality, part b)"
---
The case $p = 1$ requires more delicate treatment. For each $A \in \mathcal{S}_0$, there exists $g_A \in L^\infty$ vanishing off $A$ such that $\phi(f \chi_A) = \int f g_A d\mu$ for all $f \in L^1$ with support in $A$. This follows from the Radon-Nikodym theorem applied to the restriction.

Choose a maximal family $\mathcal{S}_1$ of disjoint sets in $\mathcal{S}_0$ and a $g_B$ extending $g_A$ for each $A \in \mathcal{S}_0$ with $A \subset B$. Now each $f \in L^1$ vanishes off some $B \in \mathcal{S}_1$; put $\phi(f) = \int f g_B d\mu$. There is a $g \in L^\infty$ with $\phi(f) = \int f g d\mu$, and $g$ is the required locally measurable function. The case of a general family $\{g_A\}$ reduces to this special one.

The norm equality $\|\phi\| = \|g\|_\infty$ follows from the definition of the essential supremum: $\|g\|_\infty = \inf\{k : |g(x)| \leq k \text{ locally almost everywhere}\}$, and the pairing estimate $|\phi(f)| \leq \|g\|_\infty \|f\|_1$.
