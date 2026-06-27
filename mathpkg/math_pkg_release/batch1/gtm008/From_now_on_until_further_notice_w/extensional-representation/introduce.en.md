---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 16.11 states that any Boolean-valued set $v \in V^{(\mathbf{B})}$ can be replaced by an extensional set $u$ with any prescribed domain $d \supseteq \mathcal{D}(v)$, while preserving Boolean-valued equality $\llbracket u = v \rrbracket = 1$. The construction is canonical: define $u(x) = \llbracket x \in v \rrbracket$ for all $x \in d$. The verification that $u$ is extensional follows from the fact that $u(x) = \llbracket x \in v \rrbracket$ implies $u(x) \leq \llbracket x \in u \rrbracket = \sum_y \llbracket y \in v \rrbracket \cdot \llbracket x = y \rrbracket \leq \llbracket x \in v \rrbracket = u(x)$. This result means we can restrict attention to extensional sets without loss of generality.
