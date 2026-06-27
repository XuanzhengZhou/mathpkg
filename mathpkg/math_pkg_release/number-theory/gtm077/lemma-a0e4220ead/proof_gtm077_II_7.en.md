---
role: proof
locale: en
of_concept: lemma-a0e4220ead
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Lemma (a): No Basis Element Is a \(p\)-th Power

Let \(\mathfrak{G}\) be a finite abelian group of prime-power order \(p^k\). Let \(B_1, \ldots, B_r\) be a maximal system of independent elements with orders \(h_1 \geq h_2 \geq \cdots \geq h_r > 1\), each a power of \(p\).

**Statement.** No element among \(B_1, \ldots, B_r\) can be the \(p\)-th power of an element of \(\mathfrak{G}\).

**Proof.** Suppose to the contrary that \(B_m = C^p\) for some \(C \in \mathfrak{G}\). Consider the system obtained by replacing \(B_m\) with \(C\) (and renumbering if needed to preserve decreasing order of orders). The element \(C\) has order \(p \cdot |B_m|\), which is strictly larger than the order of \(B_m\) (since \(C^p = B_m \neq E\) and the orders are powers of \(p\)).

The new system \(\{B_1, \ldots, B_{m-1}, C, B_{m+1}, \ldots, B_r\}\) (renumbered to decreasing orders) is still independent: if a relation
\[
B_1^{x_1} \cdots B_{m-1}^{x_{m-1}} \cdot C^y \cdot B_{m+1}^{x_{m+1}} \cdots B_r^{x_r} = E
\]
held nontrivially, raising to the \(p\)-th power would yield a nontrivial relation among the original \(B_i\) (since \(C^p = B_m\)), contradicting their independence.

But the new system has rank \(> r\) (or the same \(r\) but with larger element orders, giving a strictly larger product of orders), contradicting the maximality of the chosen system. Hence no \(B_m\) can be a \(p\)-th power.

\(\square\)
