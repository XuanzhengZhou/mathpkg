---
role: proof
locale: en
of_concept: proposition-finitely-inseparable-undecidable
source_book: gtm037
source_chapter: "15"
source_section: "3"
---

Suppose that $\Gamma$ is a finitely inseparable theory in $\mathcal{L}$, and let

$$C = \{ g^{+}\varphi : \varphi \text{ is a sentence which holds in every finite model of } \Gamma \}.$$

By 15.7, the sets $g^{+*} \operatorname{Thm}_{\mathcal{L}}$ and $g^{+*} \operatorname{Sent}_{\mathcal{L}} \smallsetminus C$ are effectively inseparable.

Assume for contradiction that $\Gamma$ is decidable. Then $g^{+*} \Gamma$ is a recursive set. Moreover, $g^{+*} \operatorname{Thm}_{\mathcal{L}} \subseteq g^{+*} \Gamma$ (since logical theorems are provable in any theory) and $g^{+*} \Gamma$ is disjoint from $g^{+*} \operatorname{Sent}_{\mathcal{L}} \smallsetminus C$: if $\varphi$ fails in some finite model of $\Gamma$, then $\varphi$ cannot belong to $\Gamma$ (otherwise that model would satisfy $\varphi$).

But a recursive set cannot separate two effectively inseparable r.e. sets, yielding a contradiction. Therefore $\Gamma$ is undecidable.
