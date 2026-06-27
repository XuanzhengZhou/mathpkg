---
role: proof
locale: en
of_concept: semantic-comparison-functor
source_book: gtm026
source_chapter: "3"
source_section: "3. Nondeterminism"
---

Since $T$ is an algebraic theory in $\mathcal{K}$, the proof that $\hat{T}$ is an algebraic theory in $\mathrm{Dyn}(X)$ requires only that we check that $\hat{T}$ is functorial and that $\hat{e}$ and $\hat{m}$ are dynamorphisms. This is clear from the three diagrams, in which all three axioms for a distributive law have been used. It is clear that a $\hat{T}$-algebra is the same thing as $(Q, \delta, \xi)$ where $(Q, \delta)$ is an $X$-dynamics, $(Q, \xi)$ is a $\mathbf{T}$-algebra, and $\xi: (Q, \delta) \hat{T} \rightarrow (Q, \delta)$ is a dynamorphism; but this last condition is just the $\lambda$-law 3.12. This completes the proof of (1).

The formulas for $\mathbf{T}^{\star}$ are direct consequences of 2.2.30 and 2.2.20. Thus $m^{\star} = F_2 F_1 \varepsilon^{\star} U_1 U_2$ where

$$(Q, \delta, \xi) \varepsilon^{\star} = QF_2 F_1 \xrightarrow{U_1 \varepsilon_2 F_1} (Q, \delta) F_1 \xrightarrow{\varepsilon_1} (Q, \delta, \xi)$$

$$= (QX^{\star} T, QX^{\star} \lambda Q \mu_0 T, QX^{\star} e) \xrightarrow{\delta^{\star} T} (QT, Q \lambda \delta T, Qe) \xrightarrow{\xi} (Q, \delta, \xi).$$

Similarly, the formula for the semantics comparison functor follows from 2.2.20. To complete the proof of the theorem we must show that $\Phi^{-1}$ is well defined and inverse to $\Phi$. To begin, the diagrams prove that $\eta T: \mathbf{T} \longrightarrow \mathbf{T}^{\star}$ is a theory map so that, by 3.2.9, $(Q, \psi) \Phi^{-1}$ is at least an $X$-dynamics and a $\mathbf{T}$-algebra. Now consider the diagram:

As a first use of diagram 3.16, we have

$$QX^{\star}T \lambda \cdot (QX^{\star}\lambda \cdot Q\mu_{0}T)T \cdot QX^{\star}m = QX^{\star}mX \cdot (QX^{\star}\lambda \cdot Q\mu_{0}T)$$

which establishes the $\lambda$-law at least for $(QX^{\star}T, Qm^{\star})\Phi^{-1}$. Now, one expects the full subcategory of $(Q, \delta, \xi)$'s satisfying the $\lambda$-law to be closed under products, subobjects, and epimorphisms split at the level of $\mathcal{K}$ because the $\lambda$-law is "an equation." That this is so follows from diagram 3.17. (The only case important to this proof is that in which $(Q, \delta, \xi)$ satisfies the $\lambda$-law and the $X$-dynamorphism and $\mathbf{T}$-homomorphism $f$ is split epi in $\mathcal{H}$; since $fTX$ is epi, we deduce that $(Q', \delta', \xi')$ satisfies the $\lambda$-law as well.) But $\Phi^{-1}$ is functorial, as is clear from the diagrams.

Since $\psi: (QX^{\star}T, Qm^{\star})\Phi^{-1} \rightarrow (Q, \psi)\Phi^{-1}$ is an $X$-dynamorphism $\mathbf{T}$-homomorphism split epi in $\mathcal{H}$, it is now clear that $\Phi^{-1}$ is a well-defined functor. Very similar arguments are used to show that $(Q, \psi)\Phi^{-1}\Phi = (Q, \psi)$. For we read from 3.16 that $(QX^{\star}T, Qm^{\star})\Phi^{-1} = (QX^{\star}T, QX^{\star}\lambda \cdot Q\mu_{0}T, QX^{\star}m)$ so that $(QX^{\star}T, Qm^{\star})\Phi^{-1}\Phi = (QX^{\star}T, Qm^{\star})$; then, because $\psi: (QX^{\star}T, Qm^{\star}) \rightarrow (Q, \psi)\Phi^{-1}\Phi$ is a $\mathbf{T}^{\star}$-homomorphism, it follows immediately from 3.1.9 that $(Q, \psi)\Phi^{-1}\Phi = (Q, \psi)$.

The last detail to check is that if $(Q, \delta, \xi)\Phi = (Q, \psi)$, so that $\psi = \delta^{\star}T \cdot \xi$, then $(Q, \psi) \Phi^{-1} = (Q, \delta, \xi)$. This follows from the diagrams, recalling from 1.4.13 that $\delta T \cdot \xi$ is the unique $\mathbf{T}$-homomorphic extension of $\delta$.
