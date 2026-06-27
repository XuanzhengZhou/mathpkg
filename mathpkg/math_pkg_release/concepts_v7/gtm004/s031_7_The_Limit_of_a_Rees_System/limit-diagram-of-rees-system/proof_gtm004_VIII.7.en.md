---
role: proof
locale: en
of_concept: limit-diagram-of-rees-system
source_book: gtm004
source_chapter: "VIII"
source_section: "7"
---

# Proof of Limit Diagram of a Rees System

Recall that the Rees system (6.9) produces the diagram (7.1), together with the exact sequences (7.2) and the commutativities (7.3). The morphisms $\beta_\infty, \gamma_\infty, \bar{\beta}_\infty, \bar{\gamma}_\infty$ were defined in Section 5, while $\xi_I, \xi_U$ arise from applying limit and colimit functors to the morphism $\xi: \bar{D} \to D$. The morphism $\varphi_U$ is obtained via the universal property of the colimit from the morphisms $\varphi_n: D_n \to \Gamma$ of the successive derived Rees systems, and similarly for $\bar{\varphi}_I$.

The exact sequence (5.18) yields exact sequences involving $\beta_*, \gamma_*$ and $\bar{\beta}_*, \bar{\gamma}_*$ respectively (applied to the objects $U$ and $\bar{U}$). Specifically, from the exact couple machinery we obtain:

$$\text{coker}\,\alpha' \xrightarrow{\beta_*} E_\infty \xrightarrow{\gamma_*} \ker \alpha'',$$

$$\text{coker}\,\bar{\alpha}' \xrightarrow{\bar{\beta}_*} E_\infty \xrightarrow{\bar{\gamma}_*} \ker \bar{\alpha}''.$$

Consider the diagram

$$
\begin{array}{ccc}
\bar{U} & \xrightarrow{\xi_U} & U & \xrightarrow{\varphi_U} & \Gamma \\
{\scriptstyle \bar{\alpha}'}\downarrow & & {\scriptstyle \alpha'}\downarrow & & {\scriptstyle \theta}\downarrow \\
\bar{U} & \xrightarrow{\xi_U} & U & \xrightarrow{\varphi_U} & \Gamma
\end{array}
$$

with exact columns (each column is an exact sequence $\bar{U} \to U \to \Gamma$ from the construction of the derived Rees system). Passing to cokernels horizontally yields the exact sequence

$$\text{coker}\,\bar{\alpha}' \xrightarrow{\xi'} \text{coker}\,\alpha' \xrightarrow{\varphi^+} \Gamma^+.$$

By duality we obtain the exact sequence

$$\Gamma^- \xrightarrow{\bar{\varphi}^-} \ker \bar{\alpha}'' \xrightarrow{\epsilon''} \ker \alpha''.$$

Finally, we set $\bar{\varphi}^+ = \bar{\varphi}^- \theta^{-1}$ by Proposition 6.7 and establish the commutativity of the upper right hand square by appeal to (7.4), namely $\bar{\varphi}_I \theta^{-1} \varphi_U = \bar{\gamma}_\infty \beta_\infty$, which implies that the square

$$
\begin{array}{ccc}
\text{coker}\,\alpha' & \xrightarrow{\varphi^+} & \Gamma^+ \\
{\scriptstyle \beta_*}\downarrow & & {\scriptstyle \bar{\varphi}^+}\downarrow \\
E_\infty & \xrightarrow{\bar{\gamma}_*} & \ker \bar{\alpha}''
\end{array}
$$

commutes. The exactness of the rows and columns of the limit diagram now follows by assembling these exact sequences together with the natural morphisms $\xi'$ and the identities on $\ker \alpha''$. $\square$
