---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The soundness theorem asserts that the syntactic notion of formal deducibility ($\Gamma \vdash \varphi$) implies the semantic notion of logical consequence ($\Gamma \models \varphi$). In other words, if a formula is provable from a set of hypotheses using the logical axioms and rules of inference, then it holds in every structure where all hypotheses are true. The proof proceeds by induction on the formal proof, reducing to showing that each of the five kinds of logical axioms (tautologies, universal quantifier distribution, vacuous quantification, existential instantiation, and equality axioms) is universally valid. This fundamental result guarantees that first-order logic is sound — no false conclusions can be derived from true premises.
