---
role: proof
locale: en
of_concept: existence-of-weakly-convergent-sequence
source_book: gtm036
source_chapter: "Chapter 5: Dual Spaces"
source_section: "L: Existence of Weakly Convergent Sequence"
---

(Sketch of proof) Let $\{U_n : n = 1, 2, \cdots\}$ be a local base for the topology of $E$ with $U_{n+1} \subset U_n$ for each $n$, and let $x$ be a point of the weak closure of $A$.

For each $n$, apply Theorem 8.21 (the bipolar theorem) to show the existence of a sequence in $A$ that converges pointwise to $x$ on $U_n^\circ$, the polar of $U_n$. That is, for each $n$ there exists a sequence $\{a_{n,k}\}_{k=1}^\infty \subseteq A$ such that $\langle a_{n,k}, f \rangle \to \langle x, f \rangle$ for every $f \in U_n^\circ$.

Enumerate the points of all these sequences triangular-wise (i.e., by a diagonal enumeration) to form a single sequence $\{x_k\}$. Then $x$ is a weak cluster point of $\{x_k\}$.

Let $H$ be the closed subspace of $E$ spanned by $\{x_k\}$. Since $E$ is metrizable, $H$ is also metrizable. Moreover, $H$ is separable because it is spanned by the countable set $\{x_k\}$.

Now $x$ belongs to the weak closure of $A \cap H$ in $H$. Since $H$ is separable and metrizable, the weak* topology on bounded subsets of $H^*$ is metrizable. It follows from the earlier results (items (a) and (b) of Section K) that the weak topology on bounded subsets of $H$ is also metrizable. Since $\{x_k\}$ is a bounded sequence (being contained in a metrizable space) and $x$ is a weak cluster point, one can extract a subsequence of $\{x_k\}$ that converges weakly to $x$. This subsequence consists of points of $A$, completing the proof.
