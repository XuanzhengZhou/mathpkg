---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This definition establishes the fundamental self-reference mechanism in Smullyan's language of arithmetic SAr. Every expression $P$ is assigned a Gödel number $n(P)$, and the label $*P*$ is the SAr term representing this number. A formula $P(x)$ with one free variable defines a set of numbers; an expression $Q$ satisfies $P$ if $n(Q)$ belongs to this set. The crucial notion of "display" says $Q$ is displayed in $P$ if the concatenation $Q * Q*$ (the display of $Q$) satisfies $P$. This definition, together with the numerical relationship $n(Q * Q*) = n(Q) \cdot 10^{n(Q)}$, allows the construction of self-referential formulas that are essential for Tarski's undefinability theorem and Gödel's incompleteness theorem.
