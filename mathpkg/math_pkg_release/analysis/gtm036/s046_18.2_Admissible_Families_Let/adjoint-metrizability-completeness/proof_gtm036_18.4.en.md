---
role: proof
locale: en
of_concept: adjoint-metrizability-completeness
source_book: gtm036
source_chapter: "18"
source_section: "18.4"
---

Let $E$ be a linear space with locally convex topology $\mathcal{T}$, and let $E^*$ be its adjoint equipped with the strong topology $s(E^*, E)$.

For (i): The strong topology on $E^*$ is the topology of uniform convergence on $\mathcal{T}$-bounded subsets of $E$ (equivalently, on $w(E, E^*)$-bounded subsets, by 17.5). A local base for this topology is given by polars of bounded sets. The space $E^*$ is metrizable if and only if it has a countable local base. Since the polars of members of a co-base for the family of all bounded subsets of $E$ form a local base, $E^*$ has a countable local base precisely when the family of bounded subsets has a countable co-base. Specifically, if $\{B_n\}$ is a countable fundamental family of bounded sets (every bounded set is contained in some scalar multiple of some $B_n$), then the polars $\{B_n^\circ\}$ form a countable local base. Conversely, a countable local base $\{U_n\}$ yields a countable co-base $\{U_n^\circ\}$ of bounded sets.

For (ii): Let $L$ be the space of all linear functionals on $E$ which are continuous on each bounded subset of $E$. The strong topology on $L$ is defined as the topology of uniform convergence on bounded subsets of $E$. Since $E^* \subset L$, we need to show $E^*$ is strongly dense in $L$. Take any $f \in L$ and any strong neighborhood of $f$, which may be taken to be of the form $\{g : |g(x) - f(x)| \leq 1 \text{ for all } x \in B\}$ for some bounded set $B \subset E$. Since $f$ is continuous on the bounded set $B$, and $E^*$ separates points of $E$, one can approximate $f$ on $B$ by members of $E^*$ using the Hahn-Banach theorem or by considering the restriction of $f$ to the subspace spanned by $B$ and extending continuous linear functionals.

For (iii): $E^*$ is complete relative to the strong topology if and only if every Cauchy net in $E^*$ converges to an element of $E^*$. A Cauchy net $\{f_\alpha\}$ in $E^*$ with the strong topology converges uniformly on each bounded set to some linear functional $f$. This limit $f$ is continuous on each bounded subset of $E$ (as a uniform limit of continuous functions on each bounded set). If every linear functional continuous on bounded subsets is continuous on $E$, then $f \in E^*$, so $E^*$ is complete. Conversely, if $E^*$ is complete, take any linear functional $f$ continuous on bounded subsets. Using (ii), $f$ is in the strong closure of $E^*$, hence there is a net in $E^*$ converging strongly to $f$. By completeness, $f \in E^*$, so $f$ is continuous on $E$.
