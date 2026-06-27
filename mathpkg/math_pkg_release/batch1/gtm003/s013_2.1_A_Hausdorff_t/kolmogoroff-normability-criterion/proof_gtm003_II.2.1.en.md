---
role: proof
locale: en
of_concept: kolmogoroff-normability-criterion
source_book: gtm003
source_chapter: "II"
source_section: "2.1"
---

The condition is necessary, for if $x \mapsto \|x\|$ generates the topology of $L$, then
$$V_1 = \{x \in L : \|x\| \leq 1\}$$
is a convex neighborhood of $0$ which is bounded, since by (i) above, the multiples $\{n^{-1} V_1\}_{n \in \mathbb{N}}$ form a $0$-neighborhood base in $L$.

Conversely, if $V$ is a convex, bounded $0$-neighborhood in $L$, there exists a circled neighborhood contained in $V$ whose convex hull $U$ is bounded (since it is contained in $V$). Clearly, the gauge $p$ of $U$ is a norm on $L$. Now the boundedness of $U$ implies that $\{n^{-1} U\}_{n \in \mathbb{N}}$ is a $0$-neighborhood base, whence it follows that $p$ generates the topology of $L$.
