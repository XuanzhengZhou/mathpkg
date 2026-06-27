---
role: proof
locale: en
of_concept: semisimple-action-on-unipotent
source_book: gtm021
source_chapter: "18"
source_section: "18.3"
---

Proof by induction on dim U. Base case dim U = 0 is trivial. For dim U > 0, U is nilpotent (Corollary 17.5), so its center Z(U) has positive dimension. Let V = Z(U)^circ. Form quotient U' = U/V with induced action of s'. The triple (N_G(V)/V, U', s') satisfies the assumptions. By induction, tau': C_{U'}(s') x M' to U' is bijective, and tau_0: C_V(s) x gamma_s(V) to V is bijective. Injectivity of tau: if z x = y with z in C, x,y in M, apply pi to get pi(z)=e so z in V. Write x=gamma_s(u), y=gamma_s(v). Then z(u s u^{-1}) = v s v^{-1}. The left side is the Jordan decomposition of v s v^{-1} (since V is central in U), whence z=e and x=y. For surjectivity: gamma_s(V) = M intersect V via tau_0 and injectivity. Then C_{U'}(s') = pi(C), completing the proof.
