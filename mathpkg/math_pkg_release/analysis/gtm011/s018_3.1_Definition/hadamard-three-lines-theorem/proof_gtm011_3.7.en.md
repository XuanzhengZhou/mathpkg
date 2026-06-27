---
role: proof
locale: en
of_concept: hadamard-three-lines-theorem
source_book: gtm011
source_chapter: "3"
source_section: "3.7"
---

To say that $\log M(x)$ is convex means that for $a \leq x < u < y \leq b$,

$$(y-x) \log M(u) \leq (y-u) \log M(x) + (u-x) \log M(y).$$

Taking the exponential of both sides, this is equivalent to

$$M(u)^{y-x} \leq M(x)^{y-u} M(y)^{u-x}.$$

To prove the theorem, it suffices to show that for $a < u < b$,

$$M(u) \leq M(a)^{(b-u)/(b-a)} M(b)^{(u-a)/(b-a)}.$$

Recall that for a constant $A > 0$, $A^z = \exp(z \log A)$ is an entire function of $z$ with no zeros. Define

$$g(z) = M(a)^{(b-z)/(b-a)} M(b)^{(z-a)/(b-a)}.$$

Then $g$ is entire, never vanishes, and because $|A^z| = A^{\operatorname{Re} z}$, for $z = x + iy$ we have

$$|g(z)| = M(a)^{(b-x)/(b-a)} M(b)^{(x-a)/(b-a)}.$$

(It is assumed here that $M(a)$ and $M(b) \neq 0$. However, if either $M(a)$ or $M(b)$ is zero then $f \equiv 0$.)

Since the right-hand side is continuous for $x$ in $[a, b]$ and never vanishes, $|g|^{-1}$ must be bounded on $G^-$. Also, $|g(a+iy)| = M(a)$ and $|g(b+iy)| = M(b)$, so that $|f(z)/g(z)| \leq 1$ for $z$ on $\partial G$. Hence $f/g$ satisfies the hypothesis of Lemma 3.10. Thus

$$|f(z)| \leq |g(z)|, \quad z \in G.$$

For $a < u < b$, taking the supremum over $y$ at $x = u$ gives

$$M(u) \leq M(a)^{(b-u)/(b-a)} M(b)^{(u-a)/(b-a)},$$

which is the desired conclusion.
