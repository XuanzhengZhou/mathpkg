---
role: proof
locale: en
of_concept: going-down-for-integrally-closed-domains
source_book: gtm028
source_chapter: "V"
source_section: "§3. Integrally closed rings"
---

Let $\mathfrak{p}'$ be a prime ideal of $A'$ lying over $\mathfrak{p}$, and set $S = A \setminus \mathfrak{q}$ (the complement of $\mathfrak{q}$ in $A$). Consider the multiplicative set $S' = A \cdot S$ in $A'$ (i.e., the set of products $a \cdot s$ with $a \in A$, $s \in S$). Let $\mathfrak{M}$ be the set of elements of the form $ab'$ where $a \in A$, $a \notin \mathfrak{q}$, $b' \in A'$, $b' \notin \mathfrak{p}'$.

We claim that the ideal $\mathfrak{q}' = A'\mathfrak{q} + \mathfrak{p}'$ does not meet $S'$. Suppose to the contrary that there exist $x \in A'\mathfrak{q}$ and $y \in \mathfrak{p}'$ such that $x + y = s \in S'$. Writing $s = a \cdot s_0$ with $a \in A$, $s_0 \in S$, we may proceed via the reduction modulo $\mathfrak{q}$.

Take any $x \in S = A \setminus \mathfrak{q}$ and $b' \in A' \setminus \mathfrak{p}'$. Let $z = xb' \in S'$. If $z$ belongs to some prime ideal $\mathfrak{q}'$ containing $\mathfrak{p}'$, then $\mathfrak{q}' \cap A$ contains $x$ (since $b' \notin \mathfrak{p}'$ implies $b' \notin \mathfrak{q}'$, and $xb' \in \mathfrak{q}'$ with $\mathfrak{q}'$ prime forces $x \in \mathfrak{q}' \cap A$). But $\mathfrak{q}' \cap A \supset \mathfrak{p}$, and $x \notin \mathfrak{q} \supset \mathfrak{p}$ was chosen arbitrarily from $S$.

The key argument uses the minimal polynomial of an element $x = ab'$ in the multiplicative set: if $f(x) = 0$ is an integral dependence equation with coefficients in $\mathfrak{q}$, then the minimal polynomial $g(X)$ of $x$ modulo $\mathfrak{q}$ has coefficients in $A$ by Theorem 5. Reducing mod $\mathfrak{q}$ and using unique factorization in $A/\mathfrak{q}[X]$, one shows that $\bar{g}(X) = X^r$, contradicting $a \notin \mathfrak{q}$.

Hence the set $S' = (A \setminus \mathfrak{q})A'$ does not meet $\mathfrak{p}' + A'\mathfrak{q}$. By standard prime avoidance, there exists a prime ideal $\mathfrak{q}'$ of $A'$ containing $\mathfrak{p}' + A'\mathfrak{q}$ and disjoint from $S'$. Then $\mathfrak{q}' \cap A$ contains $\mathfrak{q}$ and is contained in $A \setminus S = \mathfrak{q}$, so $\mathfrak{q}' \cap A = \mathfrak{q}$. Thus $\mathfrak{q}'$ lies over $\mathfrak{q}$ and contains $\mathfrak{p}'$.
