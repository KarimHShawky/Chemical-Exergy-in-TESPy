# Exergy Analysis of the CGAM process in TESPy

Example for the exergy analysis in [TESPy][]. Find more information
about the exergy analysis feature in the respective [online
documentation][].

The supercritical CO<sub>2</sub> power cycle model has the following
topology:

<figure>
<img src="./flowsheet.svg" class="align-center" />
</figure>

Find the model specifications and results in the sCO2.py script and the
corresponding [pdf model report][].

## Usage

Clone the repository and build a new python environment. From the base
directory of the repository run

``` bash
pip install -r ./requirements.txt
```

to install the version requirements for the CGAM.py python script.

The original data of the plant are obtained from the following
publication:

*Source1*

*Source2*

## Valdiation and Results of Exergy Analysis

The tables below show the results of the simulation as well as the
validation results. The original data from the publication are provided
in the .csv files [][] and
[][].

### Connection data

**TESPy simulation**

**Absolute difference in the values Δ**

**Relative deviation in the values δ**

### Component data

**TESPy simulation**


**Absolute difference in the values Δ**


**Relative deviation in the values δ**


### Network data

## Citation

The state of this repository is archived via zenodo. If you are using the
TESPy model within your own research, you can refer to this model via the
zenodo doi: [][].

## MIT License

Copyright (c) 2022 Francesco Witte, Karim Schawky, Mathias Hofmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


  [TESPy]: https://github.com/oemof/tespy
  [online documentation]: https://tespy.readthedocs.io/
  [pdf model report]: sCO2_model_report.pdf
  [component_validation.csv]: component_validation.csv
  [connection_validation.csv]: connection_validation.csv
  [10.5281/zenodo.4751796]: https://zenodo.org/record/4751796