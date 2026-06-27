---
role: proof
locale: en
of_concept: kan-extension-left-adjoint
source_book: gtm004
source_chapter: "IX"
source_section: "5. Kan Extensions"
---

# Proof of Existence of Left Adjoint to Precomposition Functor (Kan Extension)

**Theorem 5.1.** If $\mathfrak{A}$ admits colimits, then $J^*: [\mathfrak{B}, \mathfrak{A}] \rightarrow [\mathfrak{U}, \mathfrak{A}]$ has a left adjoint.

**Proof.** For any object $V$ in $\mathfrak{B}$, form the category $\mathfrak{J}_V$ of $J$-objects over $V$ as follows. An object of $\mathfrak{J}_V$ is a pair $(U, \psi)$ consisting of an object $U$ of $\mathfrak{U}$ and a morphism $\psi: JU \rightarrow V$. A morphism $\varphi: (U, \psi) \rightarrow (U', \psi')$ is a morphism $\varphi: U \rightarrow U'$ in $\mathfrak{U}$ such that the diagram

$$\begin{CD}
JU @>{J\varphi}>> JU' \\
@V{\psi}VV @VV{\psi'}V \\
V @= V
\end{CD}$$

commutes. With the evident law of composition, $\mathfrak{J}_V$ is a category. Given a functor $T: \mathfrak{U} \rightarrow \mathfrak{A}$, we define a functor $T_V: \mathfrak{J}_V \rightarrow \mathfrak{A}$ by the rule

$$T_V(U, \psi) = T(U), \quad T_V(\varphi) = T(\varphi).$$

We now set

$$\widetilde{J}T(V) = \varinjlim_{\mathfrak{J}_V} T_V.$$

This makes sense since $\mathfrak{A}$ admits colimits. Notice that $\widetilde{J}T(V)$ is a certain object of $\mathfrak{A}$, furnished with morphisms

$$\varrho_V(U, \psi): T(U) \rightarrow \widetilde{J}T(V)$$

for each $(U, \psi) \in \mathfrak{J}_V$, satisfying the usual compatibility relations for a colimit.

If $\lambda: T \rightarrow S$ is a natural transformation of functors $\mathfrak{U} \rightarrow \mathfrak{A}$, we determine a natural transformation $\widetilde{\lambda}: \widetilde{J}T \rightarrow \widetilde{J}S$ by the rule

$$\widetilde{\lambda}(V) \circ \varrho_V(U, \psi) = \sigma_V(U, \psi) \circ \lambda(U),$$

where $\sigma_V(U, \psi): S(U) \rightarrow \widetilde{J}S(V)$ are the structural morphisms for the colimit defining $\widetilde{J}S(V)$. Plainly, $\widetilde{\lambda}$ is a natural transformation; plainly, too, if we set $\widetilde{J}(\lambda) = \widetilde{\lambda}$, then $\widetilde{J}$ is a functor $[\mathfrak{U}, \mathfrak{A}] \rightarrow [\mathfrak{B}, \mathfrak{A}]$.

It remains to show that $\widetilde{J}$ is left adjoint to $J^*$. We define natural bijections

$$\operatorname{Nat}(\widetilde{J}T, S) \cong \operatorname{Nat}(T, SJ).$$

Given functors $T: \mathfrak{U} \rightarrow \mathfrak{A}$, $S: \mathfrak{B} \rightarrow \mathfrak{A}$ and a natural transformation $\tau: \widetilde{J}T \rightarrow S$, we define a natural transformation $\tau' = \eta(\tau): T \rightarrow SJ$ by

$$\tau'(U) = \tau(JU) \circ \varrho_{JU}(U, 1_{JU}), \quad U \in \mathfrak{U},$$

which is the composite

$$TU \xrightarrow{\varrho_{JU}(U, 1_{JU})} \widetilde{J}T(JU) \xrightarrow{\tau(JU)} SJU.$$

Conversely, given a natural transformation $\sigma: T \rightarrow SJ$, we define a natural transformation $\bar{\sigma} = \bar{\eta}(\sigma): \widetilde{J}T \rightarrow S$ by

$$\bar{\sigma}(V) \circ \varrho_V(U, \psi) = S\psi \circ \sigma(U),$$

for all $V \in \mathfrak{B}$, $U \in \mathfrak{U}$, $\psi: JU \rightarrow V$ in $\mathfrak{B}$.

One readily verifies that $\eta$ and $\bar{\eta}$ are mutually inverse, establishing the adjunction

$$\widetilde{J} \dashv J^*: [\mathfrak{B}, \mathfrak{A}] \rightarrow [\mathfrak{U}, \mathfrak{A}].$$

Thus $\widetilde{J}$ is a left adjoint to $J^*$, and we call $\widetilde{J}T$ the **left Kan extension** of $T$ along $J$. $\square$
