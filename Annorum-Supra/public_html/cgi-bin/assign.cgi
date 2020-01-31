#!/bin/perl

use warnings;
use DBI;
use DBD::mysql;
use CGI;
use CGI::Carp qw (fatalsToBrowser);#important for time?
use File::Basename;
use File::Copy;
use CGI::Cookie;

my $cgi = CGI->new();    # create new CGI object
my $advisor = $cgi->param('advisor');
my $student = $cgi->param('student');
my $student_advisor = '../data/student_advisor.txt';#stores user data
my $usernames_passwords = '../data/usernames_passwords.txt';
my $studentSubmissionsDir = '../studentSubmissions/';
my $student_report = '../data/student_report.txt';	

%cookies = map split(/=/), split(/; /,$ENV{'HTTP_COOKIE'});

#begin You are not using the cgi-lib so you don't need this block
if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}
#end You are not using the cgi-lib so you don't need this block
if ($cookies{"role"} ne "superuser"){
	print "Content-type: text/html\n\n";
	print "you are not authorized for changes to this page.\n"; print "<br>";
	print "Try logging in again as a super user.\n";
	exit;
}
print "Content-type: text/html\n\n";

#a cleaner way would be to snatch the contents of a stored html file and just spit it out later
print <<"nav";
<html><head><title>CMPS 394</title>
<meta charset="utf-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
         <meta name="description" content="">
         <meta name="author" content="">
         <title>Advising Tool</title>
         <!-- Bootstrap core CSS -->
          <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
		 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         <!-- Custom styles for this template -->
         <link href="justified-nav.css" rel="stylesheet">

</head>
 
<body>
<div class="container">
            <div class="masthead">
                <h3 class="text-muted">Advising Tool-Admin View</h3>
                <nav class="navbar navbar-expand-md navbar-light bg-light rounded mb-3">
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarCollapse">
                        <ul class="navbar-nav text-md-center nav-justified w-100">
                            <li class="nav-item active">
                                <a class="nav-link" href="#">Home-Dead<span class="sr-only">(current)</span></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../student_view.html">Student View</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../cgi-bin/advisor.cgi">Advisor View</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../login_view.html">Login</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../newUser_view.html">New User</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../cgi-bin/assign.cgi">Admin</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../userSearch_view.html">AJAX Assignment</a>
                            </li>
                        </ul>
                    </div>
                </nav>

nav

open (FILE, $student_advisor);
@dblines= <FILE>;#snatch the contents of file student_advisor.txt and store it to an array
close(FILE);#close it out
$length_dblines=@dblines;#determine how many records are in this file

open (FILE, $student_report);
@student_report_lines= <FILE>;#snatch the contents of file student_report.txt and store it to an array
close(FILE);#close it out
$length_student_report_lines=@student_report_lines;#determine how many records are in this file

print "Student $student has been assigned to advisor $advisor";print "<br>";#holler back so i know the circuit works

for($count = 0 ; $count <$length_dblines ; $count++){
    chomp($dblines[$count]);   
    my @userData=split(',', $dblines[$count]); #place the current line into an array split by a comma
    my $lineStudentName= $userData[0];#
    my $lineAdvisorName= $userData[1];#
    
    if ($lineStudentName eq $student){
        $dblines[$count]="$student,$advisor\n";
    }else {
    $dblines[$count]="$dblines[$count]\n";
    }
}
open (my $fh, '>', $student_advisor);
print $fh @dblines;
close $fh;

for ($count = 0 ; $count <$length_dblines ; $count++) 
{ 
    chomp($dblines[$count]);   
    my @userData=split(',', $dblines[$count]); #place the current line into an array split by a comma
    my $lineStudentName= $userData[0];#
    my $lineAdvisorName= $userData[1];#
    
        print <<"form"; 

            <div class="row">
                <div class="col-md-12">
                    <form role="form" action="./assign.cgi" method="post">
                        <div class="form-group"> 
                            <div class="row border border-dark">
                                <div class="col-md-auto label_container mt-auto mb-auto border-dark border-0">
                                    <label>Student ID: </label>
                                </div>
                                <div class="col-md-auto label_container mt-auto mb-auto border-dark border-0">
                                    <input type="text" name="student" size="8" readonly="readonly" value="$lineStudentName"=>
                                </div>
                                <div class="col-md-auto label_container mt-auto mb-auto border-dark border-0">
                                    <label>Advisor ID: </label>
                                </div>
                                <div class="col-md-auto label_container mt-auto mb-auto border-dark border-0">
                                    <input type="text" name="" size="8" readonly="readonly" value="$lineAdvisorName">
                                </div>
                                <div class="col-md-auto label_container border-0 mt-auto mb-auto">
                                    <div class="btn-group mt-auto mb-auto pb-auto pt-auto" data-toggle="buttons"> 
                                        <label class="btn btn-secondary active"> 
                                            <input type="radio" name="advisor" value="a1" autocomplete="off"> Advisor 1       
                                        </label>                             
                                        <label class="btn btcn-secondary"> 
                                            <input type="radio" name="advisor" value="a2" autocomplete="off"> Advisor 2        
                                        </label>                             
                                        <label class="btn btn-secondary"> 
                                            <input type="radio" name="advisor" value="a3" autocomplete="off"> Advisor 3        
                                        </label>
                                        <label class="btn btn-secondary"> 
                                            <input type="radio" name="advisor" value="a4" autocomplete="off"> Advisor 4        
                                        </label>                             
                                    </div>
                                </div>
                                <div class="label_container border-0 col-md-auto">
                                    <button type="submit" class="btn btn-primary">Submit</button>
                                </div>
                            </div>
                        </div>             
                        <hr/>
                    </form>
                </div>
                </div>
            </row>
form

for ($studentReportCount = 0 ; $studentReportCount <$length_student_report_lines ; $studentReportCount++) 
{ 
    chomp($student_report_lines[$studentReportCount]);#dump the hidden new line character   
    my @studentReportData=split(',', $student_report_lines[$studentReportCount]); #place the current line into an array split by a comma
    my $lineStudentID= $studentReportData[0]; 
    my $lineStudentReport= $studentReportData[1];#

    if ($lineStudentID eq $lineStudentName){
        print <<"student_report"; 
        <h5> Report $lineStudentReport for student $lineStudentID</h5>
        <div>
        <object data="$studentSubmissionsDir/$lineStudentReport" type="text/plain"
        width="100%" style="height: auto">
        <a href="$studentSubmissionsDir/$lineStudentReport">Embedded Text Document</a>
        </object>
        <hr>
        </div>
        
        
student_report

    }
}
}

print "</body></html>";

  