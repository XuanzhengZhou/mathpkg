---
role: proof
locale: en
of_concept: neighborhood-of-zero-set-closure
source_book: gtm043
source_chapter: "7"
source_section: "14 (7.14)"
---

**Necessity.** Since $\mathrm{cl}_{\beta X} Z(g)$ is compact and contained in the interior of $\mathrm{cl}_{\beta X} Z(f)$, there exists $h \in C^*(X)$ such that $h^\beta$ is equal to $1$ on the compact set $\mathrm{cl}_{\beta X} Z(g)$, and $0$ on $\beta X \setminus \mathrm{cl}_{\beta X} Z(f)$. Then $X \setminus Z(h)$ contains $Z(g)$ and is contained in $Z(f)$, i.e., $Z(f) \supset X \setminus Z(h) \supset Z(g)$.

**Sufficiency.** If $h$ is as described, then $Z(h)$ is disjoint from $Z(g)$, and so their closures in $\beta X$ are disjoint. Also, $Z(f) \cup Z(h) = X$, so that
$$\mathrm{cl}_{\beta X} Z(f) \cup \mathrm{cl}_{\beta X} Z(h) = \beta X.$$
Therefore,
$$\mathrm{cl}_{\beta X} Z(f) \supset \beta X \setminus \mathrm{cl}_{\beta X} Z(h) \supset \mathrm{cl}_{\beta X} Z(g).$$
Thus, $\mathrm{cl}_{\beta X} Z(f)$ is a neighborhood of $\mathrm{cl}_{\beta X} Z(g)$.
