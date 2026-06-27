---
role: proof
locale: en
of_concept: injective-envelope-uniqueness
source_book: gtm004
source_chapter: "I. Modules"
source_section: "9. Essential Extensions"
---

# Proof of Corollary 9.3: Uniqueness of the Injective Envelope

Let $E_1$, $E_2$ be two maximal essential extensions of $A$ contained in injective modules $I_1$, $I_2$ respectively. Consider the diagram

$$\begin{CD}
E_1 @. \\
@A{i_1}AA @. \\
A @. E_2 \\
@V{i_2}VV @. \\
E_2 @.
\end{CD}$$

Since $E_2$ is injective (by Theorem 9.2, maximal essential extensions are injective) and $i_1 : A \hookrightarrow E_1$ is a monomorphism, there exists a $\Lambda$-module homomorphism $\xi : E_1 \rightarrow E_2$ making the diagram commute: $\xi \circ i_1 = i_2$.

**$\xi$ is a monomorphism.** Suppose $\ker \xi \neq 0$. Since $E_1$ is an essential extension of $A$, we have $\ker \xi \cap A \neq 0$. But $\xi|_A = i_2$ is a monomorphism, so $\ker \xi \cap A = 0$, a contradiction. Hence $\ker \xi = 0$ and $\xi$ is monic.

**$\xi$ is an isomorphism.** Since $\xi : E_1 \hookrightarrow E_2$ is a monomorphism and $E_2$ is an essential extension of $A$, we have that $E_2$ is also an essential extension of $\xi(E_1) \cong E_1$. But $E_1$, being a maximal essential extension, admits no proper essential monomorphism (as argued in the proof of Theorem 9.2). Therefore $\xi(E_1)$ cannot be a proper submodule of $E_2$, so $\xi(E_1) = E_2$ and $\xi$ is an isomorphism.

Thus $E_1 \cong E_2$.

For the second statement, let $I$ be any injective module containing $A$. By Theorem 9.2, the maximal essential extension $E$ of $A$ contained in $I$ exists and is injective. By the first part applied with $I_1 = I_2 = I$, we have $E \cong E_1$. $\square$
