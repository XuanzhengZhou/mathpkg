---
role: proof
locale: en
of_concept: absoluteness-of-bounded-formulas
source_book: gtm008
source_chapter: "7"
source_section: "Relative Constructibility"
---
By induction on the number of logical symbols in $\varphi$. If $\varphi$ is atomic or of the form $\neg \psi$ or $\psi \wedge \eta$ the conclusion is obvious. If $\varphi(a_1, \ldots, a_n)$ is $(\exists x) \psi(x, a_1, \ldots, a_n)$ and if $b_1, \ldots, b_n \in B$ then

$$B \models (\exists x) \psi(x, b_1, \ldots, b_n) \rightarrow (\exists b \in B)[B \models \psi(b, b_1, \ldots, b_n)]$$
$$\rightarrow (\exists b \in B)[A \models \psi(b, b_1, \ldots, b_n)]$$
$$\rightarrow A \models (\exists x) \psi(x, b_1, \ldots, b_n)$$
$$\rightarrow (\exists f \in F)[A \models \psi(f(b_1, \ldots, b_n), b_1, \ldots, b_n)]$$
$$\rightarrow (\exists x \in B)[A \models \psi(x, b_1, \ldots, b_n)]$$
$$\rightarrow B \models (\exists x) \psi(x, b_1, \ldots, b_n).$$
