---
role: proof
locale: en
of_concept: tame-linear-graph-no-endpoints
source_book: gtm047
source_chapter: "5"
source_section: "15"
---

Let $\phi: U \to \mathbf{R}$ be strongly positive and let $U$ be an open set containing $M$. By Lemma 1 (applied to $K$ after a suitable subdivision $K_1$), we may assume the edges $e = h(\sigma^1)$ of $M$ (where $\sigma^1 \in K$) form a contracting collection. By Lemma 2 (applied to a further subdivision $K_2$), every $e = h(\sigma^1)$ has a neighborhood $N_e \subset U$ such that
$$\delta N_e < \inf(\phi \mid N_e).$$
If $N_e$ satisfies this, then every smaller neighborhood of $e$ does also.

Since the edges form a contracting collection, we can choose the $N_e$ so that the $\{N_e\}$ also form a contracting collection.

For each vertex $v$ of $M$, take a convex polyhedral 2-cell neighborhood $N_v$ with $\operatorname{Bd} N_v = J_v$. Choose them sufficiently small so that they are disjoint, lie in $U$, and for each edge $e$ containing $v$, we have $N_v \subset N_e$.

Let the edges emerging from $v$ intersect $J_v$ in points $w_1, \ldots, w_n$. These partition $J_v$ into arcs $e'_j$. For each arc $a_i$ of $\operatorname{Int} N_v \cap M$ with endpoints $w_j, w_k$ on $J_v$, the set $J_i = a_i \cup e'_j \cup e'_k$ is a 1-sphere with interior $I_i$ lying in $N_v$.

**Lemma 3.** The sets $I_i$ are disjoint.
*Proof.* If $I_i \cap I_j \neq \varnothing$, a broken line from an interior point of $a_i$ to an interior point of $a_j$ in $N_v$ avoiding the $e'_k$ contradicts Theorem 4.2.

**Lemma 4.** $N_v = \bigcup \overline{I}_i$.
*Proof.* Otherwise $N_v - \bigcup e'_j$ has a component $V$ with $\operatorname{Fr} V \subset \bigcup e'_j$. Since no arc separates $\mathbf{R}^2$, $\operatorname{Fr} V$ cannot lie in a single $e'_j$. Two points $P \in e'_i$, $Q \in e'_j$ in $\operatorname{Fr} V$ are separated by an arc $A$ (constructed via two applications of the Schönflies theorem) joining suitable points $X, Y$ on $J_v$ and intersecting $\bigcup e'_k$ only at $v$. This contradicts that $P$ and $Q$ both lie in $\operatorname{Fr} V$.

Since each $I_i$ is the interior of a 1-sphere, it is a 2-cell. We define a homeomorphism $h_v: N_v \leftrightarrow N_v$, fixing $\operatorname{Bd} N_v$ pointwise, such that $h_v(a_i)$ is a broken line for each $a_i$. This is done by mapping each $I_i$ to a suitably chosen polygonal 2-cell in $\mathbf{R}^2$.

Now each edge $a \subset e$ has a frame $N_a$ (as in Theorem 6) with $N_a \subset N_e$, chosen so that different $N_a$ are disjoint and $\{N_a\}$ is a contracting collection. By the method of Theorem 6, we arrange each $e \cap N_a$ to be an arc intersecting $\operatorname{Fr} N_a$ exactly at its endpoints. Define $h_a: N_a \leftrightarrow N_a$ fixing $\operatorname{Bd} N_a$ and mapping $h_a(e \cap N_a)$ to a broken line, and extend by the identity outside $N_a$.

Let $h_0$ be the composition of all $h_v$, let $h_1$ be the composition of all $h_a$, and let $h = h_1 h_0$. Since the neighborhoods are disjoint or nested appropriately, the compositions are well-defined. Moreover $h \mid (\mathbf{R}^2 - U)$ is the identity, and $h(M)$ is a polyhedron.

It remains to verify the $\phi$-approximation property. For each edge $e$ with endpoints $v, v'$ and each $a \subset e$, we have $N_v \subset N_e$, $N_{v'} \subset N_e$, and $N_a \subset N_e$. Therefore $h(N_e) \subset N_e$. Since $\delta N_e < \inf(\phi \mid N_e)$, it follows that for every $P \in N_e$,
$$d(P, h(P)) < \phi(P).$$
If $P$ lies in no $N_e$, then $h(P) = P$ and the inequality holds trivially.
