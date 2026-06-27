---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.2"
proof_technique: canonical-form
locale: en
content_hash: ""
written_against: ""
---
(i) $A$ is the matrix of some linear transformation $f : D^n \to D^m$ relative to some pair of bases by Theorem 1.2. If $\operatorname{rank} A = r$, then Corollary IV.2.14 implies there exist bases $U$ of $D^n$ and $V$ of $D^m$ such that $f(u_i) = v_i$ for $i = 1, \ldots, r$ and $f(u_i) = 0$ for $i = r+1, \ldots, n$. The matrix of $f$ relative to $U,V$ is $E_r^{n,m}$, so $A$ is equivalent to $E_r^{n,m}$ by Theorem 1.6. Conversely, if $A$ is equivalent to $E_r^{n,m}$, then there is a linear transformation $g: D^n \to D^m$ such that $A$ and $E_r^{n,m}$ are matrices of $g$ relative to different bases. Hence $\operatorname{rank} A = \operatorname{rank} g = \operatorname{rank} E_r^{n,m} = r$ by Theorem 2.3.
(ii) and (iii) are immediate consequences of (i).
