# Data visualization cheatsheet

In this cheatsheet we will be focusing on creating beautiful charts with libraries like mathplotlib, seaborn and plotly.

**Mathplotlib** is the most commonly used plotting library with a lot of flexibility, but it lacks a visually appealing 
design and has no interactivity.

**Seaborn** is build on top of Mathplotlib, enhances the style of plots  and simplifies the plot creation a bit, but 
with that it lacks some configuration capabilities Mathplotlib has.

**Plotly** is a visually beautiful interactive plotting library which also can run directly in your jupiter notebook.
While it is harder to create plots with it, these plots are production ready and can instantly turned into interactive 
plots online.

**To summarize**, you should use Mathplotlib if you need extra flexibility and Plotly if you need good looking 
interactive plots. For everything else Seaborn is the way to go.

## Mathplotlib
This library follows a simple workflow:

 1. create a specific type of plot with values for the x and y:
    ```
    plt.scatter(x_values, y_values)
    ```
 2. Change the styling (Here, scale of x-axis was changed):
    ```
    plt.xscale('log')
    ```
 3. Print the plot:
    ```
    plt.show()
    ```
 4. Clear plot for next grafic:
    ```
    plt.clf()
    ``` 
### Different Plots in mathplotlib
Here we are inspecting the different quirks each plot as and how to work with them
#### Linepot
```
plt.plot()
```

#### Scatterplot
The Scatterplot constructor has the following arguments:
* x : x values
* y : y values
* s : scale of elements
* c : color
```
plt.scatter()
```

#### Histogramm
The histogramm constructor has the following arguments:
* data: dataset that should be plottet
* bins: in how many groups should the data be sorted
* 
```
plt.hist()
```
### Most important customizations
* Add title
    ```
    plt.title('Title')
    ```
* Add label for each axis
    ```
    plt.xlabel('x')
    ```
* Scale axis differently
    ```
    # You can choose between: "linear", "log", "symlog", "logit", ...
    plt.xscale('log')
    ```
* Set Axis vaules to specific values:
    ```
    # Here the first array is used to plot the data and the second is displayed to the viewer
    plt.xticks([0,2,4,6,8],
                ['0', '2B', '4B', '6B', '8B'])
    ```
* Add grid to the plot:
    ```
    plt.grid(True)
    ```
* Add text in the graph:
    ```
    plt.text(x-coor, y-coor, 'text')
    ```
  
## Seaborn
