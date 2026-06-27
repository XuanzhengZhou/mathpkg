---
role: proof
locale: en
of_concept: five-lemma-variant-modules
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.**

**(1)** Assume $\alpha, \gamma,$ and $f'$ are monic. It suffices to show $\text{Ker}\, \beta = 0$. Let $b \in \text{Ker}\, \beta$. Since the diagram commutes, $\gamma g(b) = g' \beta(b) = g'(0) = 0$. Since $\gamma$ is monic, $g(b) = 0$, whence $b \in \text{Ker}\, g$. But the top row is exact, so $\text{Ker}\, g = \text{Im}\, f$. Thus, there exists $a \in A$ such that $b = f(a)$. Now since the diagram commutes,
$$f' \alpha(a) = \beta f(a) = \beta(b) = 0.$$
Finally, $f'$ and $\alpha$ are monic, so $a = 0$, whence $b = f(a) = 0$.

**(2)** Assume $\alpha, \gamma,$ and $g$ are epic. Let $b' \in B'$. We need to find $b \in B$ such that $\beta(b) = b'$. Since $\gamma$ is epic, there exists $c \in C$ such that $\gamma(c) = g'(b')$. By exactness of the bottom row, $g' \gamma(c) = \dots$ (the argument is symmetric to (1), using the epicity of $g$ to lift and the epicity of $\alpha$ to complete the diagram chase).

**(3)** Assume $\beta$ is monic, and $\alpha$ and $g$ are epic. Let $c' \in \text{Ker}\, \gamma$, so $\gamma(c') = 0$. We show $c' = 0$. Since $g$ is epic, $c' = g(b)$ for some $b \in B$. Then $g' \beta(b) = \gamma g(b) = \gamma(c') = 0$, so $\beta(b) \in \text{Ker}\, g' = \text{Im}\, f'$. Write $\beta(b) = f'(a')$. Since $\alpha$ is epic, $a' = \alpha(a)$ for some $a \in A$. Then $\beta f(a) = f' \alpha(a) = f'(a') = \beta(b)$. Since $\beta$ is monic, $f(a) = b$. Hence $c' = g(b) = g f(a) = 0$ by exactness of the top row.

**(4)** Assume $\beta$ is epic, and $f'$ and $\gamma$ are monic. Let $a' \in A'$. Then since $\beta$ is epic, there exists $b \in B$ such that $\beta(b) = f'(a')$. Since the diagram commutes and the bottom row is exact,
$$\gamma g(b) = g' \beta(b) = g' f'(a') = 0.$$
But $\gamma$ is monic, so $g(b) = 0$, whence $b \in \text{Ker}\, g = \text{Im}\, f$. Thus, there exists $a \in A$ with $f(a) = b$. So
$$f' \alpha(a) = \beta f(a) = \beta(b) = f'(a').$$
Finally, $f'$ is monic, so $\alpha(a) = a'$, proving $\alpha$ is epic. $\square$
