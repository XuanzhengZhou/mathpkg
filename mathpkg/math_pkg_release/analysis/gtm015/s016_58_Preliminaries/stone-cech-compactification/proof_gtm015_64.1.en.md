---
role: proof
locale: en
of_concept: stone-cech-compactification
source_book: gtm015
source_chapter: "64"
source_section: "Stone-Čech compactification"
---

# Proof of Stone-Čech compactification

Proof. Let $\mathcal{C}^\infty(T)$ be the algebra of all bounded continuous functions $x: T \to \mathbb{C}$, a commutative $C^*$-algebra with unity under the sup norm $\|x\|_\infty = \sup \{|x(t)| : t \in T\}$. Take $\mathcal{X}$ to be the character space of $\mathcal{C}^\infty(T)$ (52.8), i.e., the set of all algebra epimorphisms $f: \mathcal{C}^\infty(T) \to \mathbb{C}$ with the relative weak$^*$ topology as a subset of the dual space of $\mathcal{C}^\infty(T)$. Define $\varphi: T \to \mathcal{X}$ by $\varphi(t) = f_t$ where $f_t(x) = x(t)$ for all $x \in \mathcal{C}^\infty(T)$. Then:
(1) $\varphi$ is injective (64.2);
(2) $\overline{\varphi(T)} = \mathcal{X}$, so $\mathcal{X}$ is compact and $\varphi(T)$ is dense (64.4);
(3) Every bounded continuous real-valued function on $T$ extends uniquely to a continuous real-valued function on $\mathcal{X}$ (64.5).
The pair $(\mathcal{X}, \varphi)$ is called a Stone-\v{C}ech compactification of $T$.
