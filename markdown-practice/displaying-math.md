# Displaying Math in Markdown

It turns out properly displaying math equations specifically in _GitHub_-rendered Markdown files isn't as straightforward as I thought.

We can pretty easily display "code" using indivudual tick marks, for example:

The standard form of a 2D line is given by a form `ax + by + c` in our code, where `a,b,c` are real numbers, `x` is traditionally an independent real-valued variable, and `y` a dependent real-valued variable.

To display code more prominantly, use triple tick marks, as in:

```
ax + by + c
```

I see this all over GitHub!
I was confounding the use of tick marks with math mode in earlier versions of this demo, and I am happy to clear up this confusion for myself and hopefully others.
I also errantly used dollar signs to attempt to produce math equations, which is standard TeX syntax used in many other popular instances of markdown in action, like Jupyter Notebooks. 

I wasn't surprised when I found many others have had the same issue producing proper equations in Markdown files, for example [here](https://stackoverflow.com/questions/11256433/how-to-show-math-equations-in-general-githubs-markdownnot-githubs-blog) and [also here](https://stackoverflow.com/questions/35498525/latex-rendering-in-readme-md-on-github).

From what I can tell, the best workaround to show math is to use HTML. I am relying entirely on [SpeedCoder5's answer](https://stackoverflow.com/a/47798853) in one of those stack overflow boards (linked above).

First, let's try to produce some "nice" in-line math.

A line in 2-space may be represented y = f<sub>&theta;</sub>(x) = &theta;<sub>1</sub> x + &theta;<sub>2</sub>, where &theta; is a 2-vector with real-valued entries, &theta;<sub>i</sub>, i = 1 and 2, and x and y are real-valued variables, where y depends on x. 

Sadly we aren't going to achieve nice typsetting for any numbers or the variables "i," "x," or "y".

To have display an equation more prominantly (and correctly), use "an external LaTeX renderer like CodeCogs." (Again, thanks SpeedCoder5!) In other words, we may use standard TeX syntax and render a proper equation by shipping it off to another website to do the rendering (of what is technically just an image file).

<img src="https://latex.codecogs.com/svg.latex?\Large&space;y=h_\theta(x)=\theta_1x+\theta_2" title="\Large y=h_\theta(x)=\theta_1x+\theta_2" />

To those viewing the source code, notice spaces are not permitted in the string of TeX code I provided -- no surprise since it's a URL.
