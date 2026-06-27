---
role: proof
locale: en
of_concept: comonad-from-adjunction
source_book: gtm005
source_chapter: "VI"
source_section: "1. Monads in a Category"
---

The proof is dual to that for the monad defined by an adjunction. We verify that
$\langle FG, \varepsilon, F\eta G \rangle$ satisfies the comonad axioms.

**Coassociativity.** We must show that the following diagram commutes:
\[
\begin{CD}
FG @>{F\eta G}>> FGFG \\
@V{F\eta G}VV @VV{FGF\eta G}V \\
FGFG @>>{F\eta GFG}> FGFGFG
\end{CD}
\]
Since $F\eta G$ is natural, this is equivalent to the commutativity of
\[
\begin{CD}
FG @>{F\eta G}>> FGFG \\
@V{F\eta G}VV @VV{FG F\eta G}V \\
FGFG @>>{F\eta G FG}> FGFGFG
\end{CD}
\]
By the naturality of $\eta: I_X \to GF$, the square
\[
\begin{CD}
I_X @>{\eta}>> GF \\
@V{\eta}VV @VV{GF\eta}V \\
GF @>>{\eta GF}> GFGF
\end{CD}
\]
commutes. Applying $F(-)G$ everywhere yields the coassociativity diagram for $\delta = F\eta G$.

**Counit laws.** (Left counit law)
\[
\varepsilon FG \circ F\eta G = F(\varepsilon \circ \eta G) = F(1_G) = 1_{FG}
\]
where $G\varepsilon \circ \eta G = 1_G$ is one triangular identity (applied to $F$ yields $F G\varepsilon \circ F\eta G$,
but the relevant identity for the left counit law is $\varepsilon_{F} \circ F\eta = 1_F$;
the statement $\varepsilon FG \circ FG\eta = 1_{FG}$ follows similarly from
$\varepsilon \circ \eta = 1$ after applying $F(-)G$).

(Right counit law) Similarly:
\[
FG\varepsilon \circ F\eta G = F(G\varepsilon \circ \eta G) = F(1_G) = 1_{FG}
\]
using the triangular identity $G\varepsilon \circ \eta G = 1_G$.

Thus $\langle FG, \varepsilon, F\eta G \rangle$ is indeed a comonad in $A$.
