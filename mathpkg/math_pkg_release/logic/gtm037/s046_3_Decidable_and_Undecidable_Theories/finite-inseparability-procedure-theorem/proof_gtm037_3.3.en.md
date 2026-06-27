---
role: proof
locale: en
of_concept: finite-inseparability-procedure-theorem
source_book: gtm037
source_chapter: "3"
source_section: "3"
---

Let $f$ be a recursive function satisfying Definition 6.21 for the effectively inseparable pair $g^{+*} \text{Thm}_{\mathcal{L}}$ and $M = g^{+*} \{ \varphi : \varphi \text{ is a sentence whose negation holds in some finite model of } \Gamma \}$. Given any consistent finitely axiomatizable theory $\Delta$ such that every finite model of $\Gamma$ is a model of $\Delta$, we have $g^{+*} \Delta \supseteq g^{+*} \text{Thm}_{\mathcal{L}}$ and by Proposition (*), the set $M$ is r.e. Since $g^{+*} \text{Thm}_{\mathcal{L}}$ and $M$ are effectively inseparable via $f$, the procedure $P$ works as follows: enumerate $g^{+*} \Delta$ (which is r.e. since $\Delta$ is finitely axiomatizable) and $M$ simultaneously. By effective inseparability, $f$ will eventually produce an index $n$ such that $n \in M$ but $n \notin g^{+*} \Delta$. Translating back, this gives a sentence $\varphi$ with $g^{+}\varphi = n$ such that $\neg \varphi$ holds in all finite models of $\Gamma$ (hence in all finite models of $\Delta$) but $\varphi \notin \Delta$. Thus $\varphi$ is the desired independent sentence.
