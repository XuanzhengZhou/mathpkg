---
role: proof
locale: en
of_concept: "satisfiability-theorem-predicate"
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---
Proof. (Henkin's construction) Put $V_0 = V$, $A_0 = A$. Construct inductively $V_i$, $P_i = P(V_i, \mathcal{R})$, and $A_i$ for $i > 0$. For each $p \in A_i$ of the form $p = (\exists x)q(x)$, take a new variable $t_p^{(i)}$ and put:
$$V_{i+1} = V_i \cup \{t_p^{(i)} \mid p \in A_i, p = (\exists x)q(x)\},$$
$$A_{i+1}' = A_i \cup \{q(t_p^{(i)}) \mid p \in A_i, p = (\exists x)q(x)\}.$$

If $F \notin \operatorname{Ded}(A_i)$, Lemma 4.13 ensures $F \notin \operatorname{Ded}(A_{i+1}')$. By Lemma 2.11 of Chapter II, extend $A_{i+1}'$ to a maximal consistent $A_{i+1}$. Set $V^* = \bigcup_i V_i$, $A^* = \bigcup_i A_i$.

Then $A^*$ is maximal consistent and has the Henkin property: if $(\exists x)q(x) \in A^*$, then $q(t) \in A^*$ for some $t$. Define the universe $U$ as equivalence classes of $V^*$ under $x \sim y$ iff $\mathcal{I}(x,y) \in A^*$. Define $\varphi(x) = [x]_\sim$ and $\psi(r) = \{([x_1], \ldots, [x_n]) \mid r(x_1, \ldots, x_n) \in A^*\}$. The valuation $v$ defined by $v(p) = 1$ iff $p \in A^*$ then gives an interpretation satisfying $A$. $\square$
