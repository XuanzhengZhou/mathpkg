---
role: exercise
locale: en
chapter: "VI"
section: "2"
exercise_number: 3
---

# Exercise 2.3

Prove the long exact sequences for group cohomology and homology (property (2.3)):

Given a short exact sequence $A' \rightarrowtail A \twoheadrightarrow A''$ of $G$-modules, construct the long exact cohomology sequence

$$0 \to H^0(G, A') \to H^0(G, A) \to H^0(G, A'') \xrightarrow{\delta} H^1(G, A') \to \cdots$$

$$\cdots \to H^n(G, A') \to H^n(G, A) \to H^n(G, A'') \xrightarrow{\delta} H^{n+1}(G, A') \to \cdots.$$

Similarly, given a short exact sequence $B' \rightarrowtail B \twoheadrightarrow B''$ of right $G$-modules, construct the long exact homology sequence

$$\cdots \to H_n(G, B') \to H_n(G, B) \to H_n(G, B'') \xrightarrow{\partial} H_{n-1}(G, B') \to \cdots$$

$$\cdots \to H_1(G, B'') \xrightarrow{\partial} H_0(G, B') \to H_0(G, B) \to H_0(G, B'') \to 0.$$

Describe the connecting homomorphisms $\delta$ and $\partial$ explicitly in terms of the snake lemma.

*Hint:* Use the definition $H^n(G, A) = \operatorname{Ext}_{\mathbb{Z}G}^n(\mathbb{Z}, A)$ and $H_n(G, B) = \operatorname{Tor}_n^{\mathbb{Z}G}(B, \mathbb{Z})$, together with the long exact sequences for Ext and Tor (Section IV.7 and IV.12).
