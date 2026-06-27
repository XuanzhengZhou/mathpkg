---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.1"
proof_technique: evaluation-map
locale: en
content_hash: ""
written_against: ""
---
The evaluation homomorphism $\varphi: K[x_1, \ldots, x_n] \to K[s_1, \ldots, s_n]$ defined by
$f(x_1, \ldots, x_n) \mapsto f(s_1, \ldots, s_n)$ is a $K$-algebra homomorphism.
By algebraic independence, $\ker \varphi = \{0\}$, so $\varphi$ is an isomorphism onto $K[s_1, \ldots, s_n]$.
This extends uniquely to an isomorphism of quotient fields:
\[
\bar{\varphi}: K(x_1, \ldots, x_n) \xrightarrow{\cong} K(s_1, \ldots, s_n),
\]
\[
f/g \mapsto f(s_1, \ldots, s_n)/g(s_1, \ldots, s_n).
\]
