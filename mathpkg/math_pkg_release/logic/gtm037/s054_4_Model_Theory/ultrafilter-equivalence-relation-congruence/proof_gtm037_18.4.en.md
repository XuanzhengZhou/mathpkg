---
role: proof
locale: en
of_concept: ultrafilter-equivalence-relation-congruence
source_book: gtm037
source_chapter: "18"
source_section: "4"
---

The proof is routine; we check transitivity of $\equiv_F$ and compatibility with an operation symbol as representative cases.

**Transitivity.** Assume that $x \equiv_F y \equiv_F z$. Thus $\{i \in I : x_i = y_i\} \in F$ and $\{i \in I : y_i = z_i\} \in F$. But
$$\{i \in I : x_i = y_i\} \cap \{i \in I : y_i = z_i\} \subseteq \{i \in I : x_i = z_i\},$$
so also $\{i \in I : x_i = z_i\} \in F$, and so $x \equiv_F z$.

**Compatibility with operations.** Let $\mathbf{O}$ be an $m$-ary operation symbol, and suppose $x_t \equiv_F y_t$ for all $t < m$. Note that
$$\{i \in I : \forall t < m\,(x_{ti} = y_{ti})\} = \bigcap_{t < m} \{i \in I : x_{ti} = y_{ti}\} \in F,$$
since $F$ is closed under finite intersections. Moreover,
$$\{i \in I : \forall t < m\,(x_{ti} = y_{ti})\} \subseteq \{i \in I : (\mathbf{O}^{\mathfrak{B}}x)_i = (\mathbf{O}^{\mathfrak{B}}y)_i\}$$
because operations are defined coordinate-wise. Hence $\{i \in I : (\mathbf{O}^{\mathfrak{B}}x)_i = (\mathbf{O}^{\mathfrak{B}}y)_i\} \in F$, so $\mathbf{O}^{\mathfrak{B}}x \equiv_F \mathbf{O}^{\mathfrak{B}}y$.

Reflexivity, symmetry, and compatibility with relation symbols are similarly straightforward.
