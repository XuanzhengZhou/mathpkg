---
role: proof
locale: en
of_concept: q-process-transitivity
source_book: gtm004
source_chapter: "VIII. Exact Couples and Spectral Sequences"
source_section: "4. The Ladder of an Exact Couple"
---

# Proof of Transitivity of the Q-pullback process

**Proposition 4.3.** Consider the diagram

$$\begin{CD}
@. C_2 \\
@. @VVV \\
@. C_1 \\
@. @VV{\varrho}V \\
A @>{\beta}>> B @>{\gamma}>> C
\end{CD}$$

where $\gamma\beta$ factors through $\varrho\varrho_1$. Then, if $(\beta', \gamma') = Q^{\varrho}(\beta, \gamma)$, $\gamma'\beta'$ factors through $\varrho_1$ and

$$Q^{\varrho\varrho_1} = Q^{\varrho_1} Q^{\varrho}. \tag{4.10}$$

**Proof.** Let $\gamma\beta = \varrho\varrho_1 \delta$. Then $\varrho \gamma' \beta' = \varrho \varrho_1 \delta$ so that $\gamma' \beta' = \varrho_1 \delta$, since $\varrho$ is monic. Then (4.10) follows by observing that the juxtaposition of the two pull-back processes yields the same result as the single pull-back along $\varrho\varrho_1$. $\square$
