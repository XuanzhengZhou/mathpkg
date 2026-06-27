---
role: exercise
locale: en
chapter: "2"
section: "2.3"
exercise_number: "2a"
---

Let $X$ be a finite set on which $G$ acts, let $\rho$ be the corresponding permutation representation (1.2) and let $\chi$ be its character.

(a) The set $Gx$ of images under $G$ of an element $x \in X$ is called an orbit. Let $c$ be the number of distinct orbits. Show that $c$ is equal to the number of times that $\rho$ contains the unit representation $1$; deduce from this that $(\chi|1) = c$. In particular, if $G$ is transitive (i.e., if $c = 1$), $\rho$ can be decomposed into $1 \oplus \theta$ and $\theta$ does not contain the unit representation. If $\psi$ is the character of $\theta$, we have $\chi = 1 + \psi$ and $(\psi|1) = 0$.

**Solution.** For a permutation representation, $\chi(s) = \operatorname{Fix}(s) = |\{x \in X : s x = x\}|$, the number of fixed points of $s$ on $X$. By Burnside's lemma (Cauchy-Frobenius formula), the number of orbits is
$$c = \frac{1}{g} \sum_{s \in G} \operatorname{Fix}(s) = \frac{1}{g} \sum_{s \in G} \chi(s) = (\chi|1).$$

By Exercise 2.5, $(\chi|1)$ is precisely the multiplicity of the unit representation in $\rho$. Hence $c = (\chi|1)$.

When $G$ is transitive ($c=1$), the unit representation appears with multiplicity $1$, so $\rho = 1 \oplus \theta$ where $\theta$ is a representation not containing the unit representation. Then $\chi = 1 + \psi$ (where $1$ denotes the unit character and $\psi$ the character of $\theta$), and $(\psi|1) = (\chi - 1|1) = (\chi|1) - (1|1) = 1 - 1 = 0$. $\square$
