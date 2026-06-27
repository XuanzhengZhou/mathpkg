---
role: exercise
locale: en
chapter: "2"
section: "2"
exercise_number: 7
---

In this exercise we present an account of Lawvere's original theories as elevated to arbitrary categories by Linton. A Lawvere theory in $\mathcal{K}$ is a category $\mathcal{T}$ with the same objects as $\mathcal{K}$ together with a functor $R: \mathcal{K}^{\text{op}} \longrightarrow \mathcal{T}$ such that $R$ is the identity function on objects and such that $R$ has a left adjoint. A morphism $\psi: (\mathcal{T}, R) \longrightarrow (\mathcal{T}', R')$ is a functor $\psi$ with $R\psi = R'$.

**(a)** If $T = (T, \eta, \circ)$ is an algebraic theory in clone form in $\mathcal{K}$ show that $(\mathcal{T}, R)$ is a Lawvere theory in $\mathcal{K}$ where $\mathcal{T} = (\mathcal{K}_T)^{\text{op}}$, $AR = A$, $fR = f^A$.

[*Hint:* a left adjointness for $R$ is $AL = AT$, $(\alpha: A \rightarrow B)L = \alpha^{\#}: AT \rightarrow BT$ (see 1.5.35 for the notation), $A\iota: A \rightarrow ALR = \text{id}_{AT}: A \rightarrow AT$, $A\eta: ARL \rightarrow A = A\eta: AT \rightarrow A$; here the "$\eta$" and "$\varepsilon$" of 2.2.15 are being written "$\iota$" and "$\eta$."]

**(b)** If $\lambda: T \rightarrow S$ is a theory map as in 2.7, show that $\alpha: BT \rightarrow A \;\mapsto\; \alpha \cdot B\lambda: BS \rightarrow A$ describes a morphism between the associated Lawvere theories.

**(c)** Show that (a) and (b) establish the category of algebraic theories (as in 2.10) as a full representative subcategory of Lawvere theories.

[*Hint:* given $(\mathcal{T}, R)$ with associated adjointness $(L, \iota, \eta)$ (using the same notation as in (a)) set $AT = ARL$, $A\eta: A \rightarrow ARL = A\eta: ARL \rightarrow A$, $(\alpha: A \rightarrow BT) \circ (\beta: B \rightarrow CT) = \alpha \cdot \beta^{\#}$ where $\beta^{\#}: BRL \rightarrow CRL = \beta RL \cdot CR\iota L$.]

**(d)** If $(A, \xi)$ is a $T$-algebra as in 1.4.8 show that $(A, H)$ is an algebra over the associated Lawvere theory where $\alpha: B \rightarrow C$ induces $\mathcal{K}(B, A) \rightarrow \mathcal{K}(C, A)$.
