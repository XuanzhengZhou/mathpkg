---
role: proof
locale: en
of_concept: frobenius-group-on-l-infinity
source_book: gtm006
source_chapter: "XIV"
source_section: "5"
---
**Proof of Theorem 14.9.** Assume $\mathcal{A}$ has odd order $n$ and $\Pi$ is transitive on affine lines. Let $l$ be any affine line, and let $A = l \cap l_{\infty}$. Consider the action of $\Pi_A$ on the points of $l$.

Since $\Pi$ is transitive on affine lines (by Theorem 14.6(i)), the stabilizer $\Pi_A$ acts transitively on the affine points of $l$. Moreover, by the presence of involutory homologies (elations), one can show that $\Pi_A$ acts doubly transitively on the points of $l$. The subgroup $\Gamma_A$ of $\Pi_A$ that fixes an affine point of $l$ and acts as the identity on $\mathcal{S}\setminus\{A\}$ is a Frobenius group on $l \setminus \{A\}$.

Since $\Pi$ clearly cannot fix $A$, the transitivity of $\Gamma_A$ immediately implies that $\Pi$ acts as a doubly transitive group on the points of $l$. Finally, since the conjugate of an involutory homology is again an involutory homology, $\Gamma_A$ is normal in $\Pi_A$.

Theorem 14.9 is now proved by appealing to Result 14.4. In the situation of Theorem 14.9, the kernel of $\Gamma_A$ is the group of elations with axis $OA$. Since this group is normal in $\Pi_A$, the conditions of Result 14.4 are satisfied, yielding that the kernel is elementary abelian and $n$ is a prime power. $\square$
