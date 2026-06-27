---
role: proof
locale: en
of_concept: vector-lattice-identities
source_book: gtm003
source_chapter: "V"
source_section: "1"
---

\textbf{Identity (3):} This follows from the general lattice identity relating sum, supremum, and infimum.

\textbf{Decomposition $x = x^+ - x^-$:} To show uniqueness, suppose $x = y - z$ with $y, z \geq 0$ and $y \perp z$. Note that $x = y - z$ implies $y \geq x$, hence $y \geq x^+$, and therefore $z \geq x^-$. It follows that $(y - x^+) \perp (z - x^-)$. Since $y - x^+ = z - x^-$, this implies $y = x^+$ and $z = x^-$, as $0$ is the only element of $E$ disjoint from itself.

\textbf{Scaling (4):} If $\lambda \geq 0$, then from axiom $(LO)_2$ we obtain $(\lambda x)^+ = \lambda x^+$ and $(\lambda x)^- = \lambda x^-$. If $\lambda < 0$, then $(\lambda x)^+ = (-\lambda(-x))^+ = |\lambda| x^-$ and $(\lambda x)^- = |\lambda| x^+$.

\textbf{Triangle inequality (5):} From $\pm x \leq |x|$ and $\pm y \leq |y|$, we obtain $|x + y| = \sup(x + y, -x - y) \leq |x| + |y|$.

\textbf{Inequality (6):} From $x = y + (x - y)$ we obtain $x \leq y^+ + |x - y|$. Since the right-hand side is $\geq 0$, we have $x^+ \leq y^+ + |x - y|$, hence $x^+ - y^+ \leq |x - y|$. Interchanging $x$ and $y$ yields $y^+ - x^+ \leq |x - y|$, and together these give $|x^+ - y^+| \leq |x - y|$.

\textbf{Riesz Decomposition (D):} The inclusion $[0, x] + [0, y] \subset [0, x + y]$ is clear whenever $x, y \geq 0$. Conversely, let $z \in [0, x + y]$ and define $u = \inf(z, x)$, $v = z - u$. We must show $v \in [0, y]$. Using the identity $\inf(z, x) = z + x - \sup(z, x)$ and (3), one verifies that $0 \leq v \leq y$. Hence $z = u + v$ with $u \in [0, x]$ and $v \in [0, y]$, establishing (D).
