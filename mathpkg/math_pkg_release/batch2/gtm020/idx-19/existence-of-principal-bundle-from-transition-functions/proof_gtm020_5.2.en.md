---
role: proof
locale: en
of_concept: existence-of-principal-bundle-from-transition-functions
source_book: gtm020
source_chapter: "5"
source_section: "2"
---

By Theorem 2.7 (isomorphism criterion), if $\eta$ exists, it is unique. We begin by constructing $\xi$. For this, let $Z$ be the sum space (i.e., coproduct or disjoint union) of the family $\{V_i \times G\}$ for $i \in I$. An element of $Z$ is of the form $(b, s, i)$, where $b \in V_i$ and $s \in G$. The inclusion maps $q_i: V_i \times G \rightarrow Z$ are defined by the relation $q_i(b, s) = (b, s, i)$, and $Z$ has the largest topology such that all the $q_i$ are continuous.

On the space $Z$, we define an equivalence relation $R$ by the requirement that $(b, s, i)$ and $(b', s', j)$ are $R$-related provided $b = b'$ and $s' = g_{j,i}(b)s$. From properties (T1) to (T3) for transition functions we see that $R$ is an equivalence relation. Let $X$ be the quotient space $Z / R$, let $q: Z \rightarrow X$ be the canonical quotient map, and let $h_i = q q_i$ for each $i \in I$. We denote by $\langle b, s, i \rangle$ the class of $(b, s, i)$ in the space $X$.

We define $p: X \rightarrow B$ by $p(\langle b, s, i \rangle) = b$. Since $p$ is a quotient of a projection, it is an open map. For $b \in V_i$, we have $p h_i(b, s) = b$, and $h_i: V_i \times G \rightarrow X$ is a continuous injection.

The group $G$ acts on $Z$ by the requirement that $(b, s, i)t = (b, st, i)$. If $(b, s, i)$ and $(b', s', j)$ are $R$-related, then $(b, st, i)$ and $(b', s't, j)$ are $R$-related because $s't = (g_{j,i}(b)s)t = g_{j,i}(b)(st)$. Therefore, $X$ becomes a $G$-space under the action defined by $\langle b, s, i \rangle t = \langle b, st, i \rangle$. This action is free and the map $p$ factors through the orbit space. The $h_i$ provide the local trivializations, completing the construction.
