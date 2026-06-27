---
role: proof
locale: en
of_concept: rip-lip-moufang-plane-equivalence
source_book: gtm006
source_chapter: "V"
source_section: "6"
---

Since $R$ has RIP, by Theorem 6.12 every line through $(\infty)$ is a translation line. If $R$ also has LIP, then by Theorem 6.14, $\mathcal{P}$ is $((0,0), [0,0])$-transitive, so $[0,0]$ is a translation line. Note that $[0,0]$ passes through $(0)$, not through $(\infty)$. Thus $\mathcal{P}$ has translation lines through both $(\infty)$ and $(0)$, giving three non-concurrent translation lines: two through $(\infty)$ (guaranteed by RIP) and one through $(0)$ (guaranteed by LIP), with the latter not passing through $(\infty)$. By Theorem 4.20, the existence of three non-concurrent translation lines implies that every line of $\mathcal{P}$ is a translation line, which is precisely the definition of a Moufang plane.

Conversely, if $\mathcal{P}$ is a Moufang plane, then every line is a translation line, so in particular $[0,0]$ is a translation line, giving $((0,0), [0,0])$-transitivity, which by Theorem 6.14 implies $R$ has LIP.
