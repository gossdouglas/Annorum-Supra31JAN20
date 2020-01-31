#!usr/bin/perl
print "Content-Type: text/html\n\n";
print "Enter your name: ";
$name=<STDIN>;
print "Hello, ${name} ... you will soon be a Perl addict!";