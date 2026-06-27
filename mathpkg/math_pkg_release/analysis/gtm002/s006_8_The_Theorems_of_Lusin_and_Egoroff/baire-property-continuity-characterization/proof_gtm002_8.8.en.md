---
role: proof
locale: en
of_concept: baire-property-continuity-characterization
source_book: gtm002
source_chapter: "8"
source_section: "8"
---

Let $\{U_1, U_2, \ldots\}$ be a countable base for the topology of $\mathbb{R}$, for example the open intervals with rational endpoints.

**($\Rightarrow$)** Suppose $f$ has the property of Baire. Then for each $i$, the set $f^{-1}(U_i)$ has the property of Baire, so we can write

$$
f^{-1}(U_i) = G_i \triangle P_i,
$$

where $G_i$ is open and $P_i$ is of first category. Define

$$
P = \bigcup_{i=1}^{\infty} P_i.
$$

As a countable union of first-category sets, $P$ is of first category. Let $g$ be the restriction of $f$ to $\mathbb{R} \setminus P$. For each $i$, we have

$$
g^{-1}(U_i) = f^{-1}(U_i) \setminus P = (G_i \triangle P_i) \setminus P = G_i \setminus P,
$$

since $P_i \subset P$ and $(G_i \cap P_i) \setminus P = \emptyset$. Thus $g^{-1}(U_i) = G_i \cap (\mathbb{R} \setminus P)$ is open in the relative topology of $\mathbb{R} \setminus P$. Since the $U_i$ form a base, $g$ is continuous.

**($\Leftarrow$)** Conversely, suppose there exists a first-category set $P$ such that $g = f|_{\mathbb{R} \setminus P}$ is continuous. Let $U$ be any open set in $\mathbb{R}$. Since $g$ is continuous, $g^{-1}(U)$ is relatively open in $\mathbb{R} \setminus P$, so there exists an open set $V \subset \mathbb{R}$ such that

$$
g^{-1}(U) = V \cap (\mathbb{R} \setminus P) = V \setminus P.
$$

Now

$$
f^{-1}(U) = g^{-1}(U) \cup \bigl(f^{-1}(U) \cap P\bigr) = (V \setminus P) \cup A,
$$

where $A = f^{-1}(U) \cap P \subset P$ is of first category (as a subset of a first-category set). Then

$$
f^{-1}(U) \triangle V = \bigl((V \setminus P) \cup A\bigr) \triangle V \subset P \cup A,
$$

which is of first category. Hence $f^{-1}(U)$ has the property of Baire. Since $U$ was arbitrary, $f$ has the property of Baire.
