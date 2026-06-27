---
role: proof
locale: en
of_concept: elementary-projective-ultraproduct-compact-hierarchy
source_book: gtm037
source_chapter: "26"
source_section: "26.2"
---
Obviously $(i) \Rightarrow (ii) \Rightarrow (iii) \Rightarrow (iv)$. Now suppose that $K$ is elementarily closed and compact. We show that $K = \operatorname{Mod} \Theta_{\rho} K$, so that $(i)$ holds.

Obviously $K \subseteq \operatorname{Mod} \Theta_{\rho} K$, so we need to take any $\mathfrak{A} \in \operatorname{Mod} \Theta_{\rho} K$ and show that $\mathfrak{A} \in K$. Now

$$(1) \quad \operatorname{Mod} \Theta_{\rho} \{\mathfrak{A}\} \cap K \neq \varnothing.$$

For, otherwise $K$ compact implies that there is a finite $\Delta \subseteq \Theta_{\rho} \{\mathfrak{A}\}$ such that $\Delta$ does not have a model in $K$. Thus $\neg \bigwedge \Delta \in K$, so $\neg \bigwedge \Delta \in \Theta_{\rho} K$ and $\mathfrak{A} \models \neg \bigwedge \Delta$, which is impossible.

So (1) holds. Hence $\mathfrak{A} \equiv_{\text{ee}} \mathfrak{B} \in K$ for some $\mathfrak{B}$, so $\mathfrak{A} \in K$ since $K$ is elementarily closed.
