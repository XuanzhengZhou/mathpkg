---
role: proof
locale: en
of_concept: bicartesian-square-of-spectral-terms
source_book: gtm004
source_chapter: "VIII. Exact Couples and Spectral Sequences"
source_section: "4. The Ladder of an Exact Couple"
---

# Proof of Bicartesian square of spectral sequence terms

**Theorem 4.6.** The square

$$\begin{CD}
E_{m,n+1} @>{\sigma_{m,n+1}}>> E_{m+1,n+1} \\
@V{\varrho_{m,n}}VV @VV{\varrho_{m+1,n}}V \\
E_{m,n} @>{\sigma_{m,n}}>> E_{m+1,n}
\end{CD}$$

is bicartesian (i.e., a pull-back and push-out).

**Proof.** Recall from (4.17) the ladder sequence

$$\cdots \to D_m \xrightarrow{\beta_{m,n}} E_{m,n} \xrightarrow{\gamma_{m,n}} D_n \xrightarrow{\alpha_n} D_n \to \cdots.$$

We may apply the $Q^{\alpha_n}$-process and the $Q_{\sigma_m}$-process to the rows of this ladder. The square relating $E_{m,n}$, $E_{m+1,n}$, $E_{m,n+1}$, and $E_{m+1,n+1}$ is then obtained by applying Proposition 4.2 to the intermediate objects in the ladder construction. Indeed, the vertical morphisms $\varrho_{m,n}$ and $\sigma_{m,n}$ arise from the pull-back and push-out processes, respectively, and Proposition 4.2 states precisely that the square formed by these constructions is bicartesian. $\square$
