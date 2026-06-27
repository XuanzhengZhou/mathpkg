---
role: proof
locale: en
of_concept: nondissipative-iff-recurrence
source_book: gtm002
source_chapter: "17"
source_section: "The Poincaré Recurrence Theorem"
---

**($\Rightarrow$) Forward direction.** Suppose $T$ is nondissipative. Consider any $E \in \mathcal{S}$, and let

$$F = E - \bigcup_{k=1}^{\infty} T^{-k}E.$$

Since $T$ is $\mathcal{S}$-measurable and $\mathcal{S}$ is a $\sigma$-ring, $F$ belongs to $\mathcal{S}$. The sets $F, T^{-1}F, T^{-2}F, \ldots$ are mutually disjoint; indeed, if $x \in T^{-i}F \cap T^{-j}F$ with $i < j$, then $T^i x \in F$ and $T^j x \in F$, which would imply $T^j x = T^{j-i}(T^i x) \in T^{j-i}F \subset \bigcup_{k=1}^{\infty} T^{-k}E$, contradicting $T^j x \in F$.

Thus $F$ is a wandering set belonging to $\mathcal{S}$. Since $T$ is nondissipative, $F \in \mathcal{I}$. Now observe that $D(E)$ can be expressed as a countable union of such wandering sets: the points of $E$ that return at most finitely many times are those that eventually leave $E$ forever. Specifically,

$$D(E) \subset \bigcup_{n=0}^{\infty} \left(E \cap \bigcap_{k > n} T^{-k}(X - E)\right).$$

Each term in this union is a wandering set up to a transformation of the same form as $F$, hence belongs to $\mathcal{I}$. Since $\mathcal{I}$ is a $\sigma$-ideal, $D(E) \in \mathcal{I}$. Therefore $T$ has the recurrence property.

**($\Leftarrow$) Reverse direction.** Suppose $T$ has the recurrence property. Let $E$ be any wandering set belonging to $\mathcal{S}$. For any $x \in E$, the points $T^i x$ ($i \geq 0$) lie in at most one of the sets $E, T^{-1}E, T^{-2}E, \ldots$ because the preimages are mutually disjoint. In fact, if $x \in E$, then $T^i x \notin E$ for any $i > 0$ (otherwise $x$ would belong to both $E$ and $T^{-i}E$). Hence $E \subset D(E)$. By the recurrence property, $D(E) \in \mathcal{I}$, so $E \in \mathcal{I}$. Thus no wandering set can belong to $\mathcal{S} - \mathcal{I}$, which means $T$ is nondissipative. $\square$

**Applications.** In the measure-theoretic setting, take $\mathcal{S}$ to be the $\sigma$-algebra of measurable sets and $\mathcal{I}$ the $\sigma$-ideal of nullsets. If $X$ has finite total measure and $T$ is measure-preserving, then any measurable wandering set must be a nullset, so $T$ is nondissipative and therefore has the recurrence property. In the category setting, take $\mathcal{S}$ to be the $\sigma$-algebra of sets having the property of Baire and $\mathcal{I}$ the $\sigma$-ideal of first category sets. Using the Banach category theorem, there is a largest open set of first category $H$, and on the invariant complement $Y = X - \overline{H}$, any wandering set with the property of Baire must be of first category, so $T$ is nondissipative on $Y$ and the recurrence property follows.
