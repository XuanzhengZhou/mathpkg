---
role: proof
locale: en
of_concept: intersection-of-hyperplanes-containing-variety
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Intersection of All Hyperplanes Containing a Linear Variety

Let $E$ be a vector space over $\mathbb{K}$. Let $V = x + N$ be a proper linear variety in $E$, where $x \in E$ and $N$ is a linear subspace of $E$. Denote by $\mathcal{H}(V)$ the family of all hyperplanes in $E$ that contain $V$.

**Theorem 21.9.** $\bigcap_{H \in \mathcal{H}(V)} H = V$.

(By convention, the intersection of an empty family of subsets of $E$ equals $E$, which accounts for the case $V = E$ where no hyperplane can contain $V$.)

*Proof.*

Assume $V \subsetneq E$, so $N$ is a proper subspace of $E$.

First, we establish that as $M$ varies over all maximal linear subspaces containing $N$, the set $H = x + M$ varies over all hyperplanes containing $V = x + N$. Indeed, by Theorem 21.7, every hyperplane in $E$ has the form $z + M$ with $M$ a maximal linear subspace, and by Lemma 21.5, $x + N \subset x + M$ if and only if $N \subset M$ (since $(x + N) \subset (x + M) \iff N \subset M$ and $x - x = 0 \in M$). Conversely, given $H = z + M$ with $M$ maximal and $M \supset N$ such that $x + N \subset z + M$, we also have $x \in z + M$, so $x + M = z + M = H$. Thus every hyperplane containing $V$ is of the form $x + M$ for some maximal subspace $M \supset N$.

Now, let $\mathcal{M}(N)$ be the family of all maximal linear subspaces containing $N$. By Theorem 21.8, $\bigcap_{M \in \mathcal{M}(N)} M = N$. Therefore

$$\bigcap_{H \in \mathcal{H}(V)} H = \bigcap_{M \in \mathcal{M}(N)} (x + M) = x + \bigcap_{M \in \mathcal{M}(N)} M = x + N = V.$$

The equality $\bigcap (x + M) = x + \bigcap M$ holds because $y \in \bigcap (x + M)$ iff $y - x \in M$ for all $M \in \mathcal{M}(N)$ iff $y - x \in \bigcap \mathcal{M}(N) = N$ iff $y \in x + N$.

Thus every linear variety in $E$ (other than $E$ itself) is an intersection of hyperplanes.
