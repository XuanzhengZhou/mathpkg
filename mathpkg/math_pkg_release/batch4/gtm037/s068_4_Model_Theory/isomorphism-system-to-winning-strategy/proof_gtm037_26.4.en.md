---
role: proof
locale: en
of_concept: isomorphism-system-to-winning-strategy
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

Assume the hypothesis of Lemma 26.12, and let $\langle I_0, \ldots, I_{m+1} \rangle$ be an $(m+1)$-system of partial isomorphisms of $\mathfrak{A}$ into $\mathfrak{B}$. We construct a winning strategy $F$ for Player II as follows.

At the start of the game, choose any $f_\emptyset \in I_{m+1}$ (nonempty by condition (i) of Definition 26.9). Suppose $k < m$ rounds have been played, producing tuples $x \in {}^k A$ and $y \in {}^k B$, and we have maintained a partial isomorphism $f_k \in I_{m+1-k}$ such that $f_k(x_i) = y_i$ for all $i < k$.

If Player I now plays $a \in A$ (indicated by $(z_k)_0 = 0$), then since $f_k \in I_{m+1-k} \subseteq I_{m-k}$ (by condition (ii)) and $m - k \geq 1$, condition (iii) of Definition 26.9 yields a $g \in I_{m-k}$ extending $f_k$ with $a \in \operatorname{Dmn} g$. Set $F(x, y, 0, a) = g(a)$ and let $f_{k+1} = g$. The case where Player I plays $b \in B$ is symmetric, using the "back" direction of condition (iii).

After $m$ rounds, we obtain $f_m \in I_1$, which is a partial isomorphism whose domain contains $\{x_0,\ldots,x_{m-1}\}$. Condition (ii) of Definition 26.11 is satisfied because $f_m$ witnesses that $\{(x_i, y_i) : i < m\}$ is a partial isomorphism of $\mathfrak{A}$ into $\mathfrak{B}$.
