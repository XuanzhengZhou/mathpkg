---
role: proof
locale: en
of_concept: ladder-sequence-exactness
source_book: gtm004
source_chapter: "VIII. Exact Couples and Spectral Sequences"
source_section: "4. The Ladder of an Exact Couple"
---

# Proof of Exactness of the ladder sequence

**Theorem 4.5.** The sequence (4.17)

$$\cdots \to D_m \xrightarrow{\beta_{m,n}} E_{m,n} \xrightarrow{\gamma_{m,n}} D_n \xrightarrow{\alpha_n} D_n \to \cdots$$

is exact.

**Proof.** We have already shown exactness at $E_{m,n}$ (Theorem 4.4). To show that $E_{m,n} \xrightarrow{\gamma_{m,n}} D_n \xrightarrow{\alpha_n} D_n$ is exact, first take $m = 0$ and consider

$$E_{0,n} \xrightarrow{\gamma_{0,n}} D_n \xrightarrow{\alpha_n} D_n.$$

Here $E_{0,n}$ is defined by the pull-back

$$\begin{CD}
E_{0,n} @>{\gamma_{0,n}}>> D_n \\
@VVV @VVV \\
E @>{\gamma}>> D
\end{CD}$$

Thus $E_{0,n} = \gamma^{-1}(D_n)$, so that

$$\gamma_{0,n} E_{0,n} = \gamma E \cap D_n = \alpha^{-1}(0) \cap D_n = \alpha_n^{-1}(0),$$

since $\alpha_n$ is the restriction of $\alpha$.

The general case now follows. For the diagram

$$\begin{CD}
D_m @>{\beta_{m,n}}>> E_{m,n} @>{\gamma_{m,n}}>> D_n
\end{CD}$$

(PO = push-out) shows that $\gamma_{m,n}E_{m,n} = \gamma_{0,n}E_{0,n}$; and the remaining exactness assertion of the theorem follows by duality. $\square$

Note that

$$E_{m,n} = \gamma^{-1}(D_n) / \beta \eta_m^{-1}(0) = \gamma^{-1}(\alpha^n D) / \beta \alpha^{-m}(0). \tag{4.18}$$

In particular, $E_{n,n} = E_n$ and (4.17) in the case $m = n$ is just the $n^{\text{th}}$ derived couple.
