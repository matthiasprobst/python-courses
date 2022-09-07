# Python-Courses

Get into specific fields of application with these python courses.

## Getting started

I higly recommend using an a `anaconda` environment.

     conda create -n pycourses python=3.8 -y
     conda activate pycourses

Clone the repository:

    git clone https://github.com/matthiasprobst/python-courses

For full installation run

    pip install ".[complete]"

To install only the dependencies for a specific course, name it in brackets, e.g.:

    pip install ".[hdf5]"

Most courses are writting in python notebooks. To work on them, start a server first. 
The browser should open automatically:

    jupyter lab

Have fun :-)

## Issues and new courses
Please open an Issue on the GitHub repository if there are any problems. Feel free to also request 
topics that are not included in the courses yet.