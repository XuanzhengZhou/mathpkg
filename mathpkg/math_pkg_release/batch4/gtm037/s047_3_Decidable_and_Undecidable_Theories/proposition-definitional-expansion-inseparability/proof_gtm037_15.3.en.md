---
role: proof
locale: en
of_concept: proposition-definitional-expansion-inseparability
source_book: gtm037
source_chapter: "15"
source_section: "3"
---

(ii) Suppose $\Gamma'$ is inseparable. Let $B = g^{+*} \{ \varphi : \varphi \in \operatorname{Sent}_{\mathcal{L}'}, \neg \varphi \in \Gamma' \}$ and $D = g^{+*} \{ \varphi : \varphi \in \operatorname{Sent}_{\mathcal{L}}, \neg \varphi \in \Gamma \}$. Thus $g^{+*} \Gamma'$ and $B$ are effectively inseparable sets. By 11.30 and 11.31, for any sentence $\varphi$ of $\mathcal{L}'$, $\varphi \in \Gamma'$ iff $\varphi' \in \Gamma$, and $g^{+}\varphi \in B$ iff $g^{+}\varphi' \in D$. Hence from 6.25 it follows that $g^{+*} \Gamma$ and $D$ are effectively inseparable, so $\Gamma$ is inseparable. The converse follows similarly using the function $f$ defined by: for any $x \in \omega$,
$$f x = 0 \quad \text{if } x \notin g^{+*} \operatorname{Sent}_{\mathcal{L}},$$
$$f x = g^{+} (g^{+ -1} x)^{2\lambda} \quad \text{if } x \in g^{+*} \operatorname{Sent}_{\mathcal{L}}.$$
This function $f$ is recursive by 11.44, and satisfies $g^{+*}\Gamma \subseteq f^{-1 *} g^{+*}\Gamma'$ and the corresponding inclusion for the negated sentences, so effective inseparability is preserved by 6.25.

(iii) The implication from left to right is immediate from the definitions. For the converse (under the stated hypothesis), one constructs from a definitional expansion a recursive translation that maps sentences of $\mathcal{L}'$ to sentences of $\mathcal{L}$, preserving theoremhood.

(iv) Suppose $\Gamma$ is finitely inseparable; thus $g^{+*} \operatorname{Thm}_{\mathcal{L}}$ and $B = \{ \varphi : \varphi \in \operatorname{Sent}_{\mathcal{L}}, \neg \varphi \text{ holds in some finite model of } \Gamma \}$ are effectively inseparable. As in the proof of 11.31, any model of $\Gamma$ can be expanded to a model of $\Gamma'$. Hence $g^{+*} \operatorname{Thm}_{\mathcal{L}} \subseteq g^{+*} \operatorname{Thm}_{\mathcal{L}'}$, and $B \subseteq \{ \varphi : \varphi \in \operatorname{Sent}_{\mathcal{L}'} : \neg \varphi \text{ holds in some finite model of } \Gamma' \}$; it follows that $\Gamma'$ is finitely inseparable.

Conversely, assume that $\Gamma'$ is finitely inseparable. For each sentence $\varphi$ of $\mathcal{L}'$, let $\Delta_{\varphi}$ be the set of all existence and uniqueness conditions. The recursive translation $\varphi \mapsto \varphi^{2\lambda}$ then transfers the finite inseparability from $\Gamma'$ back to $\Gamma$.
