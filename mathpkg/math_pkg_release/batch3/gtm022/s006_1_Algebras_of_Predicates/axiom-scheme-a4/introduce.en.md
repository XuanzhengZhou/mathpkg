---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Axiom scheme $\mathcal{A}_4$ captures the interaction between universal quantification and implication. It states that if $(\forall x)(p \Rightarrow q)$ holds, and $p$ does not depend on $x$ (i.e., $x$ is not free in $p$), then $p$ implies $(\forall x)q$. The side condition $x \notin \text{var}(p)$ is essential: without it, one could derive false statements by illicitly generalizing over a variable that occurs free in an assumption.
