---
title: 3D tree, version 0.1
template: no-img
---

I've been toying around with drawing [WebGL](https://hacks.mozilla.org/2013/04/the-concepts-of-webgl/) and [three.js](http://threejs.org/) to draw a 3D tree in the browser.
The idea is to write an algorithm that can draw a tree. 

<canvas id='tree' width='600' height='600'></canvas>

<button onclick='start_animation()'>Rotate</button>
<button onclick='stop_animation()'>Stop</button>

It's been a fun experiment. I've learned a lot about WebGL and three.js. I've brushed up on some math I haven't touched since high school. Studying nature is addicting and now every day as I walk to work, I appreciate trees in a whole new way (staring at them, looking like a crazy person probably).

There's plenty to do with this experiment.

* Test (and likely fix bugs) in different browsers with different screen sizes.
  Apologies if this demo isn't showing up correctly.
* Fix the anti-aliasing. I had it working, but when I resized the canvas
  to put it on this blog, it broke.
* There's a lot of geometry there, lots of vertices. I wonder if this can be optimized.
* Even a simple animation such as rotating the model seems to heat up my
  CPU pretty quickly. Again, I wonder how I can optimize this. Could be related to the
  previous point.
* There is tons of room for improvement in the algorithm that models the tree. It's not
  even a whole tree yet, just one tiny branch!
* Textures, lights, and effects. Oh my!

The [code is on github](https://github.com/abuchanan/tree/tree/master/3d-v2).

<script src='/js/3d-tree-v0.1/branch.js'></script>
