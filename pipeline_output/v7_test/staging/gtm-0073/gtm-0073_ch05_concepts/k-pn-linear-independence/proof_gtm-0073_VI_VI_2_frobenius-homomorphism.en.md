---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.2"
proof_technique: frobenius-homomorphism
locale: en
content_hash: ""
written_against: ""
---
Every $a \in K$ is of the form $a = v^{p^n}$ for some $v \in K^{1/p^n}$.

(i) $\sum_i a_i u_i^{p^n} = 0$ with $a_i \in K$, $u_i \in X$
$\Leftrightarrow \sum_i v_i^{p^n} u_i^{p^n} = 0$ where $v_i^{p^n} = a_i$
$\Leftrightarrow (\sum_i v_i u_i)^{p^n} = 0$
$\Leftrightarrow \sum_i v_i u_i = 0$ with $v_i \in K^{1/p^n}$.

(ii) If $\sum_{i=1}^t w_i u_i = 0$ with $w_i \in K^{1/p^\infty}$ and $u_i \in X$,
then for sufficiently large $n$, all $w_1, \ldots, w_t \in K^{1/p^n}$.
