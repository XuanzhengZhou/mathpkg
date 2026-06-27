---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The partial recursive function $h$ enumerates the complement of $g^{+*}\Gamma$, i.e., the set of natural numbers that are NOT G\"{o}del numbers of sentences in $\Gamma$, together with all non-sentence numbers. Given $x$, $h$ searches for a witness $y$ showing that $x$ is excluded from some complete extension $\Theta_m$ — specifically, that $\neg g^{+-1}x$ is provable from some $\Delta_m$ together with $\Gamma$. Since each $\Theta_m$ is complete and uniformly r.e., any $x \notin g^{+*}\Gamma$ will eventually be witnessed, making $\text{Dmn}\,h = \omega \setminus g^{+*}\Gamma$. This establishes that the complement is r.e., hence $g^{+*}\Gamma$ is recursive (i.e., $\Gamma$ is decidable).
