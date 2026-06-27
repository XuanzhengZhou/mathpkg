---
role: proof
locale: en
of_concept: spectral-sequence-of-double-complex
source_book: gtm004
source_chapter: "VIII"
source_section: "9"
---

# Proof of Spectral Sequences of a Double Complex

We prove (9.7) only, and so permit ourselves to write $F^p$ for $_2 F^p$.

Clearly, $F^p(\operatorname{Tot} B)_q / F^{p-1}(\operatorname{Tot} B)_q = B_{q-p, p}$. Moreover the differential $\partial = \partial' + \partial''$ on $\operatorname{Tot} B$ induces on this quotient the horizontal differential $\partial'$. This establishes the first assertion of (9.7).

Now $d_0$ in the spectral sequence is the composite

$$H_q(F^p / F^{p-1}) \xrightarrow{\gamma} H_{q-1}(F^{p-1}) \xrightarrow{\beta} H_{q-1}(F^{p-1} / F^{p-2}).$$

We choose a representative of $x \in H_q(F^p / F^{p-1})$ to be an element $b \in B_{q-p, p}$ such that $\partial' b = 0$. Then $\gamma x$ is the homology class of $\partial'' b$, and $\beta \gamma x$ is therefore just $\partial''_* x$, where $\partial''_*$ is induced on $H(B, \partial')$ by $\partial''$.

The computation for (9.6) is entirely analogous, interchanging the roles of the two filtrations (9.4) and (9.5) and therefore the roles of the horizontal and vertical differentials. $\square$
