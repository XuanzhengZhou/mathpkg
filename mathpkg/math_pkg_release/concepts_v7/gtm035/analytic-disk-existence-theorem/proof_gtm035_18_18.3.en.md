---
role: proof
locale: en
of_concept: analytic-disk-existence-theorem
source_book: gtm035
source_chapter: "18"
source_section: "18.3"
---
# Proof of Existence of Analytic Disk with Boundary in Submanifold

**Theorem 18.3.** Let $\Sigma^{2n-1}$ be a smooth (class $C^2$) $(2n-1)$-dimensional hypersurface in an open set in $\mathbb{C}^n$, and fix $x^0 \in \Sigma^{2n-1}$. Let $U$ be a neighborhood of $x^0$ on $\Sigma^{2n-1}$. Then there exists an analytic disk $E$ whose boundary $\partial E$ lies in $U$.

**Proof.** By an affine change of complex coordinates, we arrange that $x^0 = 0$ and that the tangent space to $\Sigma^{2n-1}$ at $0$ is given by the equation $y_1 = 0$, where $z_j = x_j + iy_j$ for $j = 1, \dots, n$ are the real coordinates in $\mathbb{C}^n$. Then $\Sigma^{2n-1}$ can be described parametrically near $0$ by the equation

$$z_1 = x_1 + i h(x_1, \dots, x_n, y_2, \dots, y_n)$$

with $z_2 = x_2 + iy_2, \dots, z_n = x_n + iy_n$, where $h$ is a smooth real-valued function defined on $\mathbb{R}^{2n-1}$ in a neighborhood of $0$, vanishing at $0$ of order $\geq 2$. (The higher-order vanishing follows because the tangent space at $0$ is $y_1 = 0$.)

**Step 1: Function space and operators.** Let $\Gamma$ denote the unit circle $|\zeta| = 1$ in $\mathbb{C}$. Define $H_1$ as the space of real-valued functions $u$ on $\Gamma$ whose Fourier series

$$u(\theta) = a_0 + \sum_{n=1}^\infty a_n \cos n\theta + b_n \sin n\theta$$

satisfies $\sum_{n=1}^\infty n^2(a_n^2 + b_n^2) < \infty$ (so that $\dot{u} \in L^2(\Gamma)$). Normed with

$$\|u\|_1 = \sqrt{\int_\Gamma |u|^2 d\theta} + \sqrt{\int_\Gamma |\dot{u}|^2 d\theta},$$

$H_1$ is a Banach space.

Define the **harmonic conjugate operator** $T: H_1 \to H_1$ (the operator of "passing to the conjugate function") by

$$T u = \sum_{n=1}^\infty a_n \sin n\theta - b_n \cos n\theta.$$

The key properties are:
- If $u, v \in H_1$, then $u + iv$ is a boundary function of an analytic function on $|\zeta| < 1$ if and only if $u = -Tv$.
- $T$ is a bounded linear operator: $\|T u\|_1 \leq \|u\|_1$.

**Step 2: Setup of the functional equation.** Since $h$ vanishes at $0$ to order $\geq 2$, a point near $0$ on $\Sigma^{2n-1}$ is described by parameters $(x_1, \dots, x_n, y_2, \dots, y_n)$. We group them as $x_1 \in \mathbb{R}$ and $w = (w_2, \dots, w_n)$ with $w_j = x_j + iy_j$. The hypersurface equation becomes

$$z_1 = x_1 + i h(x_1, w), \quad (z_2, \dots, z_n) = w.$$

Now let $w_2, \dots, w_n$ be smooth boundary functions on $\Gamma$ (i.e., each is the restriction to $\Gamma$ of a function analytic in $|\zeta| < 1$ and smooth up to the boundary). Write $w = (w_2, \dots, w_n)$ as a map $\Gamma \to \mathbb{C}^{n-1}$.

For a real-valued function $x \in H_1$, define the operator

$$A_w x = -T\{h(x, w)\},$$

where $h(x, w)$ means the composition $h(x(\zeta), w(\zeta))$ for $\zeta \in \Gamma$. Then $A_w$ maps $H_1$ into $H_1$ (since $T$ maps $H_1$ into $H_1$).

**Step 3: Contraction estimates.** For a fixed $M > 0$, let $B_M = \{x \in H_1 : \|x\|_1 \leq M\}$. We claim that for sufficiently small $M$ and sufficiently small $\|w\|_1$, the operator $A = A_w$ satisfies:

1. $A(B_M) \subseteq B_M$,
2. $\|A x - A y\|_1 \leq \alpha \|x - y\|_1$ for all $x, y \in B_M$, with $0 < \alpha < 1$.

These estimates rely on the following facts (Exercises 18.2 and 18.3) about a smooth function $h$ on $\mathbb{R}^N$ vanishing at $0$ of order $\geq 2$:

- **(Exercise 18.2)** There exists a constant $K$ depending only on $h$ such that for every map $x: \Gamma \to \mathbb{R}^N$ with $\|x\|_\infty \leq 1$:

  $$\|h(x)\|_1 \leq K (\|x\|_1)^2.$$

- **(Exercise 18.3)** There exists a constant $K$ depending only on $h$ such that for maps $x, y: \Gamma \to \mathbb{R}^N$ with $\|x\|_\infty \leq 1$ and $\|y\|_\infty \leq 1$:

  $$\|h(x) - h(y)\|_1 \leq K \|x - y\|_1 (\|x\|_1 + \|y\|_1).$$

Applying these to $h(x, w)$ (viewed as a function on $\mathbb{R}^{2n-1}$) and assuming $\|w\|_1 < M$, we obtain for $x \in B_M$ with small $M$ (so that $\|(x, w)\|_\infty \leq 1$):

$$\|A x\|_1 = \|T\{h(x, w)\}\|_1 \leq \|h(x, w)\|_1 \leq K (\|(x, w)\|_1)^2 < K (\|x\|_1 + \|w\|_1)^2 < K(M + M)^2 = 4M^2 K.$$

Hence if $M < 1/(4K)$, then $\|A x\|_1 \leq M$, so $A(B_M) \subseteq B_M$.

Similarly, for $x, y \in B_M$:

$$\|A x - A y\|_1 = \|T\{h(y, w) - h(x, w)\}\|_1 \leq \|h(y, w) - h(x, w)\|_1$$
$$\leq K \|(x, w) - (y, w)\|_1 (\|(x, w)\|_1 + \|(y, w)\|_1)$$
$$\leq K \|x - y\|_1 (\|x\|_1 + \|y\|_1 + 2\|w\|_1) \leq 4MK \|x - y\|_1.$$

Set $\alpha = 4MK$. By choosing $M < 1/(4K)$, we obtain $\alpha < 1$, so $A$ is a contraction on $B_M$.

(Note: By the elementary estimate $\|x\|_\infty \leq C\|x\|_1$, the condition $\|x\|_\infty \leq 1$ for all $x \in B_M$ can indeed be satisfied when $M$ is sufficiently small.)

**Step 4: Fixed point and the analytic disk.** By the Banach contraction mapping principle (Lemma 18.5, Lemma 18.6), the contraction $A = A_w$ has a unique fixed point $x^* \in B_M$, i.e.,

$$x^* = -T\{h(x^*, w)\}.$$

Equivalently, $x^* + T\{h(x^*, w)\} = 0$, or

$$x^* = -T\{h(x^*, w)\} \quad \text{on } \Gamma.$$

Now consider the boundary function $x^* + i h(x^*, w)$ on $\Gamma$. By property (2) of the operator $T$, the function

$$x^*(\zeta) + i h(x^*(\zeta), w(\zeta))$$

is the boundary function of an analytic function on $|\zeta| < 1$ if and only if $x^* = -T\{h(x^*, w)\}$. But this is precisely the fixed point equation.

Therefore, there exists an analytic function $\psi(\zeta)$ on $|\zeta| \leq 1$ such that on $|\zeta| = 1$:

$$\psi(\zeta) = x^*(\zeta) + i h(x^*(\zeta), w(\zeta)).$$

Then the map $\Phi: |\zeta| \leq 1 \to \mathbb{C}^n$ defined by

$$z_1 = \psi(\zeta), \quad (z_2, \dots, z_n) = w(\zeta)$$

gives an analytic disk $E$ in $\mathbb{C}^n$. Its boundary $\partial E = \Phi(|\zeta| = 1)$ lies in the hypersurface $\Sigma^{2n-1}$ because

$$(z_1, z_2, \dots, z_n) = (\psi(\zeta), w(\zeta))$$
$$= (x^*(\zeta) + i h(x^*(\zeta), w(\zeta)), w(\zeta))$$

which by the parametric description of $\Sigma^{2n-1}$ is a point on the hypersurface. Moreover, by choosing $w$ sufficiently small (so that $\|w\|_1 < M$), the boundary $\partial E$ lies in the prescribed neighborhood $U$ of $x^0$.

To ensure the disk is non-degenerate (not a point), one selects $w_2$ to be a schlicht (one-to-one) analytic function (Lemma 18.4 ensures the resulting disk is embedded). ∎
