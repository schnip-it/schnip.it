# Test Plan

Since we are using a test-driven development methodology, we will be
writing tests for all features before implementing them.
Specifically, for each user story in the sprint backlog, we will first
design a functional test for the feature as a whole testing the
behaviour specified in the user story, then move on to a series of
unit tests dealing with the implementation of the code required to
make the functional test pass.

## Functional Tests

As we are using Python with the Django Web framework, we can write
functional tests based on Django's LiveServerTestCase testing
framework.  This means that we write test cases as classes extending
LiveServerTestCase, which provides setup and teardown of a running
Django instance, ideal for feature tests.  To connect to the Web
server and simulate a browser, we will be using the Selenium
browser-driving framework from our functional tests, with the
PhantomJS backend to simulate a browser.

## Unit Tests

For unit tests, Django provides the TestCase class, which sets up the
Django environment and routing such that we can issue requests
directly from our test cases without requiring a live server, as well
as providing a scratch database (SQLite, in our case) that can be used
for testing models without interfering with the real data or the data
from other test cases.  The result of performing a request is a Django
HttpResponse object returned by the routed view, giving the exact data
and metadata that would be returned from a request through the HTTP
interface.  This enables convenient, modular unit tests of views and
models, in addition to the testing of pure functions that don't rely
on Django state.
