---
role: proof
locale: en
of_concept: cantor-space-ccc
source_book: gtm027
source_chapter: "N"
source_section: "Examples on Closed Maps and Local Compactness"
---

# Proof of Every Cantor Space Satisfies the Countable Chain Condition

Let $2^A$ be a Cantor space with the product topology, where $2 = \{0,1\}$ carries the discrete topology. We must show that every disjoint family of open subsets of $2^A$ is at most countable.

Let $\mathcal{U}$ be a pairwise disjoint family of non-empty open subsets of $2^A$. Without loss of generality, we may assume that each member of $\mathcal{U}$ belongs to the standard base for the product topology. A basic open set in $2^A$ is of the form

$$
\bigcap_{a \in F} \pi_a^{-1}[\{\varepsilon_a\}],
$$

where $F \subset A$ is a finite set, $\varepsilon_a \in \{0,1\}$ for each $a \in F$, and $\pi_a : 2^A \to 2$ is the projection onto the $a$-th coordinate. Thus each basic open set is determined by specifying the values on a finite set of coordinates — it is, in a natural sense, the intersection of finitely many "half-spaces."

For each $n \in \mathbb{N}$, let $\mathcal{U}_n$ be the subfamily of $\mathcal{U}$ consisting of those basic open sets determined by precisely $n$ coordinates. Since the union of the $\mathcal{U}_n$ covers $\mathcal{U}$, and a countable union of finite (or countable) families is countable, it suffices to show that each $\mathcal{U}_n$ is countable.

Suppose, for a contradiction, that some $\mathcal{U}_n$ is uncountable (hence infinite). Members of $\mathcal{U}_n$ are determined by $n$-element subsets of $A$. Since there are only finitely many assignments of $\{0,1\}$ to a given $n$-element set (namely $2^n$), the pigeonhole principle implies that some fixed assignment $\varepsilon$ occurs for infinitely many basic open sets in $\mathcal{U}_n$.

Let these be $\{B_\alpha\}_{\alpha \in I}$, each determined by a finite set $F_\alpha \subset A$ with $|F_\alpha| = n$. Because the $B_\alpha$ are pairwise disjoint, for any two distinct $\alpha, \beta \in I$ there must exist some coordinate $a \in F_\alpha \cap F_\beta$ on which the prescribed values differ. But all $B_\alpha$ have the same restriction pattern $\varepsilon$ on their respective supports $F_\alpha$. By a simple combinatorial argument (the $\Delta$-system lemma), among uncountably many $n$-element sets there exist two, say $F_\alpha$ and $F_\beta$, whose restrictions to their intersection agree, yet whose basic open sets are disjoint — a contradiction.

More concisely, using the $\Delta$-system lemma: from $\{F_\alpha\}_{\alpha \in I}$ (an uncountable family of $n$-element sets), we can extract a $\Delta$-system with root $R$. Then for any two members $F_\alpha, F_\beta$ of the $\Delta$-system, we have $F_\alpha \cap F_\beta = R$, and the basic open sets $B_\alpha, B_\beta$ agree on $R$ (same $\varepsilon$ values) and hence have non-empty intersection, contradicting disjointness.

Therefore $\mathcal{U}$ must be countable, establishing the countable chain condition for $2^A$.
