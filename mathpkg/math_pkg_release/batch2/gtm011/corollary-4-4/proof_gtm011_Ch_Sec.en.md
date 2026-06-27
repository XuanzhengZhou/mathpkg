---
role: proof
locale: en
of_concept: corollary-4-4
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Define $F: G \to \mathbb{C}$ by $F(z) = f(z) \exp (-\epsilon z^a)$ where $\epsilon > 0$ is arbitrary. If $x > 0$ and $\delta$ is chosen with $0 < \delta < \epsilon$ then there is a constant $P$ with

$$|F(x)| \leq P \exp [(\delta - \epsilon)x^a].$$

But then $|F(x)| \to 0$ as $x \to \infty$ in $\mathbb{R}$; so $M_1 = \sup \{ |F(x)| : 0 < x < \infty \} < \infty$. Define $M_2 = \max \{ M_1, M \}$ and

$$H_+ = \{ z \in G : 0 < \arg z < \pi/2a \},$$

$$H_- = \{ z \in G : 0 > \arg z > -\pi/2a \};$$

then $\limsup |f(z)| \leq M_2$ for all $z$ in $\partial H_+$ and $\partial H_-$. Using hypothesis (4.5), Corollary 4.2 gives $|F(z)| \leq M_2$ for all $z$ in $H_+$ and $H_-$ hence, $|F(z)| \leq M_2$ for all $z$ in $G$.

We claim that $M_2 = M$. In fact, if $M_2 = M_1 >

2. In Theorem 4.1 suppose there are bounded analytic functions $\varphi_1, \varphi_2, \ldots, \varphi_n$ on $G$ that never vanish and $\partial_\infty G = A \cup B_1 \cup \ldots \cup B_n$ such that condition (a) is satisfied and condition (b) is also satisfied for each $\varphi_k$ and $B_k$. Prove that $|f(z)| \leq M$ for all $z$ in $G$.

3. Let $G = \{z: |\text{Im } z| < \frac{1}{2}\pi\}$ and suppose $f: G \to \mathbb{C}$ is analytic and lim sup $|f(z)| \leq M$ for $w$ in $\partial G$. Also, suppose $A < \infty$ and $a < 1$ can be found such that

$$|f(z)| < \exp [A \exp (a |\text{Re } z|)]$$

for all $z$ in $G$. Show that $|f(z)| \leq M$ for all $z$ in $G$. Examine exp (exp $z$) to see that this is the best possible growth condition. Can we take $a = 1$ above?

4. Let $f: G \to \mathbb{C}$ be analytic and suppose $M$ is a constant such that lim sup $|f(z_n)| \leq M$ for each sequence $\{z_n\}$ in $G$ which converges to a point in $\partial_\infty G$. Show that $|f(z)| \leq M$. (See Exercise 1.8).

5. Let $f: G \to \mathbb{C}$ be analytic and suppose that $G$ is bounded. Fix $z_0$ in $\partial G$ and suppose that lim sup $|f(z)| \leq M$ for $w$ in $\partial G$, $w \neq z_0$. Show that if $\lim |z - z_0|^c |f(z)| = 0$ for every $\epsilon > 0$ then $|f(z)| \leq M$ for every $z$ in $\partial G$.

(Hint: If $a \notin G$, consider $\varphi(z) = (z
