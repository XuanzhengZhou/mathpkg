---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.1"
proof_technique: exchange-replacement
locale: en
content_hash: ""
written_against: ""
---
Let $S = \{s_1, \ldots, s_n\}$ be a finite transcendence base and $T$ any transcendence base.
We claim that some $t_1 \in T$ is transcendental over $K(s_2, \ldots, s_n)$. Otherwise every element
of $T$ is algebraic over $K(s_2, \ldots, s_n)$, whence $K(s_2, \ldots, s_n)(T)$ is algebraic over
$K(s_2, \ldots, s_n)$. Since $F$ is algebraic over $K(T)$, $F$ is algebraic over
$K(T)(s_2, \ldots, s_n) = K(s_2, \ldots, s_n)(T)$. Then $F$ is algebraic over $K(s_2, \ldots, s_n)$,
so $s_1$ is algebraic over $K(s_2, \ldots, s_n)$, contradicting Theorem 1.5. Hence
$\{t_1, s_2, \ldots, s_n\}$ is algebraically independent.

If $s_1$ were transcendental over $K(t_1, s_2, \ldots, s_n)$, then $\{t_1, s_1, s_2, \ldots, s_n\}$
would be algebraically independent, contradicting maximality of $S$. Therefore $s_1$ is algebraic
over $K(t_1, s_2, \ldots, s_n)$, and $F$ is algebraic over $K(t_1, s_2, \ldots, s_n)$. Hence
$\{t_1, s_2, \ldots, s_n\}$ is a transcendence base. Repeating, we can replace all $s_i$ with
$t_i \in T$. If $T$ had more than $n$ elements, the process would produce an algebraically
independent set larger than the transcendence base—a contradiction. Thus $|T| = n$.

For infinite transcendence bases, the equality follows from cardinal arithmetic using the
Schroeder-Bernstein Theorem, assigning to each $t \in T$ a finite subset of $S$ on which
$t$ algebraically depends, giving $|T| \leq |S| \aleph_0 = |S|$.
