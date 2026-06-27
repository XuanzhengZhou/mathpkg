---
role: proof
locale: en
of_concept: contiguity-equivalent-conditions
source_book: gtm095
source_chapter: "3"
source_section: "10.2"
---

# Proof of Theorem 1 (Equivalent conditions for contiguity via Hellinger integrals)

Let $(\Omega^n, \mathcal{F}^n)_{n \geq 1}$ be a sequence of measurable spaces, and $P^n$, $\tilde{P}^n$ probability measures on $(\Omega^n, \mathcal{F}^n)$. Set

$$Q^n = \frac{P^n + \tilde{P}^n}{2}, \quad z^n = \frac{dP^n}{dQ^n}, \quad \tilde{z}^n = \frac{d\tilde{P}^n}{dQ^n}.$$

Let $Z^n = \tilde{z}^n/z^n$ be the Lebesgue derivative of $\tilde{P}^n$ with respect to $P^n$, with the convention $Z^n = \infty$ when $z^n = 0$.

The theorem states the equivalence of the following conditions:

(a) $(\tilde{P}^n) \triangleleft (P^n)$ (contiguity);

(b) $\limsup_{n} \tilde{P}^n(z^n < \varepsilon) = 0$ for every $\varepsilon > 0$;

(b$'$) $\limsup_{n} \tilde{P}^n(Z^n \leq N) = 0$ for every $N > 0$;

(c) $\lim_{\alpha \downarrow 0} \liminf_{n} H(\alpha; P^n, \tilde{P}^n) = 0$;

(d) $\liminf_{n} H(\alpha; P^n, \tilde{P}^n) = 0$ for all $\alpha \in (0, 1)$;

(e) $\liminf_{n} H(\alpha; P^n, \tilde{P}^n) = 0$ for some $\alpha \in (0, 1)$.

**Proof.**

**(a) $\Rightarrow$ (b).** If (b) is not satisfied, there exist $\varepsilon > 0$ and a sequence $n_k \uparrow \infty$ such that $\tilde{P}^{n_k}(z^{n_k} < 1/n_k) \geq \varepsilon$. But by the definition of $Q^n$, we have $z^n + \tilde{z}^n = 2$, so $P^{n_k}(z^{n_k} < 1/n_k) \leq 1/n_k \to 0$ as $k \to \infty$, which contradicts the assumption that $(\tilde{P}^n) \triangleleft (P^n)$.

**(b) $\Leftrightarrow$ (b$'$).** This follows from the relation $Z^n = (2/z^n) - 1$, since $z^n + \tilde{z}^n = 2$ implies $\tilde{z}^n/z^n = 2/z^n - 1$.

**(b) $\Rightarrow$ (a).** Let $A^n \in \mathcal{F}^n$ and $P^n(A^n) \to 0$ as $n \to \infty$. We have

$$\tilde{P}^n(A^n) \leq \tilde{P}^n(z^n \leq \varepsilon) + E_{Q^n}(\tilde{z}^n I(A^n \cap \{z^n > \varepsilon\}))$$

$$\leq \tilde{P}^n(z^n \leq \varepsilon) + \frac{2}{\varepsilon} E_{Q^n}(z^n I(A^n)) = \tilde{P}^n(z^n \leq \varepsilon) + \frac{2}{\varepsilon} P^n(A^n).$$

Therefore,

$$\limsup_n \tilde{P}^n(A^n) \leq \limsup_n \tilde{P}^n(z^n \leq \varepsilon).$$

Since $\varepsilon > 0$ is arbitrary, by (b) the right-hand side tends to $0$, so $\tilde{P}^n(A^n) \to 0$, establishing contiguity.

**(c) $\Rightarrow$ (b).** For any $\varepsilon > 0$, $\delta \in (0, 1)$, and $\alpha \in (0, 1)$,

$$H(\alpha; P^n, \tilde{P}^n) = E_{Q^n}((z^n)^\alpha (\tilde{z}^n)^{1-\alpha})$$

$$\leq (2\varepsilon)^\alpha + 2 \cdot \tilde{P}^n(z^n < \varepsilon) + \left(\frac{2}{\delta}\right)^{1-\alpha} \cdot 2 \cdot \tilde{P}^n(z^n \geq \delta^{-1}).$$

Using tightness of $(Z^n \mid \tilde{P}^n)$ (which follows from the estimates), one can show that

$$\liminf_{\varepsilon \downarrow 0} \liminf_{n} \tilde{P}^n(z^n \geq \varepsilon) \geq \left(\frac{\delta}{2}\right)^\alpha \liminf_{n} H(\alpha; P^n, \tilde{P}^n) - \frac{2}{2^\alpha} \delta$$

for all $\alpha \in (0, 1)$, $\delta \in (0, 1)$. Letting $\alpha \downarrow 0$, using (c), and then $\delta \downarrow 0$, we obtain

$$\liminf_{\varepsilon \downarrow 0} \liminf_{n} \tilde{P}^n(z^n \geq \varepsilon) \geq 1,$$

which implies (b).

The remaining implications among (c), (d), (e) follow from monotonicity and convexity properties of the Hellinger integral $H(\alpha; P^n, \tilde{P}^n)$ as a function of $\alpha \in (0, 1)$.
