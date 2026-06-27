---
role: proof
locale: en
of_concept: canonical-form-of-nondegenerate-finite-open-configuration
source_book: gtm006
source_chapter: "11"
source_section: "4. Classification Problems"
---

Let $\mathcal{Q}$ be a complete non-degenerate quadrangle contained in $\mathcal{A}$. By Theorem 11.8, choose a free extension sequence $\mathcal{C}_0, \mathcal{C}_1, \ldots, \mathcal{C}_n$ from $\mathcal{Q}$ to $\mathcal{A}$ such that each $\mathcal{C}_i$ is finite and open. Among all $\mathcal{Q}$-configurations free equivalent to $\mathcal{A}$, choose one, $\mathcal{C}^*$ say, which:

(i) has the smallest possible number of lines;
(ii) among those satisfying (i), $\mathcal{C}^*$ has the maximal number of 3-incident points.

Now suppose, if possible, that $m$ is a 0-incident line in $\mathcal{C}^*$. By intersecting $m$ with $k_1$ and $k_2$ (that is, adding the points $mk_1$ and $mk_2$) and then deleting $m$ (now a 2-incident line), we would have a $\mathcal{Q}$-configuration which is free equivalent to $\mathcal{A}$ but has fewer lines than $\mathcal{C}^*$, violating (i). So $\mathcal{C}^*$ has no 0-incident lines.

Next, suppose $m$ is a 1-incident line, incident with the point $X$ say. If $X$ is not on both $k_1$ and $k_2$, then suppose $X$ is not on $k_2$; we adjoin the point $mk_2$ and delete $m$; again this gives a $\mathcal{Q}$-configuration free equivalent to $\mathcal{A}$ but with fewer lines than $\mathcal{C}^*$, which violates (i), so $m$ did not exist. Suppose $X$ is the intersection point $k_1k_2$. If there is already a line on $P_1$ and $P_3$, let it be $y$; otherwise add the line $y = P_1P_3$. In either case adjoin the point $Z = ym$ and delete $m$; if the line $y$ had already existed this would violate (i) again, so we assume that $y$ was added as the union of $P_1$ and $P_3$. If we adjoin the line $w = ZP_2$ and delete $Z$; then we can delete $y$. Now the situation is that instead of the 1-incident line $m$, we have the 1-incident line $w$, but incident with the point $P_2$; since $P_2$ is not on $k_2$ this case has already been eliminated.

Now we investigate the 3-incident elements. Let $\mathcal{Z}$ be the quadrangle formed by the four points $P_1, P_2, P_3, P_4$ and the four lines $k_1, k_2$, together with the two lines through $P_1$ and $P_2$ for $\mathcal{Q}$. If there is any 3-incident point $X$ not on the four lines $k_i$ of $\mathcal{Z}$, then consider the line $u = XP_3$ (which does not exist in general, but we can adjoin it). If $P_4$ does not lie on $u$, we can replace the quadrilateral $\mathcal{Q}$ by $\mathcal{Z}$, where we write $X$ instead of $P_4$ and $u$ instead of $k_2$. This contradicts (ii).

So $P_1$, say, must lie on $u$; there is another line $w$ on $X$, such that $w$ does not contain $P_4$ (since $X$ lies on at least 3 lines), and $w$ is a 3-incident line. Again, we distinguish two cases: $P_2$ is on $u$ or not. If it is on $u$, then let $R$ be a third point on $w$; $R$ is not 1-incident (since 1-incident points are on one of the $k_i$), so $R$ must be 3-incident. Hence we replace $\mathcal{Q}$ by $\mathcal{Z}$, where the points are $P_1, P_2, P_3, R$, and the lines of $\mathcal{Z}$ are $u$ and $w$. This also violates the assumption (ii). So $P_2$ is not on $w$, and we can choose a 3-incident point $R$ on $w$, $R \neq X$. Then we replace both $P_3$ and $P_4$ in $\mathcal{Z}$ by $X$ and $R$, replacing $k_2$ by $w$ at the same time; this certainly increases the number of 3-incident points, and so violates (ii).

Consequently we now can suppose that there is no line $u = XP_3$. It is easy to see that there must be a line $w$ on $X$ which contains a point $Y$ not on any $k_i$; so as above, we discard $P_3, P_4, k_2$, replacing them with $X, Y$ and $w$. So we have:

(3) If there are any 3-incident points not on the $k_i$, or if there are any lines other than the $k_i$, then all the points $P_i$ are 3-incident.

From (3) it follows that all the 3-incident elements form a sub-quadrangle, and more generally that all elements of $\mathcal{C}^*$ are either on $k_1$ or $k_2$, or are the $P_i$. Hence $t$ elements lie on the line $k$ (the four intersection points and the points shifted from 1-incident and 0-incident elements). The 1-incident elements can be moved to points on $k$ by adjoining appropriate intersections and deleting the old element. Finally the 0-incident elements can be shifted to points on $k$ as follows: suppose $X$ is a 0-incident point, then choose two points $P$ and $Q$ in $K$ and adjoin the two lines $PX$ and $QX$, then delete $X$; now shift to points on $k$, as above. Note that a 0-incident element will contribute two points on $k$ (as it must, since open rank stays fixed).
