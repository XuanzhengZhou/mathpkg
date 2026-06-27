---
role: proof
locale: en
of_concept: gch-valid-no-definable-wellordering
source_book: gtm008
source_chapter: "19"
source_section: "19"
---

Let $B$ be as in Theorem 19.4 (the complete Boolean algebra of regular open sets of the partial order structure $P$ used for the independence of $V = L$). Then $\overline{B} \leq 2^{\aleph_0}$ and, by the GCH in $V$, $|B^{\mathcal{D}((\omega_\alpha)^\vee)}| = \aleph_{\alpha+1}$. Thus, by Theorem 19.2, the GCH is $B$-valid in $V^{(B)}$.

To show that "there is a definable well-ordering of $\mathcal{P}(\omega)$" is not $B$-valid, suppose there were a formula $\varphi$ of $\mathcal{L}_0(C(V))$ defining a well-ordering in $V^{(B)}$. Then by Theorem 19.4, the only elements of $B$ invariant under all automorphisms are $0$ and $1$. However, if $\varphi$ defines a well-ordering, then one can construct a non-trivial element of $B$ that is invariant under all automorphisms, yielding a contradiction (cf. the proof of Theorem 11.7).

Specifically, let $u \in V^{(B)}$ code a well-ordering. By considering the action of automorphisms $\pi_k$ on $P$ (as defined before Theorem 11.7) and their induced automorphisms on $B$, one shows that no such $u$ can exist unless $B$ has non-trivial invariant elements, contradicting Theorem 19.4. Therefore $\llbracket$ "there is a definable well-ordering of $\mathcal{P}(\omega)$" $\rrbracket \neq 1$.
