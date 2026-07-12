(class)=

# SpinW class overview

To perform calculation using the SpinW library, we need to create an object (spinw class type).
It stores all the necessary parameters for the calculation (crystal structure, interactions, magnetic structure, etc.).
In the object oriented programming dictionary, the data stored in an object, are called properties.
Beside the data, the object also has assigned functions that perform different computations on the object data.
These functions are called methods and they take the object as first input argument.
To create an spinw class object you can simply type:

```matlab
model1 = spinw
```

```text
spinw object (symbolic: off, symmetry: on, textoutput: "stdout")
lattice
         angle: [1x3 double]
     lat_const: [1x3 double]
           sym: [1x1 integer]
unit_cell
             r: [3xnAtom double]  nAtom=0
             S: [1xnAtom double]
         label: [1xnAtom char]
         color: [3xnAtom integer]
twin
           vol: [1xnTwin double]  nTwin=1
          rotc: [3x3xnTwin double]
matrix
           mat: [3x3xnJ double]  nJ=0
         color: [3xnJ integer]
         label: [1xnJ char]
single_ion
         aniso: [1xnMagAtom integer]  nMagAtom=0
             g: [1xnMagAtom integer]
         field: [1x3 double]
             T: [1x1 double]
coupling
            dl: [3xnCoupling integer]  nCoupling=0
         atom1: [1xnCoupling integer]
         atom2: [1xnCoupling integer]
       mat_idx: [3xnCoupling integer]
           idx: [1xnCoupling integer]
mag_str
         N_ext: [1x3 integer]
             k: [1x3 double]
             S: [3xnMagExt double]  nMagExt=0
             n: [1x3 double]
unit
            kB: [1x1 double]
           muB: [1x1 double]
```

## Properties

The output of the previous command shows all the data fields of model1. Each data field has an initial value and any of them can be modified directly:

```text
ans = 

    int32
```

Thus if we want to change it directly, we need an integer number:

```matlab
model1.lattice.sym = int32(5);
```

This will change the crystal space group to `C 2`. To avoid most common mistakes, there are several methods (functions) for modifying the above properties that also perform additional error checking and makes certain input conversions. For example all lattice related properties can be modified using the `genlattice()` function:

```matlab
model1 = genlattice('lat_const',[3 5 5],'sym','C 2','angled',[90 90 90])
```

The alternative usage of the above function is the following:

```matlab
genlattice(model1,'lat_const',[3 5 5],'sym','C 2','angled',[90 90 90])
```

This reflects better the input argument structure. The first argument is the spinw object `model1`. After the first argument comes option name and value pairs. The first options is `lat_const` and the value it expects is a vector with 3 elements if the input vector has different length, the function throws an error. The second option is `sym` that also accepts string input (name of the space group) that is automatically converted to the index of the space group and stored in model1:

```matlab
model1.lattice.sym
```

```text
ans = 5
```

The last option is `angled` that requires a vector with three elements and defines the alpha, beta, gamma lattice angles in degree. This will be converted into radian and stored:

```matlab
model1.lattice.angle
```

```text
ans =

    1.5708    1.5708    1.5708
```

### Complete list of properties

There are eight public properties of spinw each with several subfields:

- [spinw.lattice](#prop-lattice)
- [spinw.unit_cell](#prop-unit-cell)
- [spinw.twin](#prop-twin)
- [spinw.matrix](#prop-matrix)
- [spinw.single_ion](#prop-single-ion)
- [spinw.coupling](#prop-coupling)
- [spinw.mag_str](#prop-mag-str)
- [spinw.unit](#prop-unit)

## Methods

In line with the above example the general argument structure of the method functions is one of the following:

```text
function(obj,'Option1',Value1,'Option2',Value2,...)
function(obj,Value1,Value2,...)
```

The first type of argument list is used for functions that require variable number of input parameters with default values. The second type of argument structure is used for functions that require maximum up to three fixed input parameter. Every method has help that can be called by one of the following methods:

- selecting the function name in the Editor/Command Window and pressing F1
- in the Command Window typing for example:

```matlab
help spinw.genlattice
```

This shows the help of the genlattice() function in the Command Window. To open the help in a separate window you need to write:

```matlab
doc spinw.genlattice
```

To unambiguously identify the functions it is useful to refer them as spinw.function() this way matlab knows which function to select from several that has the same name. For example the plot() function is also defined for the spinw class. However by writing:

```matlab
help plot
```

we get the help for the standard MATLAB plot function. To get what we want use:

```matlab
help spinw.plot
```

By the way this function is one of the most useful ones. It can show effectively all information stored in the sw object by plotting crystal structure, couplings, magnetic structure etc. Calling it on an empty object shows only the unit cell:

```matlab
plot(model1)
```

```{image} /_static/img/gen_Swclass_01.png
:alt: 
```

As you might noticed, there is an alternative calling of any method function: obj.function(...), this is just equivalent to the previous argument structures.

## Copy

The spinw class belong to the so called handle class. It means in short that the model1 variable is just a pointer to the memory where the class is stored. Thus doing the following:

```matlab
model2 = model1;
```

It only copies the pointer. Thus if I change something on model1, model2 will change as well. Thus to clone the object (the equivalent of the usual '=' operation in MATLAB) is the copy() function:

```matlab
model2 = copy(model1);
```

<sript src="/js/toc.js"></sript>
