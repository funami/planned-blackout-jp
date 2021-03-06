#!/usr/bin/perl
use strict;
use warnings;
use File::Basename qw/dirname/;
BEGIN { require (dirname(__FILE__) . "/fatlib.pl") }
use CGI;
use PlannedBlackoutJP::Util qw/is_galapagos/;
use Text::MicroTemplate::File;

binmode STDOUT, ":utf8";

my $q = CGI->new;
my $view = $q->param('view') || (is_galapagos(\%ENV) ? 'm' : 'p');

my $template = $view eq 'm' ? 'indexm.html' : 'indexpc.html';

print $q->header("text/html;charset=utf-8");
my $mtf = Text::MicroTemplate::File->new(
    tag_start => '<%', tag_end => '%>', line_start => '%',
);
print $mtf->render_file($template, {});
