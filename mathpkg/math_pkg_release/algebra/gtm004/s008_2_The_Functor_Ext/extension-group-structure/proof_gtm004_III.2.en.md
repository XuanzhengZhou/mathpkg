---
role: proof
locale: en
of_concept: extension-group-structure
source_book: gtm004
source_chapter: "III"
source_section: "2. The Functor Ext"
---

# Proof of Abelian Group Structure on Extension Classes

By Theorem 2.4, there is a natural equivalence of set-valued bifunctors

$$
\eta : E(-, -) \to \operatorname{Ext}_\Lambda(-, -).
$$

By Theorem 2.3, $\operatorname{Ext}_\Lambda(A, B)$ carries a natural abelian group structure: for any $\Lambda$-modules $A$ and $B$, $\operatorname{Ext}_\Lambda(A, B)$ is an abelian group, with addition induced by the addition in $\operatorname{Hom}_\Lambda(R, B)$ modulo the image of $\mu^*$.

Since $\eta$ is a bijection, we can transport this group structure to $E(A, B)$: for $\xi_1, \xi_2 \in E(A, B)$, define

$$
\xi_1 + \xi_2 = \eta^{-1}(\eta(\xi_1) + \eta(\xi_2)).
$$

The neutral element of $E(A, B)$ corresponds to the zero element in $\operatorname{Ext}_\Lambda(A, B)$. Concretely, an extension $B \to E \to A$ represents the neutral element if and only if in the diagram

$$
\begin{CD}
R @>{\mu}>> P @>{\varepsilon}>> A \\
@V{\psi}VV @V{\varphi}VV @| \\
B @>{\kappa}>> E @>{\nu}>> A
\end{CD}
$$

the map $\psi : R \to B$ is the restriction of a homomorphism $\tau : P \to B$, i.e., $\psi = \tau\mu$. In this case $(\varphi - \kappa\tau)\mu = 0$, so $\varphi - \kappa\tau$ factors through $A$, giving a splitting of the extension (i.e., the extension is split).

The naturality of the group structure follows from the naturality of $\eta$: for any $\alpha : A' \to A$ and $\beta : B \to B'$, the induced maps $\alpha^*$ and $\beta_*$ are group homomorphisms.

Thus $E(A, B)$ is naturally an abelian group.
