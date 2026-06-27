---
role: proof
locale: en
of_concept: theorem-30-1-weak-second-order-indefinability
source_book: gtm037
source_chapter: "30"
source_section: "5"
---

Let $\mathfrak{A} = (A, +, \cdot, 0, f)$ be a model of $Q^w$. Define $g: \omega \rightarrow A$ recursively by $g0 = 0$ and $g(m+1) = fgm$ for all $m \in \omega$. By induction on $m$, $gm = (\Delta m)^{\mathfrak{A}}$ for each $m \in \omega$. The function $g$ preserves $+$ and $\cdot$ because $Q$ is a subtheory of $Q^w$ (specifically, Robinson's $Q$ ensures the recursive definitions behave correctly).

To show $g$ is onto, suppose there exists $a \in A \setminus g^*\omega$. By axiom 14.17(i)(c) of $Q$, we can define a sequence $\langle x_i : i \in \omega \rangle$ with $x_0 = a$ and $sx_{i+1} = x_i$ for each $i \in \omega$. The weak second-order axiom of $Q^w$, $\forall v_0 \exists F_0 [F_0 v_0 \land \forall v_1 (F_0 s v_1 \rightarrow F_0 v_1)]$, asserts that every element belongs to a finite set closed under predecessor. Applied to $a$, this gives a finite set $F$ containing $a$ such that if $sy \in F$ then $y \in F$. Since the sequence $\langle x_i \rangle$ consists of predecessors of $a$, each $x_i$ must belong to $F$ by closure under predecessor. But $F$ is finite while $\{x_i : i \in \omega\}$ is infinite, contradiction. Hence $g$ is onto, and $g$ is an isomorphism from $(\omega, +, \cdot, s, 0)$ onto $\mathfrak{A}$.

Thus $Q^w$ is categorical: every model is isomorphic to $(\omega, +, \cdot, s, 0)$. Now by the proofs of 15.20 and 15.21 (Tarski's undefinability), the set $\{g^+ \psi : Q^w \models \psi\}$ is not elementarily definable in $(\omega, +, \cdot, s, 0)$. Since $Q^w \models \psi$ iff $\models \bigwedge Q^w \rightarrow \psi$, the set $\{g^+ \psi : \models \psi\}$ of weak second-order validities is also not elementarily definable. By 14.16, a set not elementarily definable in $(\omega, +, \cdot, s, 0)$ cannot be recursively enumerable. Therefore the set of weak second-order validities is not recursively enumerable, and no complete, effective proof theory exists for weak second-order logic.
