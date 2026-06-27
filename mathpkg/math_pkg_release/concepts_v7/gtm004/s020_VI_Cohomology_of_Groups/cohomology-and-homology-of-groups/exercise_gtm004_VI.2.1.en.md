---
role: exercise
locale: en
chapter: "VI"
section: "2"
exercise_number: 1
---

# Exercise 2.1

Prove the following basic properties of group cohomology $H^n(G, A)$ and homology $H_n(G, B)$, which follow immediately from the definition as right/left derived functors:

**(2.3) Long exact sequences.** To a short exact sequence $A' \rightarrowtail A \twoheadrightarrow A''$ of $G$-modules there corresponds a long exact cohomology sequence

$$0 \to H^0(G, A') \to H^0(G, A) \to H^0(G, A'') \to H^1(G, A') \to \cdots$$

$$\cdots \to H^n(G, A') \to H^n(G, A) \to H^n(G, A'') \to H^{n+1}(G, A') \to \cdots.$$

To a short exact sequence $B' \rightarrowtail B \twoheadrightarrow B''$ of right $G$-modules there corresponds a long exact homology sequence

$$\cdots \to H_n(G, B') \to H_n(G, B) \to H_n(G, B'') \to H_{n-1}(G, B') \to \cdots$$

$$\cdots \to H_1(G, B'') \to H_0(G, B') \to H_0(G, B) \to H_0(G, B'') \to 0.$$

**(2.4) Vanishing on injectives and flats.** If $A$ is an injective $G$-module, then $H^n(G, A) = 0$ for all $n \geq 1$. If $B$ is a flat (in particular projective) right $G$-module, then $H_n(G, B) = 0$ for all $n \geq 1$.

Prove these using the fact that $H^n(G, -) = R^n(-)^G$ and $H_n(G, -) = L_n(-)_G$ are derived functors of the invariants and coinvariants functors respectively.

*Hint:* Property (2.3) follows from the general long exact sequence for derived functors (Theorem IV.6.1). Property (2.4) follows from the fact that derived functors vanish on injective/projective objects.
