---
role: proof
locale: en
of_concept: ordinal-multiplication-zero-and-one
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction).
(1) By definition $\alpha \cdot 0 = 0$ for all $\alpha$ including $\alpha = 0$. If $0 \cdot \alpha = 0$, then $0 \cdot (\alpha + 1) = 0 \cdot \alpha + 0 = 0$. If $\alpha \in K_{\mathrm{II}}$ and $0 \cdot \gamma = 0$ for $\gamma < \alpha$, then $0 \cdot \alpha = \bigcup_{\gamma < \alpha} 0 \cdot \gamma = 0$.

(2) From (1), $\alpha \cdot 1 = \alpha \cdot (0 + 1) = \alpha \cdot 0 + \alpha = 0 + \alpha = \alpha$. By definition $1 \cdot 0 = 0$. If $1 \cdot \alpha = \alpha$, then $1 \cdot (\alpha + 1) = 1 \cdot \alpha + 1 = \alpha + 1$. If $\alpha \in K_{\mathrm{II}}$ and $1 \cdot \gamma = \gamma$ for $\gamma < \alpha$, then $1 \cdot \alpha = \bigcup_{\gamma < \alpha} 1 \cdot \gamma = \alpha$.
