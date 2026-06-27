---
role: proof
locale: en
of_concept: theorem-2-5
source_book: gtm011
source_chapter: "The Maximum Modulus Theorem"
source_section: "2. Schwarz's Lemma"
---

Proof. Since $f$ is one-one and onto there is an analytic function $g: D \rightarrow D$ such that $g(f(z)) = z$ for $|z| < 1$. Applying inequality (2.3) to both $f$ and $g$ gives $|f'(a)| \leq (1 - |a|^2)^{-1}$ and $|g'(0)| \leq 1 - |a|^2$ (since $g(0) = a$). But since $

3. Suppose $f: D \to \mathbb{C}$ satisfies $\text{Re} f(z) \geq 0$ for all $z$ in $D$ and suppose that $f$ is analytic and not constant.

(a) Show that $\text{Re} f(z) > 0$ for all $z$ in $D$.

(b) By using an appropriate Möbius transformation, apply Schwarz's Lemma to prove that if $f(0) = 1$ then

$$|f(z)| \leq \frac{1 + |z|}{1 - |z|}$$

for $|z| < 1$. What can be said if $f(0) \neq 1$?

(c) Show that if $f(0) = 1$, $f$ also satisfies

$$|f(z)| \geq \frac{1 - |z|}{1 + |z|}.$$

(Hint: Use part (a)).

4. Prove Carathéodory's Inequality whose statement is as follows: Let $f$ be analytic on $\bar{B}(0; R)$ and let $M(r) = \max\{|f(z)|: |z| = r\}$, $A(r) = \max\{\text{Re} f(z): |z| = r\}$; then for $0 < r < R$, if $A(r) \geq 0$,

$$M(r) \leq \frac{R + r}{R - r} [A(R) + |f(0)|]$$

(Hint: First consider the case where $f(0) = 0$ and examine the function $g(z) = f(Rz) [2A(R) + f(Rz)]^{-1}$ for $|z| < 1$.)

5. Let $f$ be analytic in $D = \{z: |z| < 1\}$ and suppose that $|f(z)| \leq M$ for all $z$ in $D$. (a) If $f(z_k) = 0$ for $1 \leq k \leq n$ show that

$$|f(z)| \leq M \prod_{k=1}^{n} \frac{|z - z_k|}{|1 - \bar{z}_k
