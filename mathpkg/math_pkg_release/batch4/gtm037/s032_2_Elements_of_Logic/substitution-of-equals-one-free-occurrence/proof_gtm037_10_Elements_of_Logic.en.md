---
role: proof
locale: en
of_concept: substitution-of-equals-one-free-occurrence
source_book: gtm037
source_chapter: "10"
source_section: "Elements of Logic"
---

We proceed by induction on $\varphi$. For $\varphi$ atomic,

$$\vdash \sigma = \tau \rightarrow (\varphi \leftrightarrow \psi) \quad 10.23(5)$$
$$\vdash \tau = \sigma \rightarrow (\psi \leftrightarrow \varphi) \quad 10.23(5)$$

Hence by 10.35 we have

$$\vdash \sigma = \tau \rightarrow (\varphi \leftrightarrow \psi).$$

The induction steps from $\varphi$ to $\neg \varphi$, $\varphi$ and $\psi$ to $\varphi \lor \psi$, and $\varphi$ and $\psi$ to $\varphi \land \psi$ are all trivial, using suitable tautologies. Now suppose that our result holds for $\varphi$, $\alpha$ is a variable, and $\forall \alpha \psi$ is obtained from $\forall \alpha \varphi$ by replacing one free occurrence of $\sigma$ in $\forall \alpha \varphi$ by a free occurrence of $\tau$ in $\forall \alpha \psi$. Then $\psi$ is obtained from $\varphi$ by replacing one free occurrence of $\sigma$ in $\varphi$ by a free occurrence of $\tau$ in $\psi$. By the induction hypothesis,

$$\vdash \sigma = \tau \rightarrow (\varphi \leftrightarrow \psi).$$

Since $\alpha$ does not occur free in $\sigma = \tau$, we obtain by generalization and distribution:

$$\vdash \sigma = \tau \rightarrow (\forall \alpha \varphi \leftrightarrow \forall \alpha \psi).$$
