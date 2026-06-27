---
role: proof
locale: en
of_concept: duality-principle
source_book: gtm005
source_chapter: "II"
source_section: "1"
---

The dual of each of the axioms for a category is also an axiom. Indeed, the axioms of ETAC (as given in §I.1) include statements such as the associativity of composition and the identity laws. Under dualization, the associativity axiom $h \circ (g \circ f) = (h \circ g) \circ f$ becomes $h \circ (g \circ f) = (h \circ g) \circ f$ with composition order reversed, which is again an instance of the associativity axiom. The identity axioms $f \circ 1_a = f = 1_b \circ f$ for $f: a \to b$ dualize to $1_a \circ f = f = f \circ 1_b$ for $f: b \to a$, which are again identity axioms. Thus the set of axioms is closed under dualization.

Now suppose $\Sigma$ is a consequence of the axioms, so there exists a formal proof $\Pi = (\Sigma_1, \Sigma_2, \ldots, \Sigma_n)$ where each $\Sigma_i$ is either an axiom or follows from earlier statements by a rule of inference, and $\Sigma_n = \Sigma$. Consider the sequence $\Pi^{*} = (\Sigma_1^{*}, \Sigma_2^{*}, \ldots, \Sigma_n^{*})$. Each axiom $\Sigma_i$ dualizes to an axiom $\Sigma_i^{*}$. Each application of a logical rule of inference is preserved under dualization because the propositional connectives and quantifiers are unchanged by the dualization operation. Therefore $\Pi^{*}$ is a valid proof of $\Sigma_n^{*} = \Sigma^{*}$ from the axioms. Hence $\Sigma^{*}$ is a consequence of the axioms. This establishes the duality principle.
