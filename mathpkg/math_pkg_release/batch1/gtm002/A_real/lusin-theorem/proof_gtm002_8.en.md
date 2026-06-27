---
role: proof
locale: en
of_concept: lusin-theorem
source_book: gtm002
source_chapter: "8"
source_section: "The Theorems of Lusin and Egoroff"
---

Let $U_1, U_2, \ldots$ be a countable base for the topology of $\mathbb{R}$.

($\Rightarrow$) Suppose $f$ is measurable. For each $i$, $f^{-1}(U_i)$ is measurable, so there exist a closed set $F_i$ and an open set $G_i$ such that
$$F_i \subset f^{-1}(U_i) \subset G_i \quad \text{and} \quad m(G_i - F_i) < \varepsilon/2^i.$$
(This follows from the regularity of Lebesgue measure: every measurable set can be approximated from inside by a closed set and from outside by an open set, with the measure of the difference arbitrarily small.)

Put $E = \bigcup_{i=1}^{\infty}(G_i - F_i)$. Then
$$m(E) \leq \sum_{i=1}^{\infty} m(G_i - F_i) < \sum_{i=1}^{\infty} \varepsilon/2^i = \varepsilon.$$

Let $g$ denote the restriction of $f$ to $\mathbb{R} - E$. For each $i$,
$$g^{-1}(U_i) = f^{-1}(U_i) - E = F_i - E = G_i - E,$$
where the last equality holds because $f^{-1}(U_i) \subset G_i$ and $f^{-1}(U_i) - E \subset G_i - E$, while $G_i - E \subset G_i - (G_i - F_i) = F_i \subset f^{-1}(U_i)$. Thus $g^{-1}(U_i)$ is both closed and open relative to $\mathbb{R} - E$ (it equals $F_i \cap (\mathbb{R} - E)$ and also $G_i \cap (\mathbb{R} - E)$). Since the preimage of every basic open set is clopen in $\mathbb{R} - E$, the function $g$ is continuous.

($\Leftarrow$) Conversely, suppose $f$ has the stated property. Then there exists a sequence of sets $E_i$ with $m(E_i) < 1/i$ such that the restriction $f_i$ of $f$ to $\mathbb{R} - E_i$ is continuous. For any open set $U$, by continuity of $f_i$, the set $f_i^{-1}(U)$ is open in $\mathbb{R} - E_i$, so there exist open sets $G_i \subset \mathbb{R}$ such that
$$f_i^{-1}(U) = G_i \cap (\mathbb{R} - E_i) = G_i - E_i \qquad (i = 1, 2, \ldots).$$

Put $E = \bigcap_{i=1}^{\infty} E_i$. Then $m(E) = 0$. We have
$$f^{-1}(U) - E = \bigcup_{i=1}^{\infty} \bigl( f^{-1}(U) - E_i \bigr) = \bigcup_{i=1}^{\infty} f_i^{-1}(U) = \bigcup_{i=1}^{\infty} (G_i - E_i).$$

Since each $G_i - E_i$ is measurable (difference of an open set and a null set), the union is measurable. Hence $f^{-1}(U) - E$ is measurable. Adding back the null set $E$,
$$f^{-1}(U) = \bigl( f^{-1}(U) - E \bigr) \cup \bigl( f^{-1}(U) \cap E \bigr),$$
where $f^{-1}(U) \cap E \subset E$ is a subset of a null set, hence measurable. Thus $f^{-1}(U)$ is measurable for every open $U$, so $f$ is measurable.
