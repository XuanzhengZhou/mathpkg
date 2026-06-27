---
role: proof
locale: en
of_concept: macmillan-theorem
source_book: gtm017
source_chapter: "V"
source_section: "d"
---
First show $H = \lim H_n/n$ exists: $H_{n+m} \leq H_n + H_m$ implies subadditivity, giving convergence.

Then $-\log p_n(X_0, \dots, X_{n-1}) = \sum_{k=0}^{n-1} g_k(T^k w)$ where $g_k(w) = -\log P(X_0|X_{-1}, \dots, X_{-k})$. The sequence $g_k$ is uniformly integrable (via the estimate $\int_{S_{k,j}} g_k dP \leq s(j+1)e^{-j}$ where $s$ is the alphabet size). The ergodic theorem gives convergence in mean to $H$.
