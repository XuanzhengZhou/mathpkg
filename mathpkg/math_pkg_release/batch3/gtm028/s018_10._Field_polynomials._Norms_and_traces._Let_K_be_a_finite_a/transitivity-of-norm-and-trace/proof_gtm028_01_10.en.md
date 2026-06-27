---
role: proof
locale: en
of_concept: transitivity-of-norm-and-trace
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
We use the notation of the proof of Lemma 2 of §6. Let $\{\varphi_i\}_{i=1}^{n}$ be the $L$-isomorphisms of $\Delta$ into a normal closure, and $\{\psi_j\}_{j=1}^{m}$ be the $k$-isomorphisms of $L$ into the same closure. We may assume $\psi_1$ is the identity automorphism of $L$.

By formulas (19) and (20) (the isomorphism expressions for norm and trace):
$$N_{\Delta/L}(x) = \left( \prod_{i=1}^{n} x^{\varphi_i} \right)^{p^\alpha}, \quad p^\alpha = [\Delta : L]_i,$$
$$N_{L/k}(N_{\Delta/L}(x)) = \left( \prod_{j=1}^{m} (N_{\Delta/L}(x))^{\psi_j} \right)^{p^\beta}, \quad p^\beta = [L : k]_i.$$

Substituting the first into the second:
$$N_{L/k}(N_{\Delta/L}(x)) = \left( \prod_{j=1}^{m} \prod_{i=1}^{n} x^{\varphi_i \psi_j} \right)^{p^{\alpha+\beta}}.$$

From the proof of Lemma 2 of §6, the restrictions of the compositions $\varphi_i \psi_j$ to $\Delta$ are distinct and give all the $k$-isomorphisms of $\Delta$ into the normal closure. Furthermore, by Corollary 2 to Theorem 16 of §6, $p^{\alpha+\beta} = [\Delta : k]_i$. Hence the right-hand side is exactly $N_{\Delta/k}(x)$ by formula (19) applied to $\Delta/k$.

The proof for the trace is analogous, using formula (20) instead of (19).
