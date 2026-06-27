---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 17.2 is Löb's Theorem, a fundamental result in proof theory and the study of formal provability. It states that in any strong theory $\Gamma$ equipped with a provability predicate $\Pr$ satisfying the Hilbert-Bernays derivability conditions, if the theory proves $\Pr(\lceil\varphi\rceil) \rightarrow \varphi$ for some sentence $\varphi$, then $\Gamma$ already proves $\varphi$. This result is a powerful fixed-point argument that generalizes Gödel's Second Incompleteness Theorem: taking $\varphi$ to be a contradiction $0 \neq 0$ yields that if $\Gamma$ proves its own consistency (i.e., $\Pr(\lceil 0 \neq 0 \rceil) \rightarrow 0 \neq 0$), then $\Gamma$ would prove a contradiction and hence be inconsistent. The proof uses the diagonal lemma to construct a self-referential sentence and formalizes the representation of elementary functions via operation symbols in the strong theory.
