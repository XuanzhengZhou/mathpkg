---
role: proof
locale: en
of_concept: subf-recursiveness
source_book: gtm037
source_chapter: "10"
source_section: "Elements of Logic"
---

We will indicate a simple procedure for obtaining $\text{Subf}_{\sigma}^{\alpha}\varphi$ which makes the effectiveness very clear. First, it is clearly an effective matter to take the first free occurrence of $\alpha$ in $\varphi$ (if any) and replace it by $\sigma$. Formally, for any $m, x, y \in \omega$ we define a function $f'$ by considering two cases:

**Case 1:** $m = g\alpha$ for some variable $\alpha$, $x = g^+\sigma$ for some term $\sigma$, $y = g^+\varphi$ for some formula $\varphi$, and $\alpha$ occurs freely in $\varphi$. Let $\psi$ be obtained from $\varphi$ by replacing the first free occurrence of $\alpha$ in $\varphi$ by $\sigma$, and set $f'(m, x, y) = g^+\psi$.

**Case 2:** Case 1 does not hold. Let $f'(m, x, y) = y$.

This function $f'$ is recursive, since the conditions in Case 1 are recursive and the operation described is effective. Then $\text{Subf}_{\sigma}^{\alpha}\varphi$ is obtained by iterating $f'$ at most the number of free occurrences of $\alpha$ in $\varphi$ times. Since iteration of a recursive function a recursive number of times yields a recursive function, $f$ is recursive.
