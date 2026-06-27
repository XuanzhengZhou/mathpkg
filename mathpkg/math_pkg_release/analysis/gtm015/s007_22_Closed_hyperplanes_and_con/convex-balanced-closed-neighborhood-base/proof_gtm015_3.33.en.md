---
role: proof
locale: en
of_concept: convex-balanced-closed-neighborhood-base
source_book: gtm015
source_chapter: "3"
source_section: "33"
---

# Proof of Convex, balanced, closed neighborhoods form a base in locally convex TVS

Let $U$ be any neighborhood of $\theta$; we seek a neighborhood $V$ of $\theta$ such that $V \subset U$ and $V$ is convex, balanced, and closed.

Let $U_1$ be a closed neighborhood of $\theta$ with $U_1 \subset U$ (5.14), let $U_2$ be a convex neighborhood of $\theta$ with $U_2 \subset U_1$, and let $U_3$ be a balanced neighborhood of $\theta$ with $U_3 \subset U_2$. Set $W = \operatorname{conv} U_3$.

Then $W$ is a convex, balanced (25.15) neighborhood of $\theta$ such that $W = \operatorname{conv} U_3 \subset \operatorname{conv} U_2 = U_2$. Therefore $V = \overline{W}$ is a closed, convex (25.17), balanced (17.5) neighborhood of $\theta$ such that $V = \overline{W} \subset \overline{U}_2 \subset \overline{U}_1 = U_1 \subset U$. Thus $V$ has all the required properties.
