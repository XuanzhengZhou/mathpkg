---
role: proof
locale: en
of_concept: existence-of-ideal-with-given-associated-primes
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

We proceed by induction on $n$, the case $n = 1$ being trivial (take $\mathfrak{a} = \mathfrak{p}_1$).

We may suppose that $\mathfrak{p}_n$ is maximal among the given ideals. By the induction hypothesis, there exists an ideal $\mathfrak{b}$ with irredundant primary representation
$$\mathfrak{b} = \bigcap_{i=1}^{n-1} \mathfrak{q}_i,$$
where $\mathfrak{q}_i$ belongs to $\mathfrak{p}_i$.

The intersection of all primary ideals in $R$ belonging to $\mathfrak{p}_n$ cannot contain $\mathfrak{b}$. For if it did, then $\mathfrak{b}$ would be contained in some isolated prime ideal $\mathfrak{p}$ of $(0)$ (by Theorem 20), and this would imply that $\mathfrak{p}$ coincides with some $\mathfrak{p}_i$ ($1 \leq i \leq n-1$), contradicting the hypothesis that none of the $\mathfrak{p}_i$ is an isolated prime of $(0)$.

Thus there exists a primary ideal $\mathfrak{q}_n$ belonging to $\mathfrak{p}_n$ such that
$$\mathfrak{a} = \bigcap_{i=1}^{n} \mathfrak{q}_i = \mathfrak{b} \cap \mathfrak{q}_n$$
is distinct from $\mathfrak{b}$.

It remains to prove the irredundance of the primary representation $\mathfrak{a} = \bigcap_{i=1}^{n} \mathfrak{q}_i$. By construction, $\mathfrak{q}_n$ does not contain $\mathfrak{b}$, so the component $\mathfrak{q}_n$ is not redundant. For any $i < n$, if $\mathfrak{q}_i$ were redundant, then $\bigcap_{j \neq i} \mathfrak{q}_j \subset \mathfrak{q}_i$. Intersecting both sides with $\mathfrak{q}_n$ would show $\mathfrak{q}_i$ is redundant in the representation of $\mathfrak{b}$ as well, contradicting the induction hypothesis. Thus the representation is irredundant, and the associated primes of $\mathfrak{a}$ are exactly $\mathfrak{p}_1, \dots, \mathfrak{p}_n$.
