---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.2"
proof_technique: maximality-argument
locale: en
content_hash: ""
written_against: ""
---
Let $W$ be the subspace spanned by $X$. Since $X$ is linearly independent and spans $W$, $X$ is a basis of $W$. If $W = V$, we are done. If not, there exists $a \in V$, $a \notin W$. Consider $X \cup \{a\}$. If $ra + \sum r_i x_i = 0$ with $r \neq 0$, then $a = -r^{-1}\sum r_i x_i \in W$, contradiction. Hence $r = 0$ and all $r_i = 0$, so $X \cup \{a\}$ is linearly independent, contradicting maximality. Therefore $W = V$.
