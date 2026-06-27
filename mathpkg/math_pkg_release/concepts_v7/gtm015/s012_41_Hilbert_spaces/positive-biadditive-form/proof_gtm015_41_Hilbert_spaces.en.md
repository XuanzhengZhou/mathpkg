---
role: proof
locale: en
of_concept: positive-biadditive-form
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Positive bi-additive form

Let $E$ be an additively written group and $f \colon E \times E \to \mathbb{K}$ be a function satisfying conditions (i)–(iii).

Define $N(x) = f(x, x)^{1/2}$ for all $x \in E$.  By (i), $N(x) \geq 0$ is well defined.  We verify the parallelogram law for $N$.

For any $x, y \in E$, expand $f(x+y, x+y)$ using additivity in each argument:

$$f(x+y, x+y) = f(x, x+y) + f(y, x+y) = f(x,x) + f(x,y) + f(y,x) + f(y,y).$$

Similarly,

$$f(x-y, x-y) = f(x, x-y) + f(-y, x-y) = f(x,x) + f(x,-y) + f(-y,x) + f(-y,-y).$$

From the additivity conditions (ii)–(iii) one obtains $f(0,z) = 0$ and $f(z,0) = 0$ for all $z \in E$ (take $x = y = \theta$ in (ii) or (iii)).  Consequently $f(-y, z) = -f(y, z)$ and $f(z, -y) = -f(z, y)$.  Applying this,

$$f(x-y, x-y) = f(x,x) - f(x,y) - f(y,x) + f(y,y).$$

Adding the two expansions,

$$
\begin{aligned}
f(x+y, x+y) + f(x-y, x-y) &= \bigl[f(x,x) + f(x,y) + f(y,x) + f(y,y)\bigr] \\
&\quad + \bigl[f(x,x) - f(x,y) - f(y,x) + f(y,y)\bigr] \\[4pt]
&= 2f(x,x) + 2f(y,y).
\end{aligned}
$$

Substituting $N(x)^2 = f(x,x)$ and $N(y)^2 = f(y,y)$ yields

$$N(x+y)^2 + N(x-y)^2 = 2N(x)^2 + 2N(y)^2,$$

which is precisely the parallelogram law.  $\square$
