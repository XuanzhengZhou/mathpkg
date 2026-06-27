---
role: proof
locale: en
of_concept: duality-of-induced-and-quotient-s-topologies
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

For greater clarity we denote polars with respect to $\langle F, G \rangle$ by $^\circ$, and polars with respect to $\langle M, G/M^\circ \rangle$ by $^\bullet$.

**(a) $\Rightarrow$ (b):** If $S_1 \in \mathfrak{S}_1'$, it follows from the polar identity (2.3)(a) that
$$[\phi(S_1)]^\bullet = \psi^{-1}(S_1^\circ) = S_1^\circ \cap M.$$
As $S_1$ runs through $\mathfrak{S}_1'$, the polars $S_1^\circ$ run through a $\mathfrak{T}_1$-neighborhood base of $0$ in $F$. Since by assumption $\phi(S_1)$ runs through $\mathfrak{S}_2'$, the sets $[\phi(S_1)]^\bullet$ form a $\mathfrak{T}_2$-neighborhood base of $0$ in $M$. Hence the $\mathfrak{T}_1$-neighborhoods intersect $M$ in precisely the $\mathfrak{T}_2$-neighborhoods; therefore $\mathfrak{T}_1$ induces $\mathfrak{T}_2$ on $M$.

**(d) $\Rightarrow$ (c):** Let $\mathfrak{U}$ be the $\mathfrak{T}_1'$-neighborhood filter of $0$ in $G$. Then $\mathfrak{B} = \phi(\mathfrak{U})$ is the $0$-neighborhood filter of the quotient topology on $G/M^\circ$. Again by (2.3)(a) we have
$$V^\bullet = [\phi(U)]^\bullet = \psi^{-1}(U^\circ) = U^\circ \cap M$$
for all $U \in \mathfrak{U}$. Since $U^\circ$ runs through a fundamental subfamily of $\mathfrak{S}_1$ as $U$ runs through $\mathfrak{U}$, the assumption that $\mathfrak{T}_2'$ is the quotient topology implies that $\mathfrak{S}_1$ is precisely $\psi^{-1}(\mathfrak{S}_2)$, i.e., (c) holds.

**(b) $\Rightarrow$ (a) under consistency:** If $\mathfrak{T}_1$ is consistent with $\langle F, G \rangle$, then the polars of the $\mathfrak{T}_2$-neighborhoods (which are $S_1^\circ \cap M$) generate the same saturated family as $\phi(\mathfrak{S}_1')$, yielding $\mathfrak{S}_2' = \phi(\mathfrak{S}_1')$.

**(c) $\Rightarrow$ (d) under consistency and $M$ closed:** If $\mathfrak{T}_1'$ is consistent with $\langle F, G \rangle$ and $M$ is closed, the bipolar theorem applied to the relation $S_1 = \psi^{-1}(S_2)$ yields that the quotient topology on $G/M^\circ$ coincides with $\mathfrak{T}_2'$.
