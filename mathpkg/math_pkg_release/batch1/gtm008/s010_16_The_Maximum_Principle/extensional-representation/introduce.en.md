---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 16.11 shows that any Boolean-valued set $v$ can be replaced by an extensional set $u$ with a prescribed superset $d$ of its domain, while preserving Boolean equality. The construction is straightforward: define $u(x) = \llbracket x \in v \rrbracket$ for all $x \in d$. This ensures $u$ is extensional because $\llbracket x = y \rrbracket \cdot u(x) \leq u(y)$. Combined with Theorem 16.1, this means we can always assume without loss of generality that Boolean-valued sets are extensional, which greatly simplifies many proofs.
