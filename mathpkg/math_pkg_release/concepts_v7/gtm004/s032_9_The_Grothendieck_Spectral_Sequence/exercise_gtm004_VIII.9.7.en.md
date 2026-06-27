---
role: exercise
locale: en
chapter: "VIII"
section: "9"
exercise_number: 7
---

# Exercise 7

Let $\varphi, \psi : B \rightarrow \tilde{B}$ be morphisms of double complexes. We say that $\varphi, \psi$ are homotopic, and write $\varphi \simeq \psi$, if there exist families of morphisms

$$\Sigma'_{r,s} : B_{r,s} \rightarrow \tilde{B}_{r+1,s}, \quad \Sigma''_{r,s} : B_{r,s} \rightarrow \tilde{B}_{r,s+1}$$

such that

$$\varphi - \psi = \partial' \Sigma' + \Sigma' \partial' + \partial'' \Sigma'' + \Sigma'' \partial''$$

and

$$\Sigma'' \partial' + \partial' \Sigma'' = \Sigma' \partial'' + \partial'' \Sigma'.$$

Show that if $\varphi \simeq \psi$, then $\operatorname{Tot} \varphi \simeq \operatorname{Tot} \psi$ as morphisms of chain complexes.
