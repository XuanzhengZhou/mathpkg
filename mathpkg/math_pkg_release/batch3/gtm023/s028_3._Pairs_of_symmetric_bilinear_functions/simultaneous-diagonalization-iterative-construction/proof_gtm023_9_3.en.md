---
role: proof
locale: en
of_concept: simultaneous-diagonalization-iterative-construction
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

**Step 1:** Apply the construction of Section 9.14 to $E$. This yields a vector $e_1$ with $|e_1| = 1$ and a number $\lambda_1 = \Phi(e_1)/\Psi(e_1)$ such that
$$\Phi(e_1, y) = \lambda_1 \Psi(e_1, y) \quad \text{for all } y \in E,$$
and $\Psi(e_1, e_1) \neq 0$.

**Step 2:** Define $E_1 = \{z \in E : \Psi(e_1, z) = 0\}$. By the non-degeneracy lemma, $\dim E_1 = n-1$ and $\Psi|_{E_1}$ is non-degenerate. Apply the construction of Section 9.14 to $E_1$, obtaining $e_2 \in E_1$ and $\lambda_2 = \Phi(e_2)/\Psi(e_2)$ such that
$$\Phi(e_2, z) = \lambda_2 \Psi(e_2, z) \quad \text{for all } z \in E_1.$$

**Step 3 (Extension to $E$):** We claim that $\Phi(e_2, y) = \lambda_2 \Psi(e_2, y)$ for all $y \in E$. Decompose $y = \xi e_1 + z$ with $z \in E_1$. Then
$$\Phi(e_2, y) = \xi \Phi(e_2, e_1) + \Phi(e_2, z).$$
By the property of $e_1$, $\Phi(e_2, e_1) = \Phi(e_1, e_2) = \lambda_1 \Psi(e_1, e_2) = \lambda_1 \Psi(e_2, e_1) = 0$ since $e_2 \in E_1$. Also $\Psi(e_2, e_1) = 0$ by definition of $E_1$. Hence
$$\Phi(e_2, y) = \Phi(e_2, z) = \lambda_2 \Psi(e_2, z) = \lambda_2 [\xi \Psi(e_2, e_1) + \Psi(e_2, z)] = \lambda_2 \Psi(e_2, y).$$

**Step 4 (Iteration):** Continue this process. After $n$ steps we obtain vectors $e_1, \ldots, e_n$ satisfying:
$$\Phi(e_v, y) = \lambda_v \Psi(e_v, y) \quad \text{for all } y \in E,$$
$$\Psi(e_v, e_v) \neq 0, \quad \Psi(e_v, e_\mu) = 0 \quad (v \neq \mu).$$
The last orthogonality holds because each $e_v$ lies in the intersection of the $\Psi$-orthogonal complements of the previously constructed vectors.

**Step 5 (Normalization):** Rearrange the vectors so that $\Psi(e_v, e_v) > 0$ for $v = 1, \ldots, s$ and $\Psi(e_v, e_v) < 0$ for $v = s+1, \ldots, n$, where $s$ is the signature of $\Psi$. Replace each $e_v$ by $e_v / \sqrt{|\Psi(e_v, e_v)|}$ to obtain
$$\Psi(e_v, e_\mu) = \varepsilon_v \delta_{v\mu}, \quad \varepsilon_v = \pm 1.$$
Substituting $y = e_\mu$ into $\Phi(e_v, y) = \lambda_v \Psi(e_v, y)$ yields $\Phi(e_v, e_\mu) = \lambda_v \varepsilon_v \delta_{v\mu}$. Thus both forms are diagonal.
