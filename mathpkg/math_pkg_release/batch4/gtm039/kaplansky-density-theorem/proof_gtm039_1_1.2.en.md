---
role: proof
locale: en
of_concept: "kaplansky-density-theorem"
source_book: gtm039
source_chapter: "1"
source_section: "1.2"
---
For self-adjoint $T \in \mathcal{A}_s$ with $\|T\| \leqslant 1$, define $g(t) = 2t(1+t^2)^{-1}$ on $\mathbb{R}$. Then $S_0 = g(T) \in \mathcal{A}_s$ is self-adjoint. Let $S_n \in \mathcal{A}$ converge strongly to $S_0$. Using the identity $2[f(S)-f(S_0)] = 4(1+S^2)^{-1}(S-S_0)(1+S_0^2)^{-1} - f(S)(S-S_0)f(S_0)$ with $f$ the inverse of $g$, strong continuity of $f$ implies $f(S_n) \to f(S_0) = T$ strongly. Since $|f| \leqslant 1$, $\|f(S_n)\| \leqslant 1$. The general case follows from a $2 \times 2$ matrix trick. $\square$
