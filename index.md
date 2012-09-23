---
layout: default
title: greptilian.com
---
<a href="http://stackexchange.com/users/10330/philip-durbin"><img src="http://stackexchange.com/users/flair/10330.png" width="208" height="58" alt="profile for Philip Durbin on Stack Exchange, a network of free, community-driven Q&amp;A sites" title="profile for Philip Durbin on Stack Exchange, a network of free, community-driven Q&amp;A sites"></a>

{% include profiles.html %}

<p>

<script src="http://drnicjavascript.rubyforge.org/github_badge/dist/github-badge-launcher.js" type="text/javascript"></script>

<script charset="utf-8" src="http://widgets.twimg.com/j/2/widget.js" type="text/javascript"></script>
<script type="text/javascript">
new TWTR.Widget({
  version: 2,
  type: 'profile',
  rpp: 30,
  interval: 30000,
  width: 250,
  height: 300,
  theme: {
    shell: {
      background: '#333333',
      color: '#ffffff'
    },
    tweets: {
      //background: '#000000',
      //color: '#ffffff',
      //links: '#4aed05'
      background: 'silver',
      color: 'black',
      links: 'blue'
    }
  },
  features: {
    scrollbar: false,
    loop: false,
    live: false,
    behavior: 'all'
  }
}).render().setUser('philipdurbin').start();
</script>
