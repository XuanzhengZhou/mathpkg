---
role: proof
locale: en
of_concept: existence-of-bundle-from-transition-functions
source_book: gtm020
source_chapter: "5"
source_section: "2"
---

By Theorem 2.7, if $\xi$ exists, it is unique. We begin by constructing $\xi$. For this, let $Z$ be the sum space (i.e., coproduct or disjoint union) of the family $\{V_i \times G\}$ for $i \in I$. An element of $Z$ is of the form $(b, s, i)$, where $b \in V_i$ and $s \in G$. The inclusion maps $q_i: V_i \times G \to Z$ are defined by the relation $q_i(b, s) = (b, s, i)$, and $Z$ has the largest topology such that all the $q_i$ are continuous.

On the space $Z$, we define an equivalence relation $R$ by the requirement that $(b, s, i)$ and $(b', s', j)$ are $R$-related provided $b = b'$ and $s' = g_{j,i}(b)s$. From properties (T1) to (T3) for transition functions we see that $R$ is an equivalence relation. Let $X$ be the quotient space $Z \bmod R$, let $q: Z \to X$ be the canonical quotient map, and let $h_i = q q_i$ for each $i \in I$. We denote by $\langle b, s, i \rangle$ the class of $(b, s, i)$ in the space $X$.

We define $p: X \to B$ by $p(\langle b, s, i \rangle) = b$. Since $p$ is a quotient of a projection, it is an open map. For $b \in V_i$, we have $p h_i(b, s) = b$, and $h_i: V_i \times G \to X$ is a continuous injection.

The group acts on $Z$ by the requirement that $(b, s, i)t = (b, st, i)$. If $(b, s, i)$ and $(b', s', j)$ are $R$-related, then $(b, st, i)$ and $(b', s' t, j)$ are $R$-related. Therefore, $X$ becomes a $G$-space under the action of $G$ defined by $\langle b, s, i \rangle t = \langle b, st, i \rangle$. This yields the principal $G$-bundle $\xi = (X, p, B)$ with atlas $\{(V_i, h_i)\}$ whose transition functions are $\{g_{i,j}\}$.
