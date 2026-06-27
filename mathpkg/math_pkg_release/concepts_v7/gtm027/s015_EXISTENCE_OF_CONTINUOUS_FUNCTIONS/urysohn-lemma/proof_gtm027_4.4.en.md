---
role: proof
locale: en
of_concept: urysohn-lemma
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Urysohn's Lemma

**Urysohn's Lemma.** If $A$ and $B$ are disjoint closed subsets of a normal space $X$, then there is a continuous function $f$ on $X$ to the interval $[0,1]$ such that $f$ is zero on $A$ and one on $B$.

*Proof.* Let $D$ be the set of positive dyadic rational numbers (that is, the set of all numbers of the form $p2^{-q}$, where $p$ and $q$ are positive integers). For $t$ in $D$ and $t > 1$ let $F(t) = X$, let $F(1) = X \sim B$ and let $F(0)$ be an open set containing $A$ such that $F(0)^{-}$ is disjoint from $B$. For $t$ in $D$ and $0 < t < 1$ write $t$ in the form $t = (2m + 1)2^{-n}$ and choose, inductively on $n$, $F(t)$ to be an open set containing $F(2m2^{-n})^{-}$ such that $F(t)^{-} \subset F((2m+2)2^{-n})$. This construction is possible because $X$ is normal, so that disjoint closed sets have disjoint open neighborhoods and closed neighborhoods form a base for the neighborhood system of a closed set.

The family $\{F(t): t \in D\}$ then satisfies the hypotheses of Lemma 2 (by extending $D$ to include $0$ and values $>1$ appropriately). Define $f(x) = \inf \{t: x \in F(t)\}$. By Lemma 2, $\{x: f(x) < s\} = \bigcup \{F(t): t < s\}$ is open and $\{x: f(x) \leq s\} = \bigcap \{F(t): t > s\}$ is closed. Moreover, if $x \in A$ then $x \in F(0)$ so $f(x) = 0$, and if $x \in B$ then $x \notin F(1)$ so $f(x) = 1$. The continuity of $f$ follows from the fact that the sets $\{x: f(x) < s\}$ are open and $\{x: f(x) > s\} = X \sim \{x: f(x) \leq s\}$ is open.

