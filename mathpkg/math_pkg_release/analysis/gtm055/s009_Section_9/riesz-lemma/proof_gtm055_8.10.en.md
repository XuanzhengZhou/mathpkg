---
role: proof
locale: en
of_concept: riesz-lemma
source_book: gtm055
source_chapter: "8"
source_section: "9"
---

A point $t \in (a,b)$ belongs to $R_0$ if and only if there exists $u \in (t,b)$ with $f(t) < f(u)$. From this and the continuity of $f$, it follows that $R_0$ is open. Now let $(c, d)$ be a component of $R_0$. The point $d$ does not belong to $R_0$ (otherwise the component would extend further), so for all $u \in (d, b)$, $f(d) \geq f(u)$. In particular, taking $u \to d+$, continuity yields $f(c) \leq f(d)$ since arbitrary points of $(c, d)$ can be approached from within the component.
