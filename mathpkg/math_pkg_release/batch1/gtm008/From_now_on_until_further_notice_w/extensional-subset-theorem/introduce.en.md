---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 16.22 provides a useful construction: given an extensional set $v$ and the Boolean truth value $b = \llbracket v \subseteq u \rrbracket$ of $v$ being a subset of $u$, the scaled set $v' = b \cdot v$ is extensional, is fully a subset of $u$ (with truth value $1$), and its Boolean equality with $v$ exactly equals $b$. This is a technical lemma used in the treatment of power sets: it allows us to adjust an extensional set so that it becomes a subset of $u$ in the Boolean-valued sense, while exactly preserving the truth value of the original subset relationship. The proof uses the exercise identity $\llbracket v = b \cdot v \rrbracket \geq b$ when $v$ is extensional.
