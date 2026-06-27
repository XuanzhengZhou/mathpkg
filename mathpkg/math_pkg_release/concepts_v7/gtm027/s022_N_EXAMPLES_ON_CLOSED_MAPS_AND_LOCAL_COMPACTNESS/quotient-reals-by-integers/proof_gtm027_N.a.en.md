---
role: proof
locale: en
of_concept: quotient-reals-by-integers
source_book: gtm027
source_chapter: "N"
source_section: "Examples on Closed Maps and Local Compactness"
---

# Proof of Quotient of the Real Line by Collapsing the Integers

Let $X = \mathbb{R}$ with the usual topology, let $I = \mathbb{Z}$ be the set of integers, and let $\mathfrak{D}$ be the decomposition of $X$ whose non-degenerate member is $I$ and whose remaining members are the singletons $\{x\}$ for $x \in X \setminus I$.

Let $\pi : X \to X/\mathfrak{D}$ be the projection onto the quotient space.

**Closedness of $\pi$.** Let $A \subset X$ be closed. The saturation $\pi^{-1}[\pi[A]]$ is $A \cup I$ if $A$ intersects $I$, and is simply $A$ otherwise. In either case, the saturation is closed in $X$ (since $I$ is closed in $\mathbb{R}$). By definition of the quotient topology, $\pi[A]$ is closed. Hence $\pi$ is a closed map. Continuity of $\pi$ holds by definition of the quotient topology.

**Failure of local compactness.** Consider the point $\pi(I) \in X/\mathfrak{D}$. Any neighborhood of $\pi(I)$ in the quotient pulls back to a saturated open set in $\mathbb{R}$ containing $I$. Since $I$ is discrete and has no compact neighborhood that remains saturated (the integers "spread out" the space), the image point $\pi(I)$ has no compact neighborhood. Thus the quotient space is not locally compact.

**Failure of first countability.** The point $\pi(I)$ does not have a countable local base. If $\{U_n\}_{n \in \omega}$ were a countable neighborhood base at $\pi(I)$, then for each $n$ the saturated open set $\pi^{-1}[U_n]$ contains $I$. One can construct a saturated open set containing $I$ that does not contain any of the $\pi^{-1}[U_n]$ (using a diagonal argument with neighborhoods shrinking around each integer at different rates), violating the assumption of a countable base.
