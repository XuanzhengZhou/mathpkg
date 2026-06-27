---
role: proof
locale: en
of_concept: phragmen-lindelof-sub-exponential-growth
source_book: gtm011
source_chapter: "VI"
source_section: "§4"
---

Define $F: G \to \mathbb{C}$ by $F(z) = f(z) \exp(-\varepsilon z^a)$ where $\varepsilon > 0$ is arbitrary. If $x > 0$ and $\delta$ is chosen with $0 < \delta < \varepsilon$, then by hypothesis there is a constant $P$ such that
\[
|F(x)| \leq P \exp[(\delta - \varepsilon)x^a].
\]
Since $\delta - \varepsilon < 0$, we have $|F(x)| \to 0$ as $x \to \infty$ along $\mathbb{R}$. Hence
\[
M_1 = \sup\{ |F(x)| : 0 < x < \infty \} < \infty.
\]

Define $M_2 = \max\{M_1, M\}$ and set
\[
H_+ = \{ z \in G : 0 < \arg z < \pi/2a \}, \qquad
H_- = \{ z \in G : 0 > \arg z > -\pi/2a \}.
\]
Then $\limsup_{z \to w} |F(z)| \leq M_2$ for all $w \in \partial H_+$ and all $w \in \partial H_-$. Applying Corollary 4.2 to $F$ on each half-sector yields $|F(z)| \leq M_2$ for all $z \in H_+$ and $z \in H_-$, hence $|F(z)| \leq M_2$ for all $z \in G$.

We claim that $M_2 = M$. If $M_2 = M_1 > M$, then $M_1$ is attained at some point $x_0 > 0$ (since $|F(x)| \to 0$ as $x \to 0^+$ and as $x \to \infty$). But $x_0$ lies in the interior of $G$, and $|F|$ would then attain a local maximum at $x_0$, contradicting the Maximum Modulus Theorem unless $F$ is constant. Since $F$ is not constant (it decays to $0$), this is impossible. Therefore $M_2 = M$.

Consequently $|F(z)| \leq M$ for all $z \in G$, which gives
\[
|f(z)| \leq M \exp(\varepsilon \operatorname{Re}(z^a))
\]
for every $\varepsilon > 0$. Letting $\varepsilon \to 0$ yields $|f(z)| \leq M$ for all $z \in G$.
