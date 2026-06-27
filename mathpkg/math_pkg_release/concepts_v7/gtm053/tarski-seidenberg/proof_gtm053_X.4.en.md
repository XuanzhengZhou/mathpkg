---
role: proof
locale: en
of_concept: tarski-seidenberg
source_book: gtm053
source_chapter: "X"
source_section: "4"
---

# Proof of the Tarski-Seidenberg Theorem

**Theorem 4.7 (Tarski-Seidenberg).** The theory $\mathrm{RCF}$ (Real Closed Fields) is complete and admits quantifier elimination.

*Proof.* We use the same method as in the proof of Theorem 4.2 for $\mathrm{ACF}_p$, applying the quantifier elimination criterion of Theorem 3.18. Let $\mathbf{A}$ and $\mathbf{B}$ be two $\kappa$-saturated real closed fields.

**Claim.** Suppose $\mathbf{A}_0, \mathbf{B}_0$ are respectively subfields of cardinality less than $\kappa$ of $\mathbf{A}$ and $\mathbf{B}$, and suppose $\mathbf{A}_0 \cong_\varphi \mathbf{B}_0$ as ordered fields. Then $\varphi$ can be extended to an isomorphism between $\mathbf{A}$ and $\mathbf{B}$.

The claim is proved using a back-and-forth argument based on the following algebraic facts about real closed fields (Lemma in the text):

(i) The isomorphism $\varphi$ extends to an isomorphism $\psi : \tilde{\mathbf{A}}_0 \to \tilde{\mathbf{B}}_0$ between the relative algebraic closures of the respective subfields in $\mathbf{A}$ and $\mathbf{B}$.

(ii) Assuming $\mathbf{A}_0$ and $\mathbf{B}_0$ are respectively algebraically closed in $\mathbf{A}$ and $\mathbf{B}$, if $a_0 \in A \setminus A_0$ and $b_0 \in B \setminus B_0$ satisfy the same cut (i.e., for any $a \in A_0$, $a_0 \leq a$ iff $b_0 \leq \varphi(a)$), then $\varphi$ extends to an ordered field isomorphism $\psi : \mathbf{A}_0(a_0) \to \mathbf{B}_0(b_0)$.

(iii) Assuming $\mathbf{A}_0$ is algebraically closed in $\mathbf{A}$, a finite system of polynomial inequalities $f(x) \leq 0$ (with $f(x) \in A_0[x]$) has a solution in $\mathbf{A}$ iff it has a solution in $\mathbf{A}_0$.

Using these facts, one constructs a back-and-forth system between $\mathbf{A}$ and $\mathbf{B}$. Start with the isomorphism of the prime fields (both are $\mathbb{Q}$ with the usual ordering). At each step, match an element from one field with an element from the other that satisfies the same quantifier-free type (i.e., the same cut in the current subfield). The saturation guarantees that such matching elements always exist.

By the Ehrenfeucht-Fraisse criterion (Theorem 3.15), the existence of a back-and-forth system between $\aleph_0$-saturated structures implies elementary equivalence. Applied to saturated models, it yields the automorphism property required for quantifier elimination: any two tuples with the same quantifier-free type are conjugate by an automorphism.

The quantifier-free type of a tuple in a real closed field is determined by the ordering relations among polynomial expressions in the tuple entries. The back-and-forth construction shows that this information suffices to match tuples across saturated models.

Completeness follows: every sentence reduces to a quantifier-free sentence, and the truth of quantifier-free sentences in $\mathrm{RCF}$ depends only on the axioms of real closed fields (which are complete — all models of $\mathrm{RCF}$ satisfy the same quantifier-free sentences). In particular, $\mathrm{RCF}$ is the theory of the real numbers $\mathbb{R}$ as an ordered field. $\square$

**Corollary (Semialgebraic Sets).** The Tarski-Seidenberg theorem implies that subsets of $\mathbb{R}^n$ definable (using parameters) in the language of ordered fields are precisely the semialgebraic sets — finite Boolean combinations of sets defined by polynomial equations $p(\bar{x}) = 0$ and polynomial inequalities $p(\bar{x}) > 0$. In particular, the projection of a semialgebraic set is semialgebraic.
