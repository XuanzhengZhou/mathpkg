---
role: proof
locale: en
of_concept: kreins-weak-compactness-convex-hull
source_book: gtm003
source_chapter: "II"
source_section: "11. Weak Compactness. Theorems of Eberlein and Krein"
---

**Necessity.** If $C$ is weakly compact, then $C$ is weakly complete (every Cauchy net converges in $C$). Since the Mackey topology $\tau(E, E')$ is a compatible topology for the dual pair $\langle E, E' \rangle$, it has the same completion as the weak topology $\sigma(E, E')$. A weakly complete subset is therefore complete for every compatible topology; in particular, $C$ is complete for $\tau(E, E')$.

**Sufficiency.** Assume $C$ is complete for $\tau(E, E')$. We verify condition (d) of Theorem 11.2 to conclude that $C$ is weakly compact.

Since $B$ is weakly compact, $B$ is bounded. The closed convex hull $C = \overline{\operatorname{co}}(B)$ of a bounded set is bounded, so $C$ is bounded in $E$.

It remains to show that the $\sigma(E'', E')$-closure of $C$ in the bidual $E''$ is contained in $E$. Let $x^{**} \in E''$ belong to the $\sigma(E'', E')$-closure of $C$. There exists a net $\{x_\alpha\}$ in $C$ converging to $x^{**}$ in $\sigma(E'', E')$.

Take any equicontinuous sequence $\{x_n'\}$ in $E'$ such that $x_n' \to 0$ in $\sigma(E', E)$. By the bipolar theorem, the equicontinuous sets of $E'$ are precisely the subsets of polars of neighborhoods of $0$ in $E$. Since $x_n' \to 0$ weakly, $\langle x, x_n' \rangle \to 0$ for every $x \in E$.

Now, because $C$ is $\tau(E, E')$-complete, the sequence of mappings $x \mapsto \langle x, x_n' \rangle$ converges to $0$ uniformly on $C$ (this is the key point where Mackey completeness is used: a $\tau(E, E')$-complete convex bounded set absorbs equicontinuous sets). By a theorem of Pták, the $\tau(E, E')$-completeness of $C$ implies that every $\sigma(E', E)$-null sequence in $E'$ converges uniformly on $C$.

Thus $\langle x^{**}, x_n' \rangle = \lim_\alpha \langle x_\alpha, x_n' \rangle = 0$ uniformly in $n$, which shows that $x^{**}$ is $\sigma(E'', E')$-continuous on equicontinuous subsets of $E'$. By the Grothendieck completion theorem, $x^{**} \in E$. Condition (d) of Theorem 11.2 is satisfied, hence $C$ is weakly compact.
