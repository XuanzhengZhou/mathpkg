---
role: proof
locale: en
of_concept: elementary-class-equivalence
source_book: gtm037
source_chapter: "26"
source_section: "Elementary Classes and Elementary Equivalence"
---

Obviously $(i) \Rightarrow (ii) \Rightarrow (iii) \Rightarrow (iv)$. Now suppose that $K$ is elementarily closed and compact. We show that $K = \text{Mod } \Theta_{\rho} K$, so that $(i)$ holds. Obviously $K \subseteq \text{Mod } \Theta_{\rho} K$, so we need to take any $A \in \text{Mod } \Theta_{\rho} K$ and show that $A \in K$. Now

(1) $\text{Mod } \Theta_{\rho} \{A\} \cap K \neq 0$.

For, otherwise $K$ compact implies that there is a finite $\Delta \subseteq \Theta_{\rho} \{A\}$ such that $\Delta$ does not have a model in $K$. Thus $\neg \bigwedge \Delta \in K$, so $\neg \bigwedge \Delta \in \Theta_{\rho} K$ and $A \models \neg \bigwedge \Delta$, which is impossible.

So (1) holds. Hence $A \equiv_{\text{ee}} B \in K$ for some $B$, so $A \in K$ since $K$ is elementarily closed.
