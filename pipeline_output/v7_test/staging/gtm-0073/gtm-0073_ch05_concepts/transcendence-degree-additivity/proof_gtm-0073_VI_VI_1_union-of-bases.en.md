---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.1"
proof_technique: union-of-bases
locale: en
content_hash: ""
written_against: ""
---
Let $S$ be a transcendence base of $E$ over $K$ and $T$ a transcendence base of $F$ over $E$.
Since $S \subset E$, $S$ is algebraically dependent over $E$, whence $S \cap T = \varnothing$.
It suffices to show that $S \cup T$ is a transcendence base of $F$ over $K$.

First, $S \cup T$ is algebraically independent over $K$: if a polynomial relation held among
elements of $S \cup T$, then by treating elements of $S$ as constants we would get an algebraic
dependence of $T$ over $K(S)$, hence over $E$, contradicting the independence of $T$ over $E$.

Second, $F$ is algebraic over $K(S \cup T) = K(S)(T) = E(T)$ since $F$ is algebraic over $E(T)$
and $K(S)(T) \supseteq E(T)$. More precisely, $E$ is algebraic over $K(S)$, so $E(T)$ is algebraic
over $K(S)(T)$. Since $F$ is algebraic over $E(T)$, $F$ is algebraic over $K(S \cup T)$.

Thus $S \cup T$ is a transcendence base, and $|S \cup T| = |S| + |T|$ since $S \cap T = \varnothing$.
