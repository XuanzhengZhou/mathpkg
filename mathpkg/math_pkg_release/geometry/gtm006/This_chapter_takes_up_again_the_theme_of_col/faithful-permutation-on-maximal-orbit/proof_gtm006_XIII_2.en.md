---
role: proof
locale: en
of_concept: faithful-permutation-on-maximal-orbit
source_book: gtm006
source_chapter: "XIII"
source_section: "2"
---

Since $\Pi$ is finite, all orbits have finite length and, consequently, there is certainly an orbit of maximal length which, without any loss of generality, we may assume to be a point orbit. (Otherwise the dual argument will prove the theorem.)

Let $P$ and $Q$ be any pair of distinct points in an orbit $\mathcal{O}$ of maximal length and let $\Pi_e$ be the subgroup of $\Pi$ fixing every point of $\mathcal{O}$. Then $\Pi$ induces a faithful permutation group on $\mathcal{O}$ if and only if $\Pi_e = 1$. We shall assume that $\Pi_e \neq 1$ and then show that this leads to a contradiction.

Choose a non-trivial element $\pi \in \Pi_e$ and let $R$ be a point not fixed by $\pi$. (Such a point must exist since $\Pi$ is a collineation group, so $\pi \neq 1$ means $\pi$ moves some point.) The points in $\mathcal{O}$ are all fixed by $\pi$. But consider the orbit of $R$ under $\Pi$. Since $\pi$ fixes all points of $\mathcal{O}$ and $R$ is not in $\mathcal{O}$ (otherwise $\pi$ would fix $R$), the orbit of $R$ must be of larger size, contradicting the maximality of $|\mathcal{O}|$.

Thus $\Pi_e = 1$ and $\Pi$ acts faithfully on $\mathcal{O}$.
