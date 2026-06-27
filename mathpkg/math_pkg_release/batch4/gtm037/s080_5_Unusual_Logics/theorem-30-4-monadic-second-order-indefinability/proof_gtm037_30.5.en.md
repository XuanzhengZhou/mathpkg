---
role: proof
locale: en
of_concept: theorem-30-4-monadic-second-order-indefinability
source_book: gtm037
source_chapter: "30"
source_section: "5"
---

The proof parallels that of Theorem 30.1, using $Q^m$ in place of $Q^w$. First, we show $Q^m$ is categorical. Let $\mathfrak{A} = (A, +, \cdot, 0, s)$ be a model of $Q^m$. Define $g: \omega \rightarrow A$ by $g0 = 0$ and $g(m+1) = s(gm)$. As before, $g$ preserves $+$ and $\cdot$ by the axioms of $Q$.

To show $g$ is onto, suppose there exists $a \in A \setminus g^*\omega$. Consider the monadic second-order induction axiom of $Q^m$:
$$\forall P_0 [P_0 \mathbf{0} \wedge \forall v_0 (P_0 v_0 \rightarrow P_0 \mathbf{s} v_0) \rightarrow \forall v_0 P_0 v_0].$$

Let $P_0$ be interpreted as the set $g^*\omega \subseteq A$. Then $0 \in g^*\omega$ (since $g0 = 0$), and if $x \in g^*\omega$, say $x = gm$, then $sx = s(gm) = g(m+1) \in g^*\omega$. By the induction axiom, $\forall v_0 P_0 v_0$, meaning every element of $A$ is in $g^*\omega$, i.e., $g$ is onto. Hence $\mathfrak{A} \cong (\omega, +, \cdot, s, 0)$, establishing categoricity of $Q^m$.

Now, as in the proof of Theorem 30.1, the set $\{g^+ \psi : Q^m \models \psi\}$ is not elementarily definable in $(\omega, +, \cdot, s, 0)$ by the proofs of 15.20 and 15.21. Since $Q^m \models \psi$ iff $\models \bigwedge Q^m \rightarrow \psi$, the set $\{g^+ \psi : \models \psi\}$ of monadic second-order validities is not elementarily definable. By 14.16, it is not recursively enumerable. Thus no complete, effective proof theory exists for monadic second-order logic.
