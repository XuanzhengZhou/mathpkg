---
role: proof
locale: en
of_concept: non-meager-w-star-bounded-equicontinuous
source_book: gtm027
source_chapter: "7"
source_section: "N"
---

# Proof of Equicontinuity of Weak-Star Bounded Sets in Non-Meager Spaces

Let $X$ be a non-meager topological vector space (in particular, if $X$ is complete). We prove that every $w^*$-bounded subset $F \subseteq X^*$ is equicontinuous.

**Proof.** For each $n \in \mathbb{N}$, define

$$A_n = \{x \in X : |f(x)| \leq n \text{ for all } f \in F\}.$$

Since $F$ is $w^*$-bounded, for each $x \in X$ the set $\{f(x) : f \in F\}$ is bounded, so there exists $n$ such that $x \in A_n$. Thus $X = \bigcup_{n=1}^\infty A_n$.

Each $A_n$ is closed: $A_n = \bigcap_{f \in F} \{x : |f(x)| \leq n\}$, and each $f \in X^*$ is continuous, so each set $\{x : |f(x)| \leq n\}$ is closed.

Since $X$ is non-meager (i.e., of second category in itself), at least one $A_n$ has nonempty interior. Thus there exists $n_0$ and an open set $U \neq \varnothing$ with $U \subseteq A_{n_0}$. Translating by an element of $U$, we obtain a neighborhood $V = U - x_0$ of $0$ (for some $x_0 \in U$) such that for all $f \in F$ and $v \in V$,

$$|f(v)| = |f(x_0 + v) - f(x_0)| \leq |f(x_0 + v)| + |f(x_0)| \leq 2n_0.$$

After scaling, $F$ is uniformly bounded on a neighborhood of $0$, which is the definition of equicontinuity for a family of linear functionals.

For complete spaces, the Baire Category Theorem ensures they are non-meager, so the result applies. The hypothesis "non-meager" is necessary: consider $X$ as the space of all real sequences with only finitely many nonzero entries (a meager space), where point evaluations form a $w^*$-bounded but not equicontinuous family.
