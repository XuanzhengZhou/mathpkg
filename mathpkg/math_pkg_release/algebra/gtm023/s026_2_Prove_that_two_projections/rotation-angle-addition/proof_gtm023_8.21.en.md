---
role: proof
locale: en
of_concept: rotation-angle-addition
source_book: gtm023
source_chapter: "8"
source_section: "8.21"
---

For any $x \in E$, write $\varphi x = x \cos \Theta(\varphi) + j(x) \sin \Theta(\varphi)$ and $\psi x = x \cos \Theta(\psi) + j(x) \sin \Theta(\psi)$. Then
$$(\varphi \circ \psi) x = \varphi(\psi x) = \varphi(x \cos \Theta(\psi) + j(x) \sin \Theta(\psi))$$
$$= \varphi x \cos \Theta(\psi) + j(\varphi x) \sin \Theta(\psi)$$
since $j$ commutes with proper rotations. Substituting the expression for $\varphi x$ and using $j^2 = -1$ yields after collecting terms:
$$(\varphi \circ \psi) x = x \cdot \cos(\Theta(\varphi) + \Theta(\psi)) + j(x) \cdot \sin(\Theta(\varphi) + \Theta(\psi)).$$
Swapping $\varphi$ and $\psi$ gives the same result, so $\varphi \circ \psi = \psi \circ \varphi$ and $\Theta(\psi \circ \varphi) = \Theta(\varphi) + \Theta(\psi) \pmod{2\pi}$.
