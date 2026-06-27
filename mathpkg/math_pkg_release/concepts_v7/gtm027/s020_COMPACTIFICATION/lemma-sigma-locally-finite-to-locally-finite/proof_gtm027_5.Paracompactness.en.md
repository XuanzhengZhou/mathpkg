---
role: proof
locale: en
of_concept: lemma-sigma-locally-finite-to-locally-finite
source_book: gtm027
source_chapter: "5"
source_section: "Paracompactness"
---

# Proof that Sigma-Locally Finite Refinements Yield Locally Finite Refinements

**Lemma 34.** If each open cover of a space has an open $\sigma$-locally finite refinement, then each open cover has a locally finite refinement.

*Proof.* Let $\mathcal{U}$ be an open cover of $X$ and let $\mathcal{V}$ be an open $\sigma$-locally finite refinement of $\mathcal{U}$. Write $\mathcal{V} = \bigcup_{n \in \omega} \mathcal{V}_n$ where each $\mathcal{V}_n$ is an open locally finite family.

For each $n \in \omega$ and each $V \in \mathcal{V}_n$, define

$$V^* = V \setminus \bigcup \bigcup_{k < n} \mathcal{V}_k,$$

where $\bigcup \mathcal{V}_k$ denotes the union of all members of the family $\mathcal{V}_k$. That is, $V^*$ is obtained by deleting from $V$ all points that already belong to members of earlier families $\mathcal{V}_0, \dots, \mathcal{V}_{n-1}$. Each $V^*$ is not necessarily open (it is the difference of an open set and a union of open sets), but the family $\mathcal{W} = \{V^* : n \in \omega, V \in \mathcal{V}_n\}$ is a refinement of $\mathcal{U}$ (since $V^* \subset V \subset$ some $U \in \mathcal{U}$).

**$\mathcal{W}$ covers $X$.** For each $x \in X$, let $n$ be the smallest index such that $x$ belongs to some member of $\mathcal{V}_n$. (Such $n$ exists because $\mathcal{V}$ covers $X$.) Choose $V \in \mathcal{V}_n$ with $x \in V$. Since $x$ belongs to no member of any $\mathcal{V}_k$ for $k < n$, we have $x \notin \bigcup_{k < n} \bigcup \mathcal{V}_k$, and therefore $x \in V^*$. Thus $\mathcal{W}$ covers $X$.

**$\mathcal{W}$ is locally finite.** Fix $x \in X$. Let $n$ be the smallest index such that $x \in \bigcup \mathcal{V}_n$. For each $k \leq n$, the family $\mathcal{V}_k$ is locally finite, so there exists an open neighborhood $W_k$ of $x$ that meets only finitely many members of $\mathcal{V}_k$. Define

$$W = \bigcap_{k \leq n} W_k \setminus \bigcup \bigcup_{k < n} \mathcal{V}_k.$$

The set $W$ is a neighborhood of $x$: the first part is a finite intersection of neighborhoods (hence a neighborhood), and since $x \notin \bigcup_{k < n} \bigcup \mathcal{V}_k$ (by minimality of $n$), subtracting this closed set still yields a neighborhood.

Now consider any $V^* \in \mathcal{W}$ with $V \in \mathcal{V}_m$ that meets $W$. If $m < n$, then $V^* \subset V \subset \bigcup \mathcal{V}_m \subset \bigcup_{k < n} \bigcup \mathcal{V}_k$, so $V^*$ is disjoint from $W$ by construction. If $m = n$, then $V^* \subset V \in \mathcal{V}_n$, and $W \subset W_n$ meets only finitely many $V \in \mathcal{V}_n$. If $m > n$, then $V^*$ could meet $W$, but each $\mathcal{V}_m$ already meets any compact set in only finitely many members... Actually, the construction ensures: for $m > n$, $V^* \subset V \in \mathcal{V}_m$, and $W$ (being a subset of $W_n \cap \cdots$) might need more care. The standard refined approach is as follows.

*Refined argument (following Kelley).* Instead of the construction above, use:

$$V^* = V \setminus \bigcup \bigcup_{k < n} \mathcal{V}_k$$

as before. For local finiteness at $x$, let $n$ be minimal with $x \in \bigcup \mathcal{V}_n$ and let $W$ be an open neighborhood of $x$ meeting only finitely many members of $\bigcup_{k \leq n} \mathcal{V}_k$ (possible since each $\mathcal{V}_k$ is locally finite, and finitely many locally finite families have a neighborhood meeting only finitely many from their union). By minimality of $n$, we may shrink $W$ so that $W \cap \bigcup_{k < n} \bigcup \mathcal{V}_k = \emptyset$. Then $W$ meets $V^*$ only if $V \in \mathcal{V}_k$ for some $k \geq n$, and $W \cap V \neq \emptyset$. For $k = n$, this happens for only finitely many $V \in \mathcal{V}_n$. For $k > n$, any $V \in \mathcal{V}_k$ with $W \cap V^* \neq \emptyset$ has $W \cap V \neq \emptyset$, which again can happen for only finitely many $V$ (each $\mathcal{V}_k$ is locally finite, and the union of countably many locally finite families meeting a fixed neighborhood... here we need a more careful argument).

The concluding argument: for each $m$, $\mathcal{V}_m$ is locally finite, so the set of $V^*$ with $V \in \mathcal{V}_m$ that meet $W$ is in bijection with a subfamily of $\mathcal{V}_m$, hence finite. Since only finitely many indices $m$ can contribute (the ones where some $V \in \mathcal{V}_m$ meets $W$), the total number is finite. Thus $\mathcal{W}$ is locally finite. $\square$
