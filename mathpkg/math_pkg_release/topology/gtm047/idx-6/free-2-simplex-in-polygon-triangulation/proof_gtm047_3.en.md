---
role: proof
locale: en
of_concept: free-2-simplex-in-polygon-triangulation
source_book: gtm047
source_chapter: "3"
source_section: "The Schönflies theorem for polygons in R^2"
---

We prove, by induction, the stronger assertion that $K$ has at least two free 2-simplexes. If $K$ has exactly two 2-simplexes, then this is clear. We may assume, then, that $K$ has more than two 2-simplexes; and we may assume, as an induction hypothesis, that our conclusion holds for every complex $L$ which is a triangulation of a region of the type $\bar{I}$ and has fewer 2-simplexes than $K$.

There are at least two 2-simplexes $\sigma, \tau$ of $K$ which have an edge in $\operatorname{Fr}|K|$. If both of them are free, then there is nothing to prove. Suppose, then, that

$$\sigma = v_0 v_1 v_2 \in K, \quad v_0 v_1 \subset \operatorname{Fr}|K|,$$

and $\sigma$ is not free. Then neither $v_0 v_2$ nor $v_1 v_2$ lies in $\operatorname{Fr}|K|$. The segment $v_0 v_2$ divides $J = \operatorname{Fr}|K|$ into two broken lines $C_1$ and $C_2$; and $|K| = \bar{I}_1 \cup \bar{I}_2$, where $I_1$ and $I_2$ are the interiors of $C_1 \cup v_0v_2$ and $C_2 \cup v_0v_2$ respectively.

Let $L_1$ be the complex consisting of the simplexes of $K$ that lie in $\bar{I}_1$, together with $v_0v_1v_2$ and its faces. Let $L_2$ be the set of all simplexes of $K$ that lie in $\bar{I}_2$. By the induction hypothesis, each of the complexes $L_i$ has two free 2-simplexes. Therefore each of them has a free 2-simplex $\sigma_i$, different from $v_0v_1v_2$. It follows that each $\sigma_i$ is free not only in $L_i$ but also in $K$, which was to be proved.
