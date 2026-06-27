---
role: proof
locale: en
of_concept: lemma-4-3
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Define $\mathcal{F}$ by letting

$$\mathcal{F} = \{f \in H(G) : f \text{ is one-one}, f(a) = 0, f'(a) > 0, f(G) \subset D\}$$

Since $f(G) \subset D$, $\sup \{|f(z)| : z \in G\} \leq 1$ for $f$ in $\mathcal{F}$; by Montel’s Theorem $\mathcal{F}$ is normal if it is non-empty.

Since the Mobius transformation $T\zeta = \frac{\zeta - \omega}{1 - \bar{\omega}\zeta}$ maps $D$ onto $D$, $h(G) \subset D$.

Define $g: G \to \mathbb{C}$ by

$$g(z) = \frac{|h'(a)|}{h'(a)} \frac{h(z) - h(a)}{1 - \bar{h}(a)h(z)}$$

Then $g(G) \subset D$, $g(a) = 0$, and $g$ is one-one (why?). Also

$$g'(a) = \frac{|h'(a)|}{h'(a)} \cdot \frac{h'(a)[1 - |h(a)|^2]}{[1 - |h(a)|^2]^2}$$

$$= \frac{|h'(a)|}{1 - |h(a)|^2}$$

But $|h(a)|^2 = |-\omega| = |\omega|$ and differentiating (4.6) gives (since $f(a) = 0$) that

$$2h(a)h'(a) = f'(a)(1 - |\omega|^2).$$

Therefore

$$g'(a) = \frac{f'(a)(1 - |\omega|^2)}{2\sqrt{|\omega|}} \cdot \frac{1}{1 - |\omega|}$$

$$= f'(a)\left(\frac{1 + |\omega|}{2\sqrt{|\omega|}}\right)$$

$$> f'(a)$$

This gives that $g$ is in $\mathcal{F}$ and contradicts the choice of $f$. Thus it must be that $f(G) = D$.

Now to establish (4.4) and (4.5). Since $G \neq \mathbb{C}$, let $b \in \mathbb{C} - G$ and let $g$ be a function analytic on $G$ such that $[g(z)]^2 = z - b$. If $z_1$ and $z_2$ are points in $G$ and $g(z_1) = \pm g(z_2)$ then it follows that

Suppose $\{f_n\}$ is a sequence in $\mathcal{F}$ and $f_n \rightarrow f$ in $H(G)$. Clearly $f(a) = 0$ and since $f_n'(a) \rightarrow f''(a)$ it follows that

4.9 $f''(a) \geq 0$.

Let $z_1$ be an arbitrary element of $G$ and put $\zeta = f(z_1)$; let $\zeta_n = f_n(z_1)$. Let $z_2 \in G$, $z_2 \neq z_1$ and let $K$ be a closed disk centered at $z_2$ such that $z_1 \notin K$. Then $f_n(z) - \zeta_n$ never vanishes on $K$ since $f_n$ is one-one. But $f_n(z) - \zeta_n \rightarrow f(z) - \zeta$ uniformly on $K$, so Hurwitz’s Theorem gives that $f(z) - \zeta$ never vanishes on $K$ or $f(z) \equiv \zeta$. If $f(z) \equiv \zeta$ on $K$ then $f$ is the constant function $\zeta$ throughout $G$; since $f(a) = 0$ we have that $f(z) \equiv 0$. Otherwise we get that $f(z_2) \neq f(z_1)$ for $z_2 \neq z_1$; that is, $f$ is one-one. But if $f$ is one-one then $f'$ can never vanish; so (4.9) implies that $f'(a) > 0$ and $f$ is in $\mathcal{F}$. This proves (4.5) and the proof of the lemma is complete.
