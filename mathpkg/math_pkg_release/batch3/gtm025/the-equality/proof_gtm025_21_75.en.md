---
role: proof
locale: en
of_concept: "the-equality"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.75"
---

We prove (i) only for $j = r$, the case $j = l$ being almost the same.

It is easy to see that the set $M_t^{(r)}$ is open, since the function $s \rightarrow \frac{1}{s-x} \int_{x}^{s} f d\lambda$ is continuous on $]x, \infty[$. Let $\{] \beta_k, \gamma_k[ \}_{k=1}^{\infty}$ be the unique family of pairwise disjoint intervals such that

$$M_t^{(r)} = \bigcup_{k=1}^{\infty} \beta_k, \gamma_k[$$

(6.59). Consider an interval $] \beta_k, \gamma_k[$ [which may of course be unbounded]. For each $x \in ]\beta_k, \gamma_k[$, the open set

$$N_x = \{s : \int_x^s f d\lambda > t(s-x), s \in ]x, \gamma_k[ \cap R\}$$

is nonvoid. This is trivial if $\gamma_k = \infty$. If $\gamma_k < \infty$ and $N_x$ is void for some $x \in ]\beta_k, \gamma_k[$, there must be a $w > \gamma_k$ such that $\int_x^w f d\lambda > t(w-x)$. We have

$$\int_x^w f d\lambda = \int_x^w f d\lambda - \int_x^w f d\lambda > t(w-x) - t(\gamma_k-x) = t(w-\gamma_k)$.

This inequality implies that $\gamma_k \in M_t^{(r)}$, a contradiction. Let $s_x = \sup N_x$. We will prove that $s_x = \gamma_k$. If $s_x < \gamma_k$, then the equality $\int_x

since $\beta_k$ is not in $M_t^{(r)}$. Hence in all cases we have

$$\int_{\beta_k}^{\gamma_k} f \, d\lambda = t(\gamma_k - \beta_k).$$

The equality (i) follows.

To prove (ii), note that $M_t = M_t^{(r)} \cup M_t^{(l)}$. Hence we have

$$\lambda(M_t) \leq \lambda(M_t^{(r)}) + \lambda(M_t^{(l)})$$

$$= \frac{1}{t} \left[ \int_{M_t^{(r)}} f \, d\lambda + \int_{M_t^{(l)}} f \, d\lambda \right]$$

$$\leq \frac{2}{t} \int_{M_t} f \, d\lambda.$$

(21.76) HARDY-LITTLEWOOD Maximal Theorem for $\mathfrak{L}_p(p > 1)$. Let $p$ be a real number $> 1$. Notation is as in (21.74). Then

(i) $$\left[ \int_{R} (f^{\Lambda(j)})^p \, d\lambda \right]^{\frac{1}{p}} \leq \frac{p}{p-1} \left[ \int_{R} f^p \, d\lambda \right]^{\frac{1}{p}} (j = r, l)$$

and

(ii) $$\left[ \int_{R} (f^{\Lambda})^p \, d\lambda \right]^{\frac{1}{p}} \leq \frac{2p}{p-1} \left[ \int_{R} f^p \, d\lambda \right]^{\frac{1}{p}}.$$

Proof. We use (21.72), (21.75.i), FUBINI's theorem (21.12), and Hölder's inequality (13.4) [in that order] to calculate as follows:

$$\int_{R} (f^{\Lambda(j)}(x))^p \, dx = \int_{0}^{\infty} p t^{p-1} \lambda(M_t^{(j)}) \, dt$$

$$= p \int

Since $1 - \frac{1}{p'} = \frac{1}{p}$, the inequality (i) follows if $f^{A(i)} \in \mathfrak{L}_p$. To check this, use (21.79.i) [which depends only upon (21.75)] to write

$$\int_R (f^{A(i)}(x))^p dx \leq \frac{p}{1-k} \int_0^\infty t^{p-2} \int_G f(x) dx dt.$$

Then argue as above to obtain

$$\int_R (f^{A(i)}(x))^p dx \leq \frac{p k^{1-p}}{(p-1)(1-k)} \int_R (f(x))^p dx.$$

The use of Fubini's theorem is justified because the inverse image of the set $]a, \infty]$ under the map $(x, t) \rightarrow \xi_{M^{(j)}}(x)$ is $\varnothing$ if $a \geq 1$, is $R \times [0, \infty[$ if $a < 0$, and is $\{(x, t) : f^{A(i)}(x) > t\}$ if $0 \leq a < 1$. Each of these sets is product measurable. A like calculation, based on (21.75.ii), proves (ii). $\square$

The preceding theorem is ordinarily stated with $R$ replaced by an interval and with smaller functions $f^{A(r)}, f^{A(l)}$, and $f^{A}$. This case is contained in the following corollary.
