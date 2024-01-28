Feature: running a simple webpage test

   Scenario: check site title
     Given we have browser opened
     When we go to www.wp.pl
     Then wp.pl site title starts with Wirtualna Polska
