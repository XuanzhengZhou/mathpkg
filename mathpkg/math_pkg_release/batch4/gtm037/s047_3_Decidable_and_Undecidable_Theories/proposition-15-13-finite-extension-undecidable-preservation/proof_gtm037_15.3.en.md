---
role: proof
locale: en
of_concept: proposition-15-13-finite-extension-undecidable-preservation
source_book: gtm037
source_chapter: "15"
source_section: "3"
---

Let $\Theta$ be a finite set of sentences such that $\Gamma \cup \Theta$ axiomatizes $\Delta$. Then for any sentence $\varphi$, we have

$$\varphi \in \Delta \quad \text{iff} \quad \bigwedge \Theta \to \varphi \in \Gamma,$$

since $\Gamma \cup \Theta \models \varphi$ if and only if $\Gamma \models \bigwedge \Theta \to \varphi$ by the Deduction Theorem. If $\Gamma$ were decidable, then membership in $\Delta$ would be decidable via this equivalence, contradicting the undecidability of $\Delta$. Hence $\Gamma$ is undecidable.
