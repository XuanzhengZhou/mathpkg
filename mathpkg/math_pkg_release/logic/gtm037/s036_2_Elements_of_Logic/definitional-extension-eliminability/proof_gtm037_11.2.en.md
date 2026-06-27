---
role: proof
locale: en
of_concept: definitional-extension-eliminability
source_book: gtm037
source_chapter: "11"
source_section: "2"
---

We construct $\psi'$ by induction on $\psi$. In each step the desired properties of $\psi'$ are easy to prove, and we prove the desired result in only one step as an illustration.

To begin with, we construct $\psi'$ for $\psi$ of the form $\sigma = v_i$ by induction on $\sigma$. If $\sigma$ is a variable, we set $\psi' = \psi$. Now suppose inductively that $\sigma$ is $\mathbf{O} \tau_0 \cdots \tau_{n-1}$. Let $\alpha_0, \ldots, \alpha_{n-1}$ be the first $m$ variables not occurring in $\psi$. If $\mathbf{O}$ is a symbol of $\mathcal{L}$, then we let $\psi'$ be the formula

$$\exists \alpha_0 \cdots \exists \alpha_{n-1} [\mathbf{O} \alpha_0 \cdots \alpha_{n-1} = v_i \wedge \bigwedge_{j < n} \tau_j' = \alpha_j].$$

If $\mathbf{O}$ is a symbol of $\mathcal{L}'$ but not of $\mathcal{L}$, then $\mathbf{O}$ has a defining axiom in $\Gamma'$ of the form

$$\forall v_0 \cdots \forall v_{m-1} [\mathbf{O} v_0 \cdots v_{m-1} = v_m \leftrightarrow \chi],$$

and we set $\psi'$ to be the formula

$$\exists \alpha_0 \cdots \exists \alpha_{n-1} [\chi(\tau_0', \ldots, \tau_{n-1}', v_i) \wedge \bigwedge_{j < n} \tau_j' = \alpha_j].$$

Finally, let $(\neg \psi)' = \neg \psi'$, $(\psi \vee \chi)' = \psi' \vee \chi'$, $(\psi \wedge \chi)' = \psi' \wedge \chi'$, and $(\forall v_i \psi)' = \forall v_i \psi'$.

The final assertion of the theorem concerning effectiveness is clear from the above inductive construction.
