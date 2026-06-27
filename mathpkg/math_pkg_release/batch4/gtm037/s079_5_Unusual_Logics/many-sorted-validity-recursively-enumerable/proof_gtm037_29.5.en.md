---
role: proof
locale: en
of_concept: many-sorted-validity-recursively-enumerable
source_book: gtm037
source_chapter: "29"
source_section: "5. Unusual Logics"
---

By Corollary 29.29, for any many-sorted sentence $\varphi$, $\models \varphi$ iff $\Gamma \models \varphi^*$, where $\Gamma$ is the set of sort axioms and $\varphi^*$ is the translation of $\varphi$ into the associated ordinary first-order language $\mathcal{L}^*$.

The set $\Gamma$ is recursively enumerable (it consists of finitely many axiom schemas: $\exists v_0 \mathbf{P}_s(v_0)$ for each $s \in \mathcal{S}$, and closure conditions on operations and relations respecting sorts). In ordinary first-order logic, the set $\{ \psi : \Gamma \models \psi \}$ of logical consequences of an r.e. set $\Gamma$ is itself r.e. (by the completeness theorem: $\Gamma \models \psi$ iff $\Gamma \vdash \psi$, and the set of theorems of an r.e. axiom set is r.e.).

The mapping $\varphi \mapsto \varphi^*$ is recursive. Therefore the set

$$\{ \varphi : \varphi \text{ is a many-sorted sentence and } \models \varphi \} = \{ \varphi : \Gamma \models \varphi^* \}$$

is recursively enumerable.
