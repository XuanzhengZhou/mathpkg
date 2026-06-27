---
role: proof
locale: en
of_concept: exactness-preservation-in-ladder
source_book: gtm004
source_chapter: "VIII. Exact Couples and Spectral Sequences"
source_section: "4. The Ladder of an Exact Couple"
---

# Proof of Exactness preservation in the ladder construction

**Theorem 4.4.** If the bottom row of (4.4) is exact, so are all rows of (4.4) and (4.7).

Recall that (4.4) is the diagram

$$\begin{CD}
A_1 \\
@V{\sigma}VV \\
A @>{\beta_{0,1}}>> B_{0,1} @>{\gamma_{0,1}}>> C_1 \\
@| @VV{\varrho_{0,1}}V @| \\
A @>{\beta}>> B @>{\gamma}>> C
\end{CD}$$

**Proof.** That the middle row of (4.4) is exact is plain, since

$$\gamma^{-1}(0) \subseteq \gamma^{-1}(C_1)$$

and the morphism $\gamma_{0,1}$ is just the restriction of $\gamma$ to $\gamma^{-1}(C_1)$. Thus the kernel of $\gamma_{0,1}$ equals the kernel of $\gamma$, which, by exactness of the bottom row, equals the image of $\beta$. But $\beta$ factors through $B_{0,1}$ by construction, so exactness at $B_{0,1}$ follows.

The rest of the statement of the theorem follows by duality. $\square$
