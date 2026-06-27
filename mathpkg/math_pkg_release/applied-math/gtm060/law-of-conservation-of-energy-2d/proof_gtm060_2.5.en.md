---
role: proof
locale: en
of_concept: law-of-conservation-of-energy-2d
source_book: gtm060
source_chapter: "2"
source_section: "5"
---
Let $\mathbf{x}(t)$ be a solution of $\ddot{\mathbf{x}} = -\partial U/\partial \mathbf{x}$. Then

$$\frac{d}{dt}E(\mathbf{x}(t), \dot{\mathbf{x}}(t)) = \frac{d}{dt}\left(\frac{1}{2}(\dot{\mathbf{x}}, \dot{\mathbf{x}}) + U(\mathbf{x})\right) = (\dot{\mathbf{x}}, \ddot{\mathbf{x}}) + \left(\frac{\partial U}{\partial \mathbf{x}}, \dot{\mathbf{x}}\right).$$

Using the equation of motion $\ddot{\mathbf{x}} = -\partial U/\partial \mathbf{x}$, we obtain

$$\frac{dE}{dt} = (\dot{\mathbf{x}}, -\partial U/\partial \mathbf{x}) + (\partial U/\partial \mathbf{x}, \dot{\mathbf{x}}) = 0.$$

Thus $E$ is constant along solutions.
