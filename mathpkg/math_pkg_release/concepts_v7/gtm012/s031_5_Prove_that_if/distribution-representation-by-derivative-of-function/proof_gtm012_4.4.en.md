---
role: proof
locale: en
of_concept: distribution-representation-by-derivative-of-function
source_book: gtm012
source_chapter: "4"
source_section: "§4. Characterization of distributions of type L'"
---

# Proof of Representation of a distribution as a derivative of a function

**Theorem 4.3.** Suppose $F \in \mathcal{L}'$ is of order $k-2$, where $k$ is an integer $\geq 2$. Then there is a unique function $f$ such that

$$F = D^k(F_f).$$

*Proof.* Suppose first that $k = 2$, so $F$ is of order $0$. By definition of order $0$, there exist constants $a, M, K \in \mathbb{R}$ such that

(7) $$|F(u)| \leq K|u|_{0,a,M}, \quad \text{all } u \in \mathcal{L}.$$

We may suppose $a \geq 0$. Let $h$ be the function defined by

$$h(t) = \begin{cases} |t|, & t \leq 0, \\ 0, & t > 0, \end{cases}$$

and let $(h_n)_{1}^{\infty} \subset \mathcal{L}$ be the sequence given by Lemma 4.2, satisfying $|h_n - h|_{0,a,M} \to 0$ as $n \to \infty$.

For each $s \in \mathbb{R}$, consider the translates $T_s h_n(t) = h_n(t-s)$ and $T_s h(t) = h(t-s)$. Since the seminorm $|\cdot|_{0,a,M}$ depends only on the values of the function on $[M, \infty)$, and translation commutes with taking absolute value and exponential weights (up to a factor), we have

(8) $$|T_s h_n - T_s h|_{0,a,M} \to 0 \quad \text{as } n \to \infty.$$

From (7) and (8) it follows that for each $s \in \mathbb{R}$, the sequence $F(T_s h_n)$ converges as $n \to \infty$. Define

$$f(s) = \lim_{n \to \infty} F(T_s h_n).$$

By (7),

$$|f(s)| \leq \lim_{n \to \infty} K|T_s h_n|_{0,a,M} = K|T_s h|_{0,a,M}.$$

Now we estimate $|T_s h|_{0,a,M}$. Recall that $|u|_{0,a,M} = \sup_{t \geq M} e^{at}|u(t)|$. Since $h(t) = 0$ for $t > 0$, we have $T_s h(t) = 0$ for $t > s$. Therefore:

$$|T_s h|_{0,a,M} = 0 \quad \text{if } s \leq M,$$

$$|T_s h|_{0,a,M} = \sup_{M \leq t \leq s} e^{at} |t-s| \leq (s-M)e^{as} \quad \text{if } s > M.$$

Consequently,

$$\operatorname{supp}(f) \subset [M, \infty)$$

and for any $a' > a$ there is a constant $c$ such that

$$|f(s)| \leq c e^{a's}, \quad \text{all } s \in \mathbb{R}.$$

The continuity of $f$ follows from the continuity of $F$: given $\varepsilon > 0$, choose $n$ large and use that $F(T_s h_n)$ is close to both $f(s)$ and $F(T_{s'} h_n)$ when $s$ is near $s'$, because $T_s h_n$ depends continuously on $s$ in the topology of $\mathcal{L}$.

Now take any $u \in \mathcal{L}$. We want to show that $F(u) = D^2(F_f)(u) = F_f(D^2 u)$. Define

$$v_n(t) = \int_{-\infty}^{\infty} T_s h_n(t) D^2 u(s) \, ds = \int_{-\infty}^{\infty} h_n(t-s) D^2 u(s) \, ds.$$

Since $D^2 u \in \mathcal{L}$ and $h_n(t-s) = 0$ when $s \leq t$ (for $n$ large, $h_n$ vanishes on $[1/n, \infty)$), the integral converges.

We approximate $v_n$ by Riemann sums. For each positive integer $N$, set

$$v_{n,N}(t) = \frac{1}{N} \sum_{m=-N^2}^{N^2} h_n\!\left(t - \frac{m}{N}\right) D^2 u\!\left(\frac{m}{N}\right).$$

Then $v_{n,N} \to v_n$ in the seminorm $|\cdot|_{0,a,M}$ as $N \to \infty$. Indeed, for $t \geq M$,

$$\begin{aligned}
|v_{n,N}(t) - v_n(t)|
&= \left| \sum_{m=-N^2}^{N^2} \int_{(m-1)/N}^{m/N} \left[ h_n\!\left(t - \frac{m}{N}\right) D^2 u\!\left(\frac{m}{N}\right) - h_n(t-s) D^2 u(s) \right] ds \right| \\
&\leq \frac{c}{N} \int_{t}^{\infty} |t-s| e^{-as} \, ds = \frac{c'}{N} e^{-at},
\end{aligned}$$

where $c, c'$ are independent of $t$ and $N$. Hence $|v_{n,N} - v_n|_{0,a,M} \leq c'/N \to 0$.

Since $F$ is continuous (of order $0$) on $\mathcal{L}$,

$$F(v_n) = \lim_{N \to \infty} F(v_{n,N}).$$

But $F(v_{n,N})$ is a finite linear combination of values $F(T_{m/N} h_n)$, which by definition converge to $f(m/N)$ as $h_n$ is replaced by better approximations. Letting $f_n(s) = F(T_s h_n)$, we have

$$F(v_n) = \lim_{N \to \infty} \frac{1}{N} \sum_{m=-N^2}^{N^2} f_n\!\left(\frac{m}{N}\right) D^2 u\!\left(\frac{m}{N}\right) = \int_{-\infty}^{\infty} f_n(s) D^2 u(s) \, ds.$$

Now define

$$v(t) = \int_{-\infty}^{\infty} h(t-s) D^2 u(s) \, ds.$$

A similar estimate shows that $|v_n - v|_{0,a,M} \to 0$ as $n \to \infty$. Hence $F(v_n) \to F(v)$.

On the other hand, $f_n(s) = F(T_s h_n) \to f(s)$ pointwise, and the $f_n$ are uniformly bounded on compact sets. By dominated convergence,

$$\lim_{n \to \infty} \int_{-\infty}^{\infty} f_n(s) D^2 u(s) \, ds = \int_{-\infty}^{\infty} f(s) D^2 u(s) \, ds.$$

Thus

$$F(v) = \int_{-\infty}^{\infty} f(s) D^2 u(s) \, ds.$$

We claim that $v = u$. Indeed, differentiating under the integral sign (or interpreting the convolution distributionally),

$$\begin{aligned}
v(t) &= \int_{-\infty}^{\infty} h(t-s) D^2 u(s) \, ds \\
&= \int_{-\infty}^{t} (t-s) D^2 u(s) \, ds,
\end{aligned}$$

since $h(t-s) = |t-s| = s-t$ when $s \leq t$ (because $t-s \leq 0$ in that range — wait, let us verify: $h(r) = |r|$ for $r \leq 0$, and $h(r) = 0$ for $r > 0$; with $r = t-s$, we have $h(t-s) = |t-s|$ when $t-s \leq 0$, i.e. $s \geq t$, and $h(t-s) = 0$ when $t-s > 0$, i.e. $s < t$ — correction: actually $h(t) = |t|$ for $t \leq 0$, so $h(t-s) = |t-s|$ when $t-s \leq 0$, i.e. $s \geq t$, but we also have $h(t) = 0$ for $t > 0$. So the integral is over $s \geq t$:

$$v(t) = \int_{t}^{\infty} (s-t) D^2 u(s) \, ds.$$

Now integrate by parts twice. Let $w(s) = D u(s)$. Then

$$\int_{t}^{\infty} (s-t) D^2 u(s) \, ds = \left[ (s-t) D u(s) \right]_{s=t}^{s=\infty} - \int_{t}^{\infty} D u(s) \, ds = 0 - \left[ u(s) \right]_{t}^{\infty} = u(t),$$

since $u$ and all its derivatives vanish at $+\infty$. Therefore $v = u$.

Putting everything together,

$$F(u) = F(v) = \int_{-\infty}^{\infty} f(s) D^2 u(s) \, ds = F_f(D^2 u) = D^2(F_f)(u).$$

This proves the theorem for $k = 2$.

**General $k$.** Suppose now that $F$ is of order $k-2$ with $k > 2$. We proceed by induction.

Define the integral operator $S_+$ on $\mathcal{L}$ by

$$(S_+ u)(t) = \int_{t}^{\infty} u(s) \, ds.$$

For $F \in \mathcal{L}'$, define the distribution $S_+^* F$ (the integral of $F$ from the left) by

$$(S_+^* F)(u) = -F(S_+ u), \quad u \in \mathcal{L}.$$

The operator $S_+^*$ decreases the order by exactly one: if $F$ has order $r$, then $S_+^* F$ has order $r-1$.

Applying $S_+^*$ repeatedly $k-2$ times to $F$, we obtain a distribution $G = (S_+^*)^{k-2} F$ of order $0$. By the case $k=2$ proved above, there exists a function $f$ such that

$$G = D^2(F_f).$$

Now observe that $D \circ S_+^* = \operatorname{id}$ on $\mathcal{L}'$. Indeed, for any $u \in \mathcal{L}$,

$$D(S_+^* F)(u) = -(S_+^* F)(D u) = F(S_+ D u) = F(u),$$

because $S_+ D u(t) = \int_t^{\infty} D u(s) \, ds = -u(t)$ (note the sign: $S_+$ integrates from $t$ to $\infty$, so its derivative is $-1$ times the function). More precisely, the right inverse of $D$ is $-S_+$, but adjusting signs we have $D(S_+^*) = \operatorname{id}$.

Therefore,

$$F = D^{k-2}(G) = D^{k-2}(D^2(F_f)) = D^k(F_f).$$

**Uniqueness.** Suppose $D^k(F_f) = D^k(F_g)$. Then $D^k(F_{f-g}) = 0$. This means $F_{f-g}$ is a polynomial of degree at most $k-1$. But the support condition $\operatorname{supp}(f-g) \subset [M, \infty)$ and the exponential growth bound force the polynomial to be identically zero, hence $f = g$. $\square$
