---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.2"
proof_technique: basis-extension
locale: en
content_hash: ""
written_against: ""
---
(i) Let $Y$ be a basis of $W$. By Theorem 2.4 there is a basis $X$ of $V$ containing $Y$, so $\dim W = |Y| \le |X| = \dim V$.
(ii) If $|Y| = |X|$ and $|X|$ is finite, $Y = X$, so $W = V$.
(iii) Show $U = \{x + W \mid x \in X - Y\}$ is a basis of $V/W$. $U$ spans because any $v = \sum r_i y_i + \sum s_j x_j$ gives $v + W = \sum s_j(x_j + W)$. Linear independence follows from linear independence of $X$. Thus $\dim V = |X| = |Y| + |X-Y| = \dim W + \dim(V/W)$.
