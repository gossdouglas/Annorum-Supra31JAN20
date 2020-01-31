#!/bin/perl
use strict;
use warnings;
use CGI::Carp;    # send errors to the browser, not to the logfile
use CGI;

my $cgi = CGI->new();    # create new CGI object

my $name = $cgi->param('name');

print $cgi->header('text/html');

print "Hello, $name";
