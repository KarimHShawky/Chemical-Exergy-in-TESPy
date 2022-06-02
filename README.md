# Exergy Analysis of the CGAM process in TESPy

Example for the exergy analysis in [TESPy][]. Find more information
about the exergy analysis feature in the respective [online
documentation][].

The CGAM model has the following topology:

<figure>
<img src="./flowsheet.svg" class="align-center" />
</figure>

Find the model specifications and results in the CGAM.py script and the
corresponding [pdf model report][].

## Usage

Clone the repository and build a new `python3.8` environment. From the base
directory of the repository run

``` bash
pip install -r ./requirements.txt
```

to install the version requirements for the `CGAM.py` python script. The
original data of the plant are obtained from the following publications:

CGAM process simulation:
*A. Bejan, G. Tsatsaronis, M. Moran: Thermal Design and Optimization, Wiley,*
*New York, 1996.*

KKH polynomials: *O. Knacke, O. Kubschewski, K. Hesselmann, Thermochemical*
*Properties of Inorganic Substances, 2nd ed., Springer, Berlin, 1991.*

## Validation of the model and running the scripts

The [validation][] folder contains the original data from literature. The
deviation between literature and TESPy values can be obtained by changing to
validation directory and running validation.py.

``` bash
cd validation
python validation.py
```

To run the TESPy scripts yourself, in your environment run

``` bash
python CGAM.py
```

from the root of this project. This script contains the full process simulation.

To run the combustion chamber validation scripts, please change into that
directory and run the `cc_coolprop.py` script.

``` bash
cd validation/combustion
python cc_coolprop.py
```

The `cc_kkh.py` script requires a different version of TESPy to run. It builds
on the Knacke, Kubschewski, Hesselmann polynomial functions, which were used in
Thermal Design and Optimization. Currently, there is no native support for these
polynomials in TESPy. They have been implemented for the validation only.
Furthermore, the lower heating value of Methane is hard-coded to
`50.01315 MJ/kg` in this version of TESPy.

For this, please create a fresh environment and install the dependencies with
the respective requirements file.

``` bash
pip install -r ./requirements_kkh.txt
```

Then change into the validation/combustion directory and run the script.

``` bash
cd validation/combustion
python cc_kkh.py
```

## Citation

The state of this repository is archived via zenodo. If you are using the
TESPy model within your own research, you can refer to this model via the
zenodo doi: [10.5281/zenodo.6592257][].

## MIT License

Copyright (c) 2022 Francesco Witte, Karim Shawky, Mathias Hofmann

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
  [pdf model report]: CGAM_model_report.pdf
  [validation]: ./validation/
  [10.5281/zenodo.6592257]: https://zenodo.org/record/6592257
