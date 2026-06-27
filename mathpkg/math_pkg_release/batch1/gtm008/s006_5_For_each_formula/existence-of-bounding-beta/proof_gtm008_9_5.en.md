---
role: proof
locale: en
of_concept: existence-of-bounding-beta
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

$B^{M_{\alpha}}$ is a set. For $s \in B^{M_{\alpha}}$, define $f(s) = \mu_{\beta}((\exists a \in M_{\beta})[a \text{ is defined over } M_{\alpha} \land s = \{\langle x, \llbracket x \in a \rrbracket \rangle \mid x \in M_{\alpha}\}])$ (or $0$ if none). Then $\beta = \sup_{s \in B^{M_{\alpha}}} f(s)$ exists. If $a$ is defined over $M_{\alpha}$ with $s = \{\langle x, \llbracket x \in a \rrbracket \rangle \mid x \in M_{\alpha}\}$, then $s \in B^{M_{\alpha}}$, so $b \in M_{f(s)}$ with $\llbracket a = b \rrbracket = 1$ and $b \in M_{\beta}$.
