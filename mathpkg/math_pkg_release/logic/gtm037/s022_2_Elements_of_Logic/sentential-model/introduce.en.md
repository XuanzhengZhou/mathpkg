---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This definition introduces the semantic side of sentential logic. A model is a truth assignment $f: P \to \{0,1\}$ to the sentence symbols, which extends uniquely via the recursion principle to a truth evaluation $f^+$ on all sentences. A sentence is called a tautology if it evaluates to true under every possible truth assignment. The semantic consequence relation $\Gamma \models \varphi$ (logical implication) holds when every model of $\Gamma$ is also a model of $\varphi$. Whether a sentence is a tautology can be decided by the familiar truth table method.
