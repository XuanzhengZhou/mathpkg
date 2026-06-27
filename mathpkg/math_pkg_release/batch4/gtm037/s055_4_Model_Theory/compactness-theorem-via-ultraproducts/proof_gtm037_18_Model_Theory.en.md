---
role: proof
locale: en
of_concept: compactness-theorem-via-ultraproducts
source_book: gtm037
source_chapter: "18"
source_section: "Model Theory"
---

Assume that each finite subset $\Delta$ of $\Gamma$ has a model $\mathfrak{A}_{\Delta}$. Let $I = \{\Delta : \Delta \text{ is a finite subset of } \Gamma\}$. For each $\Delta \in I$ let $G_{\Delta} = \{\Theta : \Delta \subseteq \Theta \in I\}$. If $\Delta_0, \ldots, \Delta_{m-1} \in I$, then

$$G_{\Delta_0} \cap \cdots \cap G_{\Delta_{m-1}} = G_{\Delta_0 \cup \cdots \cup \Delta_{m-1}} \neq \varnothing.$$

Thus $\{G_{\Delta} : \Delta \in I\}$ has the finite intersection property, so by Proposition 18.18 let $F$ be an ultrafilter over $I$ such that $G_{\Delta} \in F$ for each $\Delta \in I$.

Then $P_{\Delta \in I} \mathfrak{A}_{\Delta} / F$ is a model of $\Gamma$. In fact, let $\varphi \in \Gamma$. Then $G_{\{\varphi\}} \subseteq \{\Delta \in I : \varphi \text{ holds in } \mathfrak{A}_{\Delta}\}$, and $G_{\{\varphi\}} \in F$, so $\{\Delta \in I : \varphi \text{ holds in } \mathfrak{A}_{\Delta}\} \in F$. Hence by Corollary 18.30 (Łoś's Theorem), $\varphi$ holds in $P_{\Delta \in I} \mathfrak{A}_{\Delta} / F$, as desired.
