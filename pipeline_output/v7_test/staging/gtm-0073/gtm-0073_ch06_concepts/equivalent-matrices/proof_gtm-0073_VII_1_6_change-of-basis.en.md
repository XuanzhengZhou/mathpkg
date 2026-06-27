---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.1"
proof_technique: change-of-basis
locale: en
content_hash: ""
written_against: ""
---
($\Rightarrow$) Let $P$ be the matrix of $1_E$ relative to $U'$ and $U$, and let $Q$ be the matrix of $1_F$ relative to $V$ and $V'$. Then $P$ and $Q$ are invertible by Lemma 1.5. Since $f = 1_F f 1_E$, Theorem 1.3 implies the matrix of $f$ relative to $U'$ and $V'$ is $PAQ$. Therefore $B = PAQ$.
($\Leftarrow$) Given $B = PAQ$ with $P,Q$ invertible, let $g: E \to E$ be the isomorphism with matrix $P$ relative to $U$ and $h: F \to F$ the isomorphism with matrix $Q^{-1}$ relative to $V$. Then $g(U)$ and $h(V)$ are ordered bases and the matrix of $f$ relative to $g(U), h(V)$ is $PAQ = B$.
