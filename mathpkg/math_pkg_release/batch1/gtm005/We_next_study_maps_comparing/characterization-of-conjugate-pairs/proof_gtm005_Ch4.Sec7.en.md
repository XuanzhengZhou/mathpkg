---
role: proof
locale: en
of_concept: characterization-of-conjugate-pairs
source_book: gtm005
source_chapter: "IV"
source_section: "7"
---

**Proof.** First, the conjugacy condition (5) implies each of the four diagrammatic conditions (6) and (7). To see that (5) implies the first diagram of (6), put $x = G'a$ in (5), start with the identity arrow $1 : G'a \to G'a$ in the upper right corner, and use the description of $\varphi$ and $\varphi'$ by unit and counit to chase this element around the diagram:

From $1_{G'a}$ in $X(G'a, G'a)$:
- Applying $\varphi'^{-1}$ yields $\varepsilon'_a : F'G'a \to a$ in $A(F'G'a, a)$.
- Then applying $(\sigma_{G'a})^*$ gives $\varepsilon'_a \circ \sigma_{G'a} : FG'a \to a$.
- Applying $\varphi$ yields $G(\varepsilon'_a \circ \sigma_{G'a}) \circ \eta_{G'a} : G'a \to Ga$.

Going the other way:
- From $1_{G'a}$, applying $X(G'a, \tau_a)$ yields $\tau_a : G'a \to Ga$.

The commutativity of (5) forces these to be equal, giving the first diagrammatic condition. The other three conditions are obtained similarly by starting from appropriate identity arrows.

Now suppose $\sigma$ is given but $\tau$ is not. Apply the Yoneda Lemma to the composite natural transformation
$$\varphi \circ (\sigma_x)^* \circ \varphi'^{-1}$$
(three legs of diagram (5)). This shows there exists a unique family of arrows $\tau'_a$ for which (5) commutes, and this family is a natural transformation.

Since each $\varepsilon_a : FGa \to a$ is universal from $F$ to $a$, there is also a unique family of arrows $\tau''_a : G'a \to Ga$ for which the first diagram of (7) commutes. Since (5) implies (7), we have $\tau'_a = \tau''_a$. In other words, if $\tau = \tau''$ makes the first square of (7) commute, it also makes (5) commute. Therefore the first square of (7) implies (5).

Given $\sigma$, there is immediately a unique natural transformation $\tau : G' \to G$ for which the first of (6) commutes; since (5) implies (6), $\tau'_a = \tau_a$, and hence the solutions $\tau'_a$ of (5) are necessarily natural. Moreover, (6) implies (5).

Thus any of the equivalent conditions determines $\tau$ uniquely from $\sigma$, and dually, determines $\sigma$ uniquely from $\tau$. This establishes both the characterization and the bijective correspondence.
