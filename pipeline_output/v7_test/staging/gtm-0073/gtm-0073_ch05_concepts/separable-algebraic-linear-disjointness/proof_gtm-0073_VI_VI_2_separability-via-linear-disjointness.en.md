---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.2"
proof_technique: separability-via-linear-disjointness
locale: en
content_hash: ""
written_against: ""
---
($\Rightarrow$) Suppose $F$ is separable algebraic over $K$. Let $X \subset F$ be
$K$-linearly independent. By Lemma 2.6, it suffices to show $X^p$ is $K$-linearly independent.
If $\sum a_i u_i^p = 0$ with $a_i \in K$, $u_i \in X$, then extending $\{u_i\}$ to a $K$-basis
$U$ of $F$, and using the fact that the minimal polynomial of each element of $F$ over $K$
is separable, one can show $\{u^p \mid u \in U\}$ is $K$-linearly independent. Thus all $a_i = 0$,
and $F$ and $K^{1/p}$ are linearly disjoint.

($\Leftarrow$) If $F$ and $K^{1/p}$ are linearly disjoint and $F$ is algebraic over $K$,
take any $u \in F$ with minimal polynomial $f \in K[x]$. If $f$ were inseparable, then
$f'(u) = 0$, and a linear dependence over $K^{1/p}$ would arise, contradicting linear
disjointness. Hence $f$ is separable and $F$ is separable algebraic over $K$.
