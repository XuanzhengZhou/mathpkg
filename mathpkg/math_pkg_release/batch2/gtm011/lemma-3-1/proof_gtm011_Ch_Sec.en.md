---
role: proof
locale: en
of_concept: lemma-3-1
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. If $R(t) = \infty$ for some value of $t$ then it is possible to extend $f_t$ to an entire function. It follows that $f_s(z) = f_t(z)$ for all $z$ in $D_s$ so that $R(s) = \infty$ for each $s$ in $[0, 1]$; that is $R(s) \equiv \infty$. So suppose that $R(t) < \infty$ for all $t$. Fix $t$ in $[0, 1]$ and let $\tau = \gamma(t)$; let

$$f_t(z) = \sum_{n=0}^{\infty} \tau_n(z - \tau)^n$$

be the power series expansion of $f_t$ about $\tau$. Now let $\delta_1 > 0$ be such that $|s - t| < \delta_1$ implies that $\gamma(s) \in D_t \cap B(\tau; R(t))$ and $[f_s]_{\gamma(s)} = [f_t]_{\gamma(s)}$. Fix $s$ with $|s - t| < \delta_1$ and let $\sigma = \gamma(s)$. Now $f_t$ can be extended to an analytic function on $B(\tau; R(t))$. Since $f_s$ agrees with $f_t$ on a neighborhood of $\sigma$, $f_s$ can be extended so that it is also analytic on $B(\tau; R(t)) \cup D_s$. If $f_s

Furthermore, suppose that $D_t$ is a disk of radius $R(t)$ about $\gamma(t)$. The truth of the conclusion will not be affected by this assumption (Why?), and the exposition will be greatly simplified by it. For the same reason it will also be assumed that each $B_t$ is a disk.

Since $|\sigma(t) - \gamma(t)| < \epsilon < R(t)$, $\sigma(t) \in B_t \cap D_t$ for all $t$. Thus, it makes sense to ask whether $g_t(z) = f_t(z)$ for all $z$ in $B_t \cap D_t$. Indeed, to complete the proof we must show that this is precisely the case for $t = 1$. Define the set $T = \{t \in [0, 1] : f_t(z) = g_t(z) \text{ for } z \text{ in } B_t \cap D_t\}$; and show that $1 \in T$. This is done by showing that $T$ is a non-empty open and closed subset of $[0, 1]$.

From the hypothesis of the lemma, $0 \in T$ so that $T \neq \square$. To show $T$ is open fix $t$ in $T$ and choose $\delta > 0$ such that

3.4 $$\begin{cases} |\gamma(s) - \gamma(t)| < \epsilon, [f_s]_{\gamma(s)} = [f_t]_{\gamma(s)}, \\ |\sigma(s) - \sigma(t)| < \epsilon, [g_s]_{\sigma(s)} = [g_t]_{\sigma(s)}, \\ \sigma(s) \in B_t \end{cases}$$ and whenever $|s-t| < \delta$. We will now show that $B_s \cap B_t \cap D_s \cap D_t \neq \square$ for $|s-t| < \delta$; in fact, we will show that $\sigma(s)$ is in this intersection. If $|s-t| < \delta$ then

$$|\sigma(s) - \gamma(s)| < \epsilon < R(s)$$

so that $\sigma(s) \in D_s$. Also

$$|\sigma(s) - \gamma(t)| \leq |\sigma(s) - \gamma

Let $a \in D$, $b \in G$ and let $\gamma_0$ and $\gamma_1$ be paths in $G$ from $a$ to $b$; let $\{(f_t, D_t): 0 \leq t \leq 1\}$ and $\{(g_t, B_t): 0 \leq t \leq 1\}$ be analytic continuations of $(f, D)$ along $\gamma_0$ and $\gamma_1$ respectively. If $\gamma_0$ and $\gamma_1$ are FEP homotopic in $G$ then

$$[f_1]_b = [g_1]_b.$$

Proof. Since $\gamma_0$ and $\gamma_1$ are fixed-end-point homotopic in $G$ there is a continuous function $\Gamma: [0, 1] \times [0, 1] \rightarrow G$ such that

$$\Gamma(t, 0) = \gamma_0(t) \quad \Gamma(t, 1) = \gamma_1(t)$$

$$\Gamma(0, u) = a \quad \Gamma(1, u) = b$$

for all $t$ and $u$ in $[0, 1]$. Fix $u, 0 \leq u \leq 1$ and consider
