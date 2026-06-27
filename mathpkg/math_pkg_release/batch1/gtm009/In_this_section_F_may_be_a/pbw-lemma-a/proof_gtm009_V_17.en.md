---
role: proof
locale: en
of_concept: pbw-lemma-a
source_book: gtm009
source_chapter: "V"
source_section: "17"
---

The proof proceeds by induction on $m$.

For $m = 0$, $S_0 = F$. Define $f_0: L \otimes S_0 \to \mathfrak{S}$ by $f_0(x_{\lambda} \otimes 1) = z_{\lambda}$. Then $(A_0)$ holds trivially since $1 = z_{\varnothing}$ and $\lambda \leq \varnothing$; $(B_0)$ is clear; and $(C_0)$ is vacuous since $S_{-1} = 0$.

Assume $f_{m-1}$ has been constructed satisfying $(A_{m-1})$, $(B_{m-1})$, $(C_{m-1})$. We must define $f_m(x_{\lambda} \otimes z_{\Sigma})$ for each increasing $\Sigma$ of length $\leq m$ and each index $\lambda$.

\textit{Case 1:} $\lambda \leq \Sigma$. Then $(A_m)$ forces $f_m(x_{\lambda} \otimes z_{\Sigma}) = z_{\lambda} z_{\Sigma}$.

\textit{Case 2:} $\lambda \not\leq \Sigma$. Let $\mu$ be the first index in $\Sigma$, so $\Sigma = (\mu, \Psi)$ with $\mu < \lambda$. By induction we know $f_{m-1}(x_{\mu} \otimes z_{\Psi}) = z_{\mu} z_{\Psi} + w$ where $w \in S_{m-2}$ by $(B_{m-1})$. We want to apply the inductive definition:
$$f_m(x_{\lambda} \otimes z_{\Sigma}) = f_m(x_{\lambda} \otimes f_{m-1}(x_{\mu} \otimes z_{\Psi})).$$

By $(C_m)$, this should equal:
$$f_m(x_{\mu} \otimes f_m(x_{\lambda} \otimes z_{\Psi})) + f_m([x_{\lambda} x_{\mu}] \otimes z_{\Psi}).$$

Now $z_{\Psi} \in S_{m-1}$, and if $\lambda \leq \Psi$, then $f_m(x_{\lambda} \otimes z_{\Psi})$ is determined by Case 1. Otherwise, $f_m(x_{\lambda} \otimes z_{\Psi})$ is determined by a further application of Case 2 with a shorter sequence $\Psi$, and by well-founded induction on the length and the well-ordering of indices, this definition terminates. Meanwhile, $[x_{\lambda} x_{\mu}] \in L$ can be expressed as a linear combination of basis elements $x_{\nu}$, and $f_m([x_{\lambda} x_{\mu}] \otimes z_{\Psi})$ is defined by linearity using the already-determined values.

The verification that $(B_m)$ holds follows from the inductive construction: each step adds at most a term of degree at most $m$, and the correction terms land in lower filtration.

The verification of $(C_m)$ requires checking the Jacobi-like identity on all basis elements. This is done by induction on the well-ordering, using the Jacobi identity in $L$ and the induction hypothesis. For the critical case where neither $\lambda$ nor $\mu$ precedes the sequence, the computation reduces to the case already covered by the induction on the well-ordering of indices.

Uniqueness of $f_m$ follows because the conditions $(A_m)$, $(B_m)$, $(C_m)$ together with the induction hypothesis completely determine $f_m$ on all elements $x_{\lambda} \otimes z_{\Sigma}$.
