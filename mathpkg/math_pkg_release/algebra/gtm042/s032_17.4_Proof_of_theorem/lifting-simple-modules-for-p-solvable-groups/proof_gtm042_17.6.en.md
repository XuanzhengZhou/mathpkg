---
role: proof
locale: en
of_concept: lifting-simple-modules-for-p-solvable-groups
source_book: gtm042
source_chapter: "17"
source_section: "17.6"
---

We say that a group $G$ is $p$-solvable of height $h$ if it is a successive extension of $h$ groups which are either of order prime to $p$ or of order a power of $p$. We want to show that, if $K$ is sufficiently large, then every simple $k[G]$-module lifts to an $A$-free $A[G]$-module.

We proceed by induction on $h$ (the case $h = 0$ being trivial) and, for groups of height $h$, by induction on the group order.

Let $E$ be a simple $k[G]$-module. If $G$ has a normal subgroup $P$ which is a $p$-group, then $P$ acts trivially on $E$ (since the only simple $k[P]$-module is the trivial one). We may then view $E$ as a $k[G/P]$-module, where $G/P$ has the same $p$-height as $G$, and by induction on the group order the lifting exists. We may therefore assume that $G$ has no nontrivial normal $p$-subgroup; in particular, the largest normal subgroup of $G$ of order prime to $p$, denoted $I$, is nontrivial.

Let $\bar{S}$ be an irreducible constituent of the restriction of $E$ to $I$. Since $I$ is normal in $G$, Clifford theory tells us that $E$ is an isotypic $k[I]$-module of type $\bar{S}$.

We can now assume that $E$ is an isotypic $k[I]$-module of type $\bar{S}$ where $\bar{S}$ is a simple $k[I]$-module. Since $I$ has order prime to $p$, we can lift $\bar{S}$ in an essentially unique way to an $A$-free $A[I]$-module, say $S$, and it is clear that $K \otimes S$ is absolutely simple. By Corollary 2 to Proposition 16 of Section 6.5, it follows that $\dim S$ divides the order of $I$; in particular, $\dim S$ is prime to $p$.

Now let $s \in G$, and denote by $i_s$ the automorphism $x \mapsto sxs^{-1}$ of $I$. Since $E$ is isotypic of type $\bar{S}$, it follows that $\bar{S}$ (and hence $S$) is isomorphic to its transform by $i_s$. This can be expressed as follows:

Let $\rho: I \to \operatorname{Aut}(S)$ be the homomorphism defining the $I$-module structure of $S$, and let $U_s$ be the set of $t \in \operatorname{Aut}(S)$ such that

$$
t\rho(x)t^{-1} = \rho(sxs^{-1}) \quad \text{for all } x \in I.
$$

Then $U_s$ is not empty.

Let $G_1$ be the group of all pairs $(s, t)$ with $s \in G$, $t \in U_s$. The map $(s, t) \mapsto s$ is a surjective homomorphism $G_1 \to G$; its kernel is equal to $U_1$, which is the multiplicative group $A^*$ of $A$. The group $G_1$ is thus a central extension of $G$ by $A^*$; it acts on $S$ via the homomorphism $(s, t) \mapsto t$.

We shall now replace $G_1$ by a finite group. Let $d = \dim S$. If $s \in G$, the elements $\det(t)$, $t \in U_s$, form a coset of $A^*$ modulo $A^{*d}$. Let $G_2$ be the subgroup of $G_1$ consisting of pairs $(s, t)$ such that $\det(t) \in A^{*d}$. Then $G_2$ is a finite group, $G_2$ acts on $S$, and the homomorphism $G_2 \to G$ is surjective. Its kernel is the group $\mu_d$ of $d$-th roots of unity in $K$, which is cyclic of order dividing $d$, hence prime to $p$.

The $G_2$-module $S$ is $A$-free and lifts $\bar{S}$. By tensoring with the contragredient of $S$, we may assume that $I$ acts trivially on $S$. Now let $F$ be the $k[G_2]$-module such that $E = S \otimes F$ as $k[I]$-modules, with $I$ acting trivially on $F$ by construction. The existence of such an $F$ follows from the theory of lifting exposed in Sections 17.1–17.3; we shall then get an $A$-free $A[G]$-module $\tilde{E}$. Since $N = \ker(G_2 \to G)$ has order prime to $p$ and acts trivially on the reduction $E$ of $\tilde{E}$, it will follow that $N$ acts trivially on $E$ (cf. Section 15.5) and that $\tilde{E}$ can be viewed as an $A[G]$-module—indeed, we will have lifted $E$.

Hence it remains to show that $F$ can be lifted (the case of $\bar{S}$ being already settled). But $F$ is a simple $k[G_2]$-module (since $E$ is) upon which $I$ acts trivially by construction. So we may consider it as a simple $k[H]$-module, where $H = G_2/I$.

The group $H$ is a central extension of $G/I$ (which is $p$-solvable of height $\leqslant h - 1$) by the group $N$, which is cyclic of order prime to $p$.

If $h = 1$, we have $H = N$, and the lifting of $F$ is immediate (Section 15.5).

If $h \geqslant 2$, the group $H/N$ contains a normal subgroup $M/N$ satisfying the following two conditions:

(a) $H/M = (H/N)/(M/N)$ has height $\leqslant h - 2$.

(b) $M/N$ is either a $p$-group or a group of order prime to $p$.

If $M/N$ is a $p$-group, then since $N$ has order prime to $p$, $M$ can be written as a product $N \times P$ where $P$ is a $p$-group. The argument given at the beginning of the proof shows that $P$ acts trivially on $F$, so $F$ can be viewed as a $k[H/P]$-module. But it is clear that the height of $H/P$ is $\leqslant h - 1$, so $F$ can be lifted by induction.

There remains the case where $M/N$ has order prime to $p$. The order of $M$ is then prime to $p$, and since $H/M$ has height $\leqslant h - 2$, the height of $H$ is $\leqslant h - 1$, and again induction applies.

This completes the proof. $\square$
