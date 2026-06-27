---
role: proof
locale: en
of_concept: fourier-transform-l2-norm
source_book: gtm025
source_chapter: "21"
source_section: "SS 21"
---

Let $\tilde{f}(x) = \overline{f(-x)}$ and $g = f * \tilde{f}$. Then $g \in \mathfrak{L}_1(R)$ is continuous and bounded, and by (21.41), $\hat{g} = \hat{f} \cdot \overline{\hat{f}} = |\hat{f}|^2$. At $0$, $g(0) = (2\pi)^{-\frac{1}{2}} \int_R |f(x)|^2 dx$. By (21.43), $g(0) = \lim_{n\to\infty} (2\pi)^{-\frac{1}{2}} \int_R |\hat{f}(y)|^2 \exp(-|y|/n)dy = (2\pi)^{-\frac{1}{2}} \int_R |\hat{f}(y)|^2 dy$ by monotone convergence. Hence $\|\hat{f}\|_2 = \|f\|_2$.
