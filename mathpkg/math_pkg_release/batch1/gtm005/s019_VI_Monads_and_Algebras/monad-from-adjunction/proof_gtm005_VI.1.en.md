---
role: proof
locale: en
of_concept: monad-from-adjunction
source_book: gtm005
source_chapter: "VI"
source_section: "1. Monads in a Category"
---

We verify that $\langle GF, \eta, G\varepsilon F \rangle$ satisfies the axioms of a monad.

**Associativity.** We must show that the following diagram commutes:
\[
\begin{CD}
GFGFGF @>{GF(G\varepsilon F)}>> GFGF \\
@V{(G\varepsilon F)GF}VV @VV{G\varepsilon F}V \\
GFGF @>>{G\varepsilon F}> GF
\end{CD}
\]
Since $G\varepsilon F$ is natural in its components, this is equivalent to the commutativity of
\[
\begin{CD}
GFGFGF @>{G\varepsilon FGF}>> GFGF \\
@V{GFG\varepsilon F}VV @VV{G\varepsilon F}V \\
GFGF @>>{G\varepsilon F}> GF
\end{CD}
\]
Both paths equal $G(\varepsilon \circ F G \varepsilon \circ \varepsilon_{FG})F$, which by the triangle identity
$\varepsilon_{F} \circ F\eta = 1_F$ reduces as required. More directly, by the naturality of
$\varepsilon: FG \to I_A$, the square
\[
\begin{CD}
FGFG @>{FG\varepsilon}>> FG \\
@V{\varepsilon FG}VV @VV{\varepsilon}V \\
FG @>>{\varepsilon}> I_A
\end{CD}
\]
commutes. Applying $G(-)F$ everywhere yields the associativity diagram for $\mu = G\varepsilon F$.

**Left unit law.** We must show $T \xrightarrow{\eta T} T^2 \xrightarrow{\mu} T$ equals the identity:
\[
\mu \circ (\eta T) = G\varepsilon F \circ \eta GF = G(\varepsilon F \circ F\eta G) = G(1_F G) = 1_{GF}
\]
where $\varepsilon F \circ F\eta = 1_F$ is one of the triangle identities of the adjunction.

**Right unit law.** Similarly:
\[
\mu \circ (T\eta) = G\varepsilon F \circ GF\eta = G(\varepsilon F \circ F\eta) = G(1_F) = 1_{GF}
\]
using the same triangle identity.

Thus $\langle GF, \eta, G\varepsilon F \rangle$ is indeed a monad in $X$.
