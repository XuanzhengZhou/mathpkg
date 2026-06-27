---
role: proof
locale: en
of_concept: los-universal-class-characterization
source_book: gtm037
source_chapter: "25"
source_section: "25"
---

($\Rightarrow$) If $K = \operatorname{Mod} \Gamma$ with $\Gamma$ universal, then closure under $\mathbf{S}$ and $\mathbf{Up}$ follows from the fact that universal sentences are preserved under substructures and ultraproducts.

($\Leftarrow$) Assume $\mathbf{S}K = K$ and $\mathbf{Up}K = K$. Let $\Gamma = \{\varphi : \varphi \text{ is a universal sentence which holds in each } \mathfrak{A} \in K\}$. Clearly $K \subseteq \operatorname{Mod} \Gamma$. It suffices to show $\operatorname{Mod} \Gamma \subseteq \mathbf{SUp}K \subseteq K$.

Take $\mathfrak{A} \in \operatorname{Mod} \Gamma$. Let $<$ be a well-ordering of $A$ and let $\mathcal{L}'$ be the $A$-expansion with constants $\mathbf{c}_a$ for $a \in A$. Let $\Delta$ be the $\mathcal{L}'$-diagram of $\mathfrak{A}$. Form an ultraproduct over $I = \{\Theta : \Theta \text{ finite } \subseteq \Delta\}$. For each $\Theta \in I$, let $\psi_\Theta$ be the conjunction and $\varphi_\Theta = \forall \bar{v} \neg \psi_\Theta$. Since $\mathfrak{A} \models \neg \varphi_\Theta$, $\varphi_\Theta \notin \Gamma$. Choose $\mathfrak{B}_\Theta \in K$ with $\mathfrak{B}_\Theta \models \neg \varphi_\Theta$.

Let $M_\Theta = \{\Omega \in I : \Theta \subseteq \Omega\}$. The family $\{M_\Theta : \Theta \in I\}$ has the finite intersection property. Let $F$ be an ultrafilter over $I$ containing all $M_\Theta$. The ultraproduct $\prod_{\Theta \in I} \mathfrak{B}_\Theta / F$ then yields a structure into which $\mathfrak{A}$ embeds elementarily, so $\mathfrak{A} \in \mathbf{SUp}K$.
