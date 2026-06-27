---
role: proof
locale: en
of_concept: set-input-output-process
source_book: gtm026
source_chapter: "2"
source_section: "2.3 Input Processes and Output Processes"
---

For the input process structure, the forgetful functor $U: \operatorname{Dyn}(- \times X_0) \to \mathbf{Set}$ has a left adjoint sending a set $A$ to $(A \times X_0^*, A\mu_0)$ where $A\mu_0(a, w, x) = (a, wx)$ and the unit $A\eta(a) = (a, \Lambda)$. To verify, given any $X$-dynamics $(Q, \delta)$ and a function $f: A \to Q$, we must produce a unique $X$-dynamorphism $f^{\#}: (A \times X_0^*, A\mu_0) \to (Q, \delta)$ with $f^{\#} \circ A\eta = f$. The definition is by induction on word length:

$$(a, \Lambda) f^{\#} = a f, \qquad (a, wx) f^{\#} = ((a, w) f^{\#}, x) \delta.$$

One checks that $f^{\#}$ is indeed an $X$-dynamorphism (it respects the dynamics maps) and is uniquely determined by these recursion equations. The response map is then $r \circ \beta$ where $r$ is the reachability map obtained as $f^{\#}$ when $A = I$ and $f = \tau$.

For the output process structure, the forgetful functor $U$ has a right adjoint sending $A$ to $(A^{(X_0^*)}, AL)$ where $AL(g, x) = L_x \circ g$ (with $L_x(w) = xw$) and the counit $A\Lambda(g) = g(\Lambda)$. Given any $X$-dynamics $(Q, \delta)$ and a function $f: Q \to A$, we construct the unique $X$-dynamorphism $f_{\#}: (Q, \delta) \to (A^{(X_0^*)}, AL)$ coextending $f$ via:

$$\langle \Lambda, q f_{\#} \rangle = \langle q, f \rangle, \qquad \langle xw, q f_{\#} \rangle = \langle w, \langle (q, x)\delta, f_{\#} \rangle \rangle$$

where $\langle w, g \rangle = g(w)$. This recursion proceeds simultaneously on all $q \in Q$, defining at each step the image of $q f_{\#}$ on words of increasing length. The observability map is obtained as $f_{\#}$ when $A = Y$ and $f = \beta$.

It is easy to check that the reachability and observability maps defined here coincide with the constructions given in Section 2.1 (the concrete automaton realization and minimalization procedures).
