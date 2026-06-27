---
role: proof
locale: en
of_concept: proposition-18-13
source_book: gtm055
source_chapter: "18"
source_section: "Section 19_Section_19"
---

Proof. A sequence $\{p_n\}$ of polynomials converging uniformly on $K$ automatically converges uniformly on the outer boundary of $K$. But then, by the maximum modulus principle (Ex. 5M), $\{p_n\}$ converges uniformly on $\hat{K}$, and the limit is therefore differentiable at each point of $\hat{K}^{\circ}$ (see Problem 11U).

The foregoing discussion shows that for a compact subset $K$ of $\mathbb{C}$, the algebra $\mathcal{P}(K)$ may fail to be equal to $\mathcal{C}(K)$ for two quite different reasons, either because $K^{\circ} \neq \emptyset$, or because $K$ has one or more holes.

Example G. Let us take for $K$ the unit circle $Z$. Then $\hat{K}$ is just the closed unit disc $D^{-}$ of Example F, so $\mathcal{P}(Z)$ consists of the restrictions to $Z$ of all of the functions in $\mathcal{P}(D^{-}) = \mathcal{A}(D^{-})$. We observe

linear functional on $\mathcal{A}(D^-)$, so there exists a complex Borel measure $\xi_\alpha$ on $Z$ such that

$$f(\alpha) = \int_Z f d\xi_\alpha, \quad f \in \mathcal{A}(D^-).$$

Thus, for example, for $\alpha = 0$ we have

$$f(0) = \frac{1}{2\pi i} \int_Z \frac{f(\xi)}{\xi} d\xi = \frac{1}{2\pi} \int_0^{2\pi} f(e^{it}) dt = \frac{1}{2\pi} \int_Z f d\theta$$

(where $\theta$ denotes arc-length measure; see Example 8F), so we may take $\xi_0$ to be $\theta/2\pi$. (This use of the Cauchy integral formula is readily justified because of the uniform continuity of $f$ on $D^-$.)

**Example I.** Let $r$ and $R$ be radii such that $0 < r < R$, let $A$ denote the annular domain $\{\lambda \in \mathbb{C}: r < |\lambda| < R\}$, and let $K = A^-$. Then the circle $C_R = \{\lambda \in \mathbb{C}: |\lambda| = R\}$ is the outer boundary of $K$ and $\hat{K}$ is the closed disc $D_R^- = \{\lambda \in \mathbb{C}: |\lambda| \leq R\}$. Thus every function $f$ in $\mathcal{P}(K)$ is the restriction to $K$ of a function $g$ in the algebra $\mathcal{A}(D_R^-) = \mathcal{P}(D_R^-)$.

Next let us consider the algebra $\mathcal{A}(K)$. If $f \in \mathcal{A}(K)$ then $f$ possesses a Laurent expansion

$$f(\lambda) = \sum_{n=-\infty}^{+\infty} \alpha_n \lambda^n, \quad \lambda \in A$$

(Prop. 5.9), and we may write $f = f_1 + f_2$ where

$$f_1(\lambda) =
