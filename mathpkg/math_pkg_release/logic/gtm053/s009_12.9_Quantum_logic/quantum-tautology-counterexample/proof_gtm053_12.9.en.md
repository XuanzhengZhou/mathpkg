---
role: proof
locale: en
of_concept: quantum-tautology-counterexample
source_book: gtm053
source_chapter: "12"
source_section: "12.9"
---

**Proof sketch.** If $p_r$ and $p_s$ are orthogonal lines in $E^3$, then their orthogonal complements satisfy $p_r' \vee p_s' = E^3$, so $Q(p_r, p_s) = p_r' \vee p_s' = 1 \in B(E^3)$. Similarly, if $p_i, p_j, p_k$ are three mutually orthogonal lines, then

$$P(p_i, p_j, p_k) = 1 \in B(E^3).$$

To verify the latter, define the symmetric difference operation

$$a + b = (a \wedge b') \vee (a' \wedge b).$$

Then we may take

$$P(p, q, r) = p + q + r + p \wedge q \wedge r$$

(for any arrangement of parentheses on the right), so that

$$P(p_i, p_j, p_k) = p_i \oplus p_j \oplus p_k = E^3 = 1 \in B(E^3).$$

Now, substituting the lines corresponding to the vertices of a fixed realization of $\Gamma_2$ on $S^2$ for the variables $p_1, \ldots, p_{117}$ makes every conjunct in the big conjunction equal to $1$, so the whole conjunction equals $1$, and its negation $R$ equals $0 \in B(E^3)$. On the other hand, $R$ is a classical tautology because in any Boolean valuation, the orthogonality constraints encoded by the graph $\Gamma_2$ cannot all be satisfied simultaneously (by the Kochen–Specker theorem proved above), so at least one of the $P(p_i, p_j, p_k)$ or $Q(p_r, p_s)$ conjuncts must evaluate to $0$, making the big conjunction $0$ and its negation $1$.
