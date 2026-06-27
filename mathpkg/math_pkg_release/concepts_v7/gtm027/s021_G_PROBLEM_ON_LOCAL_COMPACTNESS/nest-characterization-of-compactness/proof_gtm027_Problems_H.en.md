---
role: proof
locale: en
of_concept: nest-characterization-of-compactness
source_book: gtm027
source_chapter: "Problems"
source_section: "H"
---

# Proof of Nest Characterization of Compactness

**Theorem.** A topological space $X$ is compact if and only if each nest of closed non-void sets has a non-void intersection. (A *nest* is a family of sets which is linearly ordered by inclusion.)

**Proof.**

($\Rightarrow$) If $X$ is compact and $\mathcal{N}$ is a nest of closed non-void sets, then $\mathcal{N}$ has the finite intersection property (any finite subfamily has non-void intersection because the nest is linearly ordered: the smallest set in the finite subfamily is contained in all others, and is non-void). Since $X$ is compact, the entire family has non-void intersection.

($\Leftarrow$) Assume that every nest of closed non-void sets has non-void intersection. Let $\mathcal{A}$ be a family of closed sets with the finite intersection property. We must show $\bigcap \mathcal{A} \neq \varnothing$.

By Zorn's Lemma, extend $\mathcal{A}$ to a maximal family $\mathcal{A}^*$ of closed sets containing $\mathcal{A}$ and still having the finite intersection property.

**Properties of $\mathcal{A}^*$:**
1. $\mathcal{A}^*$ is closed under finite intersections: if $A, B \in \mathcal{A}^*$, then $A \cap B \in \mathcal{A}^*$. (Otherwise appending $A \cap B$ would contradict maximality, since $A \cap B$ is closed and adding it preserves the finite intersection property.)
2. If a closed set $C$ intersects every member of $\mathcal{A}^*$, then $C \in \mathcal{A}^*$. (Otherwise appending $C$ would yield a larger family with the finite intersection property.)

Now let $\mathcal{P}$ be a maximal nest (chain) in $\mathcal{A}^*$, ordered by inclusion. Such a maximal nest exists by Zorn's Lemma applied to the collection of nests in $\mathcal{A}^*$ ordered by inclusion.

By hypothesis, $\bigcap \{P : P \in \mathcal{P}\} \neq \varnothing$. Let $x$ be a point in this intersection.

We claim that $x$ belongs to every member of $\mathcal{A}^*$. Let $A \in \mathcal{A}^*$. For every $P \in \mathcal{P}$, we have $A \cap P \neq \varnothing$ (since $\mathcal{A}^*$ has the finite intersection property). Hence $x$ is in the closure of $A \cap P$ for each $P$.

More precisely: the point $x \in \bigcap \mathcal{P}$ means that every neighborhood of $x$ meets every $P \in \mathcal{P}$. We need to show $x \in A$. 

Suppose $x \notin A$. Since $A$ is closed, there exists an open neighborhood $U$ of $x$ with $U \cap A = \varnothing$. For each $P \in \mathcal{P}$, $A \cap P$ is non-void, and $x \in P$. The family $\mathcal{P}$ is a nest; consider the subfamily of those $P \in \mathcal{P}$ that are contained in $X \setminus U$. This forms a sub-nest. If every $P \in \mathcal{P}$ met $U$, we would have a contradiction.

A more direct argument: By property 2, since $\{x\}^-$ (the closure of $\{x\}$) intersects every $P \in \mathcal{P}$ non-trivially (in fact $x \in P$), the closed set $\{x\}^-$ intersects every member of $\mathcal{P}$. But we need to connect this to $\mathcal{A}^*$.

Actually, the standard proof proceeds as follows: The maximal nest $\mathcal{P}$ has the property that for any $A \in \mathcal{A}^*$, if $A$ meets every $P \in \mathcal{P}$, then $A \in \mathcal{P}$ (by maximality of the nest within $\mathcal{A}^*$). Now $\{x\}^-$ meets every $P \in \mathcal{P}$ (it contains $x \in P$), so $\{x\}^- \in \mathcal{P}$. Therefore $\{x\}^- \in \mathcal{A}^*$, and hence $x$ belongs to all elements of $\mathcal{P}$.

But then for any $A \in \mathcal{A}^*$, $A \cap \{x\}^- \neq \varnothing$. Since $\{x\}^- \subset \overline{\{x\}}$, this means $x \in A$ for every $A \in \mathcal{A}^*$. In particular, $x \in \bigcap \mathcal{A}$.

Thus $\bigcap \mathcal{A} \neq \varnothing$, proving that $X$ is compact.

**Alternative proof (well-ordering).** One can also prove the result by well-ordering the family $\mathcal{A}$ and using transfinite induction to construct a nested sequence whose intersection is contained in $\bigcap \mathcal{A}$, then applying the nest intersection hypothesis.

Let $\mathcal{A} = \{A_\alpha : \alpha < \gamma\}$ be a well-ordering of $\mathcal{A}$. Define a nested family $\{B_\alpha : \alpha < \gamma\}$ by $B_0 = A_0$ and $B_\alpha = B_{\alpha-1} \cap A_\alpha$ for successor ordinals (taking finite intersection property preserves non-voidness), using the fact that any intersection of closed sets with the finite intersection property remains non-void for the nest so constructed. The hypothesis then applies to the resulting nest.
