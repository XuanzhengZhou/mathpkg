---
role: proof
locale: en
of_concept: hadamard-boundedness-lemma
source_book: gtm011
source_chapter: "3"
source_section: "3.10"
---

For each $\epsilon > 0$ define

$$g_\epsilon(z) = \frac{1}{1 + \epsilon(z-a)}$$

for each $z$ in $G^-$. This function is analytic in $G$ and continuous on $G^-$. Moreover, for $z = x + iy$,

$$|g_\epsilon(z)| = \frac{1}{\sqrt{(1 + \epsilon(x-a))^2 + \epsilon^2 y^2}} \leq 1$$

since $x \geq a$ on $G^-$, so $1 + \epsilon(x-a) \geq 1$.

Now consider $h_\epsilon(z) = f(z) g_\epsilon(z)$. On $\partial G$, we have $|f(z)| \leq 1$ by hypothesis, and $|g_\epsilon(z)| \leq 1$, so $|h_\epsilon(z)| \leq 1$ on $\partial G$. Also, $|g_\epsilon(z)| \to 0$ as $|y| \to \infty$ uniformly in $x \in [a, b]$, and $|f(z)| < B$ for all $z \in G$. Hence $|h_\epsilon(z)| \to 0$ as $|y| \to \infty$.

For any $Y > 0$, consider the truncated strip

$$G_Y = \{z = x + iy: a < x < b, -Y < y < Y\}.$$

By the Maximum Modulus Principle applied to $h_\epsilon$ on $G_Y$,
$|h_\epsilon(z)| \leq \max\{1, \sup_{|y|=Y} |h_\epsilon(x+iy)|\}$
for all $z \in G_Y$. Letting $Y \to \infty$, the supremum over $|y|=Y$ tends to 0, so we obtain $|h_\epsilon(z)| \leq 1$ for all $z \in G$.

Therefore $|f(z) g_\epsilon(z)| \leq 1$ for all $z \in G$. Fixing $z \in G$ and letting $\epsilon \to 0$, we have $g_\epsilon(z) \to 1$, which yields $|f(z)| \leq 1$ for all $z \in G$.
