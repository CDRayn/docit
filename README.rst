*****
DocIt
*****

DocIt is a quick and easy command line utility for auto-generating 
documentation of a command line based work flow from a user's .bash_history 
file generated during said work flow. This allows for a procedure executed 
in the command line to be quickly documented as it is developed and ironed
out. Doing so means producing documentation of a new procedure does not 
interfere with the actual development and experimentation of that procedure.

DocIt can generate documentation in either the Markdown (GitHub Flavored),
or reStructuredText formats.

Repository Structure
====================

The Docit repository structure consists of the following major child directories:

*   /docs   : contains all documentation source material and rendered documentation
*   /tests  : all unit tests and automated tests should be placed here
*   /src    : contains modules and source that is imported by the main executable

Branching Methodology
=====================

DocIt follows the Git Flow strategy. The primary branches are: master, develop, and release. All development should be
done in a "feature" branch created from the develop branch. Once a feature is complete, its corresponding branch is
merged into the development branch. Releases are formed by merging the develop branch into the release and master branch
and tagging those two branches with the release version number.


Contributing
============

If you wish to make a contribution to this project please create a fork of the project's repository. Use a feature
branch to make any changes. Once you have finished making your changes issue a pull request. Please be sure to include a
detailed description of what you changed and why you changed it. All changes or additions contained in the pull request
should be documented and provide unit testing.

License
=======

GNU General Public License v3.0
