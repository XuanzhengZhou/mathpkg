---
role: proof
locale: en
of_concept: algebraic-properties-of-limits
source_book: gtm012
source_chapter: "3"
source_section: "3. Sequences of real and complex numbers"
---

# Proof of Algebraic properties of limits of sequences (Proposition 3.1)

**Proposition 3.1.** Suppose $(z_n)_{n=1}^{\infty}$, $(w_n)_{n=1}^{\infty}$ are sequences in $\mathbb{C}$ and $z_n \to z$, $w_n \to w$, $c \in \mathbb{C}$. Then

(a) $z_n + w_n \to z + w$,

(b) $c z_n \to c z$,

(c) $\overline{z_n} \to \overline{z}$,

(d) $z_n w_n \to z w$,

(e) if $z \neq 0$, then there exists $M$ such that $z_n \neq 0$ for $n \geq M$, and $z_n^{-1} \to z^{-1}$.

**Proof.**

**(a)** Given $\varepsilon > 0$, choose $N$ such that $|z_n - z| < \varepsilon/2$ and $|w_n - w| < \varepsilon/2$ whenever $n \geq N$. Then for $n \geq N$,

$$|(z_n + w_n) - (z + w)| \leq |z_n - z| + |w_n - w| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

Thus $z_n + w_n \to z + w$.

**(b)** If $c = 0$, this is trivial. If $c \neq 0$, given $\varepsilon > 0$, choose $N$ such that $|z_n - z| < \varepsilon/|c|$ for $n \geq N$. Then

$$|c z_n - c z| = |c|\, |z_n - z| < |c| \cdot \frac{\varepsilon}{|c|} = \varepsilon.$$

Thus $c z_n \to c z$.

**(c)** $|\overline{z_n} - \overline{z}| = |\overline{z_n - z}| = |z_n - z| \to 0$, hence $\overline{z_n} \to \overline{z}$.

**(d)** First note that convergent sequences are bounded (see the definition of bounded sequence), so there exists $M$ such that $|z_n| \leq M$, $|w_n| \leq M$ for all $n$, and also $|z|, |w| \leq M$. Let $K = 1 + |w| + |z|$. Then for all sufficiently large $n$ (so that $|z_n| < |z| + 1$ and $|w_n| < |w| + 1$), we have $|z_n| \leq K$, and

$$|z_n w_n - z w| = |z_n(w_n - w) + (z_n - z)w| \leq |z_n|\,|w_n - w| + |z_n - z|\,|w| \leq K(|w_n - w| + |z_n - z|).$$

Since $w_n - w \to 0$ and $z_n - z \to 0$, it follows that $z_n w_n - z w \to 0$.

**(e)** Since $z \neq 0$, choose $M$ so large that $|z_n - z| \leq \frac{1}{2}|z|$ when $n \geq M$. Then for $n \geq M$,

$$|z_n| = |z_n| + \tfrac{1}{2}|z| - \tfrac{1}{2}|z| \geq |z_n| + |z - z_n| - \tfrac{1}{2}|z| \geq |z_n + (z - z_n)| - \tfrac{1}{2}|z| = |z| - \tfrac{1}{2}|z| = \tfrac{1}{2}|z|.$$

Therefore, $z_n \neq 0$ for $n \geq M$. Also for $n \geq M$,

$$|z_n^{-1} - z^{-1}| = |(z - z_n) z^{-1} z_n^{-1}| \leq |z - z_n| \cdot |z|^{-1} \cdot \big(\tfrac{1}{2}|z|\big)^{-1} = K|z - z_n|,$$

where $K = 2|z|^{-2}$. Since $z - z_n \to 0$, we have $z_n^{-1} - z^{-1} \to 0$. $\square$
