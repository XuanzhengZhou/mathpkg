---
role: proof
locale: en
of_concept: absolute-continuity-epsilon-delta
source_book: gtm018
source_chapter: "VI"
source_section: "30"
---
Suppose that it is possible, for some $\varepsilon > 0$, to find a sequence $\{E_n\}$ of measurable sets such that $|\mu|(E_n) < 1/2^n$ and $|\nu|(E_n) \geq \varepsilon$, $n = 1, 2, \dots$. If $E = \limsup_n E_n$, then
$$|\mu|(E) \leq \sum_{i=n}^{\infty} |\mu|(E_i) < \frac{1}{2^{n-1}}, \quad n = 1, 2, \dots,$$
and therefore $|\mu|(E) = 0$. On the other hand (since $\nu$ is finite),
$$|\nu|(E) = \lim_n |\nu|(E_n \cup E_{n+1} \cup \cdots) \geq \limsup_n |\nu|(E_n) \geq \varepsilon.$$
Since this contradicts the relation $\nu \ll \mu$, the proof of the theorem is complete.
