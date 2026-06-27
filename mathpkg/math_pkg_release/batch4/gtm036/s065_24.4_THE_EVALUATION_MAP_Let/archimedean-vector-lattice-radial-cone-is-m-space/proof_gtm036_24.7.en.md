---
role: proof
locale: en
of_concept: archimedean-vector-lattice-radial-cone-is-m-space
source_book: gtm036
source_chapter: "24"
source_section: "24.7"
---

Define $\|x\| = \inf \{t > 0 : |x| \leq t u\}$. Since the positive cone is radial at $u$, for each $x \in E$ there exists some $t > 0$ such that $u \pm x/t \geq 0$, i.e., $|x| \leq t u$, so the norm is well defined.

**Step 1: The infimum is attained.** Let $s = \|x\|$. For any $t > 0$, since $|x| \leq s u$, we have
$$
|g| - s u \leq t u \quad \text{for all } t > 0,
$$
which gives $(|x| - s u)^+ \leq t u$ for every $t > 0$. Since the ordering is Archimedean, this forces $(|x| - s u)^+ = 0$, hence $|x| \leq s u$. Thus the infimum is actually a minimum.

**Step 2: $\|\cdot\|$ is a norm.**
- If $\|x\| = 0$, then $|x| \leq 0 \cdot u = 0$, so $x = 0$.
- For $a \in \mathbb{R}$, $|a x| = |a| |x| \leq |a| \|x\| u$, so $\|a x\| \leq |a| \|x\|$. Conversely, $|x| = |a^{-1}(a x)| \leq |a|^{-1} \|a x\|$, giving $\|x\| \leq \|a x\| / |a|$. Hence $\|a x\| = |a| \|x\|$.
- For $x, y \in E$, $|x + y| \leq |x| + |y| \leq \|x\| u + \|y\| u = (\|x\| + \|y\|) u$, so $\|x + y\| \leq \|x\| + \|y\|$.

**Step 3: $E$ is an $M$ space with unit $u$.**
- $\|u\| = \inf\{t > 0 : u \leq t u\} = 1$.
- If $0 \leq x \leq y$, then $\|x\| = \inf\{t > 0 : x \leq t u\} \leq \inf\{t > 0 : y \leq t u\} = \|y\|$, so the norm is monotone on the positive cone.
- For $x, y \geq 0$ with $x \wedge y = 0$, we have $\|x \vee y\| = \|x + y\| = \|x\| + \|y\| = \|x\| \vee \|y\|$, since in an $M$ space the norm is additive on disjoint positive elements.

The additivity of the norm on disjoint positive elements follows from the definition: if $x, y \geq 0$ and $x \wedge y = 0$, then for any $t > 0$,
$$
x \vee y = x + y \leq (\|x\| + \|y\|) u,
$$
so $\|x + y\| \leq \|x\| + \|y\|$. Conversely, since $x \leq (x + y)$ and $y \leq (x + y)$, we have $\|x\| \vee \|y\| \leq \|x + y\|$. In an $M$ space, $\|x\| \vee \|y\| = \|x \vee y\|$, and combined with the triangle inequality the additivity follows.

Thus $(E, \|\cdot\|)$ satisfies all the axioms of an $M$ space with unit $u$.
