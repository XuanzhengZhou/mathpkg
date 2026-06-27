---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This is the most commonly stated form of Gödel's completeness theorem: syntactic deducibility ($\Gamma \vdash \varphi$) coincides with semantic logical consequence ($\Gamma \models \varphi$). The forward direction is the Soundness Theorem (Lemma 11.8). The reverse direction is proved by contraposition: if $\Gamma \not\vdash \varphi$, then $\Gamma \cup \{\neg\varphi\}$ is consistent, hence by the first form has a model, which witnesses $\Gamma \not\models \varphi$. Together with soundness, this establishes the perfect correspondence between syntax and semantics in first-order logic: truth in all models is exactly what is formally provable.
