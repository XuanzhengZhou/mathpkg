---
role: proof
locale: en
of_concept: lemma-let-model-subset-dominates-then
source_book: gtm029
source_chapter: "VI"
source_section: "17"
---

Let $M = \bigcup_{i=1}^{n} V(\vartheta_i)$, where the $V(\vartheta_i)$'s are affine models, and let $U$ be an open set in $M$. We show that $f^{-1}(U)$ is open. Since $U$ is the union of the open sets $U \cap V(\vartheta_i)$ (Lemma 2), we may assume that $U$ is contained in some $V(\vartheta_i)$, say $V(\vartheta_1)$. Now, by Lemma 1, the mapping $g$ of $L(\vartheta_1)$ onto $V(\varthe

$f(\bigcup_{s \in R} G_s) = \bigcup_{s \in R} f(G_s)$, and since $R$ is a finite set, it is sufficient to prove that each $f(G_s)$ is closed in $M$. To simplify notations we prove that, if $G = F(x_1) \cap F(x_2) \cap \cdots \cap F(x_q)(x_j \in K, x_j \neq 0)$, then $f(G)$ is closed. Notice that $G$ is the set of all valuations $v$ such that $v(x_j) < 0$ for every $j$, i.e., such that the valuation ideal $\mathfrak{M}_v$ contains all the elements $y_j = 1/x_j$.

For proving that $f(G)$ is closed in $M$, we use Lemma 2 and write $M = \bigcup_{i} V(\mathfrak{o}_i)$ where the $V(\mathfrak{o}_i)$ are affine models; it is sufficient to prove that $f(G) \cap V(\mathfrak{o}_i)$ is closed in $V(\mathfrak{o}_i)$ for any $i$. Let $\mathfrak{o}$ be any one of the rings $\mathfrak{o}_i$. We consider the ideal $\mathfrak{a} = \mathfrak{o} \cap \left( \sum_{j=1}^{q} y_j \cdot \mathfrak{o}[y_1, \cdots, y_q] \right)$ of $\mathfrak{o}$. If $P \in f(G) \cap V(\mathfrak{o})$, the prime ideal $\mathfrak{p} = \mathfrak{o} \cap m(P)$ is the center in $\mathfrak{o}$ of a valuation $v (\in G)$ such that $\mathfrak{M}_v$ contains $y_1, \cdots, y_q$; then $\mathfrak{M}_v$ contains the ideal $\mathfrak{a}$, whence $\mathfrak{p}$ contains $\mathfrak{a}$. Conversely, if $\mathfrak{p}$ is a prime ideal in $\math

of the collection have a non-empty intersection, i.e., $f^{-1}(P) \cap F$ is non-empty. Thus $P$ would belong to $f(F)$, and the proof would be complete. Bearing in mind this observation, we shall use the following device:

Let us denote by $k^\star$ the quasi-local ring $P$ and let $S^\star$ be the Riemann surface of $K/k^\star$. Then $S^\star$ is a subset of $S$ (since $k^\star \supset k$). If $v = k[z]$ is any finitely generated subring of $K$ and if we set $v^\star = k^\star[z]$, then $E^\star(v^\star) = E(v) \cap S^\star$, where $E^\star(v^\star)$ denotes the basic open set on $S^\star$ which is defined by $v^\star$. It follows that the topology of $S^\star$ is at least as strong as the topology induced on $S^\star$ by that of $S$.

We now set $v_i^\star = k^\star[v_i]$, $M^\star = \bigcup_i V^\star(v_i^\star)$, where the symbol $V^\star$ has the same meaning relative to the ring $k^\star$ as $V$ had relative to $K$. It is clear that $M^\star \subset M$, and since $S^\star \subset S$ and $M$ is irredundant, also $M^\star$ is irredundant. Since each $v_i^\star$ is finitely generated over $k^\star$, each $V^\star(v_i^\star)$ is an affine model over $k^\star$. Therefore $M^\star$ is a model over $k^\star$. If $v$ is one of the rings $v_i$ such that $P \supset v$ then $v^\star = P = k^\star$, the ideal $\mathfrak{m}(P)$ is a maximal ideal of $v^\star$ and therefore the point $P$ is a closed subset of $M^\star$. Now, it is obvious that if $f^\star$ is the domination mapping of $S^\star$ onto $M

and $P' \in V(\mathfrak{o}_1)$. We set $\mathfrak{o} = k[\mathfrak{o}_0, \mathfrak{o}_1]$. The local rings $P$ and $P'$ are dominated by the quotient ring $\mathfrak{o}_p$ of $\mathfrak{o}$, where $\mathfrak{p} = \mathfrak{o} \cap \mathfrak{M}_v$. Since $\mathfrak{o}$ contains $x_1/x_0$ and $x_0/x_1$, these elements are units in $\mathfrak{o}$, hence also in $\mathfrak{o}_p$. Since $P$ contains $x_1/x_0$ and is dominated by $\mathfrak{o}_p$, it follows that $x_1/x_0$ is a unit in $P$; therefore, since $x_j/x_0 \in P$, we have $x_j/x_1 = (x_j/x_0)/(x_1/x_0) \in P$ for every $j$, whence $P$ contains $\mathfrak{o}_1$ and consequently $\mathfrak{o}$. From the inclusions $\mathfrak{o} \subset P \subset \mathfrak{o}_p$ and from the fact that $\mathfrak{o}_p$ dominates $P$ we conclude that $\mathfrak{m}(P) \cap \mathfrak{o} = \mathfrak{p}$, whence the elements of $\mathfrak{o} - \mathfrak{p}$ are units in $P$. Therefore $P$ contains $\mathfrak{o}_p$, whence $P = \mathfrak{o}_p$. In a similar way, we see that $P' = \mathfrak{o}_p$. Consequently $P = P'$ and $M$ is irredundant.

(b) $M$ is complete. In fact, given any valuation $v$ of $K/k$, we choose an index $j$ for which $v(x_j)$ takes its least value. We then have $v(x_i/x_j) \geq 0$ for every $i$, whence $\mathf

$P''_1$, and the fact that $P''_1$ is a quotient ring of $v_{ij}$, we deduce that $P''_1$ is a quotient ring of $k[P_1, P'_1]$, necessarily with respect to a prime ideal $q_1$; we obviously have $q_1 = k[P_1, P'_1] \cap \mathfrak{m}(P''_1)$, whence $q_1 = k[P_1, P'_1] \cap \mathfrak{M}_v$. Similarly $P''_2$ is also a quotient ring $k[P_1, P'_1]q_2$, and we also have $q_2 = k[P_1, P'_1] \cap \mathfrak{M}_v$. Consequently $q_1 = q_2$, whence $P''_1 = P''_2$. This proves that $M''$ is irredundant.

We have thus proved that $M''$ is the least upper bound of $M$ and $M'$ in the ordered set of all models. This proves the uniqueness of $M''$; in particular $M''$ is independent of the representations of $M$ and $M'$ as finite unions of affine models.

Now, if $M$ and $M'$ are affine models, say $M = V(v)$ and $M' = V(v')$, we have $M'' = V(k[v, v'])$, whence $M''$ is an affine model.

Let us now suppose that $M$ and $M'$ are projective models, respectively determined by $\{x_0, \cdots, x_n\}$ and $\{x'_0, \cdots, x'_q\}$. Setting $v_i = k[x_0/x_i, \cdots, x_n/x_i]$ and $v'_j = k[x'_0/x'_j, \cdots, x'_q/x'_j}$, the ring $v_{ij} = k[v_i, v'_j]$ is obviously equal to $k[x_0x'_0/x_ix'_j, \cdots, x_sx'_t/x

It may be shown by examples that there exist complete models which are not projective (see M. Nagata, "Existence theorems for non-projective complete algebraic varieties," Illinois J. of Mathematics, Dec. 1958).
