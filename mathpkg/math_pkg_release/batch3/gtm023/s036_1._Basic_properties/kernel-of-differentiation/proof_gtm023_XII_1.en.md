---
role: proof
locale: en
of_concept: kernel-of-differentiation
source_book: gtm023
source_chapter: "XII"
source_section: "1"
---

If $f = \sum_{k=0}^n \alpha_k t^k$, then $df = \sum_{k=1}^n k\alpha_k t^{k-1}$. Thus $\deg(df) = \deg(f) - 1$ when $\deg f \geq 1$ (since $n\alpha_n \neq 0$ in characteristic zero). If $\deg f = 0$, then $f = \alpha_0$ and $df = 0$. Hence $\ker d = \{\alpha_0 \mid \alpha_0 \in \Gamma\} = \Gamma$ (identified with its image under $i$). Now $df = dg \iff d(f-g) = 0 \iff f-g \in \ker d = \Gamma \iff f-g = \alpha$ for some $\alpha \in \Gamma$.
