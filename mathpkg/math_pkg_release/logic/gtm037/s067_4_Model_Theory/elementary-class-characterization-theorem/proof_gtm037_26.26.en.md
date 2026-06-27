---
role: proof
locale: en
of_concept: elementary-class-characterization-theorem
source_book: gtm037
source_chapter: "26"
source_section: "26"
---

$(i) \Rightarrow (ii) \Rightarrow (iii) \Rightarrow (iv)$ are straightforward.

Now suppose $K$ is elementarily closed and compact. We show $K = \operatorname{Mod} \Theta_{\rho}K$. Obviously $K \subseteq \operatorname{Mod} \Theta_{\rho}K$. Take $\mathfrak{A} \in \operatorname{Mod} \Theta_{\rho}K$. We need $\mathfrak{A} \in K$.

Claim: $\operatorname{Mod} \Theta_{\rho}\{\mathfrak{A}\} \cap K \neq 0$. If not, by compactness of $K$, there is a finite $\Delta \subseteq \Theta_{\rho}\{\mathfrak{A}\}$ with no model in $K$. Then $\neg \bigwedge \Delta \in \Theta_{\rho}K$, so $\mathfrak{A} \models \neg \bigwedge \Delta$, contradiction.

Thus $\mathfrak{A} \equiv_{\text{ee}} \mathfrak{B} \in K$ for some $\mathfrak{B}$. Since $K$ is elementarily closed, $\mathfrak{A} \in K$.
