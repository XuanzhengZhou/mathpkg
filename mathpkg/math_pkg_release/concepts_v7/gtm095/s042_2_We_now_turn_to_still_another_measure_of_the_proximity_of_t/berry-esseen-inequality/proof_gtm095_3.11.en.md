---
role: proof
locale: en
of_concept: berry-esseen-inequality
source_book: gtm095
source_chapter: "3"
source_section: "11.1"
---

# Proof of the Berry–Esseen inequality

**Theorem (Berry–Esseen).** Let $\xi_1, \xi_2, \ldots$ be independent identically distributed random variables with $\mathbb{E}\xi_k = 0$, $\mathbb{V}\text{ar}\,\xi_k = \sigma^2 > 0$, and $\mathbb{E}|\xi_1|^3 < \infty$. Set

$$S_n = \frac{\xi_1 + \cdots + \xi_n}{\sigma\sqrt{n}}, \quad F_n(x) = \mathbb{P}(S_n \leq x).$$

Then there exists an absolute constant $C$ such that

$$\sup_x |F_n(x) - \Phi(x)| \leq \frac{C \mathbb{E}|\xi_1|^3}{\sigma^3 \sqrt{n}},$$

where $\Phi(x)$ is the standard normal distribution function. (The optimal constant satisfies $0.4097 < C < 0.469$.)

**Outline of the proof.**

Assume without loss of generality that $\sigma^2 = 1$ and set $\beta_3 = \mathbb{E}|\xi_1|^3$. Let $f(t) = \mathbb{E}e^{it\xi_1}$ be the characteristic function of $\xi_1$, and $f_n(t) = [f(t/\sqrt{n})]^n$ the characteristic function of $S_n$. Let $\varphi(t) = e^{-t^2/2}$ be the characteristic function of $\mathcal{N}(0,1)$.

The proof is based on the smoothing inequality (Esseen's lemma):

$$\sup_x |F_n(x) - \Phi(x)| \leq \frac{1}{\pi} \int_{-T}^{T} \left| \frac{f_n(t) - \varphi(t)}{t} \right| dt + \frac{24}{\pi T}, \tag{3}$$

where $T$ can be chosen arbitrarily. Set $T = \sqrt{n}/(5\beta_3)$.

The key step is to establish the estimate

$$|f_n(t) - \varphi(t)| \leq \frac{7}{6} \frac{\beta_3}{\sqrt{n}} |t|^3 e^{-t^2/4}, \quad |t| \leq T. \tag{4}$$

**Proof of (4).** By Taylor expansion of $f(t)$ (formula (18) in Sect. 2, Chap. 2 with $n = 3$):

$$f(t) = \mathbb{E}e^{it\xi_1} = 1 - \frac{t^2}{2} + \frac{(it)^3}{6} \left[\mathbb{E}\xi_1^3(\cos \theta_1 t\xi_1 + i \sin \theta_2 t\xi_1)\right],$$

where $|\theta_1| \leq 1$, $|\theta_2| \leq 1$. Consequently,

$$f\left(\frac{t}{\sqrt{n}}\right) = 1 - \frac{t^2}{2n} + \frac{(it)^3}{6n^{3/2}} \left[ \mathbb{E}\xi_1^3\left(\cos \theta_1 \frac{t}{\sqrt{n}}\xi_1 + i \sin \theta_2 \frac{t}{\sqrt{n}}\xi_1\right) \right].$$

For $|t| \leq T = \sqrt{n}/(5\beta_3)$, using the inequality $\beta_3 \geq \sigma^3 = 1$ (Lyapunov's inequality), one can show that $|f(t/\sqrt{n})| \geq 24/25$.

Considering the third derivative of $\log f(s)$:

$$(\log f)'''(s) = \frac{f'''(s) f^2(s) - 3 f''(s) f'(s) f(s) + 2(f'(s))^3}{f^3(s)}$$

$$= \frac{\mathbb{E}[(i\xi_1)^3 e^{i\xi_1 s}] f^2(s) - 3 \mathbb{E}[(i\xi_1)^2 e^{i\xi_1 s}] \mathbb{E}[(i\xi_1)e^{i\xi_1 s}] f(s) + 2 \mathbb{E}[(i\xi_1)e^{i\xi_1 s}]^3}{f^3(s)}.$$

Taking into account that $|f(t/\sqrt{n})| \geq 24/25$ for $|t| \leq T$ and $|f(s)| \leq 1$, we obtain

$$\left| (\log f)'''\!\left( \theta \frac{t}{\sqrt{n}} \right) \right| \leq \frac{\beta_3 + 3\beta_1 \beta_2 + 2\beta_1^3}{(24/25)^3} \leq 7\beta_3,$$

where $\beta_k = \mathbb{E}|\xi_1|^k$ ($\beta_1 \leq \beta_2^{1/2} \leq \beta_3^{1/3}$ by Lyapunov's inequality).

Using the Taylor expansion of $\log f(t/\sqrt{n})$ to third order and the estimate of the third derivative, together with the inequality $|e^z - 1| \leq |z| e^{|z|}$, one derives

$$\left| \left[ f\left( \frac{t}{\sqrt{n}} \right) \right]^n - e^{-t^2/2} \right| = \left| e^{n \log f(t/\sqrt{n})} - e^{-t^2/2} \right| \leq \frac{7}{6} \frac{\beta_3}{\sqrt{n}} |t|^3 e^{-t^2/4}$$

for $|t| \leq T$.

Finally, substituting (4) into the smoothing inequality (3) and performing the integration yields the Berry–Esseen bound with a universal constant $C$.
