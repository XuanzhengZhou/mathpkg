---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.2"
proof_technique: monomial-basis-frobenius
locale: en
content_hash: ""
written_against: ""
---
Let $F = K(S)$ with $S$ a transcendence base of $F$ over $K$. If $S = \varnothing$,
then $F = K$ and the singleton $\{1\}$ is linearly independent over any subfield, so the
result holds. If $S \neq \varnothing$, let $M$ be the set of monomials over $S$ (all finite
products of elements of $S$). Then $M$ is linearly independent over $K$ since $S$ is
algebraically independent. By Theorem V.1.3, $M$ spans the polynomial ring $K[S]$ as a
$K$-vector space, so $M$ is a $K$-basis of $K[S]$. By Lemma 2.3, it suffices to show that
$M$ is linearly independent over $K^{1/p}$ (then the result extends to all $K^{1/p^n}$).

If $\sum_i a_i m_i = 0$ with $a_i \in K^{1/p}$, $m_i \in M$, then taking $p$-th powers:
$\sum_i a_i^p m_i^p = 0$ with $a_i^p \in K$ and $m_i^p \in M$ (distinct monomials stay
distinct since $p > 0$ and exponents multiply by $p$). Since $M$ is $K$-linearly independent,
all $a_i^p = 0$, hence all $a_i = 0$. Thus $M$ is linearly independent over $K^{1/p}$.
