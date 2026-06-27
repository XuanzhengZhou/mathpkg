---
role: proof
locale: en
of_concept: duality-principle-for-functors
source_book: gtm005
source_chapter: "II"
source_section: "1"
---

Consider the elementary theory of one functor $T: C \to B$. The atomic statements are those for the category $C$ (domain, codomain, identity, composition, equality on objects and arrows), a corresponding list for the category $B$, and the statements $Tc = b$ and $Tf = h$ giving the values of the object and arrow functions of $T$. The axioms include the axioms for a category for $C$, the axioms for a category for $B$, and the functor axioms $T(g \circ_C f) = T(g) \circ_B T(f)$ and $T(1_a) = 1_{Ta}$.

The dual of a statement is formed by simultaneously dualizing the atomic parts referring to $C$ and to $B$. When we dualize, the functor axiom $T(g \circ_C f) = T(g) \circ_B T(f)$ becomes $T(f \circ_C g) = T(f) \circ_B T(g)$ (since the order of composition is reversed in both $C$ and $B$), which is again an instance of the same functor axiom (just with $f$ and $g$ swapped). Similarly, $T(1_a) = 1_{Ta}$ dualizes to itself since the identity arrow is self-dual. Thus the statement that $T$ is a functor is self-dual, and the set of axioms for the theory of a functor is closed under dualization.

Now if $\Sigma$ is a consequence of the axioms, there exists a proof from the axioms. Taking the dual of every statement in that proof yields a valid proof of $\Sigma^{*}$, because each axiom dualizes to an axiom and each logical rule of inference is preserved under dualization. Hence $\Sigma^{*}$ is also a consequence of the axioms. This extends the duality principle to theories involving multiple categories and functors.
