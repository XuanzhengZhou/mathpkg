---
role: proof
locale: en
of_concept: "open-subspace-of-polish-is-polish"
source_book: gtm039
source_chapter: "3"
source_section: "3.1"
---
Let $G \subseteq P$ be open. Define $f(x) = 1/d(x, P\setminus G)$. The map $x \mapsto (x,f(x))$ is a homeomorphism of $G$ onto the graph of $f$ in $P \times \mathbb{R}$. The graph is closed: if $x_n \to x$ and $f(x_n) \to t$, then $f(x_n)$ bounded implies $x \notin P\setminus G$, so $x \in G$ and $t = f(x)$. Thus $G$ is Polish as a closed subset of $P \times \mathbb{R}$. $\square$
