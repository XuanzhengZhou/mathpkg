---
role: proof
locale: en
of_concept: basic-ergodic-theorem
source_book: gtm046
source_chapter: "X"
source_section: "32-33"
---

We have to prove that the invariant event $D = [\lim \inf X^n/Y^n \neq \lim \sup X^n/Y^n]$ is null. Since $D = \bigcup_{a,b} C_{ab}$ where $C_{ab} = [\lim \inf X^n/Y^n < a < b < \lim \sup X^n/Y^n]$ with $a < b$ rational, it suffices to prove every $C_{ab}$ is null. Set $Z^n = Y^n$, $C = C_{ab}$, and apply the basic inequality. Because of invariance, $C_{ab} = B_k^m C_{ab} + A_k^m$. Taking limits yields $(a-b)PC_{ab} \geq 0$ with $a < b$, so $PC_{ab} = 0$.
