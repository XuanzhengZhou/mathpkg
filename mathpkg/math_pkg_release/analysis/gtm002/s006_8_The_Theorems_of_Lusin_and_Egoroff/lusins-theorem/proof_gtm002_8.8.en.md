---
role: proof
locale: en
of_concept: lusins-theorem
source_book: gtm002
source_chapter: "8"
source_section: "8"
---

Let $\{U_1, U_2, \ldots\}$ be a countable base for the topology of $\mathbb{R}$, for example the open intervals with rational endpoints.

**($\Rightarrow$)** Suppose $f$ is measurable and fix $\varepsilon > 0$. For each $i$, the set $f^{-1}(U_i)$ is measurable. By the regularity of Lebesgue measure, there exist a closed set $F_i$ and an open set $G_i$ such that

$$
F_i \subset f^{-1}(U_i) \subset G_i \quad \text{and} \quad m(G_i \setminus F_i) < \frac{\varepsilon}{2^i}.
$$

Define

$$
E = \bigcup_{i=1}^{\infty} (G_i \setminus F_i).
$$

Then $m(E) < \sum_{i=1}^{\infty} \varepsilon/2^i = \varepsilon$. Let $g$ be the restriction of $f$ to $\mathbb{R} \setminus E$. For each $i$, we have

$$
g^{-1}(U_i) = f^{-1}(U_i) \setminus E.
$$

Since $F_i \subset f^{-1}(U_i) \subset G_i$, we obtain

$$
F_i \setminus E \subset g^{-1}(U_i) \subset G_i \setminus E.
$$

But $F_i \setminus E = G_i \setminus E$, because any point in $G_i \setminus F_i$ lies in $E$. Hence

$$
g^{-1}(U_i) = F_i \setminus E = G_i \setminus E
$$

is both closed and open relative to $\mathbb{R} \setminus E$. Since the $U_i$ form a base, $g$ is continuous.

**($\Leftarrow$)** Conversely, suppose that for each $\varepsilon > 0$, $f$ is continuous off a set of measure less than $\varepsilon$. In particular, there exists a sequence of sets $E_k$ with $m(E_k) < 1/k$ such that the restriction $f_k = f|_{\mathbb{R} \setminus E_k}$ is continuous. Let $U$ be any open set. For each $k$, since $f_k$ is continuous, $f_k^{-1}(U)$ is relatively open in $\mathbb{R} \setminus E_k$, so there exists an open set $G_k$ such that

$$
f_k^{-1}(U) = G_k \setminus E_k.
$$

Set $E = \bigcap_{k=1}^{\infty} E_k$. Then $m(E) = 0$. Now

$$
f^{-1}(U) \setminus E = \bigcup_{k=1}^{\infty} \bigl(f^{-1}(U) \setminus E_k\bigr)
= \bigcup_{k=1}^{\infty} f_k^{-1}(U)
= \bigcup_{k=1}^{\infty} (G_k \setminus E_k).
$$

Each $G_k \setminus E_k$ is the difference of an open set and a null set, hence measurable. The countable union of measurable sets is measurable, so $f^{-1}(U) \setminus E$ is measurable. Since $f^{-1}(U) = (f^{-1}(U) \setminus E) \cup (f^{-1}(U) \cap E)$ and $f^{-1}(U) \cap E$ is a subset of the null set $E$, it is measurable as well (by completeness of Lebesgue measure). Hence $f^{-1}(U)$ is measurable. Since $U$ was arbitrary, $f$ is measurable.
