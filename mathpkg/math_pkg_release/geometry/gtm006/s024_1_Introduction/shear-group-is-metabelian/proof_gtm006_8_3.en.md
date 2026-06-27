---
role: proof
locale: en
of_concept: shear-group-is-metabelian
source_book: gtm006
source_chapter: "VIII"
source_section: "3"
---

**Proof.** If $H, K$ are subgroups of a given group $G$ then the complex $HK$ is a subgroup if either $H$ or $K$ is normal in $G$. Thus if we show that $\Pi_{([\infty], [0])} \trianglelefteq \Pi$ we will have proved (i) and the first part of (ii).

By Corollary 2 of Lemma 4.11, for any $\alpha$ in $\Pi$ we have

$$\alpha^{-1} \Pi_{([\infty], [0])} \alpha = \Pi_{([\infty]^\alpha, [0]^\alpha)}.$$

Since $[\infty]^\alpha = [\infty]$ (as $[\infty]$ is fixed by the collineation group of a proper division ring plane), we obtain $\alpha^{-1} \Pi_{([\infty], [0])} \alpha = \Pi_{([\infty], [0]^\alpha)}$. As $[0]^\alpha$ is an affine line through $(\infty)$, the subgroup is conjugate to one of the shear groups, hence normal in the subgroup of $\Pi$ fixing $[\infty]$. The intersection $\Pi_{([\infty], [0])} \cap \Pi_{([\infty], [\infty])} = 1$ follows because a non-identity shear cannot fix both $[0]$ and $[\infty]$. The metabelian property follows from the fact that $\Sigma / \Pi_{([\infty], [0])} \cong \Pi_{([\infty], [\infty])}$ which is abelian. $\square$
