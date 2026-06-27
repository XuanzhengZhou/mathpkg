---
role: proof
locale: en
of_concept: bounded-iff-continuous
source_book: gtm023
source_chapter: "VII"
source_section: "5 (7.21)"
---

If $\varphi$ is bounded, then $\|\varphi x - \varphi y\| = \|\varphi(x-y)\| \leq M\|x-y\|$, so $\varphi$ is Lipschitz continuous, hence continuous. Conversely, if $\varphi$ is continuous at $0$, there exists $\delta > 0$ such that $\|x\| \leq \delta$ implies $\|\varphi x\| \leq 1$. Then for any $x \neq 0$, setting $y = \delta x/\|x\|$ gives $\|y\| = \delta$, so $\|\varphi y\| \leq 1$. By linearity, $\|\varphi x\| = (\|x\|/\delta)\|\varphi y\| \leq (1/\delta)\|x\|$, showing $\varphi$ is bounded with $M = 1/\delta$.
