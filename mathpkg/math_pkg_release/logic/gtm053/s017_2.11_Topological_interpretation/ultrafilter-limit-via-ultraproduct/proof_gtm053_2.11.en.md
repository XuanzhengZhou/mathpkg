---
role: proof
locale: en
of_concept: ultrafilter-limit-via-ultraproduct
source_book: gtm053
source_chapter: "2"
source_section: "2.11"
---

The Stone space $\mathcal{S}$ is Hausdorff because distinct elementary equivalence classes $[\mathbf{A}] \neq [\mathbf{B}]$ are separated by some $L$-sentence $P$ with $\mathbf{A} \vDash P$ and $\mathbf{B} \vDash \neg P$, so $[P]$ and $[\neg P]$ are disjoint open neighborhoods. By the topological compactness theorem, $\mathcal{S}$ is also compact. In any compact Hausdorff space, every ultrafilter converges to a unique limit point.

Let $I \subseteq \mathcal{S}$ and let $U$ be an ultrafilter on $I$. For each $i \in I$, choose a representative structure $\mathbf{A}_i \in \mathbf{S}$ whose elementary equivalence class is $i$. Form the ultraproduct
$$\mathbf{A}_U = \prod_{i \in I} \mathbf{A}_i / U,$$
and let $[\mathbf{A}_U]$ be its elementary equivalence class in $\mathcal{S}$.

We claim $\lim_U I = [\mathbf{A}_U]$. For any basic open neighborhood $[P]$ of $[\mathbf{A}_U]$, we have $\mathbf{A}_U \vDash P$. By Łoś's theorem,
$$\mathbf{A}_U \vDash P \iff \{i \in I : \mathbf{A}_i \vDash P\} \in U.$$
Thus $U$-almost all $i$ satisfy that the corresponding point lies in $[P]$, which is precisely the condition that $U$ converges to $[\mathbf{A}_U]$. Uniqueness follows from the Hausdorff property.
