---
role: proof
locale: en
of_concept: subspaces-in-general-position
source_book: gtm014
source_chapter: "V"
source_section: "§1"
---

**Proof of Lemma 1.7.** [Note: The original OCR text was partially truncated. The following is reconstructed from context and the usage in Lemma 1.9.]

Condition $(\dagger)$ at $S$ gives the jet-space equality
\[
J^m(f^*TY)_S = (df)\, J^m(TX)_S + f^*\, J^m(TY)_q.
\]
By Proposition 1.5, this implies simultaneous local infinitesimal stability at $S$, so for any $\tau \in C^\infty(f^*TY)_S$ there exist $\zeta \in C^\infty(TX)_S$ and $\eta \in C^\infty(TY)_q$ such that $\tau = (df)(\zeta) + f^*\eta$ on a neighborhood of $S$.

Now set $h_i = (df)_{p_i}(\zeta_i) \in H_i$ and $y = \eta_q \in T_qY$. The equation $\tau_i = h_i + y$ (where the pullback acts by $f^*\eta_q = \eta_q$ at the level of tangent vectors after evaluation) shows that any tuple $(\tau_1,\ldots,\tau_k)$ with $\tau_i \in T_qY$ can be expressed as $(h_1 + y, \ldots, h_k + y)$ with $h_i \in H_i$ and $y \in T_qY$. This implies that the $H_i$ are in general position: the dimension of their intersection is minimal, i.e., $\operatorname{codim}(\bigcap H_i) = \sum \operatorname{codim} H_i$. This follows from the fact that the map $\bigoplus_i H_i \oplus T_qY \to \bigoplus_i T_qY$ given by $((h_i), y) \mapsto (h_i + y)$ is surjective, which forces the codimension additivity. $\square$
