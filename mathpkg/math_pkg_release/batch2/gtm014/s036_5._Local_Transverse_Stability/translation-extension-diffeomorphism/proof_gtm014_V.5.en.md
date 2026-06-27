---
role: proof
locale: en
of_concept: translation-extension-diffeomorphism
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Choose a smooth function $u: \mathbb{R}^n \to \mathbb{R}$ which is $1$ on a ball centered at $0$ containing $B$ and which has compact support. Let $\rho(x) = u(tx)$ for some $t$. Choose $t$ so small that $|d\rho| = t|du| < 1/|a|$. By also demanding that $t \leq 1$ we see that $\rho \equiv 1$ on $B$.

Now consider $\eta(x) = x + \rho(x)a$ and observe that $\eta = T_a$ on $B$ and $\eta = \mathrm{id}_{\mathbb{R}^n}$ off of some compact set. By applying Lemma 5.2 it is enough to show that $\eta$ is an immersion in order to show that $\eta$ is a diffeomorphism. Now
$$(d\eta)_x = I_n + a \begin{pmatrix} \frac{\partial \rho}{\partial x_1}, \ldots, \frac{\partial \rho}{\partial x_n} \end{pmatrix}$$
where $a = (a_1, \ldots, a_n)$. Thus for $v \neq 0$,
$$|(d\eta)_x(v)| \geq |v| - |a| \cdot |d\rho| \cdot |v| > 0$$
by the choice of $\rho$. Hence $\eta$ is an immersion.
