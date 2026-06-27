---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.1"
proof_technique: polynomial-common-denominator
locale: en
content_hash: ""
written_against: ""
---
Suppose $S \cup \{u\}$ is algebraically independent. If $u$ were algebraic over $K(S)$, then
$f(u) = 0$ for some nonzero polynomial $f \in K(S)[x]$. Write $f(x) = \sum a_i x^i$ with
$a_i \in K(S)$. By Theorem V.1.3, there is a finite subset $\{s_1, \ldots, s_r\} \subseteq S$ such that
$a_i = f_i(s_1, \ldots, s_r)/g_i(s_1, \ldots, s_r)$ for some $f_i, g_i \in K[x_1, \ldots, x_r]$.
Let $g = g_1 \cdots g_n$ and $\tilde{f}_i = f_i \cdot \prod_{j \neq i} g_j$. Then
$a_i = \tilde{f}_i(s_1, \ldots, s_r)/g(s_1, \ldots, s_r)$ and
\[
f(x) = g(s_1, \ldots, s_r)^{-1} \sum \tilde{f}_i(s_1, \ldots, s_r) x^i.
\]
Let $h(x_1, \ldots, x_r, x) = \sum \tilde{f}_i(x_1, \ldots, x_r) x^i \in K[x_1, \ldots, x_r, x]$.
Since $f(u) = 0$ and $g(s_1, \ldots, s_r)^{-1} \neq 0$, we have $h(s_1, \ldots, s_r, u) = 0$.
But $S \cup \{u\}$ is algebraically independent, so $h = 0$, whence all $\tilde{f}_i = 0$, so all $a_i = 0$,
contradicting $f \neq 0$. Therefore $u$ must be transcendental over $K(S)$.
