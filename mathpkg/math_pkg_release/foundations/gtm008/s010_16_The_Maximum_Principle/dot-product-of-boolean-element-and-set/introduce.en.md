---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This exercise (following Definition 16.7) introduces the dot product $b \cdot u$, which scales a Boolean-valued set $u$ by a Boolean element $b \in B$. The operation is defined pointwise: $(b \cdot u)(x) = b \land u(x)$. Two key properties are established: Boolean membership scales linearly ($\llbracket v \in b \cdot u \rrbracket = b \land \llbracket v \in u \rrbracket$), and scaling two sets equally preserves their difference ($\llbracket b \cdot u = b \cdot v \rrbracket = \neg b \lor \llbracket u = v \rrbracket$). This operation is used extensively in later theorems for adjusting Boolean truth values.
