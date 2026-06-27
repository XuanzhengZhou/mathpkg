---
role: proof
locale: en
of_concept: psf-dominated-by-inner-product-lemma
source_book: gtm015
source_chapter: "67"
source_section: "States and representations"
---

# Proof of PSF dominated by inner product yields bounded operator

Proof. (i) is obvious (for the meaning of $0 \leq T \leq I$, see (57.28)).

(ii) Suppose $\psi$ is a PSF on $A$ with $\psi \leq \varphi$. Clearly $N_\varphi \subset N_\psi$, therefore

$$x_\varphi \mapsto x_\psi \quad (x \in A)$$

is a well-defined linear mapping $A_\varphi \rightarrow A_\psi$; moreover,

$$\|x_\psi\|^2 = \psi(x, x) \leq \varphi(x, x) = \|x_\varphi\|^2$$

shows that the mapping (*) is continuous for the respective norms. The formula

$$\psi'(x_\varphi, y_\varphi) = (x_\psi|y_\psi) = \psi(x, y) \quad (x, y \in A)$$

defines a PSF $\psi'$ on $A_\varphi$, and the inequalities $\psi(x, x) \leq \varphi(x, x)$ ($x \in A$) may be written

$$\psi'(x_\varphi, x_\varphi) \leq (x_\varphi|x_\varphi) \quad (x \in A).$$

Citing the lemma, there exists $T \in \mathcal{L}(H_\varphi)$ with $0 \leq T \leq I$, such that

$$\psi'(x_\varphi, y_\varphi) = (Tx_\varphi|y_\varphi)$$

for all $x, y \in A$; in other words, $\psi = \varphi_T$. If also $\psi = \varphi_S$, $S \in \mathcal{L}(H_\varphi)$, then

$$(Tx_\varphi|y_\varphi) = \psi(x, y) = (Sx_\varphi|y_\varphi)$$

for all $x,

defines an adjunctive PSF $\varphi_f$ on $A$.

(ii) If $A$ has a unity element 1 and if $\varphi$ is an adjunctive PSF on $A$, then the formula

$$f_\varphi(x) = \varphi(x, 1) \quad (x \in A)$$

defines a state $f_\varphi$ on $A$. Moreover, the correspondences $f \mapsto \varphi_f$ and $\varphi \mapsto f_\varphi$ are mutually inverse bijections between the set of all states $f$ and the set of all adjunctive PSF’s $\varphi$; both of these sets are convex, and the correspondences preserve convex combinations.

Proof. There is nothing deeper here than the associativity of multiplication in $A$.
