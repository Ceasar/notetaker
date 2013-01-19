

# ex_nihilo

Easy hack-creation kit (bootstrap + flask + heroku). Create something out of nothing.

ex_nihilio is designed with the following goals in mind:

- Speed. Application setup time should be minimized.
- Abstraction. ex_nihilio is meant for group projects, and knowledge of specific tools like virtualenv and heroku is not assumed.


# Installation

- Download [Heroku Toolbelt](https://toolbelt.heroku.com/)
- Install [pip](http://www.pip-installer.org/en/latest/installing.html)
- Install [virtualenv](http://www.virtualenv.org/en/latest/#installation)
- Install fabric. (`pip install fabric`)
- Finally, download this project a zip file (do _not_ clone) and run `fab bootstrap`.

# Usage

ex_nihilio is just a regular flask app at its core, which means you can use it as such if that's all you need.

ex_nihilio also comes with a fabfile that is useful for automating common tasks (such as creating a heroku app) as well as providing more user-friendly commands to people not familiar with standard web tools.
