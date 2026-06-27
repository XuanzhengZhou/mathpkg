---
role: exercise
locale: en
chapter: "IV"
section: "7. The Functors Ext^n_A Using Projectives"
exercise_number: 3
---

# Exercise 7.3

Let $M^* = \operatorname{Hom}_A(M, \Lambda)$ for any $\Lambda$-module $M$. Let $P_1 \to P_0 \to M \to 0$ be an exact sequence of $\Lambda$-modules with $P_0, P_1$ finitely generated projective. Let

$$D = \operatorname{coker}(P_0^* \to P_1^*).$$

Show that the sequence

$$0 \to \operatorname{Ext}_A^1(D, \Lambda) \to M \to M^{**} \to \operatorname{Ext}_A^2(D, \Lambda) \to 0$$

is exact.

*Hint:* Consider the diagram

$$\begin{CD}
P_1 @>>> P_0 @>>> M @>>> 0
\end{CD}$$

$$\begin{CD}
0 @>>> K^* @>>> P_0^* @>>> M^*
\end{CD}$$

where $K = \ker(P_1^* \to D) = \operatorname{coker}(M^* \to P_0^*)$; and show that $P_0 \to P_0^{**}$ is an isomorphism.
