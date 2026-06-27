---
role: proof
locale: en
of_concept: skew-symmetrization
source_book: gtm023
source_chapter: "IV"
source_section: "§1. Determinant functions"
---

Define $\Psi = \sum_{\sigma \in S_p} \varepsilon_\sigma \cdot \sigma \Phi$. Since each $\sigma\Phi$ is $p$-linear and a linear combination of $p$-linear maps is $p$-linear, $\Psi$ is $p$-linear. To check skew symmetry, let $\tau \in S_p$. Then
\begin{align*}
\tau \Psi &= \sum_{\sigma} \varepsilon_\sigma \cdot \tau(\sigma \Phi) \\
&= \sum_{\sigma} \varepsilon_\sigma \cdot (\tau \sigma) \Phi \\
&= \varepsilon_\tau \sum_{\sigma} \varepsilon_\tau \varepsilon_\sigma \cdot (\tau\sigma)\Phi \\
&= \varepsilon_\tau \sum_{\sigma} \varepsilon_{\tau\sigma} \cdot (\tau\sigma)\Phi.
\end{align*}
As $\sigma$ runs over $S_p$, $\tau\sigma$ also runs over $S_p$. Hence the last sum equals $\sum_{\rho} \varepsilon_\rho \cdot \rho\Phi = \Psi$, where $\rho = \tau\sigma$. Therefore $\tau\Psi = \varepsilon_\tau \Psi$, so $\Psi$ is skew symmetric.
