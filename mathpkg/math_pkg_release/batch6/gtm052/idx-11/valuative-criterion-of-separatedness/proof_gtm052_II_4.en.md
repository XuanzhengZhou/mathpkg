---
role: proof
locale: en
of_concept: valuative-criterion-of-separatedness
source_book: gtm052
source_chapter: "II"
source_section: "4"
---

($\Rightarrow$) Suppose $f$ is separated, and suppose we have two morphisms $h, h': T \to X$ making the diagram commute. Then we obtain a morphism $h'': T \to X \times_Y X$. Since the restrictions of $h$ and $h'$ to $U$ are the same, the generic point $t_1$ of $T$ has image in the diagonal $\Delta(X)$. Since $\Delta(X)$ is closed, the image of $t_0$ is also in the diagonal. Therefore $h$ and $h'$ both send the points $t_0, t_1$ to the same points $x_0, x_1$ of $X$. Since the inclusions of $k(x_1) \subseteq K$ induced by $h$ and $h'$ are also the same, it follows from (4.4) that $h$ and $h'$ are equal.

($\Leftarrow$) Suppose the condition holds. To show $f$ is separated, it suffices by (4.2) to show that $\Delta(X)$ is a closed subset of $X \times_Y X$. Since $X$ is noetherian, the morphism $\Delta$ is quasi-compact, so by (4.5) it suffices to show that $\Delta(X)$ is stable under specialization. Let $\xi_1 \in \Delta(X)$ be a point, and let $\xi_1 \rightsquigarrow \xi_0$ be a specialization. Let $K = k(\xi_1)$ and let $\mathcal{O}$ be the local ring of $\xi_0$ on the subscheme $\{\xi_1\}^-$ with its reduced induced structure. Then $\mathcal{O}$ is a local ring contained in $K$, so by (I, 6.1A) there is a valuation ring $R$ of $K$ which dominates $\mathcal{O}$. Now by (4.4) we obtain a morphism of $T = \operatorname{Spec} R$ to $X \times_Y X$ sending $t_0$ and $t_1$ to $\xi_0$ and $\xi_1$. Composing with the projections $p_1, p_2$ gives two morphisms of $T$ to $X$, which give the same morphism to $Y$, and whose restrictions to $U = \operatorname{Spec} K$ are the same. By the condition, these two morphisms agree, so the image of $T$ lies in $\Delta(X)$. Thus $\xi_0 \in \Delta(X)$, so $\Delta(X)$ is stable under specialization.
