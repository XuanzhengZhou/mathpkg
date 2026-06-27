---
role: proof
locale: en
of_concept: "let-be-a-locally-compact-hausdorff-space-and-3"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.32"
---

By (19.31), $(X, M_i, \iota)$ is decomposable. Now we have only to apply (19.27).

(19.33) Remark. If $X$ is a locally compact Hausdorff space and if $\iota$ and $\eta$ are any two outer measures on $X$ constructed from nonnegative linear functionals as in § 9 such that $\iota(E) = 0$ implies $\eta(E) = 0$, then $M_i \subset M_\eta$. To see this, let $A \in M_i$ and let $F$ be compact. According to (10.34), we have $A \cap F = B \cup E$ where $B \in \mathcal{B}(X)$ and $\iota(E) = 0$. Since $\mathcal{B}(X) \subset M_\eta$ and $\eta(E) = 0$, we have $A \cap F \in M_\eta$. It follows from (10.31) that $A \in M_\eta$. Thus (19.27) holds for $\iota$ and $\eta$ on $(X, M_i)$.

(19.34) Note. Our labors throughout (19.25) to (19.33) would be unnecessary if all measures were $\sigma$-finite and all locally compact Hausdorff spaces $\sigma$-compact. One may well ask if the generality obtained in (19.27) and (19.33) is worth the effort. Many mathematicians believe it is not. But we feel it our duty to show the reader the most general

finite measures on $(X, \mathcal{A})$, and each of them is absolutely continuous with respect to $\mu$. By (19.24), there exist nonnegative, finite-valued, $\mathcal{A}$-measurable functions $f_k$ on $X$ such that $f \in \mathfrak{L}_1(X, \mathcal{A}, v_k)$ implies

$$\int_X f \, dv_k = \int_X ff_k \, d\mu$$

$(k \in \{1, 2, 3, 4\})$. Let $f_0 = \sum_{k=1}^{4} \alpha_k f_k$, where $\alpha_1 = 1, \alpha_2 = -1, \alpha_3 = i$, and $\alpha_4 = -i$. Of course $f_0$ is in $\mathfrak{L}_1(X, \mathcal{A}, \mu)$ since each $f_k$ is in $\mathfrak{L}_1(X, \mathcal{A}, \mu)$ [set $f = 1$ in (1)]. Then if $f \in \mathfrak{L}_1(X, \mathcal{A}, |v|)$, (19.16) shows that $f \in \mathfrak{L}_1(X, \mathcal{A}, v_k)$ for all $k$, and so (1) and (19.17) yield

$$\int_X f \, dv = \sum_{k=1}^{4} \alpha_k \int_X f \, dv_k = \sum_{k=1}^{4} \alpha_k \int_X ff_k \, d\mu = \int_X ff_0 \, d\mu$$

[here we have used the fact that $ff_k \in \mathfrak{L}_1(X, \mathcal{A}, \mu)$ for all $k$, which is evident from (1)]. This proves (i). The identity (ii) follows from (i) upon taking $f = \xi_A$, since $|v|$ is a finite measure.

To prove the uniqueness of $f_0$ in $\mathfrak{L}_1(X, \mathcal{A}, \mu)$, suppose that $h_

Each $\sigma_m$ has the form $\sum_{j=1}^{n} \beta_j \xi_{A_j}$, where $\{A_1, \ldots, A_n\}$ is a measurable dissection of $A$ and $|\beta_j| \leq 1$ for all $j$. Therefore

$$\left| \int_X f_0 \sigma_m d\mu \right| = \left| \sum_{j=1}^{n} \beta_j \int_A f_0 d\mu \right| \leq \sum_{j=1}^{n} \left| \int_A f_0 d\mu \right|$$

$$= \sum_{j=1}^{n} |v(A_j)| \leq |v|(A).$$

Combining (3) and (4), we have

$$\int_A |f_0| d\mu \leq |v|(A).$$

Now (2) and (5) together imply (iii). Setting $A = X$, we get (iv).

(19.37) Note. The reader should find it illuminating to compare the statement and the proof of (19.36.iii) with the corresponding result about absolutely continuous functions (18.1).
