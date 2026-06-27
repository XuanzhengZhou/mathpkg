---
role: proof
locale: en
of_concept: components-not-separated-by-clopen-sets
source_book: gtm027
source_chapter: "1"
source_section: "P"
---

# Proof that Components Need Not Be Separated by Clopen Sets

**Proposition.** There exists a topological space $X$ in which two distinct components are not separated by any clopen set; that is, every clopen subset of $X$ contains either both components or neither.

*Proof.* We construct the example as described in Kelley.

For each positive integer $n$, let $A_n = \{1/n\} \times [0,1]$ where $[0,1]$ is the closed unit interval. Let $X$ be the union of all $A_n$ together with the two points $(0,0)$ and $(0,1)$:
$$X = \{(0,0), (0,1)\} \cup \bigcup_{n=1}^\infty A_n,$$
endowed with the subspace topology inherited from the Euclidean plane.

**Step 1: $\{(0,0)\}$ and $\{(0,1)\}$ are components of $X$.**

Each $A_n$ is homeomorphic to $[0,1]$ (via $y \mapsto (1/n, y)$), hence connected. Moreover, for $n \neq m$, $A_n$ and $A_m$ are separated by a positive distance $|1/n - 1/m|$, so they lie in distinct components. The point $(0,0)$ is a limit point of the bottom endpoints $\{(1/n, 0) : n \in \mathbb{N}\}$ and $(0,1)$ is a limit point of the top endpoints $\{(1/n, 1) : n \in \mathbb{N}\}$.

However, $(0,0)$ and $(0,1)$ are not connected to each other via any path or connected subset of $X$: any connected set containing $(0,0)$ would have to "climb" through some $A_n$, but each $A_n$ is a vertical segment whose closure in $X$ only adds $(0,0)$ at the bottom and $(0,1)$ at the top — and they cannot meet in the middle space between columns.

Thus $\{(0,0)\}$ and $\{(0,1)\}$ are distinct components.

**Step 2: Every clopen subset of $X$ contains either both or neither of $\{(0,0)\}$ and $\{(0,1)\}$.**

Let $C \subseteq X$ be clopen (both closed and open). Without loss, assume $(0,0) \in C$.

Since $C$ is open in $X$, there exists an open neighborhood of $(0,0)$ in the plane whose intersection with $X$ is contained in $C$. Any such neighborhood contains all but finitely many of the bottom endpoints $(1/n, 0)$ of the segments $A_n$ (since $(1/n, 0) \to (0,0)$ as $n \to \infty$).

For sufficiently large $n$, $(1/n, 0) \in C$. Since $C$ is closed and each $A_n$ is connected, the entire segment $A_n$ must be contained in $C$ (otherwise $C \cap A_n$ would be a proper clopen subset of the connected space $A_n$).

Thus for all large $n$, $(1/n, 1) \in C$. Since $(1/n, 1) \to (0,1)$ as $n \to \infty$ and $C$ is closed, we have $(0,1) \in C$.

A symmetric argument shows that if $(0,1) \in C$, then $(0,0) \in C$. Therefore any clopen set contains both or neither. $\square$

This example demonstrates that components in a general topological space need not be "separated" by clopen sets; the notion of quasi-component captures the equivalence relation of not being separable by clopen sets.
