---
role: proof
locale: en
of_concept: boolean-valued-tautologies
source_book: gtm053
source_chapter: "5"
source_section: "5.8"
---

An example of a natural map $\|\cdot\|$ can be obtained as follows: if we are given an interpretation of $L$ in a set $M$, then the truth functions $|P|(\xi)$ can be considered as the characteristic functions of the definable subsets of the interpretation class $\overline{M}$ (compare Section 2). Hence, our usual truth functions are essentially Boolean-valued. They are embedded in the Boolean algebra of all subsets of $\overline{M}$, which decomposes as a direct product of two-point Boolean algebras $\{0,1\}$. Hence the proposition follows trivially in this case.

In the general case one could use Stone's structure theorem for Boolean algebras. However, instead of this we shall indicate how to reduce the problem to some simple computations using Proposition 5.1. Because of Proposition 5.1, it suffices to verify that the basis tautologies are $\|\cdot\|$-true and that $\|\cdot\|$-truth is preserved when we use MP.

**Preservation under MP.** If $\|P\| = 1$ and $\|P \Rightarrow Q\| = 1$, then by the Boolean definition of implication, $\|P \Rightarrow Q\| = \|P\|' \lor \|Q\|$. Hence $\|P\|' \lor \|Q\| = 1$. Since $\|P\| = 1$, we have $\|P\|' = 0$, so $0 \lor \|Q\| = 1$. By axiom 5.6(f), $0 \lor \|Q\| = \|Q\|$, hence $\|Q\| = 1$. This shows that MP preserves $\|\cdot\|$-truth.

**Basis tautologies.** The truth values of the basis tautologies (A0--A3, B1, B2, C1, C2, etc.) are computed in a similar manner using the axioms in 5.6. For each basis tautology, one expresses its Boolean truth value using the operations $'$, $\lor$, $\land$ and verifies that it equals $1$ by algebraic manipulation using the Boolean algebra axioms (a)--(f).

Since every tautology $P$ is deducible from the basis tautologies using MP (Proposition 5.1), and both the basis tautologies and the deduction rule MP preserve $\|\cdot\|$-truth, it follows that $\|P\| = 1$ for every tautology $P$.
