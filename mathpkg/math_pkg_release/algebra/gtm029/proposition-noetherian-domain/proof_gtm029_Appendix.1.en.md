---
role: proof
locale: en
of_concept: proposition-noetherian-domain
source_book: gtm029
source_chapter: "Appendix"
source_section: "1"
---

If $x \in o$ is a non-unit in $o$ it must be a non-unit in at least one of the rings $\mathfrak{D}_i$. Thus $x$ belongs to one of the ideals $m_i$. This proves the lemma, in view of Lemma 2.

Let $R = k[x, y]$ be a polynomial ring in two independent variables $x, y$ over a field $k$. We fix a zero-dimensional discrete valuation $v$, of rank 1, which is non-negative on $R$, has $k$ as residue field, and is such that $v(x) = 1$ (see VI, §15, Example 2). Furthermore, we assume that the center of $v$ in $R$ is the maximal ideal $(x, y)$ of $R$. We set $\mathfrak{D}_1 = R_v = \text{valuation ring of } v$. We then consider the point $x = 1$, $y = 0$ in the $(x, y)$-plane and we denote by $\mathfrak{D}_2$ the local ring of that point, i.e., the ring of quotients of $k[x, y]$ with respect to the maximal ideal $(x - 1, y)$. If $\mathfrak{M}_1 = \mathfrak{D}_1 x$ and $\mathfrak{M}_2 = \mathfrak{D}_2 (x - 1, y)$ denote the maximal ideals of $\mathfrak{D}_1$ and $\mathfrak{D}_2$ respectively, we set $o' = \mathfrak{D}_1 \cap \mathfrak{D}_2$, $m'_1 = \mathfrak{M}_1 \cap o'$, $m'_2 = \mathfrak{M}_2 \cap o'$.

Since $o' \supset k[x, y]$ it is clear

for some $n$. Without loss of generality, we may assume that this is so already for $n=1$. Then

$$\mathfrak{A}_1 \subset \mathfrak{A}_2 \subset \cdots \subset \mathfrak{A}_1 \mathfrak{o}'$$

and this shows, by what we have just proved above, that $\mathfrak{A}_q = \mathfrak{A}_{q+1} = \cdots$ for some $q$. Hence $\mathfrak{o}$ is noetherian.

We have $h(m'_1) = 1$, $h(m'_2) = 2$, whence $\dim (\mathfrak{o}') = 2$. By the dimension theory of semi-local rings we have $\dim (\mathfrak{o}) = 2$, since $\mathfrak{o}'$ is integral over $\mathfrak{o}$. Therefore $h(m) = 2$. On the other hand, $h(m'_1) = 1 < h(m)$, and the $m'_1$-residue of $x$ is algebraic over $\mathfrak{o}/m$ (= $k$; in fact, that residue is equal to 0). Therefore, the dimension formula (5) does not hold for $\mathfrak{o}, \mathfrak{o}'$, with $\mathfrak{p} = m$ and $\mathfrak{p}' = m'_1$. Consequently, $\mathfrak{o}[T]$ does not satisfy the chain condition for prime ideals.
