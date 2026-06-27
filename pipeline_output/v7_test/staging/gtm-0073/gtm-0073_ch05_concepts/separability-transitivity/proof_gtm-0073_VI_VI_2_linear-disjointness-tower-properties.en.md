---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.2"
proof_technique: linear-disjointness-tower-properties
locale: en
content_hash: ""
written_against: ""
---
(i) If $F$ and $K^{1/p}$ are linearly disjoint over $K$, then certainly any subset of
$E$ that is $K$-linearly independent is also independent over $K^{1/p}$, so $E$ is separable.

(ii) By Theorem 2.10, $F$ and $E^{1/p}$ are linearly disjoint over $E$, and $E$ and $K^{1/p}$
are linearly disjoint over $K$. Using Theorem 2.4 (the tower property) with $L = E^{1/p}$, one
shows $F$ and $K^{1/p}$ are linearly disjoint over $K$. Thus $F$ is separable over $K$.

(iii) If char $K = p \neq 0$, let $X \subset F$ be $E$-linearly independent. Extend $X$ to a
basis $U$ of $F$ over $E$ and let $V$ be a basis of $E$ over $K$. The proof of Theorem IV.2.16
shows $UV = \{uv \mid u \in U, v \in V\}$ is a $K$-basis of $F$. By separability of $F/K$,
$UV$ is linearly independent over $K^{1/p}$. By Lemma 2.6, $(UV)^p = \{u^p v^p\}$ is $K$-linearly
independent. Moreover, $V^p$ is a $K$-basis of $E$ (since $E/K$ is separable algebraic).
This implies $U$ is linearly independent over $K^{1/p}$, hence over $E^{1/p}$. Thus $F/E$ is
separable.
