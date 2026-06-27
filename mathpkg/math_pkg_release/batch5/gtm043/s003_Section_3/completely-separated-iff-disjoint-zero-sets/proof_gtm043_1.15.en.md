---
role: proof
locale: en
of_concept: completely-separated-iff-disjoint-zero-sets
source_book: gtm043
source_chapter: "1"
source_section: "1.15"
---

**Sufficiency.** If $Z(f) \cap Z(g) = \emptyset$, then $|f| + |g|$ has no zeros, and we may define
$$h(x) = \frac{|f(x)|}{|f(x)| + |g(x)|} \quad (x \in X),$$
in brief, $h = |f| \cdot (|f| + |g|)^{-1}$. Then $h \in C(X)$, and $h$ is equal to $0$ on $Z(f)$ and to $1$ on $Z(g)$. Thus the sets $Z(f)$ and $Z(g)$ are completely separated.

**Necessity.** If $A$ and $A'$ are completely separated, there exists $f \in C(X)$ equal to $0$ on $A$ and to $1$ on $A'$. The disjoint sets
$$F = \{x: f(x) \leq \tfrac{1}{3}\}, \quad F' = \{x: f(x) \geq \tfrac{2}{3}\}$$
are zero-set-neighborhoods of $A$ and $A'$, respectively. Moreover, if $A$ and $A'$ are completely separated, there exist zero-sets $F$ and $Z$ such that
$$A \subset X - Z \subset F \subset X - A',$$
by taking $F$ as above and $Z = \{x: f(x) \geq \tfrac{1}{3}\}$.
