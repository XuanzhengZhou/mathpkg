---
role: exercise
locale: en
chapter: "VI"
section: "6.1"
exercise_number: 7
---
Let $$u = b - c, v = a - b$$. Then

$$\|u + v\|^2 = (\|u\| + \|v\|)^2 = \|u\|^2 + \|v\|^2 + 2\|u\| \|v\|.$$

Hence $$\sigma(u, v) = \|u\| \|v\|$$ and, by Schwarz's Inequality (Lemma 1), $$u, v$$ are linearly dependent. Thus $$a, b, c$$ are linearly dependent.

For the second part: Let $$S = a + M$$ and $$S' = a' + M'$$, where we choose $$a' = a\varphi$$. Then $$\varphi$$ induces a one-one mapping $$\psi$$ of $$M$$ onto $$M'$$ by $$v \rightarrow (a + v)\varphi - a'$$. Thus $$0\psi = 0$$ and $$\psi$$ preserves distance. By the first part, $$\psi$$ maps lines to lines. Hence for any $$v \neq 0$$ in $$M$$ and any $$x$$ in $$\mathbf{R}$$, $$(xv)\psi$$ lies on the line $$[v\psi]$$, so $$\psi$$ is linear and therefore $$\varphi$$ is a Euclidean isomorphism.
