---
role: proof
locale: en
of_concept: "let-be-any-measure-space-and-let-define"
source_book: gtm025
source_chapter: "Integration Theory Continued"
source_section: "20.33"
---

For $g \in \mathfrak{L}_{\infty}$, choose a bounded $f \in \mathfrak{L}_{\infty}$ such that $\|f - g\|_{\infty} = 0$ and $\|f\|_u = \|g\|_{\infty}$ (20.14). By (20.32), we have

$$|L_{\tau}(g)| = \int_X g d\tau = \int_X f d\tau \leq \int_X |f| d|\tau| \leq \|f\|_u \|\tau\|$$

$$= \|g\|_{\infty} \|\tau\|.$$

Thus $L_{\tau} \in \mathfrak{L}_{\infty}^*$ and

$$\|L_{\tau}\| \leq \|\tau\|.$$

Let $\varepsilon > 0$ be given and select a measurable dissection $\{A_1, \ldots, A_n\}$ of $X$ such that

$$\sum_{j=1}^{n} |\tau(A_j)| > \|\tau\| - \varepsilon.$$

For each $j$, let $\alpha_j = \text{sgn}(\overline{\tau(A_j)})$ and set $g = \sum_{j=1}^{n} \alpha_j \xi_{A_j}$. It is plain that $g \in

Thus (20.27.i) holds for $\tau$. Also, if $A$ and $B$ are disjoint sets in $\mathcal{A}$, then $\xi_A + \xi_B = \xi_{A \cup B}$, and so

$$\tau(A \cup B) = L(\xi_A \cup B) = L(\xi_A + \xi_B) = L(\xi_A) + L(\xi_B) = \tau(A) + \tau(B);$$

hence (20.27.ii) holds. Next, if $A \in \mathcal{A}$ and $A$ is locally $\mu$-null, then $\xi_A = 0$ in $\mathcal{L}_\infty$ and therefore

$$\tau(A) = L(\xi_A) = L(0) = 0.$$

Thus (20.27.iii) holds, and so $\tau \in F(X, \mathcal{A}, \mu)$. Let $g$ be any function in $\mathcal{L}_\infty$. Choose a bounded $f \in \mathcal{L}_\infty$ such that $\|f - f\|_\infty = 0$ and $\|f\|_u = \|g\|_\infty$. Choose a sequence $(s_n)$ of $\mathcal{A}$-measurable simple functions such that $\|f - s_n\|_u \to 0$. It is clear from (1), the linearity of $L$, and (20.29.i) that

$$L(s_n) = \int_X s_n d\tau$$

for each $n \in N$. Since $\|f - s_n\|_\infty \to 0$ and $L$ is continuous on $\mathcal{L}_\infty$, (2) and (20.29.ii) imply that

$$L(g) = L(f) = \lim_{n \to \infty} L(s_n) = \lim_{n \to \infty} \int_X s_n d\tau = \int_X f d\tau$$

$$= \int_X g d\tau = L_\tau(g).$$
