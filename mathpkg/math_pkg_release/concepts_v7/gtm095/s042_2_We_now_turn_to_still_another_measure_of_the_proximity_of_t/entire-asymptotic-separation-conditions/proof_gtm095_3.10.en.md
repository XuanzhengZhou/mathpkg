---
role: proof
locale: en
of_concept: entire-asymptotic-separation-conditions
source_book: gtm095
source_chapter: "3"
source_section: "10.2"
---

# Proof of Theorem 2 (Equivalent conditions for entire asymptotic separation via Hellinger integrals)

Let $(\Omega^n, \mathcal{F}^n)_{n \geq 1}$, $P^n$, $\tilde{P}^n$, $Q^n$, $z^n$, $\tilde{z}^n$, and $Z^n$ be as in Theorem 1.

The theorem states the equivalence of:

(a) $(\tilde{P}^n) \triangle (P^n)$ (entire asymptotic separation);

(b) $\limsup_{n} \tilde{P}^n(z^n \geq \varepsilon) = 0$ for every $\varepsilon > 0$;

(c) $\limsup_{n} H(\alpha; P^n, \tilde{P}^n) = 0$ for all $\alpha \in (0, 1)$;

(d) $\limsup_{n} H(\alpha; P^n, \tilde{P}^n) = 0$ for some $\alpha \in (0, 1)$.

**Proof.**

**(a) $\Rightarrow$ (b).** Let $(\tilde{P}^n) \triangle (P^n)$, $n_k \uparrow \infty$, and let $A^{n_k} \in \mathcal{F}^{n_k}$ have the property that $P^{n_k}(A^{n_k}) \to 1$ and $\tilde{P}^{n_k}(A^{n_k}) \to 0$. Then, since $z^n + \tilde{z}^n = 2$, we have

$$\tilde{P}^{n_k}(z^{n_k} \geq \varepsilon) \leq \tilde{P}^{n_k}(A^{n_k}) + E_{Q^{n_k}}\left\{ z^{n_k} \cdot \frac{\tilde{z}^{n_k}}{z^{n_k}} I(\overline{A}^{n_k}) I(z^{n_k} \geq \varepsilon) \right\}$$

$$= \tilde{P}^{n_k}(A^{n_k}) + E_{P^{n_k}}\left\{ \frac{\tilde{z}^{n_k}}{z^{n_k}} I(\overline{A}^{n_k}) I(z^{n_k} \geq \varepsilon) \right\} \leq \tilde{P}^{n_k}(A^{n_k}) + \frac{2}{\varepsilon} P^{n_k}(\overline{A}^{n_k}).$$

As $k \to \infty$, $\tilde{P}^{n_k}(A^{n_k}) \to 0$ and $P^{n_k}(\overline{A}^{n_k}) \to 0$, so $\tilde{P}^{n_k}(z^{n_k} \geq \varepsilon) \to 0$, establishing (b).

**(b) $\Rightarrow$ (c).** For any $\alpha \in (0, 1)$,

$$H(\alpha; P^n, \tilde{P}^n) = E_{Q^n}((z^n)^\alpha (\tilde{z}^n)^{1-\alpha})$$

$$\leq \varepsilon^\alpha + 2 \cdot \tilde{P}^n(z^n < \varepsilon) + 2 \cdot \tilde{P}^n(z^n \geq \varepsilon).$$

Taking $\limsup_{n \to \infty}$ and using (b), then letting $\varepsilon \downarrow 0$, we obtain $\limsup_{n} H(\alpha; P^n, \tilde{P}^n) = 0$.

**(c) $\Rightarrow$ (d).** Trivial.

**(d) $\Rightarrow$ (a).** If $\limsup_{n} H(\alpha; P^n, \tilde{P}^n) = 0$ for some $\alpha \in (0, 1)$, then by properties of the Hellinger integral, the measures $P^n$ and $\tilde{P}^n$ become asymptotically singular (entirely separated) as $n \to \infty$.

**Special case: Product measures.** When $P^n = P_1 \times \cdots \times P_n$ and $\tilde{P}^n = \tilde{P}_1 \times \cdots \times \tilde{P}_n$, we have

$$H(\alpha; P^n, \tilde{P}^n) = \prod_{k=1}^{n} H(\alpha; P_k, \tilde{P}_k) = \exp\left(\sum_{k=1}^{n} \log[1 - (1 - H(\alpha; P_k, \tilde{P}_k))]\right).$$

From Theorems 1 and 2 we then obtain:

$$(\tilde{P}^n) \triangleleft (P^n) \iff \lim_{\alpha \downarrow 0} \limsup_{n} \sum_{k=1}^{n} [1 - H(\alpha; P_k, \tilde{P}_k)] = 0,$$

$$(\tilde{P}^n) \triangle (P^n) \iff \limsup_{n} \sum_{k=1}^{n} [1 - H(\alpha; P_k, \tilde{P}_k)] = \infty \quad \text{for all } \alpha \in (0, 1).$$
