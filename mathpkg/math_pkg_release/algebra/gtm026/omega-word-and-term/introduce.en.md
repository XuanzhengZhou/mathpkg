---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

To formalize equational presentations, one needs a precise syntactic framework. Given a set $A$ of variable symbols and an operator domain $\Omega$, an $\Omega$-word in $A$ is any finite nonempty sequence of symbols from $A \cup |\Omega|$. Not all such words are meaningful algebraic expressions — the well-formed ones are called $\Omega$-terms. They are built inductively: every variable is a term, and if $p_1, \ldots, p_n$ are terms and $\omega \in \Omega_n$ is an $n$-ary operator label, then the concatenation $p_1 \cdots p_n \omega$ is a term (using Polish notation where the operator symbol follows its arguments). This construction provides the formal language for writing equations in universal algebra.
