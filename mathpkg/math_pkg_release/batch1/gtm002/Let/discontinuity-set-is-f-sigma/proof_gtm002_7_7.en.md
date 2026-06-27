---
role: proof
locale: en
of_concept: discontinuity-set-is-f-sigma
source_book: gtm002
source_chapter: "7"
source_section: "7"
---

If $\omega(x_0) < \varepsilon$, then $\omega(x) < \varepsilon$ for all $x$ in a neighborhood of $x_0$. Hence the set $\{x : \omega(x) < \varepsilon\}$ is open for every $\varepsilon > 0$. The set $D$ of all points at which $f$ is discontinuous can be represented in the form

$$D = \bigcup_{n=1}^{\infty} \{x : \omega(x) \geq 1/n\}.$$

Each set $\{x : \omega(x) \geq 1/n\}$ is the complement of the open set $\{x : \omega(x) < 1/n\}$, hence closed. Therefore $D$ is a countable union of closed sets, i.e., an $F_\sigma$ set.
