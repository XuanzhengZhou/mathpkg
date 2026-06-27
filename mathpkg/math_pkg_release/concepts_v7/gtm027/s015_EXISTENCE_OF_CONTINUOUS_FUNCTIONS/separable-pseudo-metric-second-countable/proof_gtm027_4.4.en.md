---
role: proof
locale: en
of_concept: separable-pseudo-metric-second-countable
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Separable Pseudo-Metric Spaces are Second Countable

**Theorem 11.** A pseudo-metric space is separable if and only if its topology satisfies the second axiom of countability.

*Proof.* Each space which satisfies the second axiom of countability is separable, so it remains to prove that a separable pseudo-metric space has a countable base for its topology. Let $Y$ be a countable dense subset and let $\mathcal{U}$ be the family of all open spheres with rational radii about members of $Y$. Surely $\mathcal{U}$ is countable. If $U$ is a neighborhood of a point $x$ there is, for some positive $r$, an open $r$-sphere about $x$ which is contained in $U$. Let $s$ be a positive rational number less than $r$, let $y$ be a point of $Y$ such that $d(x,y) < s/3$, and let $V$ be the open $2s/3$-sphere about $y$. Then $x \in V$ (since $d(x,y) < s/3 < 2s/3$) and for any $z \in V$, $d(x,z) \leq d(x,y) + d(y,z) < s/3 + 2s/3 = s < r$, so $V \subset U$. Hence $\mathcal{U}$ is a base for the topology.

