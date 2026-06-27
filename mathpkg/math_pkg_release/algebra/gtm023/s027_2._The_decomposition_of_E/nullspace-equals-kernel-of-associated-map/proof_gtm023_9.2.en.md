---
role: proof
locale: en
of_concept: nullspace-equals-kernel-of-associated-map
source_book: gtm023
source_chapter: "9"
source_section: "2. The decomposition of E"
---

Define the linear mapping $\varphi: E \rightarrow E^*$ by

$$\Phi(x, y) = \langle \varphi x, y \rangle \quad x, y \in E.$$

If $x_0 \in E_0$, then by definition $\Phi(x_0, y) = 0$ for all $y \in E$. Hence $\langle \varphi x_0, y \rangle = 0$ for all $y \in E$, which means $\varphi x_0 = 0$ in $E^*$. Thus $x_0 \in \ker \varphi$, showing $E_0 \subseteq \ker \varphi$.

Conversely, if $x \in \ker \varphi$, then $\varphi x = 0$, so $\langle \varphi x, y \rangle = 0$ for all $y \in E$. By definition of $\varphi$, this means $\Phi(x, y) = 0$ for all $y \in E$, hence $x \in E_0$. Thus $\ker \varphi \subseteq E_0$.

Therefore $E_0 = \ker \varphi$.

For the matrix claim, let $(x_v)_{v=1}^n$ be a basis of $E$. Then

$$\langle \varphi x_v, x_\mu \rangle = \Phi(x_v, x_\mu) = \alpha_{v\mu},$$

which shows that $(\alpha_{v\mu})$ is precisely the matrix of $\varphi$ with respect to the basis $(x_v)$ of $E$ and the dual basis of $E^*$. Hence $\operatorname{rank}(\Phi) = \dim E - \dim E_0 = \dim E - \dim \ker \varphi = \operatorname{rank}(\varphi) = \operatorname{rank}(\alpha_{v\mu})$.
