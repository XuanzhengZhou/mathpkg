---
role: proof
locale: en
of_concept: induced-quotient-topology-duality
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

**Proof.** For greater clarity we denote polars with respect to $\langle F, G \rangle$ by $^\circ$, and polars with respect to $\langle M, G/M^\circ \rangle$ by $^\bullet$.

(a) $\Rightarrow$ (b): If $S_1 \in \mathfrak{S}_1'$, it follows from (2.3)(a) that

$$[\phi(S_1)]^\bullet = \psi^{-1}(S_1^\circ) = S_1^\circ \cap M.$$

As $S_1$ runs through $\mathfrak{S}_1'$, $S_1^\circ$ runs through a $\mathfrak{T}_1$-neighborhood base of 0 in $F$; since by assumption $\phi(S_1)$ runs through $\mathfrak{S}_2'$, it is clear that $\mathfrak{T}_1$ induces $\mathfrak{T}_2$ on $M$.

(d) $\Rightarrow$ (c): Let $\mathfrak{U}$ be the $\mathfrak{T}_1'$-neighborhood filter of 0 in $G$. Then $\mathfrak{B} = \phi(\mathfrak{U})$ is the 0-neighborhood filter of the quotient topology on $G/M^\circ$. Again by (2.3)(a) we have

$$V^\bullet = [\phi(U)]^\bullet = \psi^{-1}(U^\circ) = U^\circ \cap M$$

for all $U \in \mathfrak{U}$. Since $U^\circ$ runs through a fundamental subfamily of $\mathfrak{S}_1$ as $U$ runs through $\mathfrak{U}$, the assumption that $\mathfrak{T}_2$ is the quotient topology of $\mathfrak{T}_1$ (equivalently, $\mathfrak{S}_2' = \phi(\mathfrak{S}_1')$) implies that $\psi^{-1}(\mathfrak{S}_1)$ runs through a fundamental subfamily of $\mathfrak{S}_2$, establishing (d).

Now suppose $\mathfrak{T}_1$ is consistent with $\langle F, G \rangle$. For (b) $\Rightarrow$ (a): If $\mathfrak{T}_1$ induces $\mathfrak{T}_2$ on $M$, then the polars $S_2^\bullet$ for $S_2 \in \mathfrak{S}_2$ form a 0-neighborhood base in $M$. Each $S_2^\bullet = \psi^{-1}(S_1^\circ)$ for some $S_1 \in \mathfrak{S}_1$, giving $\mathfrak{S}_2 = \psi^{-1}(\mathfrak{S}_1)$.

If $\mathfrak{T}_1'$ is consistent with $\langle F, G \rangle$ and $M$ is closed, then (c) $\Rightarrow$ (d) follows by a dual argument using the fact that $M^{\circ\circ} = M$ under these assumptions. $\square$
