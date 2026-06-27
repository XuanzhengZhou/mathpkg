---
role: proof
locale: en
of_concept: los-universal-class-theorem
source_book: gtm037
source_chapter: "25"
source_section: "Preservation and Characterization Theorems"
---

The direction $\Rightarrow$ is trivial (universal sentences are preserved under substructures and ultraproducts). For the converse, assume $\mathbf{S}K = K$ and $\mathbf{Up}K = K$. Let $\Gamma$ be the set of all universal sentences true in every member of $K$. Clearly $K \subseteq \text{Mod } \Gamma$. Take any $\mathfrak{A} \in \text{Mod } \Gamma$; we show $\mathfrak{A} \in K$. It suffices to show $\mathfrak{A} \in \mathbf{SUp}K$.

Let $<$ be a well-ordering of $A$. Let $\mathcal{L}'$ be an $A$-expansion of $\mathcal{L}$ and $\Delta$ be the $\mathcal{L}'$-diagram of $\mathfrak{A}$. Form an ultraproduct over $I = \{\Theta : \Theta \text{ is a finite subset of } \Delta\}$. For each $\Theta \in I$, let $\psi_\Theta$ be the conjunction of $\Theta$ with constants replaced by variables, and let $\varphi_\Theta = \forall v_0 \cdots \forall v_{m_\Theta-1} \neg \psi_\Theta$. Since $\mathfrak{A} \models \neg \varphi_\Theta$ and $\varphi_\Theta$ is universal, $\varphi_\Theta \notin \Gamma$, so there exists $\mathfrak{B}_\Theta \in K$ with $\mathfrak{B}_\Theta \models \neg \varphi_\Theta$. The ultraproduct of the $\mathfrak{B}_\Theta$'s yields a structure in $\mathbf{Up}K$ into which $\mathfrak{A}$ embeds. Hence $\mathfrak{A} \in \mathbf{SUp}K \subseteq K$.
