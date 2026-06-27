---
role: exercise
locale: en
chapter: "1"
section: "1.35"
exercise_number: 11
---

We must show that every epimorphism has a dense image. For any $f: A \longrightarrow B$, let $I$ be the closure of the image of $f$ and form $(B + B)/I$ as shown below:

$$
\begin{array}{ccc}
I & B & (B + B)/I
\end{array}
$$

There are injections $\mathrm{in}_1, \mathrm{in}_2: B \longrightarrow B + B$ and a canonical projection $p: B + B \longrightarrow (B + B)/I$. Since $f \cdot (\mathrm{in}_1 \cdot p) = f \cdot (\mathrm{in}_2 \cdot p)$, we have that $I = B$ when $f$ is epi. (We leave it as an exercise to prove that $(B + B)/I$ is Hausdorff.)
