---
role: proof
locale: en
of_concept: compositum-degree-inequalities
source_book: gtm028
source_chapter: "II"
source_section: "§16. Order of inseparability"
---

**Proof.** Let $\{u_1, u_2, \dots, u_n\}$ be a basis of $K$ over $L$. Since the elements of $K$ are algebraic over the field $(L, k')$, we have $(K, k') = (L, k')[K] = (L, k') \sum_{q=1}^{n} L u_q = \sum_{q=1}^{n} (L, k') u_q$, and this proves inequality (1).

Let $K_0$ be the maximal separable extension of $L$ in $K$. From the separability of the extension $K_0 / L$ follows the separability of the extension $(K_0, k') / (L, k')$, while from the fact that $K/K_0$ is purely inseparable it follows that $(K, k')/(K_0, k')$ is purely inseparable. Hence $[(K, k') : (L, k')]_s = [(K_0, k') : (L, k')] \leq [K_0 : L] = [K : L]_s$, proving (2). Inequality (3) follows from (1) and (2) since $[\,\cdot\, : \,\cdot\,]_i = [\,\cdot\, : \,\cdot\,] / [\,\cdot\, : \,\cdot\,]_s$.

Now assume $K$ and $k'$ are linearly disjoint over a common subfield $k$ of $L$ and $k'$. Let $\{v_1, \dots, v_r\}$ be elements of $K$ that are linearly independent over $L$. We need to show they remain linearly independent over $(L, k')$. Any linear relation over $(L, k')$ can be written with coefficients that are rational functions in elements of $k'$ with coefficients in $L$:

$$\sum_i \frac{f_i}{g} v_i = 0,$$

where the $f_i$ belong to $k'[L]$. The numerators are linearly independent over $L$ and we have to show that they are also linearly independent over $K$. In other words, it is sufficient to show the linear disjointness of $K$ and $k'[L]$ over $L$. Now the ring $k'[L]$, regarded as a vector space over $L$, is spanned by the field $k'$. Hence we can find a basis $B$ of $k'[L]$ over $L$ such that $B \subset k'$. The elements of $B$ are linearly independent over $L$, hence a fortiori also over $k$. It follows that the elements of $B$ are also linearly independent over $K$, since $k'$ and $K$ are linearly disjoint over $k$. We have therefore shown that the vector space $k'[L]/L$ has an $L$-basis $B$ whose elements are linearly independent over $K$, and the linear disjointness of $k'[L]$ and $K$ over $L$ now follows from the lemma proved in §15. Therefore $[(K, k') : (L, k')] = [K : L]$, and the equalities for the separable and inseparable degrees follow.
