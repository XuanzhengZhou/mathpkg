---
role: proof
locale: en
of_concept: induced-bundle-functor
source_book: gtm020
source_chapter: "5"
source_section: "6"
---
For each map $f: B_1 \to B$, the family of functions $f^*: \mathrm{Bun}_B \to \mathrm{Bun}_{B_1}$ defines a functor. Moreover, for a $B$-morphism $u: \xi \to \eta$, the following diagram is commutative:

$$\begin{CD}
E(f^*(\eta)) @>>> E(\eta) \\
@VVV @VVV \\
E(f^*(\xi)) @>>> E(\xi) \\
@VVV @VVV \\
B_1 @>>> B
\end{CD}$$

*Proof.* We must check the last statement. Let $(b_1, x) \in E(f^*(\xi))$, and compute $u(f_\xi(b_1, x)) = u(x) = f_\eta(b_1, u(x)) = f_\eta(f^*(\eta))(b_1, x)$. We have $u f_\xi = f_\eta f^*(u)$.
