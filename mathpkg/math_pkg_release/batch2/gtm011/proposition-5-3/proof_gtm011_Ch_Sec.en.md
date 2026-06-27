---
role: proof
locale: en
of_concept: proposition-5-3
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. (a) implies (b): Let $\Delta$ be open in $\Omega$ and let $x \in f^{-1}(\Delta)$. If $\omega = f(x)$ then $\omega$ is in $\Delta$; by definition, there is an $\epsilon > 0$ with $B(\omega; \epsilon) \subset \Delta$. Since $f$ is continuous, part (b) of the preceding proposition gives a $\delta > 0$ with $B(x; \delta) \subset f^{-1}(B(\omega; \epsilon)) \subset f^{-1}(\Delta)$. Hence, $f^{-1}(\Delta)$ is open.

(b) implies (c): If $\Gamma \subset \Omega$ is closed then let $\Delta = \Omega - \Gamma$. By (b), $f^{-1}(\Delta) = X - f^{-1}(\Gamma)$ is open, so that $f^{-1}(\Gamma)$ is closed.

(c) implies (a): Suppose there is a point $x$ in $X$ at which $f$ is not continuous. Then there is an $\epsilon > 0$ and a sequence $\{x_n\}$ such that $\rho(f(x_n), f(x)) \geq \epsilon$ for every $n$ while $x = \lim x_n$. Let $\Gamma = \Omega - B(f(x); \epsilon)$; then $\Gamma$ is closed and each $x_n$ is in $f^{-1}(\Gamma)$. Since $(by(c)) f^{-1}(\Gamma)$ is closed we have $x \in f^{-1}(\Gamma)$. But this implies $\rho(f(x), f(x)) \geq \epsilon > 0$, a contradiction.

The following type of result is probably well understood by the reader and so the proof

(b) $d(x, A) = 0$ iff $x \in A^-$;
(c) $|d(x, A) - d(y, A)| \leq d(x, y)$ for all $x, y$ in $X$.

Proof. (a) If $A \subset B$ then it is clear from the definition that $d(x, B) \leq d(x, A)$. Hence, $d(x, A^-) \leq d(x, A)$. On the other hand, if $\epsilon > 0$ there is a point $y$ in $A^-$ such that $d(x, A^-) \geq d(x, y) - \epsilon/2$. Also, there is a point $a$ in $A$ with $d(y, a) < \epsilon/2$. But $|d(x, y) - d(x, a)| \leq d(y, a) < \epsilon/2$ by the triangle inequality. In particular, $d(x, y) > d(x, a) - \epsilon/2$. This gives, $d(x, A^-) \geq d(x, a) - \epsilon \geq d(x, A) - \epsilon$. Since $\epsilon$ was arbitrary $d(x, A^-) \geq d(x, A)$, so that (a) is proved.

(b) If $x \in A^-$ then $0 = d(x, A^-) = d(x, A)$. Now for any $x$ in $X$ there is a minimizing sequence $\{a_n\}$ in $A$ such that $d(x, A) = \lim d(x, a_n)$. So if $d(x, A) = 0$, $\lim d(x, a_n) = 0$; that is, $x = \lim a_n$ and so $x \in A^-$.

(c) For $a$ in $A$ $d(x, a) \leq d(x, y) + d(y, a)$. Hence, $d(x, A) = \inf \{d(x, a): a \in A\} \leq \inf \{d(x, y) + d(y, a): a \in A\} = d(x, y) + d(y, A)$. This gives $d(x, A

5.11 Intermediate Value Theorem. If $f: [a, b] \to \mathbb{R}$ is continuous and $f(a) \leq \xi \leq f(b)$ then there is a point $x$, $a \leq x \leq b$, with $f(x) = \xi$.
