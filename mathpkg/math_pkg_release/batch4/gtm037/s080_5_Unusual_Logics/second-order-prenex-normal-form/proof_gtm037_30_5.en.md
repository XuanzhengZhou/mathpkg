---
role: proof
locale: en
of_concept: second-order-prenex-normal-form
source_book: gtm037
source_chapter: "30"
source_section: "Unusual Logics"
---

The usual transformations yield a prenex normal form for $\varphi$. To get the quantifier prefix in the specific form (relation quantifiers first, then universal individual quantifiers, then existential individual quantifiers), we use the following interchange principles:

(1) $\models \exists v_i \exists R_k^j \psi \leftrightarrow \exists R_k^j \exists v_i \psi$
(2) $\models \forall v_i \exists R_k^j \psi \leftrightarrow \exists R_k^{j+1} \forall v_i \psi'$, where $R_k^{j+1}$ is new
(3) $\models \forall v_i \forall R_k^j \psi \leftrightarrow \forall R_k^j \forall v_i \psi$
(4) $\models \exists v_i \forall R_k^j \psi \leftrightarrow \forall R_k^{j+1} \exists v_i \psi'$

and the key transformation (6) for shifting an existential individual quantifier past a universal individual quantifier. Using (1)-(6), all existential quantifiers $\exists v_i$ can be shifted to the far right, and all second-order quantifiers to the far left of the prefix.
