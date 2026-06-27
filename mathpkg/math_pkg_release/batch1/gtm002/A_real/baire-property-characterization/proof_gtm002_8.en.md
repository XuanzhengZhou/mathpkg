---
role: proof
locale: en
of_concept: baire-property-characterization
source_book: gtm002
source_chapter: "8"
source_section: "The Theorems of Lusin and Egoroff"
---

Let $U_1, U_2, \ldots$ be a countable base for the topology of $\mathbb{R}$ (for example, the open intervals with rational endpoints).

($\Rightarrow$) Suppose $f$ has the property of Baire. Then for each $i$, $f^{-1}(U_i)$ has the property of Baire, so we can write
$$f^{-1}(U_i) = G_i \triangle P_i,$$
where $G_i$ is open and $P_i$ is of first category. Put $P = \bigcup_{i=1}^{\infty} P_i$. Since a countable union of first-category sets is of first category, $P$ is of first category. Let $g$ be the restriction of $f$ to $\mathbb{R} - P$. For each $i$,
$$g^{-1}(U_i) = f^{-1}(U_i) \cap (\mathbb{R} - P) = (G_i \triangle P_i) \cap (\mathbb{R} - P).$$
Since $P_i \subset P$, we have $P_i \cap (\mathbb{R} - P) = \emptyset$. Moreover, $G_i \cap P_i \subset P_i \subset P$, so $(G_i \setminus P_i) \cap (\mathbb{R} - P) = G_i \cap (\mathbb{R} - P)$. Thus
$$g^{-1}(U_i) = G_i \cap (\mathbb{R} - P),$$
which is open in the relative topology of $\mathbb{R} - P$. Since the $U_i$ form a base, $g$ is continuous.

($\Leftarrow$) Conversely, suppose there exists a first-category set $P$ such that the restriction of $f$ to $\mathbb{R} - P$ is continuous. For any basic open set $U_i$, the set $f^{-1}(U_i) \cap (\mathbb{R} - P)$ is open in $\mathbb{R} - P$, so there exists an open set $G_i \subset \mathbb{R}$ such that
$$f^{-1}(U_i) \cap (\mathbb{R} - P) = G_i \cap (\mathbb{R} - P).$$
Then
$$f^{-1}(U_i) = \bigl( f^{-1}(U_i) \cap (\mathbb{R} - P) \bigr) \cup \bigl( f^{-1}(U_i) \cap P \bigr) = \bigl( G_i \cap (\mathbb{R} - P) \bigr) \cup \bigl( f^{-1}(U_i) \cap P \bigr).$$
Now $G_i = \bigl( G_i \cap (\mathbb{R} - P) \bigr) \cup \bigl( G_i \cap P \bigr)$, and $G_i \cap P$ is of first category (as a subset of $P$). Also $f^{-1}(U_i) \cap P$ is a subset of $P$, hence of first category. Therefore
$$f^{-1}(U_i) = G_i \triangle \bigl( (G_i \cap P) \triangle (f^{-1}(U_i) \cap P) \bigr),$$
where the symmetric difference term is of first category. Thus $f^{-1}(U_i)$ has the property of Baire for each $i$, and consequently for every open set $U$. Hence $f$ has the property of Baire.
