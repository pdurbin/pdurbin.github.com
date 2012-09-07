#!/usr/bin/perl
use strict;
use warnings;
use v5.10;
use Readonly;
use YAML qw{ LoadFile };
use Data::Dumper;
use URI::URL;
use LWP::Simple;

Readonly my $checkout      => "$ENV{HOME}/github/pdurbin/pdurbin.github.com";
Readonly my $googfav       => 'http://www.google.com/s2/u/0/favicons?domain=';
Readonly my $grabicon      => 'http://grabicon.com/';
Readonly my $favicondir    => 'images/favicons';
Readonly my $includedir    => "$checkout/_includes";
Readonly my $profileout    => "$includedir/profiles.html";
Readonly my $profiles_yaml => "$includedir/profiles.yaml";

chdir $checkout or die "Couldn't cd to $checkout";

mkdir $includedir unless -d $includedir;

my $profs = LoadFile($profiles_yaml);

my $html;

$html .= '<ul style="padding: 0px; margin: 0em; margin-left: 20px">' . "\n";
for my $proff (@$profs) {

    my $url = URI::URL->new($proff);

    my $googhost      = $googfav . $url->host;
    my $grabhost      = $grabicon . $url->host . '.png.16';
    my $url_host_real = $url->host;
    my $url_host_und  = $url_host_real;
    $url_host_und =~ s/\./_/;

    my $png = "$favicondir/$url_host_real.png";

    mkdir $favicondir unless -d $favicondir;

    unless ( -f $png ) {
        #system( "curl -s $googhost > $png");
        system("curl -s $grabhost > $png");
        sleep .5;
    }
    my $nohttp = $url->host . $url->path;

    my $li = qq{<li style="list-style-image:url('/$png')"><a href="$proff">$nohttp</a></li>};
    $html .= "$li\n";

}

$html .= "</ul>\n";

open( my $fh, '>', $profileout ) or die "cannot open > $profileout: $!";
print $fh $html;
