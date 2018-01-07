# Part 4: Forms

In this part we'll build on top of our login form to start handling authentication.

To handle authentication we need to choose an identity policy as described in the [Security section of the morepath documentation](http://morepath.readthedocs.io/en/latest/security.html). We decided to use [more.itsdangerous](https://github.com/morepath/more.itsdangerous) for a cookie based workflow.

In order to protect our microblog against CSRF attacks we need to make some changes on our form using [WTForms built-in session based CSRF](http://wtforms.readthedocs.io/en/latest/csrf.html)

To run the example:

1. `cd 04_forms`
2. `pip install -e .`
3. `python -m microblog.run`
