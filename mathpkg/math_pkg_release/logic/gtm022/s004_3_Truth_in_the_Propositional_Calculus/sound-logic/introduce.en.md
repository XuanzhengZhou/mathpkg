---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A logic is called sound if syntactic provability implies semantic truth: whenever $A \vdash p$ (there is a proof of $p$ from assumptions $A$), it follows that $A \models p$ (every valuation making $A$ true also makes $p$ true). Soundness is the property that the proof system does not prove anything false — it only derives propositions that are genuine logical consequences of the assumptions. For the propositional calculus $\text{Prop}(X)$, soundness is verified by checking that the axioms are tautologies and that modus ponens preserves truth.
