---
role: proof
locale: en
of_concept: comparability-theorem-factors
source_book: gtm003
source_chapter: "VI"
source_section: "8"
---

If $W$ is a factor, then $Z(W) = \mathbb{C}e$, so the only central projections are $0$ and $e$. For any two projections $p, q \in P(W)$, their central supports satisfy $z(p) = e$ (unless $p = 0$) and similarly $z(q) = e$ (unless $q = 0$). Hence $p$ and $q$ are never centrally orthogonal (unless one is zero, in which case the result is trivial).

By the lemma on centrally orthogonal projections, $pWq \neq \{0\}$, so there exist non-zero equivalent sub-projections $p_1 \leq p$ and $q_1 \leq q$. This implies neither $p \prec q$ nor $q \prec p$ can be ruled out trivially.

The full comparability theorem (Theorem 8.6, of which this is a corollary) uses a maximality argument to show that at least one of $p \preceq q$ or $q \preceq p$ holds in any $W^*$-algebra. In a factor, the total order property (exactly one of $p \prec q$, $p \sim q$, $q \prec p$) follows because the central support argument ensures that non-comparability would produce non-trivial central projections, contradicting factoriality.
