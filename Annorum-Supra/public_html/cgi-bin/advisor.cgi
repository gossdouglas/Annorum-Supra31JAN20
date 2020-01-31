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
my $role= $cookies{"role"};
my $userID= $cookies{"userID"};
my $authenticated= $cookies{"authenticated"};


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
if ($cookies{"role"} ne ("advisor" or "superuser")){
	print "Content-type: text/html\n\n";
	print "you are not authorized for changes to this page.\n"; print "<br>";
	print "Try logging in again as an advisor or super user.\n";
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
                <h3 class="text-muted">Advising Tool-Advisor View</h3>
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
                                <a class="nav-link" href="cgi-bin/advisor.cgi">Advisor View</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../login_view.html">Login</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../newUser_view.html">New User</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="cgi-bin/assign.cgi">Admin</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../userSearch_view.html">AJAX Assignment</a>
                            </li>
                        </ul>
                    </div>
                </nav>
nav
print <<"advisor";
                <h2 class="align-middle text-center">You are logged in as user $userID.</h2>
            </div>
            <!-- Jumbotron -->
            <!-- Example row of columns -->
            <div class="row">
                <div class="col-md-12">
                    <form role="form">
                        <div class="form-group"> 
                            <div class="row">
                                <div class="col-md-auto label_container">
                                    <select id="formInput78" class="form-control"> 
                                        <option>Select Student</option>
                                        <option>Blow, Joe</option>                                         
                                        <option>Castor, Mike</option>                                         
                                        <option>Donaldson, Nicole</option>                                         
                                        <option>Evans, Will</option>                                         
                                        <option>Franklin, Max</option>                                         
                                    </select>
                                </div>
                                <div class="col-md-auto label_container">
                                    <label for="exampleInputEmail1">First Name:</label>
                                    <label for="exampleInputEmail1">Douglas</label>
                                </div>
                                <div class="col-md-auto label_container">
                                    <label for="exampleInputEmail1">Middle Name:&nbsp;</label>
                                    <label for="exampleInputEmail1">Anthony</label>
                                </div>
                                <div class="col-md-auto label_container">
                                    <label for="exampleInputEmail1">Last Name:</label>
                                    <label for="exampleInputEmail1">Goss</label>                                                                                                                                                                                                                                                                                                                                                                                                                &nbsp;
                                </div>
                                <div class="col-md-auto label_container">
                                    <label for="exampleInputEmail1">W Number:</label>
                                    <label for="exampleInputEmail1">W12345678</label>                                                                                                                                                                                                                                                                                                                                                                                                                &nbsp;
                                </div>
                            </div>                             
                        </div>                         
                        <hr/>
                        <div class="row pg-empty-placeholder">
                            <div class="container">
                        </div>
                        </div>
                        <hr/>
                        <div class="row">
                            <div class="form-group"> 
                                <label for="exampleInputFile">Advisor Remarks:&nbsp;</label>
                                <label for="formInput78">Grade:&nbsp</label>                                 
                            </div>
                            <div class="form-group"> 
                                <select id="formInput78" class="form-control"> 
                                    <option>SELECT</option>
                                    <option>Outstanding</option>                                     
                                    <option>Great</option>                                     
                                    <option>OK</option>                                     
                                    <option>D</option>                                     
                                    <option>F</option>                                     
                                </select>                                 
                            </div>
                            <div class="col-md-auto label_container">
                                <label for="exampleInputEmail1">Advisor:&nbsp;</label>
                                <label for="exampleInputEmail1">Koutsougeras, Kris</label>
                            </div>
                            <div class="col-md-auto label_container">
                                <label for="exampleInputEmail1">W Number:</label>
                                <label for="exampleInputEmail1">W87654321</label>                                                                                                                                                                                                                                                                                                                                                &nbsp;
                            </div>
                            <div class="form-group"> 
                            </div>
                        </div>
                        <textarea class="form-control" rows="3"></textarea>
                        <button type="submit" class="btn btn-primary">Submit</button>                         
                    </form>
                </div>
            </div>          
        </div>                

advisor

open (FILE, $student_advisor);
@dblines= <FILE>;#snatch the contents of file student_advisor.txt and store it to an array
close(FILE);#close it out
$length_dblines=@dblines;#determine how many records are in this file

open (FILE, $student_report);
@student_report_lines= <FILE>;#snatch the contents of file student_report.txt and store it to an array
close(FILE);#close it out
$length_student_report_lines=@student_report_lines;#determine how many records are in this file

for ($count = 0 ; $count <$length_dblines ; $count++) 
{ 
    chomp($dblines[$count]);   
    my @userData=split(',', $dblines[$count]); #place the current line into an array split by a comma
    my $lineStudentName= $userData[0];#
    my $lineAdvisorName= $userData[1];#

    if ($lineAdvisorName eq $userID){

        for ($countStudentReports = 0 ; $countStudentReports <$length_student_report_lines ; $countStudentReports++){
            chomp($dblines[$count]);   
            my @StudentReportData=split(',', $student_report_lines[$countStudentReports]); #place the current line into an array split by a comma

            if ($StudentReportData[0] eq $lineStudentName){

                 print <<"student_report"; 
                    
                    <div class="container">
                    <hr> 
                        <div class="masthead">
                                    <div class="row">
                        <div class="col-md-1 label_container">
                            <label for="exampleInputEmail1">Student:</label>
                        </div>
                        <div class="col-md-1 label_container">
                            <label for="exampleInputEmail1">$lineStudentName</label>
                        </div>
                        <div class="col-md-1 label_container">
                            <label for="exampleInputEmail1">Report:</label>
                        </div>
                        <div class="col-md-2 label_container">
                            <label for="exampleInputEmail1">$StudentReportData[1]</label>
                        </div>
                        <div class="col-md-7">
                            <object data="$studentSubmissionsDir/$StudentReportData[1]" type="text/plain"
                            width="100%" style="height: auto">
                            <a href="$studentSubmissionsDir/$StudentReportData[1]">Embedded Text Document</a>
                            </object>
                           
                        </div>
                    <hr>                      
                    </div>
                    </div>
                    </div>       
student_report

            }
        }
    }   
}
print "</body></html>";

  