---
role: exercise
locale: en
chapter: "2"
section: "2.3"
exercise_number: "2c"
---

Suppose that $G$ is transitive on $X$ and that $X$ has at least two elements. We say that $G$ is \emph{doubly transitive} if, for all $x, y, x', y' \in X$ with $x \neq y$ and $x' \neq y'$, there exists $s \in G$ such that $s x = x'$ and $s y = y'$.

(From part (b), the character of the permutation representation on $X \times X$ is $\chi^2$. Using the decomposition from part (a) where $\chi = 1 + \psi$, compute $(\chi^2|1)$ and relate it to the number of orbits of $G$ on $X \times X$. For a doubly transitive group, there are exactly two orbits on $X \times X$: the diagonal $\{(x,x) : x \in X\}$ and its complement. This yields $(\chi^2|1) = 2$, and using $\chi = 1 + \psi$ one can deduce that $(\psi^2|1) = 1$, implying $\psi$ is irreducible.)

**Solution sketch.** The action of $G$ on $X \times X$ has the diagonal $\Delta = \{(x,x) : x \in X\}$ as one orbit (since $G$ is transitive, it acts transitively on $\Delta$). If $G$ is doubly transitive, the off-diagonal pairs also form a single orbit. Hence there are exactly $2$ orbits, so by part (a), the multiplicity of the unit representation in the permutation representation on $X \times X$ is $2$. By part (b), the character of this representation is $\chi^2$, so $(\chi^2|1) = 2$.

From part (a), $\chi = 1 + \psi$ with $(\psi|1) = 0$. Then $\chi^2 = 1 + 2\psi + \psi^2$, so $(\chi^2|1) = (1|1) + 2(\psi|1) + (\psi^2|1) = 1 + 0 + (\psi^2|1)$. Hence $(\psi^2|1) = 1$. Since $(\psi|\psi) = (\psi^2|1)$ (because characters are real-valued for permutation representations) or more generally using orthogonality, one can conclude $\psi$ is irreducible.
