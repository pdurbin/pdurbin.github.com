---
layout: default
title: Room for the hacker emblem to move
---
Maybe you've seen this:

<img src="http://greptilian.com/images/glider-orig.png" alt="official hacker emblem SVG, dots blackened and turned to PNG">

It's the hacker emblem, which I believe first caught my attention a couple years ago in a sidebar at http://synflood.at/blog/ when accompanied by the word "hacker":

<img src="http://greptilian.com/images/hacker.png" alt="hacker emblem with text">

I clicked the icon and read the [hacker emblem page](http://www.catb.org/hacker-emblem) and [the frequently asked questions](http://www.catb.org/hacker-emblem/faqs.html), which state. . .

> The graphic at the top of the page is called a glider. It's a pattern from a mathematical simulation called the Game of Life. In this simulation, very simple rules about the behavior of dots on a grid give rise to wonderfully complex emergent phenomena. The glider is the simplest Life pattern that moves, and the most instantly recognizable of all Life patterns.

. . . but I was full of questions that I didn't bother to seek answers to until now.

[Conway's Game of Life](http://www.conwaylife.com/wiki/Conway%27s_Game_of_Life) is pretty cool, as it turns out.  Again, this particular [pattern][] is a [glider][], a type of [spaceship][], and like all spaceships, **it moves across the grid** and eventually returns to its initial configuration.

**Pop quiz: In what direction does the hacker emblem move?**

Unless you know what a glider is and that it moves, when you look at the hacker emblem you just see a bunch of dots on a grid.  You wouldn't necessary know that **the hacker emblem is predetermined to move down and to the right**.

Let's give the hacker emblem room to move:

<div style="float:left; width=180px;">
<a href="http://greptilian.com/images/glidermove0.png">
<img src="http://greptilian.com/images/glidermove0.png" alt="glider generation 0">
</a>
<br>

<a href="http://greptilian.com/images/glidermove1.png">
<img src="http://greptilian.com/images/glidermove1.png" alt="glider generation 1">
</a>
<br>

<a href="http://greptilian.com/images/glidermove2.png">
<img src="http://greptilian.com/images/glidermove2.png" alt="glider generation 2">
</a>
<br>

<a href="http://greptilian.com/images/glidermove3.png">
<img src="http://greptilian.com/images/glidermove3.png" alt="glider generation 3">
</a>
<br>

<a href="http://greptilian.com/images/glidermove4.png">
<img src="http://greptilian.com/images/glidermove4.png" alt="glider generation 4">
</a>
<br>

</div>
<p>
Rules from <a href="http://web.archive.org/web/20090603015231/http://ddi.cs.uni-potsdam.de/HyFISCH/Produzieren/lis_projekt/proj_gamelife/ConwayScientificAmerican.htm">The fantastic combinations of John Conway's new solitaire game "life"</a>:
</p>

<p>
1. Survivals. Every counter with two or three neighboring counters survives for the next generation.
</p>

<p>
2. Deaths. Each counter with four or more neighbors dies (is removed) from overpopulation. Every counter with one neighbor or none dies from isolation.
</p>

<p>
3. Births. Each empty cell adjacent to exactly three neighbors--no more, no fewer--is a birth cell. A counter is placed on it at the next move.
</p>

<div style="clear:left;">
</div>

If you'd like to see glider animated, I'd suggest opening each of the images above in browser tabs and toggling through with Ctrl-Tab.  Or you could check out an animation on [the glider Wikipedia page](http://en.wikipedia.org/wiki/Glider_%28Conway%27s_Life%29).  Personally, I find the static images above easier to study when reading the rules.

The images above are PNG files (converted from SVG with `inkscape --export-png=image.png --export-background-opacity=0 --without-gui image.svg`), which won't render correctly in every browser.  Below is is ascii art version as well. :)

    |_|0|_|_|   1. Survivals. Every
    |_|_|0|_|   counter with two or three
    |0|0|0|_|   neighboring counters
    |_|_|_|_|   survives for the next
                generation.            

    |_|_|_|_|   2. Deaths. Each counter
    |0|_|0|_|   with four or more
    |_|0|0|_|   neighbors dies (is
    |_|0|_|_|   removed) from
                overpopulation. Every
                counter with one neighbor
    |_|_|_|_|   or none dies from
    |_|_|0|_|   isolation.
    |0|_|0|_|                            
    |_|0|0|_|   3. Births. Each empty
                cell adjacent to exactly
                three neighbors--no more,
    |_|_|_|_|   no fewer--is a birth
    |_|0|_|_|   cell. A counter is placed
    |_|_|0|0|   on it at the next move.
    |_|0|0|_|


    |_|_|_|_|
    |_|_|0|_|
    |_|_|_|0|
    |_|0|0|0|


[pattern]: http://www.conwaylife.com/wiki/Pattern
[glider]: http://www.conwaylife.com/wiki/Glider
[spaceship]: http://www.conwaylife.com/wiki/Spaceship
