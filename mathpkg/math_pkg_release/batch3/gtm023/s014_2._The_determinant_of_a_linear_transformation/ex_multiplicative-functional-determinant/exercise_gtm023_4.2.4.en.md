---
role: exercise
locale: en
chapter: "4"
section: "2"
exercise_number: 4
---

Let $E$ be a vector space of dimension $n$ and consider the space $L(E; E)$ of linear transformations.

a) Assume that $F$ is a function in $L(E; E)$ satisfying

$$F(\psi \circ \varphi) = F(\psi) F(\varphi)$$

and

$$F(\iota) = 1.$$

Prove that $F$ can be written in the form

$$F(\varphi) = f(\det \varphi)$$

where $f: \Gamma \to \Gamma$ is a mapping such that

$$f(\lambda \mu) = f(\lambda) f(\mu).$$

b) Suppose that $F$ satisfies the additional condition that

$$F(\lambda \iota) = \lambda^n.$$

Then, if $E$ is a real vector space,

$$F(\varphi) = \det \varphi \quad \text{or} \quad F(\varphi) = |\det \varphi|$$

and if $E$ is a complex vector space,

$$F(\varphi) = \det \varphi.$$

Hint for part a): Let $e_i$ ($i = 1, \ldots, n$) be a basis for $E$ and define the transformations $\psi_{ij}$ and $\varphi_i$ by

$$\psi_{ij} e_v = \begin{cases} e_v & v \neq i \\ e_i + \lambda e_j & v = i \end{cases}, \quad i,j = 1, \ldots, n$$

and

$$\varphi_i e_v = \begin{cases} e_v & v \neq i \\ \lambda e_i & v = i \end{cases}.$$
