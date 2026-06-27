---
role: proof
locale: en
of_concept: kuratowski-ulam-theorem
source_book: gtm002
source_chapter: "15"
source_section: "15. The Kuratowski-Ulam Theorem"
---

The two statements are essentially equivalent. For if $E = \bigcup E_i$, then $E_x = \bigcup_i (E_i)_x$. Hence the first statement follows from the second. If $E$ is nowhere dense, so is $\bar{E}$, and $E_x$ is nowhere dense whenever $(\bar{E})_x$ is of first category. Hence the second statement follows from the first. It is therefore sufficient to prove the second statement for any nowhere dense closed set $E$.

Let $\{V_n\}$ be a countable base for $Y$, and put $G = (X \times Y) - E$. Then $G$ is a dense open subset of the plane. For each positive integer $n$, let $G_n$ be the projection of $G \cap (X \times V_n)$ in $X$, that is,

$$G_n = \{x : (x, y) \in G \text{ for some } y \in V_n\}.$$

Let $x \in G_n$ and $y \in V_n$ be such that $(x, y) \in G$. Since $G$ is open, there exist open intervals $U$ and $V$ such that $x \in U$, $y \in V \subset V_n$, and $U \times V \subset G$. It follows that $U \subset G_n$. Hence $G_n$ is an open subset of $X$. For any non-empty open set $U$, the set $G \cap (U \times V_n)$ is non-empty, since $G$ is dense in $X \times Y$. Therefore $G_n \cap U$ is non-empty, which shows that each $G_n$ is dense in $X$.

Let $D = \bigcap_n G_n$. Then $D$ is a dense $G_\delta$ set, so its complement is of first category. For each $x \in D$, the set $G_x$ intersects every $V_n$, hence $G_x$ is dense in $Y$. Therefore $E_x = Y - G_x$ is nowhere dense in $Y$ for every $x \in D$. This establishes the second statement for nowhere dense closed $E$, and consequently the full theorem. $\square$
